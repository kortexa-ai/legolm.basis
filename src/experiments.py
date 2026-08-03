from __future__ import annotations

import itertools
import json
import math
import random
import re
import time
from dataclasses import dataclass
from pathlib import Path

import torch
import torch.nn as nn
import torch.nn.functional as F

from .common import (
    DEFAULT_MINI_CHECKPOINT,
    EVAL_TOKENS,
    MAX_SEQ_LEN,
    Tokenizer,
    apply_hypernet_weights,
    apply_lora,
    autocast_for,
    cycle_batch,
    evaluate_bpb,
    freeze_non_lora,
    get_device,
    get_token_bytes,
    get_lora_params,
    load_lm,
    LoRALinear,
    make_dataloader,
    seed_everything,
    sensor_limit_for,
    total_lora_dim,
)
from .modalities import ModalityBundle, TaskDataset, load_modality_bundle, load_task_dataset
from .step_log import StepLogger


class PaperBridgeHyper(nn.Module):
    """Paper-facing bridge hypernetwork with explicit per-sample outputs."""

    def __init__(self, input_dim: int, output_dim: int, context_dim: int = 64):
        super().__init__()
        self.context = nn.Parameter(torch.randn(context_dim) * 0.02)
        self.proj = nn.Sequential(nn.Linear(input_dim, context_dim), nn.GELU())
        self.mlp = nn.Sequential(
            nn.Linear(context_dim * 2, 256),
            nn.GELU(),
            nn.Linear(256, 256),
            nn.GELU(),
            nn.Linear(256, output_dim),
        )
        nn.init.normal_(self.mlp[-1].weight, std=0.001)
        nn.init.zeros_(self.mlp[-1].bias)

    def forward(self, features: torch.Tensor, pool_batch: bool = False) -> torch.Tensor:
        if features.dim() == 1:
            features = features.unsqueeze(0)
        if features.dim() > 2:
            features = features.mean(dim=tuple(range(1, features.dim() - 1)))
        if pool_batch:
            features = features.mean(dim=0, keepdim=True)
        feat = self.proj(features)
        context = self.context.unsqueeze(0).expand(feat.size(0), -1)
        output = self.mlp(torch.cat([feat, context], dim=1))
        if pool_batch:
            return output[0]
        return output


class BasisBridgeHyper(nn.Module):
    """Bridge that emits coefficients over a learned basis of LoRA directions.

    Same trunk as PaperBridgeHyper; instead of a dense 256->D output layer it
    predicts k coefficients and mixes a learned (k, D) basis: w = c @ B. The
    basis rows start orthonormal and the coefficient head starts near zero, so
    generated LoRA weights begin near zero exactly like the dense bridge.
    """

    def __init__(self, input_dim: int, output_dim: int, basis_dim: int, context_dim: int = 64):
        super().__init__()
        self.basis_dim = basis_dim
        self.context = nn.Parameter(torch.randn(context_dim) * 0.02)
        self.proj = nn.Sequential(nn.Linear(input_dim, context_dim), nn.GELU())
        self.mlp = nn.Sequential(
            nn.Linear(context_dim * 2, 256),
            nn.GELU(),
            nn.Linear(256, 256),
            nn.GELU(),
            nn.Linear(256, basis_dim),
        )
        nn.init.normal_(self.mlp[-1].weight, std=0.001)
        nn.init.zeros_(self.mlp[-1].bias)
        basis = torch.empty(basis_dim, output_dim)
        nn.init.orthogonal_(basis)
        self.basis = nn.Parameter(basis)

    def forward(self, features: torch.Tensor, pool_batch: bool = False) -> torch.Tensor:
        if features.dim() == 1:
            features = features.unsqueeze(0)
        if features.dim() > 2:
            features = features.mean(dim=tuple(range(1, features.dim() - 1)))
        if pool_batch:
            features = features.mean(dim=0, keepdim=True)
        feat = self.proj(features)
        context = self.context.unsqueeze(0).expand(feat.size(0), -1)
        coefficients = self.mlp(torch.cat([feat, context], dim=1))
        output = coefficients @ self.basis
        if pool_batch:
            return output[0]
        return output


_FROZEN_BASIS_CACHE: dict[tuple[int, int, int, str], torch.Tensor] = {}
_FROZEN_BASIS_DIAGNOSTICS: dict[tuple[int, int, int, str], dict] = {}


def _orthonormality_residual(basis: torch.Tensor) -> dict:
    gram = basis @ basis.T
    eye = torch.eye(gram.size(0), device=gram.device, dtype=gram.dtype)
    offdiag = (gram - torch.diag(torch.diagonal(gram))).abs().max().item()
    diag = (torch.diagonal(gram) - 1.0).abs().max().item()
    del gram, eye
    return {"max_offdiag_abs": offdiag, "max_diag_error": diag}


def _whiten_rows(matrix: torch.Tensor) -> torch.Tensor:
    """Row-orthonormalize a (k, D) matrix in place of QR (Cholesky whitening).

    Lower-triangular whitening is prefix-stable: the first j rows of a whitened
    (k, D) matrix equal the whitening of its own first j rows. That is what lets
    a shared-basis arm (k rows) and a disjoint-slice arm (n*k rows) share the
    exact same basis rows, and it is far cheaper than QR at D ~ 7.7e5.
    """
    gram = (matrix @ matrix.T).cpu().double()
    chol = torch.linalg.cholesky(gram)
    inverse = torch.linalg.solve_triangular(
        chol, torch.eye(chol.size(0), dtype=chol.dtype), upper=False
    )
    return inverse.to(dtype=matrix.dtype, device=matrix.device) @ matrix


def frozen_orthonormal_basis(
    basis_dim: int,
    output_dim: int,
    seed: int,
    device: torch.device,
) -> torch.Tensor:
    """A seeded, frozen, row-orthonormal (basis_dim, output_dim) LoRA basis.

    Cached per (dim, output_dim, seed, device) so every brick in a process gets
    literally the same rows; a request for k rows is served as a view of an
    already-materialized k' > k basis (prefix stability, see _whiten_rows).
    """
    key = (basis_dim, output_dim, seed, str(device))
    cached = _FROZEN_BASIS_CACHE.get(key)
    if cached is not None:
        return cached
    for (other_dim, other_out, other_seed, other_device), tensor in list(_FROZEN_BASIS_CACHE.items()):
        if other_out == output_dim and other_seed == seed and other_device == str(device) and other_dim > basis_dim:
            view = tensor[:basis_dim]
            _FROZEN_BASIS_CACHE[key] = view
            _FROZEN_BASIS_DIAGNOSTICS[key] = dict(
                _FROZEN_BASIS_DIAGNOSTICS[(other_dim, other_out, other_seed, other_device)],
                served_as_prefix_of=other_dim,
            )
            return view
    generator = torch.Generator().manual_seed(seed)
    gaussian = torch.randn(basis_dim, output_dim, generator=generator).to(device)
    basis = _whiten_rows(gaussian)
    del gaussian
    residual = _orthonormality_residual(basis)
    passes = 1
    if max(residual["max_offdiag_abs"], residual["max_diag_error"]) > 1e-5:
        basis = _whiten_rows(basis)
        residual = _orthonormality_residual(basis)
        passes = 2
    _FROZEN_BASIS_CACHE[key] = basis
    _FROZEN_BASIS_DIAGNOSTICS[key] = {
        "basis_dim": basis_dim,
        "output_dim": output_dim,
        "basis_seed": seed,
        "whitening_passes": passes,
        **residual,
    }
    return basis


def frozen_basis_diagnostics(basis_dim: int, output_dim: int, seed: int, device: torch.device) -> dict:
    return dict(_FROZEN_BASIS_DIAGNOSTICS.get((basis_dim, output_dim, seed, str(device)), {}))


class FrozenBasisBridgeHyper(nn.Module):
    """Bridge that writes coefficients into a slice of a shared frozen basis.

    The basis is a buffer, not a parameter: it is regenerated from its seed, it
    holds no optimizer state, and it never moves. With `slice_offset`/
    `slice_width` a bridge writes only its own block of rows, so two bridges
    over the same frozen basis with disjoint slices produce LoRA deltas that are
    exactly orthogonal in weight space and whose sum has zero cross-terms.
    """

    def __init__(
        self,
        input_dim: int,
        output_dim: int,
        basis_dim: int,
        *,
        slice_offset: int = 0,
        slice_width: int | None = None,
        basis_seed: int = 42,
        context_dim: int = 64,
        device: torch.device | None = None,
    ):
        super().__init__()
        if device is None:
            device, _ = get_device()
        width = basis_dim - slice_offset if slice_width is None else slice_width
        if slice_offset < 0 or width < 1 or slice_offset + width > basis_dim:
            raise ValueError(f"Invalid basis slice [{slice_offset}, {slice_offset + width}) of {basis_dim}")
        self.basis_dim = basis_dim
        self.slice_offset = slice_offset
        self.slice_width = width
        self.basis_seed = basis_seed
        full = frozen_orthonormal_basis(basis_dim, output_dim, basis_seed, device)
        self.register_buffer("basis", full[slice_offset : slice_offset + width], persistent=False)
        self.context = nn.Parameter(torch.randn(context_dim) * 0.02)
        self.proj = nn.Sequential(nn.Linear(input_dim, context_dim), nn.GELU())
        self.mlp = nn.Sequential(
            nn.Linear(context_dim * 2, 256),
            nn.GELU(),
            nn.Linear(256, 256),
            nn.GELU(),
            nn.Linear(256, width),
        )
        nn.init.normal_(self.mlp[-1].weight, std=0.001)
        nn.init.zeros_(self.mlp[-1].bias)

    def coefficients(self, features: torch.Tensor, pool_batch: bool = False) -> torch.Tensor:
        if features.dim() == 1:
            features = features.unsqueeze(0)
        if features.dim() > 2:
            features = features.mean(dim=tuple(range(1, features.dim() - 1)))
        if pool_batch:
            features = features.mean(dim=0, keepdim=True)
        feat = self.proj(features)
        context = self.context.unsqueeze(0).expand(feat.size(0), -1)
        return self.mlp(torch.cat([feat, context], dim=1))

    def forward(self, features: torch.Tensor, pool_batch: bool = False) -> torch.Tensor:
        output = self.coefficients(features, pool_batch=pool_batch) @ self.basis
        if pool_batch:
            return output[0]
        return output


class LayerSlicedBridge(nn.Module):
    """A frozen-basis bridge confined to one contiguous LAYER BLOCK of the LM.

    Phase 3 v1/v2 partitioned the *coefficient* space over a basis that spanned
    every LoRA site, so the merged delta was off-axis at every site each brick
    wrote, and the dose-response showed six degrees of rotation is enough to
    erase the probe. This partitions the *sites* instead: brick i writes only
    the flat coordinates belonging to its own layers, so the merged delta
    restricted to brick i's block is *exactly* brick i's own delta — cos = 1 at
    every site it touches, whatever the other bricks do.

    Note the global cosine is still < 1 (the merged vector carries mass in
    coordinates this brick never writes), which is exactly what makes this the
    decisive test: the phase-2 angle account, read globally, predicts failure;
    read site-locally it predicts ~100% retention. They finally disagree.
    """

    def __init__(self, inner: nn.Module, start: int, end: int, output_dim: int):
        super().__init__()
        self.inner = inner
        self.start = int(start)
        self.end = int(end)
        self.output_dim = int(output_dim)

    @property
    def basis(self) -> torch.Tensor:
        return self.inner.basis

    @property
    def basis_seed(self) -> int:
        return self.inner.basis_seed

    def coefficients(self, features: torch.Tensor, pool_batch: bool = False) -> torch.Tensor:
        return self.inner.coefficients(features, pool_batch=pool_batch)

    def forward(self, features: torch.Tensor, pool_batch: bool = False) -> torch.Tensor:
        block = self.inner(features, pool_batch=pool_batch)
        return F.pad(block, (self.start, self.output_dim - self.end))


def lora_layer_sizes(model: nn.Module) -> list[int]:
    """Flat-vector size of every transformer layer's LoRA block.

    `apply_hypernet_weights` walks `model.modules()` in registration order, which
    is layer-major, so each layer owns a *contiguous* range of the flat vector.
    Verified on LFM2.5-230M: 14 layers, 66 LoRA modules, D = 774,144.
    """
    raw = model._orig_mod if hasattr(model, "_orig_mod") else model
    layers = raw.hf.model.layers if hasattr(raw, "hf") else raw.transformer.h
    sizes = []
    for layer in layers:
        sizes.append(
            sum(
                module.lora_a.numel() + module.lora_b.numel()
                for module in layer.modules()
                if isinstance(module, LoRALinear)
            )
        )
    return sizes


def balanced_layer_blocks(sizes: list[int], n_blocks: int) -> tuple[list[tuple[int, int]], list[int]]:
    """Split layers into n contiguous groups of the most equal flat size.

    Returns the flat-vector (start, end) ranges and the layer cut points. Brute
    force over cut positions: 14 layers into 3 blocks is 78 candidates.
    """
    if n_blocks > len(sizes):
        raise ValueError(f"Cannot split {len(sizes)} layers into {n_blocks} blocks")
    offsets = [0]
    for size in sizes:
        offsets.append(offsets[-1] + size)
    target = offsets[-1] / n_blocks
    best = None
    for cuts in itertools.combinations(range(1, len(sizes)), n_blocks - 1):
        bounds = (0,) + cuts + (len(sizes),)
        cost = sum((offsets[bounds[i + 1]] - offsets[bounds[i]] - target) ** 2 for i in range(n_blocks))
        if best is None or cost < best[0]:
            best = (cost, bounds)
    bounds = best[1]
    blocks = [(offsets[bounds[i]], offsets[bounds[i + 1]]) for i in range(n_blocks)]
    return blocks, list(bounds)


def _flat_feature(feature: torch.Tensor) -> torch.Tensor:
    """Collapse a sensor feature to the 1-D vector the bridges actually consume.

    The bridges mean-pool every dimension except the last; doing the same here
    means a gate and a bridge see the identical summary of the same sample.
    """
    if feature.dim() == 1:
        return feature
    return feature.reshape(-1, feature.size(-1)).mean(dim=0)


class GateNet(nn.Module):
    """Input-conditioned softmax router over per-brick coefficient heads.

    Composition by merging asks "how do I add these bricks"; gating asks "which
    brick should be speaking". The gate emits one convex weight per brick, so a
    fully confident gate reproduces that brick's single-brick delta *exactly*
    (the oracle ceiling) and a uniform gate reproduces the mean merge — the two
    endpoints of the phase-1 result are both inside this family, and the zero
    init starts training at the uniform (mean-merge) end.

    `n_tasks > 0` adds a learned task embedding: the router is told which
    question is being asked, but still has to learn the routing from data. That
    separates "the router cannot learn" from "the sensor stream does not carry
    the routing signal", which are very different negatives.

    Note on what the feature-only router *can* know (phase 3 v3): the live slot
    and the ambient slots are drawn from the same per-brick pool, so the
    concatenated input has the *same distribution* whichever modality is being
    asked. A feature-only router therefore has no Bayes-admissible input-
    conditioned solution — a constant is its optimum — and only the task
    embedding carries the routing signal at all.
    """

    def __init__(self, feature_dims: list[int], n_bricks: int, n_tasks: int = 0, hidden: int = 64):
        super().__init__()
        self.n_tasks = n_tasks
        self.task_embedding = nn.Embedding(n_tasks, hidden) if n_tasks else None
        in_dim = sum(feature_dims) + (hidden if n_tasks else 0)
        self.mlp = nn.Sequential(nn.Linear(in_dim, hidden), nn.GELU(), nn.Linear(hidden, n_bricks))
        nn.init.zeros_(self.mlp[-1].weight)
        nn.init.zeros_(self.mlp[-1].bias)

    def forward(self, features: list[torch.Tensor], task_index: int | None = None) -> torch.Tensor:
        parts = [F.layer_norm(part, part.shape[-1:]) for part in features]
        vector = torch.cat(parts, dim=-1)
        if self.task_embedding is not None:
            index = torch.tensor(int(task_index or 0), device=vector.device)
            vector = torch.cat([vector, self.task_embedding(index)], dim=-1)
        return torch.softmax(self.mlp(vector), dim=-1)


_GATE_ENTROPY_RE = re.compile(r"-ent([0-9.]+)$")


def parse_gate_mode(mode: str, default_balance_weight: float = 0.1) -> dict:
    """Decode a gate-mode name into its router configuration.

    Grammar (every earlier name still parses to what it meant before):
      gate-oracle                 hard one-hot ceiling, no router trained
      gate-learned                feature-only router,  lr = 10x bridge lr
      gate-task                   + learned task embedding, lr = 10x
      gate-balanced[-<lambda>]    + Switch-style load-balancing penalty
      gate-lr-<x>                 feature-only router at x times the bridge lr
      gate-task-lr-<x>            task-conditioned router at x times bridge lr
      <any learned mode>-ent<w>   + entropy bonus w (maximize per-example
                                  routing entropy, i.e. hold the softmax off
                                  its saturation floor so the losing experts
                                  keep receiving gradient)
    """
    spec = {"task": False, "lr_scale": 10.0, "balance": 0.0, "entropy": 0.0}
    body = mode
    matched = _GATE_ENTROPY_RE.search(body)
    if matched:
        spec["entropy"] = float(matched.group(1))
        body = body[: matched.start()]
    if body.startswith("gate-balanced"):
        suffix = body.removeprefix("gate-balanced").lstrip("-")
        spec["balance"] = float(suffix) if suffix else default_balance_weight
        return spec
    if body.startswith("gate-task"):
        spec["task"] = True
        rest = body.removeprefix("gate-task")
    elif body.startswith("gate-learned"):
        rest = body.removeprefix("gate-learned")
    elif body.startswith("gate-lr-"):
        spec["lr_scale"] = float(body.removeprefix("gate-lr-"))
        return spec
    else:
        rest = ""
    rest = rest.lstrip("-")
    if rest.startswith("lr-"):
        spec["lr_scale"] = float(rest.removeprefix("lr-"))
    elif rest:
        raise ValueError(f"Unparsable gate mode: {mode}")
    return spec


def _gate_row_stats(trace: list[list[float]], self_slot: int) -> dict:
    """Per-example routing diagnostics — the test for a *learned constant*.

    `per_brick_mean` alone cannot tell a router that routes from one that emits
    the same vector every time; phase-2's collapse was only caught because the
    mean was byte-identical across modalities. These add the within-modality
    dispersion (`per_brick_std`, `self_std`) and the per-example entropy, so a
    constant router is visible in a single run.
    """
    n_bricks = len(trace[0])
    n_rows = len(trace)

    def mean(values):
        return sum(values) / len(values)

    def std(values):
        average = mean(values)
        return math.sqrt(max(0.0, sum((value - average) ** 2 for value in values) / len(values)))

    entropies = [-sum(value * math.log(value) for value in row if value > 0) for row in trace]
    return {
        "self_mean": mean([row[self_slot] for row in trace]),
        "self_min": min(row[self_slot] for row in trace),
        "self_max": max(row[self_slot] for row in trace),
        "self_std": std([row[self_slot] for row in trace]),
        "per_brick_mean": [mean([row[slot] for row in trace]) for slot in range(n_bricks)],
        "per_brick_std": [std([row[slot] for row in trace]) for slot in range(n_bricks)],
        "entropy_mean": mean(entropies),
        "entropy_min": min(entropies),
        "entropy_max": max(entropies),
        "entropy_max_possible": math.log(n_bricks),
        "n_examples": n_rows,
    }


def bridge_param_groups(bridge: nn.Module, lr: float, basis_lr_scale: float = 1.0) -> list[dict]:
    """Optimizer param groups; optionally give the basis matrix its own lr.

    The basis dominates the parameter count, so under a global grad clip and a
    uniform lr it reorients slowly; scaling its lr tests the adaptation-speed
    hypothesis without touching the shared trunk/head recipe.
    """
    if basis_lr_scale == 1.0 or not isinstance(bridge, BasisBridgeHyper):
        return [{"params": list(bridge.parameters()), "lr": lr}]
    rest = [param for name, param in bridge.named_parameters() if name != "basis"]
    return [
        {"params": rest, "lr": lr},
        {"params": [bridge.basis], "lr": lr * basis_lr_scale},
    ]


FROZEN_BASIS_PREFIXES = ("basis-frozen-", "basis-disjoint-")


def is_frozen_basis_spec(bridge_spec: str) -> bool:
    return bridge_spec.startswith(FROZEN_BASIS_PREFIXES)


def basis_dim_of(bridge_spec: str) -> int:
    for prefix in FROZEN_BASIS_PREFIXES:
        if bridge_spec.startswith(prefix):
            return int(bridge_spec.removeprefix(prefix))
    return int(bridge_spec.removeprefix("basis-"))


def make_bridge(
    bridge_spec: str,
    input_dim: int,
    output_dim: int,
    *,
    slice_offset: int = 0,
    slice_width: int | None = None,
    basis_seed: int = 42,
    device: torch.device | None = None,
    layer_range: tuple[int, int] | None = None,
) -> nn.Module:
    """Build a bridge from its spec.

    "dense"                  — the paper-1 hypernetwork (256 -> D output layer)
    "basis-<k>"              — learned basis, w = c @ B (paper 2)
    "basis-frozen-<k>"       — seeded frozen orthonormal basis, no optimizer state
    "basis-disjoint-<k>"     — same, but this bridge writes only [slice_offset,
                               slice_offset+slice_width) of the k shared rows

    `layer_range` (phase 3 v3) confines the bridge to one contiguous block of
    the flat LoRA vector: the k basis rows are drawn over that block only, and
    the emitted delta is zero everywhere else. Same architecture, same trainable
    parameter count, disjoint *sites* instead of disjoint coefficients.
    """
    if layer_range is not None:
        if not is_frozen_basis_spec(bridge_spec):
            raise ValueError(f"Layer-partitioned bridges need a frozen-basis spec, got: {bridge_spec}")
        start, end = layer_range
        inner = FrozenBasisBridgeHyper(
            input_dim,
            end - start,
            basis_dim_of(bridge_spec),
            slice_offset=slice_offset,
            slice_width=slice_width,
            basis_seed=basis_seed,
            device=device,
        )
        return LayerSlicedBridge(inner, start, end, output_dim)
    if bridge_spec == "dense":
        return PaperBridgeHyper(input_dim, output_dim)
    if is_frozen_basis_spec(bridge_spec):
        basis_dim = basis_dim_of(bridge_spec)
        if basis_dim < 1:
            raise ValueError(f"Basis dim must be positive: {bridge_spec}")
        return FrozenBasisBridgeHyper(
            input_dim,
            output_dim,
            basis_dim,
            slice_offset=slice_offset,
            slice_width=slice_width,
            basis_seed=basis_seed,
            device=device,
        )
    if bridge_spec.startswith("basis-"):
        basis_dim = int(bridge_spec.removeprefix("basis-"))
        if basis_dim < 1:
            raise ValueError(f"Basis dim must be positive: {bridge_spec}")
        return BasisBridgeHyper(input_dim, output_dim, basis_dim)
    raise ValueError(f"Unsupported bridge spec: {bridge_spec}")


def slice_assignments(bridge_spec: str, n_bricks: int, allocation: str) -> list[tuple[int, int | None]]:
    """Per-brick (offset, width) into the shared basis.

    "shared" gives every brick the whole basis (the v0 regime, where a mean
    merge is exactly a coefficient mean); "disjoint" splits the k rows into
    n_bricks contiguous blocks so no two bricks can write the same coordinate;
    "layer" gives every brick the whole k rows but over its own layer block
    only (the separation is by *site*, handled by `layer_range` in make_bridge).
    """
    if allocation in ("shared", "layer"):
        return [(0, None)] * n_bricks
    if allocation != "disjoint":
        raise ValueError(f"Unsupported allocation: {allocation}")
    if not is_frozen_basis_spec(bridge_spec):
        raise ValueError(f"Disjoint allocation needs a frozen-basis bridge spec, got: {bridge_spec}")
    basis_dim = basis_dim_of(bridge_spec)
    if basis_dim % n_bricks:
        raise ValueError(f"Basis dim {basis_dim} is not divisible by {n_bricks} bricks")
    width = basis_dim // n_bricks
    return [(index * width, width) for index in range(n_bricks)]


class PrefixProjection(nn.Module):
    """Project sensor features into continuous prefix tokens."""

    def __init__(self, feature_dim: int, d_model: int, n_prefix: int):
        super().__init__()
        self.n_prefix = n_prefix
        self.d_model = d_model
        self.proj = nn.Sequential(
            nn.Linear(feature_dim, d_model * n_prefix),
            nn.GELU(),
        )

    def forward(self, features: torch.Tensor) -> torch.Tensor:
        if features.dim() == 1:
            features = features.unsqueeze(0)
        if features.dim() > 2:
            features = features.mean(dim=tuple(range(1, features.dim() - 1)))
        projected = self.proj(features)
        return projected.view(features.size(0), self.n_prefix, self.d_model)


@dataclass
class BridgeArtifacts:
    bridge: nn.Module
    bundle: ModalityBundle


def _throughput_metrics(total_time: float, steps: int, batch_size: int, seq_len: int = MAX_SEQ_LEN) -> dict:
    examples_seen = steps * batch_size
    tokens_seen = examples_seen * seq_len
    return {
        "train_elapsed_s": total_time,
        "steps_per_second": (steps / total_time) if total_time > 0 else 0.0,
        "examples_seen": examples_seen,
        "tokens_seen": tokens_seen,
    }


def _display_activity(label: str) -> str:
    return label.replace("_", " ")


def _suffix_log_path(log_path: str | None, suffix: str) -> str | None:
    if not log_path:
        return None
    path = Path(log_path)
    return str(path.with_name(f"{path.stem}-{suffix}{path.suffix}"))


def _make_global_shuffle_map(size: int, seed: int, device: torch.device) -> torch.Tensor | None:
    if size < 2:
        return None
    base = torch.arange(size, dtype=torch.long)
    generator = torch.Generator().manual_seed(seed)
    perm = torch.randperm(size, generator=generator)
    while bool(torch.any(perm == base)):
        perm = torch.randperm(size, generator=generator)
    return perm.to(device)


def _cycle_indices(size: int, batch_size: int, offset: int, device: torch.device) -> tuple[torch.Tensor, int]:
    if size <= 0:
        raise ValueError("Cannot cycle an empty tensor")
    indices = (torch.arange(batch_size, device=device) + offset) % size
    return indices, (offset + batch_size) % size


def _offdiag_cosine(vectors: torch.Tensor) -> torch.Tensor:
    if vectors.dim() == 1 or vectors.size(0) < 2:
        return vectors.new_tensor(0.0)
    normed = F.normalize(vectors, dim=1)
    sim = normed @ normed.T
    mask = ~torch.eye(vectors.size(0), dtype=torch.bool, device=vectors.device)
    return sim[mask].mean()


def _mean_pairwise_cosine(vectors: list[torch.Tensor]) -> float:
    if len(vectors) < 2:
        return 0.0
    stacked = torch.stack(vectors)
    return float(_offdiag_cosine(stacked).item())


def _forward_with_prefix(raw_model, prefix_tokens: torch.Tensor, text_ids: torch.Tensor) -> torch.Tensor:
    if hasattr(raw_model, "forward_with_prefix"):
        return raw_model.forward_with_prefix(prefix_tokens, text_ids)
    batch_size, text_len = text_ids.size()
    n_prefix = prefix_tokens.size(1)
    cos_sin = raw_model.cos[:, : text_len + n_prefix], raw_model.sin[:, : text_len + n_prefix]
    text_embeds = raw_model.transformer.wte(text_ids)
    combined = torch.cat([prefix_tokens, text_embeds], dim=1)
    hidden = combined
    for block in raw_model.transformer.h:
        hidden = block(hidden, cos_sin)
    hidden = raw_model.transformer.ln_f(hidden)
    logits = raw_model.lm_head(hidden).float()
    softcap = 30
    return softcap * torch.tanh(logits / softcap)


def _bridge_features_for_indices(
    bundle: ModalityBundle,
    indices: torch.Tensor,
    feature_mode: str,
    shuffle_map: torch.Tensor | None = None,
    constant_feature: torch.Tensor | None = None,
) -> torch.Tensor:
    if feature_mode == "true":
        return bundle.get_features(bundle.data[indices])
    if feature_mode == "shuffled":
        if shuffle_map is None:
            return bundle.get_features(bundle.data[indices])
        return bundle.get_features(bundle.data[shuffle_map[indices]])
    if feature_mode == "random":
        features = bundle.get_features(bundle.data[indices])
        return torch.randn_like(features)
    if feature_mode == "constant":
        if constant_feature is None:
            raise ValueError("constant feature mode requires a precomputed feature vector")
        return constant_feature.unsqueeze(0).expand(len(indices), -1)
    raise ValueError(f"Unsupported feature mode: {feature_mode}")


def _backprop_conditioned_batch_loss(
    model: torch.nn.Module,
    tx: torch.Tensor,
    ty: torch.Tensor,
    bridge: PaperBridgeHyper,
    features: torch.Tensor,
    rank: int,
    target: str,
    autocast_ctx,
) -> torch.Tensor:
    total_loss = torch.zeros((), device=tx.device)
    batch_size = tx.size(0)
    for idx, feature in enumerate(features):
        weight_vector = bridge(feature.unsqueeze(0))[0]
        apply_hypernet_weights(model, weight_vector, rank, target)
        with autocast_ctx:
            sample_loss = model(tx[idx : idx + 1], ty[idx : idx + 1]) / batch_size
        total_loss = total_loss + sample_loss.detach()
        sample_loss.backward()
    return total_loss


def _evaluate_bridge_bpb(
    model: torch.nn.Module,
    tokenizer: Tokenizer,
    bridge: PaperBridgeHyper,
    bundle: ModalityBundle,
    rank: int,
    target: str,
    feature_mode: str,
    eval_tokens: int | None,
    autocast_ctx,
    batch_size: int = 8,
    shuffle_map: torch.Tensor | None = None,
    constant_feature: torch.Tensor | None = None,
) -> float:
    was_training = bridge.training
    bridge.eval()
    device = next(model.parameters()).device
    token_bytes = get_token_bytes(device=device)
    val_loader = make_dataloader(tokenizer, batch_size, MAX_SEQ_LEN, "val")
    steps = max(1, (eval_tokens or EVAL_TOKENS) // (batch_size * MAX_SEQ_LEN))
    total_nats = 0.0
    total_bytes = 0
    sensor_offset = 0

    try:
        with torch.no_grad():
            for _ in range(steps):
                x, y, _ = next(val_loader)
                x = x.to(device)
                y = y.to(device)
                indices, sensor_offset = _cycle_indices(len(bundle.data), x.size(0), sensor_offset, device)
                features = _bridge_features_for_indices(bundle, indices, feature_mode, shuffle_map, constant_feature)
                weight_vectors = bridge(features)
                for idx, weight_vector in enumerate(weight_vectors):
                    apply_hypernet_weights(model, weight_vector, rank, target)
                    with autocast_ctx:
                        loss_flat = model(x[idx : idx + 1], y[idx : idx + 1], reduction="none").view(-1)
                    y_flat = y[idx : idx + 1].view(-1)
                    nbytes = token_bytes[y_flat]
                    mask = nbytes > 0
                    total_nats += (loss_flat * mask).sum().item()
                    total_bytes += nbytes.sum().item()
    finally:
        if was_training:
            bridge.train()
    return total_nats / (math.log(2) * total_bytes)


def probe_imu_diversity(
    bridge: PaperBridgeHyper,
    *,
    max_items_per_activity: int = 32,
    selection_seed: int = 42,
) -> dict:
    device = next(bridge.parameters()).device
    was_training = bridge.training
    bridge.eval()
    task_data = load_task_dataset("imu", device)
    grouped: dict[str, list[torch.Tensor]] = {}
    for sensor_tensor, label in task_data.test_pairs:
        grouped.setdefault(label, []).append(sensor_tensor)

    selector = random.Random(selection_seed)
    selected_pairs: list[tuple[torch.Tensor, str]] = []
    for label in sorted(grouped):
        items = list(grouped[label])
        selector.shuffle(items)
        limit = min(max_items_per_activity, len(items))
        selected_pairs.extend((item, label) for item in items[:limit])

    labels: list[str] = []
    weight_vectors: list[torch.Tensor] = []
    try:
        with torch.no_grad():
            for sensor_tensor, label in selected_pairs:
                feature = task_data.get_feature(sensor_tensor)
                weight_vector = bridge(feature)[0].detach().float().cpu()
                labels.append(label)
                weight_vectors.append(weight_vector)
    finally:
        if was_training:
            bridge.train()

    if not weight_vectors:
        raise ValueError("IMU diversity probe selected no held-out examples")

    all_weights = torch.stack(weight_vectors)
    cross_input_cosine = float(_offdiag_cosine(all_weights).item())

    by_label: dict[str, list[torch.Tensor]] = {}
    for label, weight_vector in zip(labels, weight_vectors):
        by_label.setdefault(label, []).append(weight_vector)

    centroids: dict[str, torch.Tensor] = {
        label: torch.stack(vectors).mean(dim=0)
        for label, vectors in sorted(by_label.items())
    }
    centroid_labels = list(centroids.keys())
    centroid_stack = torch.stack([centroids[label] for label in centroid_labels])
    centroid_normed = F.normalize(centroid_stack, dim=1)
    centroid_sim = centroid_normed @ centroid_normed.T

    centroid_pair_cosines: dict[str, float] = {}
    for i, left in enumerate(centroid_labels):
        for j in range(i + 1, len(centroid_labels)):
            right = centroid_labels[j]
            pair_name = f"{_display_activity(left)} <-> {_display_activity(right)}"
            centroid_pair_cosines[pair_name] = float(centroid_sim[i, j].item())

    motion_labels = [label for label in centroid_labels if label.startswith("walking")]
    still_labels = [label for label in centroid_labels if label in {"sitting", "standing", "laying"}]
    motion_centroids = [centroids[label] for label in motion_labels]
    still_centroids = [centroids[label] for label in still_labels]
    motion_vs_still = [
        float(F.cosine_similarity(centroids[left].unsqueeze(0), centroids[right].unsqueeze(0)).item())
        for left in motion_labels
        for right in still_labels
    ]

    paper_pairs = {}
    for left, right in [
        ("walking", "walking_upstairs"),
        ("walking", "sitting"),
        ("walking", "standing"),
        ("sitting", "standing"),
        ("walking_downstairs", "laying"),
    ]:
        if left in centroids and right in centroids:
            paper_pairs[f"{_display_activity(left)} <-> {_display_activity(right)}"] = float(
                F.cosine_similarity(centroids[left].unsqueeze(0), centroids[right].unsqueeze(0)).item()
            )

    return {
        "probe_dataset": "uci-har-test",
        "selection_seed": selection_seed,
        "max_items_per_activity": max_items_per_activity,
        "selected_examples": len(weight_vectors),
        "activity_counts": { _display_activity(label): len(vectors) for label, vectors in sorted(by_label.items()) },
        "cross_input_cosine_mean": cross_input_cosine,
        "within_activity_cosine_mean": {
            _display_activity(label): _mean_pairwise_cosine(vectors)
            for label, vectors in sorted(by_label.items())
        },
        "motion_cluster_centroid_cosine_mean": _mean_pairwise_cosine(motion_centroids),
        "still_cluster_centroid_cosine_mean": _mean_pairwise_cosine(still_centroids),
        "motion_vs_still_centroid_cosine_mean": sum(motion_vs_still) / len(motion_vs_still) if motion_vs_still else 0.0,
        "activity_centroid_pair_cosines": centroid_pair_cosines,
        "paper_pairs": paper_pairs,
    }


def run_diversity_experiment(
    checkpoint: str | Path = DEFAULT_MINI_CHECKPOINT,
    train_steps: int = 300,
    rank: int = 4,
    target: str = "all",
    lr: float = 1e-3,
    diversity_weight: float = 0.1,
    log_csv: str | None = None,
    eval_tokens: int | None = None,
    sensor_limit: int | None = None,
    seed: int = 42,
    probe_max_items_per_activity: int = 32,
    probe_seed: int | None = None,
    bridge_spec: str = "dense",
    basis_lr_scale: float = 1.0,
):
    result = run_bridge_experiment(
        modality="imu",
        feature_mode="true",
        checkpoint=checkpoint,
        train_steps=train_steps,
        rank=rank,
        target=target,
        lr=lr,
        diversity_weight=diversity_weight,
        log_csv=log_csv,
        eval_tokens=eval_tokens,
        sensor_limit=sensor_limit,
        seed=seed,
        return_artifacts=True,
        bridge_spec=bridge_spec,
        basis_lr_scale=basis_lr_scale,
    )
    artifacts = result.pop("artifacts")
    result["experiment"] = f"diversity-imu-l{diversity_weight:.2f}"
    result["heldout_probe"] = probe_imu_diversity(
        artifacts.bridge,
        max_items_per_activity=probe_max_items_per_activity,
        selection_seed=seed if probe_seed is None else probe_seed,
    )
    result["paper_summary"] = {
        "lambda": diversity_weight,
        "bpb_improvement": result["improvement"],
        "cross_input_cosine_mean": result["heldout_probe"]["cross_input_cosine_mean"],
    }
    return result


def _load_bridge_setup(
    modality: str,
    checkpoint: str | Path,
    rank: int,
    target: str,
    sensor_limit: int | None,
    eval_tokens: int | None,
    seed: int,
    bridge_spec: str = "dense",
    slice_offset: int = 0,
    slice_width: int | None = None,
    basis_seed: int | None = None,
    layer_block_index: int | None = None,
    n_layer_blocks: int | None = None,
):
    seed_everything(seed)
    device, device_type = get_device()
    model, _, _ = load_lm(checkpoint)
    model = model.to(device)
    tokenizer = Tokenizer.from_directory()
    autocast_ctx = autocast_for(device_type)
    model.eval()
    with torch.no_grad(), autocast_ctx:
        baseline = evaluate_bpb(model, tokenizer, 8, eval_tokens=eval_tokens)

    apply_lora(model, rank=rank, target=target)
    model = model.to(device)
    freeze_non_lora(model)
    bundle = load_modality_bundle(modality, device, limit=sensor_limit_for(modality, sensor_limit))
    # The layer partition is recomputed here rather than passed in: this
    # function owns its own copy of the LM, and the architecture (hence the
    # per-layer flat sizes) is identical to the caller's.
    layer_range = None
    if layer_block_index is not None:
        blocks, _ = balanced_layer_blocks(lora_layer_sizes(model), n_layer_blocks)
        layer_range = blocks[layer_block_index]
    bridge = make_bridge(
        bridge_spec,
        bundle.feature_dim,
        total_lora_dim(model),
        slice_offset=slice_offset,
        slice_width=slice_width,
        basis_seed=seed if basis_seed is None else basis_seed,
        device=device,
        layer_range=layer_range,
    ).to(device)
    return device, device_type, model, tokenizer, autocast_ctx, baseline, bundle, bridge


def run_static_lora(
    modality: str,
    checkpoint: str | Path = DEFAULT_MINI_CHECKPOINT,
    train_steps: int = 300,
    rank: int = 4,
    target: str = "all",
    lr: float = 1e-3,
    log_csv: str | None = None,
    eval_tokens: int | None = None,
    seed: int = 42,
):
    seed_everything(seed)
    device, device_type = get_device()
    model, _, _ = load_lm(checkpoint)
    model = model.to(device)
    tokenizer = Tokenizer.from_directory()
    autocast_ctx = autocast_for(device_type)

    model.eval()
    with torch.no_grad(), autocast_ctx:
        baseline = evaluate_bpb(model, tokenizer, 8, eval_tokens=eval_tokens)

    apply_lora(model, rank=rank, target=target)
    model = model.to(device)
    freeze_non_lora(model)

    # Same optimizer recipe as the bridge experiments (METHOD_CONTRACT §1.2):
    # only the source of the LoRA weights may differ between conditions.
    lora_params = get_lora_params(model)
    optimizer = torch.optim.AdamW(lora_params, lr=lr, weight_decay=0.01)
    text_loader = make_dataloader(tokenizer, 8, MAX_SEQ_LEN, "train")
    step_log = StepLogger(log_csv) if log_csv else None

    total_time = 0.0
    steps = 0
    model.train()
    while steps < train_steps:
        t0 = time.time()
        tx, ty, _ = next(text_loader)
        tx = tx.to(device)
        ty = ty.to(device)
        with autocast_ctx:
            loss = model(tx, ty)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(lora_params, 1.0)
        optimizer.step()
        optimizer.zero_grad(set_to_none=True)
        if device.type == "mps":
            torch.mps.synchronize()
        elif device.type == "cuda":
            torch.cuda.synchronize()
        total_time += time.time() - t0
        if step_log and steps % 10 == 0:
            step_log.log(step=steps, elapsed_s=round(total_time, 1), loss=round(loss.item(), 6))
        steps += 1
    if step_log:
        step_log.close()

    model.eval()
    eval_t0 = time.time()
    with torch.no_grad(), autocast_ctx:
        final = evaluate_bpb(model, tokenizer, 8, eval_tokens=eval_tokens)
    eval_elapsed = time.time() - eval_t0
    result = {
        "experiment": f"static-lora-{modality}",
        "baseline": baseline,
        "final": final,
        "improvement": baseline - final,
        "steps": steps,
        "lr": lr,
        "trainable_params": sum(p.numel() for p in lora_params),
        "eval_elapsed_s": eval_elapsed,
    }
    result.update(_throughput_metrics(total_time, steps, batch_size=8))
    return result


def run_bridge_experiment(
    modality: str,
    feature_mode: str = "true",
    checkpoint: str | Path = DEFAULT_MINI_CHECKPOINT,
    train_steps: int = 300,
    rank: int = 4,
    target: str = "all",
    lr: float = 1e-3,
    diversity_weight: float = 0.0,
    log_csv: str | None = None,
    eval_tokens: int | None = None,
    sensor_limit: int | None = None,
    seed: int = 42,
    return_artifacts: bool = False,
    bridge_spec: str = "dense",
    basis_lr_scale: float = 1.0,
    slice_offset: int = 0,
    slice_width: int | None = None,
    basis_seed: int | None = None,
    layer_block_index: int | None = None,
    n_layer_blocks: int | None = None,
):
    device, _, model, tokenizer, autocast_ctx, baseline, bundle, bridge = _load_bridge_setup(
        modality=modality,
        checkpoint=checkpoint,
        rank=rank,
        target=target,
        sensor_limit=sensor_limit,
        eval_tokens=eval_tokens,
        seed=seed,
        bridge_spec=bridge_spec,
        slice_offset=slice_offset,
        slice_width=slice_width,
        basis_seed=basis_seed,
        layer_block_index=layer_block_index,
        n_layer_blocks=n_layer_blocks,
    )

    optimizer = torch.optim.AdamW(bridge_param_groups(bridge, lr, basis_lr_scale), weight_decay=0.01)
    text_loader = make_dataloader(tokenizer, 8, MAX_SEQ_LEN, "train")
    step_log = StepLogger(log_csv) if log_csv else None
    shuffle_map = _make_global_shuffle_map(len(bundle.data), seed + 17, device) if feature_mode == "shuffled" else None
    # Capacity-matched control: the bridge sees one fixed feature vector (the
    # bundle mean) on every step, isolating "extra trainable parameters" from
    # any per-input conditioning signal.
    constant_feature = bundle.get_features(bundle.data).mean(dim=0) if feature_mode == "constant" else None

    total_time = 0.0
    steps = 0
    last_diversity = 0.0
    model.train()
    while steps < train_steps:
        t0 = time.time()
        indices = torch.randperm(len(bundle.data), device=device)[:8]
        features = _bridge_features_for_indices(bundle, indices, feature_mode, shuffle_map, constant_feature)

        tx, ty, _ = next(text_loader)
        tx = tx.to(device)
        ty = ty.to(device)
        loss = _backprop_conditioned_batch_loss(model, tx, ty, bridge, features, rank, target, autocast_ctx)

        if diversity_weight > 0:
            per_sample_weights = bridge(features)
            diversity = _offdiag_cosine(per_sample_weights)
            (diversity_weight * diversity).backward()
            loss = loss + diversity_weight * diversity.detach()
            last_diversity = diversity.item()

        torch.nn.utils.clip_grad_norm_(bridge.parameters(), 1.0)
        optimizer.step()
        optimizer.zero_grad(set_to_none=True)
        if device.type == "mps":
            torch.mps.synchronize()
        elif device.type == "cuda":
            torch.cuda.synchronize()
        total_time += time.time() - t0
        if step_log and steps % 10 == 0:
            log = {"step": steps, "elapsed_s": round(total_time, 1), "loss": round(loss.item(), 6)}
            if diversity_weight > 0:
                log["diversity"] = round(last_diversity, 6)
            step_log.log(**log)
        steps += 1
    if step_log:
        step_log.close()

    model.eval()
    eval_t0 = time.time()
    final = _evaluate_bridge_bpb(
        model,
        tokenizer,
        bridge,
        bundle,
        rank,
        target,
        feature_mode,
        eval_tokens,
        autocast_ctx,
        shuffle_map=shuffle_map,
        constant_feature=constant_feature,
    )
    eval_elapsed = time.time() - eval_t0

    result = {
        "experiment": f"{feature_mode}-{modality}" if feature_mode != "true" else f"bridge-{modality}",
        "baseline": baseline,
        "final": final,
        "improvement": baseline - final,
        "steps": steps,
        "lr": lr,
        "diversity_weight": diversity_weight,
        "last_diversity": last_diversity,
        "bridge": bridge_spec,
        "basis_lr_scale": basis_lr_scale,
        "trainable_params": sum(p.numel() for p in bridge.parameters()),
        "lora_dim": total_lora_dim(model),
        "eval_elapsed_s": eval_elapsed,
    }
    if isinstance(bridge, FrozenBasisBridgeHyper):
        result["basis_slice"] = [bridge.slice_offset, bridge.slice_offset + bridge.slice_width]
        result["basis_seed"] = bridge.basis_seed
    if isinstance(bridge, LayerSlicedBridge):
        result["layer_block"] = [bridge.start, bridge.end]
        result["basis_slice"] = [bridge.inner.slice_offset, bridge.inner.slice_offset + bridge.inner.slice_width]
        result["basis_seed"] = bridge.basis_seed
    result.update(_throughput_metrics(total_time, steps, batch_size=8))
    if return_artifacts:
        result["artifacts"] = BridgeArtifacts(bridge=bridge, bundle=bundle)
    return result


def _merge_weight_vectors(vectors: list[torch.Tensor], merge_mode: str) -> torch.Tensor:
    stacked = torch.stack(vectors)
    if merge_mode == "mean":
        return stacked.mean(dim=0)
    if merge_mode == "sum":
        return stacked.sum(dim=0)
    raise ValueError(f"Unsupported merge mode: {merge_mode}")


def run_composition(
    bricks: list[str],
    checkpoint: str | Path = DEFAULT_MINI_CHECKPOINT,
    steps_per_brick: int = 150,
    rank: int = 4,
    target: str = "all",
    lr: float = 1e-3,
    eval_tokens: int | None = None,
    sensor_limit: int | None = None,
    seed: int = 42,
    log_csv: str | None = None,
    eval_mode: str = "conditioned",
    bridge_spec: str = "dense",
    basis_lr_scale: float = 1.0,
    merge_modes: tuple[str, ...] = ("mean",),
    allocation: str = "shared",
    basis_seed: int | None = None,
):
    trained = []
    per_brick = {}
    train_elapsed_s = 0.0
    total_steps = 0
    total_examples_seen = 0
    total_tokens_seen = 0
    assignments = slice_assignments(bridge_spec, len(bricks), allocation)
    for brick, (offset, width) in zip(bricks, assignments):
        result = run_bridge_experiment(
            modality=brick,
            feature_mode="true",
            checkpoint=checkpoint,
            train_steps=steps_per_brick,
            rank=rank,
            target=target,
            lr=lr,
            eval_tokens=eval_tokens,
            sensor_limit=sensor_limit,
            seed=seed,
            log_csv=_suffix_log_path(log_csv, brick),
            return_artifacts=True,
            bridge_spec=bridge_spec,
            basis_lr_scale=basis_lr_scale,
            slice_offset=offset,
            slice_width=width,
            basis_seed=basis_seed,
        )
        trained.append(result["artifacts"])
        # The single-brick BPB measured on exactly the brick that enters the
        # merge: retention denominators no longer come from a separate run.
        per_brick[brick] = {
            "final": result["final"],
            "improvement": result["improvement"],
            "basis_slice": result.get("basis_slice"),
            "trainable_params": result["trainable_params"],
        }
        train_elapsed_s += result.get("train_elapsed_s", 0.0)
        total_steps += result.get("steps", 0)
        total_examples_seen += result.get("examples_seen", 0)
        total_tokens_seen += result.get("tokens_seen", 0)

    seed_everything(seed)
    device, device_type = get_device()
    model, _, _ = load_lm(checkpoint)
    model = model.to(device)
    tokenizer = Tokenizer.from_directory()
    autocast_ctx = autocast_for(device_type)

    model.eval()
    with torch.no_grad(), autocast_ctx:
        baseline = evaluate_bpb(model, tokenizer, 8, eval_tokens=eval_tokens)

    apply_lora(model, rank=rank, target=target)
    model = model.to(device)

    model.eval()
    for artifact in trained:
        artifact.bridge.eval()
    eval_t0 = time.time()
    merge_results: dict[str, dict] = {}
    magnitudes: dict[str, float] = {}
    for merge_mode in merge_modes:
        if eval_mode == "fixed":
            with torch.no_grad():
                vectors = []
                for artifact in trained:
                    indices, _ = _cycle_indices(len(artifact.bundle.data), 8, 0, device)
                    features = artifact.bundle.get_features(artifact.bundle.data[indices])
                    vectors.append(artifact.bridge(features).mean(dim=0))
                combined = _merge_weight_vectors(vectors, merge_mode)
            apply_hypernet_weights(model, combined, rank, target)
            with torch.no_grad(), autocast_ctx:
                mode_final = evaluate_bpb(model, tokenizer, 8, eval_tokens=eval_tokens)
        elif eval_mode == "conditioned":
            device = next(model.parameters()).device
            token_bytes = get_token_bytes(device=device)
            val_loader = make_dataloader(tokenizer, 8, MAX_SEQ_LEN, "val")
            steps = max(1, (eval_tokens or EVAL_TOKENS) // (8 * MAX_SEQ_LEN))
            total_nats = 0.0
            total_bytes = 0
            offsets = [0 for _ in trained]
            first_batch = True
            with torch.no_grad():
                for _ in range(steps):
                    x, y, _ = next(val_loader)
                    x = x.to(device)
                    y = y.to(device)
                    weight_vectors = []
                    for idx, artifact in enumerate(trained):
                        sensor_indices, offsets[idx] = _cycle_indices(len(artifact.bundle.data), x.size(0), offsets[idx], device)
                        features = artifact.bundle.get_features(artifact.bundle.data[sensor_indices])
                        weight_vectors.append(artifact.bridge(features))
                    merged = _merge_weight_vectors(weight_vectors, merge_mode)
                    if first_batch:
                        for brick, vectors in zip(bricks, weight_vectors):
                            magnitudes[f"single_{brick}_l2"] = float(vectors.norm(dim=1).mean().item())
                        magnitudes[f"merged_{merge_mode}_l2"] = float(merged.norm(dim=1).mean().item())
                        first_batch = False
                    for row, weight_vector in enumerate(merged):
                        apply_hypernet_weights(model, weight_vector, rank, target)
                        with autocast_ctx:
                            loss_flat = model(x[row : row + 1], y[row : row + 1], reduction="none").view(-1)
                        y_flat = y[row : row + 1].view(-1)
                        nbytes = token_bytes[y_flat]
                        mask = nbytes > 0
                        total_nats += (loss_flat * mask).sum().item()
                        total_bytes += nbytes.sum().item()
            mode_final = total_nats / (math.log(2) * total_bytes)
        else:
            raise ValueError(f"Unsupported composition eval mode: {eval_mode}")
        merge_results[merge_mode] = {"final": mode_final, "improvement": baseline - mode_final}
    eval_elapsed = time.time() - eval_t0

    singles_mean_improvement = (
        sum(entry["improvement"] for entry in per_brick.values()) / len(per_brick) if per_brick else 0.0
    )
    for merge_mode, entry in merge_results.items():
        entry["retention_vs_singles_mean"] = (
            entry["improvement"] / singles_mean_improvement if singles_mean_improvement else 0.0
        )
    primary = merge_results[merge_modes[0]]
    result = {
        "experiment": f"compose-{''.join(brick[0].upper() for brick in bricks)}",
        "baseline": baseline,
        "final": primary["final"],
        "improvement": primary["improvement"],
        "bricks": bricks,
        "steps_per_brick": steps_per_brick,
        "lr": lr,
        "eval_mode": eval_mode,
        "bridge": bridge_spec,
        "allocation": allocation,
        "merge_modes": list(merge_modes),
        "merge_results": merge_results,
        "per_brick": per_brick,
        "singles_mean_improvement": singles_mean_improvement,
        "magnitudes": magnitudes,
        "steps": total_steps,
        "train_elapsed_s": train_elapsed_s,
        "eval_elapsed_s": eval_elapsed,
        "steps_per_second": (total_steps / train_elapsed_s) if train_elapsed_s > 0 else 0.0,
        "examples_seen": total_examples_seen,
        "tokens_seen": total_tokens_seen,
    }
    if is_frozen_basis_spec(bridge_spec):
        result["basis_diagnostics"] = frozen_basis_diagnostics(
            basis_dim_of(bridge_spec), total_lora_dim(model), seed if basis_seed is None else basis_seed, device
        )
    return result


def run_prefix_experiment(
    modality: str,
    checkpoint: str | Path = DEFAULT_MINI_CHECKPOINT,
    train_steps: int = 300,
    n_prefix: int = 8,
    lr: float = 1e-3,
    log_csv: str | None = None,
    eval_tokens: int | None = None,
    sensor_limit: int | None = None,
    seed: int = 42,
):
    seed_everything(seed)
    device, device_type = get_device()
    model, config, _ = load_lm(checkpoint)
    model = model.to(device)
    tokenizer = Tokenizer.from_directory()
    autocast_ctx = autocast_for(device_type)

    model.eval()
    with torch.no_grad(), autocast_ctx:
        baseline = evaluate_bpb(model, tokenizer, 8, eval_tokens=eval_tokens)

    for param in model.parameters():
        param.requires_grad_(False)
    raw = model._orig_mod if hasattr(model, "_orig_mod") else model

    bundle = load_modality_bundle(modality, device, limit=sensor_limit_for(modality, sensor_limit))
    prefix_proj = PrefixProjection(bundle.feature_dim, config.n_embd, n_prefix).to(device)

    optimizer = torch.optim.AdamW(prefix_proj.parameters(), lr=lr, weight_decay=0.01)
    text_loader = make_dataloader(tokenizer, 8, MAX_SEQ_LEN - n_prefix, "train")
    val_loader = make_dataloader(tokenizer, 8, MAX_SEQ_LEN - n_prefix, "val")
    step_log = StepLogger(log_csv) if log_csv else None

    total_time = 0.0
    steps = 0
    model.train()
    while steps < train_steps:
        t0 = time.time()
        indices = torch.randperm(len(bundle.data), device=device)[:8]
        sensor_batch = bundle.data[indices]
        features = bundle.get_features(sensor_batch)
        prefix_tokens = prefix_proj(features)

        tx, ty, _ = next(text_loader)
        tx = tx.to(device)
        ty = ty.to(device)
        with autocast_ctx:
            logits = _forward_with_prefix(raw, prefix_tokens, tx)
        # Dataloader targets are already shifted (y = row[1:]), so the logit at
        # combined position n_prefix+k predicts ty[k]: drop only the prefix part.
        text_logits = logits[:, n_prefix:]
        loss = F.cross_entropy(text_logits.reshape(-1, text_logits.size(-1)), ty.reshape(-1))

        loss.backward()
        torch.nn.utils.clip_grad_norm_(prefix_proj.parameters(), 1.0)
        optimizer.step()
        optimizer.zero_grad(set_to_none=True)
        if device.type == "mps":
            torch.mps.synchronize()
        elif device.type == "cuda":
            torch.cuda.synchronize()
        total_time += time.time() - t0
        if step_log and steps % 10 == 0:
            step_log.log(step=steps, elapsed_s=round(total_time, 1), loss=round(loss.item(), 6))
        steps += 1
    if step_log:
        step_log.close()

    model.eval()
    # Byte-weighted BPB, matching evaluate_bpb/_evaluate_bridge_bpb exactly, so
    # the prefix final is in the same units as the baseline it is compared to.
    token_bytes = get_token_bytes(device=device)
    total_nats = 0.0
    total_bytes = 0
    sensor_offset = 0
    eval_steps = max(1, (eval_tokens or EVAL_TOKENS) // (8 * (MAX_SEQ_LEN - n_prefix)))
    eval_t0 = time.time()
    with torch.no_grad():
        for _ in range(eval_steps):
            vx, vy, _ = next(val_loader)
            vx = vx.to(device)
            vy = vy.to(device)
            sensor_batch, sensor_offset = cycle_batch(bundle.data, vx.size(0), sensor_offset)
            prefix_tokens = prefix_proj(bundle.get_features(sensor_batch))
            # Same precision context as evaluate_bpb/_evaluate_bridge_bpb so the
            # baseline-vs-final comparison stays like-for-like on CUDA (bf16).
            with autocast_ctx:
                logits = _forward_with_prefix(raw, prefix_tokens, vx)
            text_logits = logits[:, n_prefix:]
            loss_flat = F.cross_entropy(
                text_logits.reshape(-1, text_logits.size(-1)),
                vy.reshape(-1),
                reduction="none",
            )
            vy_flat = vy.reshape(-1)
            nbytes = token_bytes[vy_flat]
            mask = nbytes > 0
            total_nats += (loss_flat * mask).sum().item()
            total_bytes += nbytes.sum().item()
    final = total_nats / (math.log(2) * total_bytes)
    eval_elapsed = time.time() - eval_t0
    result = {
        "experiment": f"prefix-{modality}-{n_prefix}tok",
        "baseline": baseline,
        "final": final,
        "improvement": baseline - final,
        "steps": steps,
        "n_prefix": n_prefix,
        "lr": lr,
        "params": sum(param.numel() for param in prefix_proj.parameters()),
        "eval_elapsed_s": eval_elapsed,
    }
    result.update(_throughput_metrics(total_time, steps, batch_size=8, seq_len=MAX_SEQ_LEN - n_prefix))
    return result


def _task_feature_for_condition(
    cond_mode: str,
    own_feature: torch.Tensor,
    alt_feature: torch.Tensor | None = None,
) -> torch.Tensor:
    if cond_mode == "true":
        return own_feature
    if cond_mode == "shuffled":
        if alt_feature is None:
            return own_feature
        return alt_feature
    if cond_mode == "random":
        return torch.randn_like(own_feature)
    raise ValueError(f"Unsupported task condition: {cond_mode}")


def _split_label_ids(prompt_ids: list[int], full_ids: list[int]) -> tuple[list[int], list[int]]:
    """Split the natural tokenization of prompt+label into shared context and label tokens.

    The template's trailing space can merge into the first label token, so the
    shared context can be shorter than the standalone prompt tokenization. Scoring
    everything after the longest common prefix guarantees no label token is lost.
    """
    common = 0
    for prompt_token, full_token in zip(prompt_ids, full_ids):
        if prompt_token != full_token:
            break
        common += 1
    return full_ids[:common], full_ids[common:]


def _stratified_subset(
    pairs: list[tuple[torch.Tensor, str]],
    max_items: int,
    seed: int,
) -> list[tuple[torch.Tensor, str]]:
    """Label-stratified, seed-shuffled eval subset (round-robin across labels)."""
    grouped: dict[str, list[tuple[torch.Tensor, str]]] = {}
    for pair in pairs:
        grouped.setdefault(pair[1], []).append(pair)
    selector = random.Random(seed)
    for items in grouped.values():
        selector.shuffle(items)
    labels = sorted(grouped)
    target = min(max_items, len(pairs))
    subset: list[tuple[torch.Tensor, str]] = []
    while len(subset) < target:
        progressed = False
        for label in labels:
            if grouped[label] and len(subset) < target:
                subset.append(grouped[label].pop())
                progressed = True
        if not progressed:
            break
    return subset


def _score_label(model, tokenizer: Tokenizer, context_ids: list[int], label_ids: list[int]) -> float:
    if not label_ids or not context_ids:
        return float("-inf")
    full = context_ids + label_ids
    x = torch.tensor([full[:-1]], dtype=torch.long, device=next(model.parameters()).device)
    with torch.no_grad():
        logits = model(x, targets=None)[0]
    start = len(context_ids) - 1
    positions = logits[start : start + len(label_ids)]
    log_probs = F.log_softmax(positions, dim=-1)
    targets = torch.tensor(label_ids, dtype=torch.long, device=logits.device)
    return log_probs[torch.arange(len(label_ids), device=logits.device), targets].mean().item()


def _train_task_bridge(
    model,
    tokenizer: Tokenizer,
    task_data: TaskDataset,
    bridge: nn.Module,
    optimizer,
    *,
    cond_mode: str,
    train_steps: int,
    rank: int,
    target: str,
    scoring_bos,
    device: torch.device,
) -> dict:
    """The paper-1 task-probe training loop (single source of truth).

    Shared by run_task_eval and run_composition_task_eval so a brick that is
    later merged is trained by exactly the same recipe as a brick that is
    measured alone.
    """
    total_time = 0.0
    steps = 0
    batch_size = min(4, len(task_data.train_pairs))
    model.train()
    while steps < train_steps:
        t0 = time.time()
        batch = random.sample(task_data.train_pairs, batch_size)
        alt_batch = batch[1:] + batch[:1]
        loss_total = 0.0
        for (sensor_data, label), (alt_sensor, _) in zip(batch, alt_batch):
            own_feature = task_data.get_feature(sensor_data)
            alt_feature = task_data.get_feature(alt_sensor)
            feature = _task_feature_for_condition(cond_mode, own_feature, alt_feature)
            weight_vector = bridge(feature)[0]
            apply_hypernet_weights(model, weight_vector, rank, target)
            ids = tokenizer.encode(task_data.prompt_template + label, prepend=scoring_bos)
            x = torch.tensor([ids[:-1]], dtype=torch.long, device=device)
            y = torch.tensor([ids[1:]], dtype=torch.long, device=device)
            loss_total = loss_total + model(x, y)
        (loss_total / len(batch)).backward()
        torch.nn.utils.clip_grad_norm_(bridge.parameters(), 1.0)
        optimizer.step()
        optimizer.zero_grad(set_to_none=True)
        if device.type == "mps":
            torch.mps.synchronize()
        elif device.type == "cuda":
            torch.cuda.synchronize()
        total_time += time.time() - t0
        steps += 1
    return {"steps": steps, "train_elapsed_s": total_time, "examples_seen": steps * batch_size}


def run_task_eval(
    modality: str,
    checkpoint: str | Path = DEFAULT_MINI_CHECKPOINT,
    train_steps: int = 600,
    rank: int = 4,
    target: str = "all",
    lr: float = 1e-3,
    max_eval_items: int = 200,
    seed: int = 42,
    bridge_spec: str = "dense",
    basis_lr_scale: float = 1.0,
    conditions: tuple[str, ...] = ("true", "shuffled", "random", "no_bridge"),
    slice_offset: int = 0,
    slice_width: int | None = None,
    basis_seed: int | None = None,
):
    device, _, = get_device()
    seed_everything(seed)
    task_data = load_task_dataset(modality, device)
    tokenizer = Tokenizer.from_directory()
    # HF base models (e.g. LFM) are trained with BOS at sequence start and are
    # far off-distribution without it; score prompt+label under the model's
    # natural document convention. The mini path stays BOS-free as published.
    scoring_bos = tokenizer.get_bos_token_id() if str(checkpoint).startswith("hf:") else None
    prompt_ids = tokenizer.encode(task_data.prompt_template, prepend=scoring_bos)

    results = {}
    all_conditions = {
        "true": "true",
        "shuffled": "shuffled",
        "random": "random",
        "no_bridge": "none",
    }
    selected = {name: all_conditions[name] for name in conditions}

    for cond_name, cond_mode in selected.items():
        seed_everything(seed)
        model, _, ckpt = load_lm(checkpoint)
        model = model.to(device)
        apply_lora(model, rank=rank, target=target)
        model = model.to(device)
        freeze_non_lora(model)
        lora_dim = total_lora_dim(model)

        if cond_mode != "none":
            bridge = make_bridge(
                bridge_spec,
                task_data.feature_dim,
                lora_dim,
                slice_offset=slice_offset,
                slice_width=slice_width,
                basis_seed=seed if basis_seed is None else basis_seed,
                device=device,
            ).to(device)
            trainable = list(bridge.parameters())
        else:
            bridge = None
            trainable = []

        # Same optimizer recipe as run_bridge_experiment (METHOD_CONTRACT §1.2):
        # mean loss over the batch, weight decay 0.01, grad clip 1.0.
        optimizer = (
            torch.optim.AdamW(bridge_param_groups(bridge, lr, basis_lr_scale), weight_decay=0.01)
            if trainable
            else None
        )
        total_time = 0.0
        steps = 0
        if cond_mode != "none":
            training = _train_task_bridge(
                model,
                tokenizer,
                task_data,
                bridge,
                optimizer,
                cond_mode=cond_mode,
                train_steps=train_steps,
                rank=rank,
                target=target,
                scoring_bos=scoring_bos,
                device=device,
            )
            total_time = training["train_elapsed_s"]
            steps = training["steps"]

        model.eval()
        test_subset = _stratified_subset(task_data.test_pairs, max_eval_items, seed)
        cached_features = [task_data.get_feature(sensor_data) for sensor_data, _ in test_subset]
        rank1 = 0
        top2 = 0
        ranks = []
        for idx, ((_, true_label), own_feature) in enumerate(zip(test_subset, cached_features)):
            if cond_mode == "none":
                zeros = torch.zeros(lora_dim, device=device)
                apply_hypernet_weights(model, zeros, rank, target)
            else:
                alt_feature = cached_features[(idx + 1) % len(cached_features)]
                feature = _task_feature_for_condition(cond_mode, own_feature, alt_feature)
                weight_vector = bridge(feature)[0]
                apply_hypernet_weights(model, weight_vector, rank, target)

            scored = []
            for category in task_data.categories:
                full_ids = tokenizer.encode(task_data.prompt_template + category, prepend=scoring_bos)
                context_ids, label_ids = _split_label_ids(prompt_ids, full_ids)
                scored.append((category, _score_label(model, tokenizer, context_ids, label_ids)))
            scored.sort(key=lambda item: item[1], reverse=True)
            ordered = [label for label, _ in scored]
            label_rank = ordered.index(true_label) + 1
            ranks.append(label_rank)
            if label_rank == 1:
                rank1 += 1
            if label_rank <= 2:
                top2 += 1

        n_eval = len(ranks)
        results[cond_name] = {
            "rank1": rank1 / n_eval if n_eval else 0.0,
            "top2": top2 / n_eval if n_eval else 0.0,
            "avg_rank": sum(ranks) / n_eval if n_eval else 0.0,
            "count": n_eval,
            "steps": steps,
            "lr": lr,
            "train_elapsed_s": total_time,
            "examples_seen": steps * min(4, len(task_data.train_pairs)),
        }

    return {
        "experiment": f"task-{modality}",
        "modality": modality,
        "bridge": bridge_spec,
        "basis_lr_scale": basis_lr_scale,
        "results": results,
    }


def _category_scoring_ids(tokenizer: Tokenizer, task_data: TaskDataset, prompt_ids: list[int], scoring_bos):
    prepared = []
    for category in task_data.categories:
        full_ids = tokenizer.encode(task_data.prompt_template + category, prepend=scoring_bos)
        context_ids, label_ids = _split_label_ids(prompt_ids, full_ids)
        prepared.append((category, context_ids, label_ids))
    return prepared


def _rank_of_label(model, tokenizer: Tokenizer, prepared, true_label: str) -> int:
    scored = [
        (category, _score_label(model, tokenizer, context_ids, label_ids))
        for category, context_ids, label_ids in prepared
    ]
    scored.sort(key=lambda item: item[1], reverse=True)
    return [label for label, _ in scored].index(true_label) + 1


def _prepare_batched_scoring(tokenizer: Tokenizer, task_data: TaskDataset, prompt_ids: list[int], scoring_bos, device):
    """Pack every category into one padded batch of scoring sequences.

    For a given eval item all categories are scored under the same conditioned
    weights and differ only in their label tokens, and a causal LM cannot see
    right-padding, so C separate forwards collapse into one batched forward with
    identical per-position logits. That is the difference between a 50-way audio
    probe grid costing minutes and costing hours.
    """
    rows = _category_scoring_ids(tokenizer, task_data, prompt_ids, scoring_bos)
    n_rows = len(rows)
    max_input = max(len(context) + len(label) for _, context, label in rows) - 1
    max_label = max(len(label) for _, _, label in rows)
    inputs = torch.zeros(n_rows, max_input, dtype=torch.long)
    positions = torch.zeros(n_rows, max_label, dtype=torch.long)
    targets = torch.zeros(n_rows, max_label, dtype=torch.long)
    mask = torch.zeros(n_rows, max_label, dtype=torch.bool)
    for row, (_, context_ids, label_ids) in enumerate(rows):
        full = context_ids + label_ids
        inputs[row, : len(full) - 1] = torch.tensor(full[:-1], dtype=torch.long)
        start = len(context_ids) - 1
        for offset, token in enumerate(label_ids):
            positions[row, offset] = start + offset
            targets[row, offset] = token
            mask[row, offset] = True
    return {
        "categories": [row[0] for row in rows],
        "inputs": inputs.to(device),
        "positions": positions.to(device),
        "targets": targets.to(device),
        "mask": mask.to(device),
        "rows": torch.arange(n_rows, device=device).unsqueeze(1),
    }


def _batched_label_rank(model, packed: dict, true_label: str) -> int:
    logits = model(packed["inputs"], targets=None)
    log_probs = F.log_softmax(logits, dim=-1)
    picked = log_probs[packed["rows"], packed["positions"], packed["targets"]]
    counts = packed["mask"].sum(dim=1).clamp(min=1)
    scores = (picked * packed["mask"]).sum(dim=1) / counts
    order = torch.argsort(scores, descending=True).tolist()
    return [packed["categories"][index] for index in order].index(true_label) + 1


def _probe_scores(ranks: list[int]) -> dict:
    count = len(ranks)
    return {
        "rank1": sum(1 for value in ranks if value == 1) / count if count else 0.0,
        "top2": sum(1 for value in ranks if value <= 2) / count if count else 0.0,
        "avg_rank": sum(ranks) / count if count else 0.0,
        "count": count,
    }


def run_composition_task_eval(
    task_bricks: list[str],
    context_bricks: list[str] | tuple[str, ...] = (),
    checkpoint: str | Path = DEFAULT_MINI_CHECKPOINT,
    task_steps: int = 600,
    text_steps: int = 300,
    rank: int = 4,
    target: str = "all",
    lr: float = 1e-3,
    max_eval_items: int = 64,
    seed: int = 42,
    bridge_spec: str = "basis-frozen-256",
    allocation: str = "shared",
    basis_seed: int | None = None,
    merge_modes: tuple[str, ...] = ("sum", "mean"),
    conditions: tuple[str, ...] = ("true", "shuffled", "random"),
    sensor_limit: int | None = None,
    eval_tokens: int | None = None,
    log_csv: str | None = None,
    task_steps_per_brick: dict[str, int] | None = None,
    gate_steps: int = 0,
    gate_modes: tuple[str, ...] = (),
    gate_balance_weight: float = 0.1,
):
    """Task probes under merged weights — the composition instrument.

    Every brick is trained alone, exactly as in the single-modality runs: task
    bricks (audio/imu, the ones with a label probe) on their task objective,
    context bricks (vision, which has no probe) on the text objective. At eval
    the bricks' LoRA deltas are merged and EACH task brick's own rank-1 probe is
    re-measured under the merged weights, against its own single-brick score and
    the paper-1 controls (shuffled/random features, no bridge), plus an
    others-only control that removes the measured brick from the merge.

    BPB retention is deliberately not the instrument here (paper 2 showed BPB
    gain tracks adaptation magnitude, so a mean merge scores dilution rather
    than interference); run_composition carries that secondary column.

    Merge modes: "sum" and "mean" are the phase-1 pair; "alpha-norm" rescales
    the sum so its L2 matches the measured brick's own single-brick delta at
    that item (the magnitude-mediated-damage hypothesis), and "alpha-rsqrtn"
    is the variance-preserving 1/sqrt(n) point. Gate modes (phase 2) replace
    the fixed merge with a per-brick convex combination; see _GateNet.
    """
    bricks = list(task_bricks) + list(context_bricks)
    assignments = slice_assignments(bridge_spec, len(bricks), allocation)
    slot = dict(zip(bricks, assignments))
    block_index = {brick: index for index, brick in enumerate(bricks)} if allocation == "layer" else {}
    basis_seed_value = seed if basis_seed is None else basis_seed
    steps_for = dict(task_steps_per_brick or {})
    gate_modes = tuple(gate_modes)

    device, _ = get_device()
    tokenizer = Tokenizer.from_directory()
    scoring_bos = tokenizer.get_bos_token_id() if str(checkpoint).startswith("hf:") else None

    train_elapsed_s = 0.0
    context: dict[str, dict] = {}
    for brick in context_bricks:
        offset, width = slot[brick]
        result = run_bridge_experiment(
            modality=brick,
            feature_mode="true",
            checkpoint=checkpoint,
            train_steps=text_steps,
            rank=rank,
            target=target,
            lr=lr,
            eval_tokens=eval_tokens,
            sensor_limit=sensor_limit,
            seed=seed,
            log_csv=_suffix_log_path(log_csv, brick),
            return_artifacts=True,
            bridge_spec=bridge_spec,
            slice_offset=offset,
            slice_width=width,
            basis_seed=basis_seed_value,
            layer_block_index=block_index.get(brick),
            n_layer_blocks=len(bricks) if allocation == "layer" else None,
        )
        artifacts = result.pop("artifacts")
        train_elapsed_s += result.get("train_elapsed_s", 0.0)
        context[brick] = {"artifacts": artifacts, "result": results_to_jsonable(result)}

    seed_everything(seed)
    model, _, _ = load_lm(checkpoint)
    model = model.to(device)
    apply_lora(model, rank=rank, target=target)
    model = model.to(device)
    freeze_non_lora(model)
    lora_dim = total_lora_dim(model)

    layer_blocks: list[tuple[int, int]] = []
    layer_bounds: list[int] = []
    if allocation == "layer":
        layer_blocks, layer_bounds = balanced_layer_blocks(lora_layer_sizes(model), len(bricks))

    task_datasets = {brick: load_task_dataset(brick, device) for brick in task_bricks}
    bridges: dict[str, dict[str, nn.Module]] = {}
    training_stats: dict[str, dict] = {}
    for brick in task_bricks:
        task_data = task_datasets[brick]
        offset, width = slot[brick]
        bridges[brick] = {}
        for cond in conditions:
            seed_everything(seed)
            bridge = make_bridge(
                bridge_spec,
                task_data.feature_dim,
                lora_dim,
                slice_offset=offset,
                slice_width=width,
                basis_seed=basis_seed_value,
                device=device,
                layer_range=layer_blocks[block_index[brick]] if allocation == "layer" else None,
            ).to(device)
            optimizer = torch.optim.AdamW(bridge_param_groups(bridge, lr), weight_decay=0.01)
            stats = _train_task_bridge(
                model,
                tokenizer,
                task_data,
                bridge,
                optimizer,
                cond_mode=cond,
                train_steps=steps_for.get(brick, task_steps),
                rank=rank,
                target=target,
                scoring_bos=scoring_bos,
                device=device,
            )
            bridge.eval()
            bridges[brick][cond] = bridge
            training_stats[f"{brick}-{cond}"] = stats
            train_elapsed_s += stats["train_elapsed_s"]

    for brick in context_bricks:
        context[brick]["artifacts"].bridge.eval()

    deployed_cond = {
        brick: ("true" if "true" in bridges[brick] else conditions[0]) for brick in task_bricks
    }

    def brick_delta(brick: str, flat: torch.Tensor) -> torch.Tensor:
        """The LoRA delta brick `brick` would apply given this (flat) feature."""
        if brick in bridges:
            return bridges[brick][deployed_cond[brick]](flat)[0]
        return context[brick]["artifacts"].bridge(flat)[0]

    def context_flat(brick: str, index: int) -> torch.Tensor:
        bundle = context[brick]["artifacts"].bundle
        item = bundle.data[index % len(bundle.data)].unsqueeze(0)
        return _flat_feature(bundle.get_features(item))

    # --- gated arm (phase 2): train the routers before anything is evaluated ---
    task_index = {brick: position for position, brick in enumerate(task_bricks)}
    gates: dict[str, nn.Module] = {}
    gate_stats: dict[str, dict] = {}
    learned_gate_modes = [mode for mode in gate_modes if mode != "gate-oracle"]
    gate_specs = {mode: parse_gate_mode(mode, gate_balance_weight) for mode in learned_gate_modes}
    if learned_gate_modes and gate_steps > 0:
        # The live slot and the ambient slots are drawn from the SAME pool per
        # brick, so nothing distinguishes "this brick owns the question" from
        # "this brick is just switched on" except which slot it lands in. Any
        # other arrangement would leak the answer to the router.
        gate_pool_size = 256
        train_pool: dict[str, list[torch.Tensor]] = {}
        gate_train_pairs: dict[str, list] = {}
        for brick in task_bricks:
            data = task_datasets[brick]
            gate_train_pairs[brick] = data.train_pairs[:gate_pool_size]
            train_pool[brick] = [_flat_feature(data.get_feature(sensor)) for sensor, _ in gate_train_pairs[brick]]
        for brick in context_bricks:
            bundle = context[brick]["artifacts"].bundle
            train_pool[brick] = [context_flat(brick, index) for index in range(min(gate_pool_size, len(bundle.data)))]
        feature_dims = [int(train_pool[brick][0].numel()) for brick in bricks]
        for mode in learned_gate_modes:
            spec = gate_specs[mode]
            seed_everything(seed)
            gate = GateNet(
                feature_dims,
                len(bricks),
                n_tasks=len(task_bricks) if spec["task"] else 0,
            ).to(device)
            # A three-way router has ~10k parameters against a brick's ~190k and
            # only `gate_steps` updates to move; the default is 10x the bridge lr
            # so that a failed gate is a failed *router*, not a failed optimizer.
            # v2 then showed 10x is itself the failure mode (saturation inside a
            # handful of steps), so `gate-*-lr-<x>` names its own multiplier.
            optimizer = torch.optim.AdamW(gate.parameters(), lr=lr * spec["lr_scale"], weight_decay=0.01)
            picker = random.Random(seed)
            model.train()
            gate_t0 = time.time()
            # Switch-Transformer-style load balancing, as a single-sample
            # surrogate: an EMA of the router's own output stands in for the
            # per-expert load, and the penalty n * sum_i load_i * g_i is
            # minimized when the gate spreads mass. Without it the router
            # saturates on whichever task moves the LM loss most, after which
            # the other experts' logits get no gradient at all.
            load_ema = torch.full((len(bricks),), 1.0 / len(bricks), device=device)
            balance_trace: list[float] = []
            entropy_trace: list[float] = []
            lam = spec["balance"]
            ent_w = spec["entropy"]
            for step in range(gate_steps):
                measured = task_bricks[step % len(task_bricks)]
                data = task_datasets[measured]
                sensor, label = picker.choice(gate_train_pairs[measured])
                flats = []
                for brick in bricks:
                    if brick == measured:
                        flats.append(_flat_feature(data.get_feature(sensor)))
                    else:
                        pool = train_pool[brick]
                        flats.append(pool[picker.randrange(len(pool))])
                with torch.no_grad():
                    deltas = torch.stack([brick_delta(brick, flat) for brick, flat in zip(bricks, flats)])
                weights = gate(flats, task_index=task_index[measured])
                merged = (weights.unsqueeze(1) * deltas).sum(dim=0)
                apply_hypernet_weights(model, merged, rank, target)
                ids = tokenizer.encode(data.prompt_template + label, prepend=scoring_bos)
                x = torch.tensor([ids[:-1]], dtype=torch.long, device=device)
                y = torch.tensor([ids[1:]], dtype=torch.long, device=device)
                loss = model(x, y)
                if lam:
                    balance = len(bricks) * (load_ema * weights).sum()
                    balance_trace.append(float(balance.item()))
                    loss = loss + lam * balance
                if ent_w:
                    # Entropy BONUS (subtracted from the loss): the v2 diagnosis
                    # was that the router saturates within a handful of steps,
                    # after which the softmax Jacobian is ~0 and the losing
                    # experts receive no gradient at all. Holding entropy up
                    # keeps every expert's logit alive long enough for the task
                    # embedding to separate them — or shows that it cannot.
                    entropy = -(weights * (weights + 1e-9).log()).sum()
                    entropy_trace.append(float(entropy.item()))
                    loss = loss - ent_w * entropy
                loss.backward()
                torch.nn.utils.clip_grad_norm_(gate.parameters(), 1.0)
                optimizer.step()
                optimizer.zero_grad(set_to_none=True)
                load_ema = 0.99 * load_ema + 0.01 * weights.detach()
                if device.type == "mps":
                    torch.mps.synchronize()
            gate.eval()
            gates[mode] = gate
            gate_stats[mode] = {"steps": gate_steps, "train_elapsed_s": time.time() - gate_t0}
            if balance_trace:
                gate_stats[mode]["balance_loss_last50_mean"] = sum(balance_trace[-50:]) / len(balance_trace[-50:])
                gate_stats[mode]["balance_weight"] = lam
            if entropy_trace:
                gate_stats[mode]["train_entropy_last50_mean"] = sum(entropy_trace[-50:]) / len(entropy_trace[-50:])
                gate_stats[mode]["entropy_weight"] = ent_w
            gate_stats[mode]["load_ema_final"] = [float(value) for value in load_ema]
            gate_stats[mode]["lr"] = lr * spec["lr_scale"]
            gate_stats[mode]["task_conditioned"] = bool(spec["task"])
            train_elapsed_s += gate_stats[mode]["train_elapsed_s"]

    model.eval()

    eval_subsets = {
        brick: _stratified_subset(task_datasets[brick].test_pairs, max_eval_items, seed) for brick in task_bricks
    }
    eval_features = {
        brick: [task_datasets[brick].get_feature(sensor_data) for sensor_data, _ in eval_subsets[brick]]
        for brick in task_bricks
    }

    results: dict[str, dict] = {}
    magnitudes: dict[str, dict] = {}
    coefficient_checks: dict[str, dict] = {}
    eval_t0 = time.time()
    with torch.no_grad():
        for measured in task_bricks:
            task_data = task_datasets[measured]
            prompt_ids = tokenizer.encode(task_data.prompt_template, prepend=scoring_bos)
            packed = _prepare_batched_scoring(tokenizer, task_data, prompt_ids, scoring_bos, device)
            subset = eval_subsets[measured]
            features = eval_features[measured]
            n_items = len(subset)
            other_names = [brick for brick in bricks if brick != measured]
            n_merged = 1 + len(other_names)

            # Ambient contribution of the other bricks: each other brick sees its
            # own held-out data, cycled against the measured brick's eval index.
            # Other bricks always contribute their deployed ("true") brick; only
            # the measured brick's condition varies.
            others = []
            other_deltas: list[list[torch.Tensor]] = []
            other_flats: list[list[torch.Tensor]] = []
            for index in range(n_items):
                vectors = []
                flats = []
                for other in other_names:
                    if other in task_datasets:
                        pool = eval_features[other]
                        flat = _flat_feature(pool[index % len(pool)])
                    else:
                        flat = context_flat(other, index)
                    flats.append(flat)
                    vectors.append(brick_delta(other, flat))
                others.append(torch.stack(vectors).sum(dim=0) if vectors else torch.zeros(lora_dim, device=device))
                if gate_modes:
                    other_deltas.append(vectors)
                    other_flats.append(flats)

            # Reference norm for the alpha-norm merge: the measured brick's own
            # deployed delta at this item. Taken from the deployed ("true")
            # bridge so that every condition and the others_only control are
            # rescaled to the same target, instead of collapsing to zero when
            # the measured brick is removed.
            deployed_measured = "true" if "true" in bridges[measured] else conditions[0]
            own_norm_ref = [
                float(bridges[measured][deployed_measured](feature)[0].norm().item()) for feature in features
            ]
            probe_for_block = bridges[measured][conditions[0]]
            own_block = (
                (probe_for_block.start, probe_for_block.end)
                if isinstance(probe_for_block, LayerSlicedBridge)
                else None
            )

            def merged_weight(own: torch.Tensor, index: int, mode: str) -> torch.Tensor:
                if mode == "single":
                    return own
                total = own + others[index]
                if mode == "sum":
                    return total
                if mode == "mean":
                    return total / n_merged
                if mode == "alpha-rsqrtn":
                    return total / math.sqrt(n_merged)
                if mode == "alpha-norm":
                    norm = float(total.norm().item())
                    return total * (own_norm_ref[index] / norm) if norm > 0 else total
                if mode.startswith("beta-"):
                    # Dose-response knob: attenuate the foreign bricks by beta,
                    # which sweeps cos(merged, own) continuously between 1 (the
                    # single brick) and the full merge, holding everything else
                    # fixed. beta-1 is exactly `sum`.
                    return own + float(mode.removeprefix("beta-")) * others[index]
                raise ValueError(f"Unsupported merge mode: {mode}")

            gate_trace: dict[str, list[list[float]]] = {mode: [] for mode in gate_modes}

            def gated_weight(own, index: int, mode: str, own_flat, record: bool = False):
                """Convex combination of the bricks under an input-conditioned gate.

                Brick order is `bricks`; the measured brick's slot carries `own`
                (which the caller may have zeroed for the others_only control)
                and the rest carry their ambient deltas at this eval index.
                """
                slots = {measured: (own, own_flat)}
                for other, delta, flat in zip(other_names, other_deltas[index], other_flats[index]):
                    slots[other] = (delta, flat)
                ordered = [slots[brick] for brick in bricks]
                if mode == "gate-oracle":
                    weights = torch.zeros(len(bricks), device=device)
                    weights[bricks.index(measured)] = 1.0
                else:
                    weights = gates[mode](
                        [flat for _, flat in ordered], task_index=task_index[measured]
                    )
                if record:
                    gate_trace[mode].append([float(value) for value in weights])
                stacked = torch.stack([delta for delta, _ in ordered])
                return (weights.unsqueeze(1) * stacked).sum(dim=0)

            all_merge_modes = tuple(merge_modes) + tuple(gate_modes)
            modes = ("single",) + all_merge_modes
            measured_results: dict[str, dict] = {mode: {} for mode in modes}
            for cond in conditions:
                bridge = bridges[measured][cond]
                for mode in modes:
                    ranks = []
                    for index, ((_, true_label), feature) in enumerate(zip(subset, features)):
                        alt_feature = features[(index + 1) % n_items]
                        cond_feature = _task_feature_for_condition(cond, feature, alt_feature)
                        own = bridge(cond_feature)[0]
                        if mode.startswith("gate-"):
                            weight = gated_weight(
                                own, index, mode, _flat_feature(cond_feature), record=(cond == "true")
                            )
                        else:
                            weight = merged_weight(own, index, mode)
                        if cond == "true" and index == 0:
                            magnitudes.setdefault(measured, {})[f"{mode}_l2"] = float(weight.norm().item())
                            magnitudes[measured]["own_l2"] = float(own.norm().item())
                            magnitudes[measured]["others_sum_l2"] = float(others[index].norm().item())
                            magnitudes[measured][f"{mode}_cos_own"] = float(
                                F.cosine_similarity(weight.unsqueeze(0), own.unsqueeze(0)).item()
                            )
                            if own_block is not None:
                                # The decisive pair of numbers for the layer arm:
                                # the GLOBAL cosine is diluted by the coordinates
                                # this brick never writes, while the cosine
                                # restricted to its own layer block is 1.0 by
                                # construction. If retention tracks the global
                                # number the angle account is global; if it
                                # tracks the block number the account is
                                # site-local and composition by site works.
                                start, end = own_block
                                magnitudes[measured]["layer_block"] = [start, end]
                                block_weight = weight[start:end]
                                block_own = own[start:end]
                                magnitudes[measured][f"{mode}_cos_own_inblock"] = float(
                                    F.cosine_similarity(
                                        block_weight.unsqueeze(0), block_own.unsqueeze(0)
                                    ).item()
                                )
                                magnitudes[measured]["others_in_own_block_l2"] = float(
                                    others[index][start:end].norm().item()
                                )
                                magnitudes[measured]["own_outside_block_l2"] = float(
                                    (own.norm() ** 2 - block_own.norm() ** 2).clamp_min(0).sqrt().item()
                                )
                        apply_hypernet_weights(model, weight, rank, target)
                        ranks.append(_batched_label_rank(model, packed, true_label))
                    measured_results[mode][cond] = _probe_scores(ranks)

            # Controls that do not depend on the measured brick's condition.
            zeros = torch.zeros(lora_dim, device=device)
            no_bridge_ranks = []
            for (_, true_label) in subset:
                apply_hypernet_weights(model, zeros, rank, target)
                no_bridge_ranks.append(_batched_label_rank(model, packed, true_label))
            measured_results["single"]["no_bridge"] = _probe_scores(no_bridge_ranks)
            for mode in all_merge_modes:
                ranks = []
                for index, (_, true_label) in enumerate(subset):
                    if mode.startswith("gate-"):
                        # Same gate weights the deployed brick would have got;
                        # only the measured brick's own delta is removed.
                        weight = gated_weight(zeros, index, mode, _flat_feature(features[index]))
                    else:
                        weight = merged_weight(zeros, index, mode)
                    apply_hypernet_weights(model, weight, rank, target)
                    ranks.append(_batched_label_rank(model, packed, true_label))
                measured_results[mode]["others_only"] = _probe_scores(ranks)

            # Weight-space bookkeeping: with disjoint slices the merged delta
            # still projects onto the measured brick's own basis block exactly
            # (ratio 1.0 under sum, 1/n under mean); a shared basis contaminates it.
            probe_bridge = bridges[measured][conditions[0]]
            if isinstance(probe_bridge, (FrozenBasisBridgeHyper, LayerSlicedBridge)):
                ratios: dict[str, list[float]] = {mode: [] for mode in merge_modes}
                errors: dict[str, list[float]] = {mode: [] for mode in merge_modes}
                for index in range(min(8, n_items)):
                    own_coefficients = probe_bridge.coefficients(features[index])[0]
                    own = probe_bridge(features[index])[0]
                    denom = float((own_coefficients @ own_coefficients).item())
                    for mode in merge_modes:
                        merged_full = merged_weight(own, index, mode)
                        if own_block is not None:
                            merged_full = merged_full[own_block[0] : own_block[1]]
                        recovered = merged_full @ probe_bridge.basis.T
                        ratios[mode].append(float((recovered @ own_coefficients).item()) / denom if denom else 0.0)
                        errors[mode].append(
                            float(((recovered - own_coefficients).norm() / own_coefficients.norm()).item())
                        )
                coefficient_checks[measured] = {
                    mode: {
                        "recovered_scale_ratio_mean": sum(ratios[mode]) / len(ratios[mode]),
                        "coefficient_rel_error_mean": sum(errors[mode]) / len(errors[mode]),
                    }
                    for mode in merge_modes
                }

            single_true = measured_results["single"]["true"]["rank1"]
            results[measured] = {
                "categories": len(task_data.categories),
                "chance_rank1": 1.0 / len(task_data.categories),
                "modes": measured_results,
                "retention": {
                    mode: (measured_results[mode]["true"]["rank1"] / single_true) if single_true else 0.0
                    for mode in all_merge_modes
                },
            }
            if gate_modes:
                # How much mass did each router put on the brick that actually
                # owns the question? A uniform gate is the mean merge; 1.0 is
                # the oracle. This is the diagnostic that says whether a failed
                # gate failed at routing or at composing.
                self_slot = bricks.index(measured)
                results[measured]["gate_weights"] = {
                    mode: _gate_row_stats(trace, self_slot) for mode, trace in gate_trace.items() if trace
                }
    eval_elapsed = time.time() - eval_t0

    result = {
        "experiment": f"compose-task-{''.join(brick[0].upper() for brick in bricks)}",
        "task_bricks": list(task_bricks),
        "context_bricks": list(context_bricks),
        "bricks": bricks,
        "bridge": bridge_spec,
        "allocation": allocation,
        "basis_seed": basis_seed_value,
        "slices": {brick: [offset, (offset + width) if width else basis_dim_of(bridge_spec)]
                   for brick, (offset, width) in slot.items()} if is_frozen_basis_spec(bridge_spec) else {},
        "merge_modes": list(merge_modes) + list(gate_modes),
        "fixed_merge_modes": list(merge_modes),
        "gate_modes": list(gate_modes),
        "gate_steps": gate_steps if gate_modes else 0,
        "gate_stats": gate_stats,
        "gate_specs": {mode: gate_specs[mode] for mode in learned_gate_modes} if gate_modes else {},
        "layer_blocks": (
            {brick: list(layer_blocks[block_index[brick]]) for brick in bricks} if allocation == "layer" else {}
        ),
        "layer_bounds": layer_bounds,
        "layer_sizes": lora_layer_sizes(model) if allocation == "layer" else [],
        "conditions": list(conditions),
        "task_steps": task_steps,
        "task_steps_per_brick": {brick: steps_for.get(brick, task_steps) for brick in task_bricks},
        "text_steps": text_steps,
        "lr": lr,
        "rank": rank,
        "target": target,
        "seed": seed,
        "max_eval_items": max_eval_items,
        "results": results,
        "magnitudes": magnitudes,
        "coefficient_checks": coefficient_checks,
        "context_results": {brick: entry["result"] for brick, entry in context.items()},
        "training_stats": training_stats,
        "trainable_params_per_brick": {
            brick: sum(p.numel() for p in bridges[brick][conditions[0]].parameters()) for brick in task_bricks
        },
        "lora_dim": lora_dim,
        "train_elapsed_s": train_elapsed_s,
        "eval_elapsed_s": eval_elapsed,
    }
    if is_frozen_basis_spec(bridge_spec) and allocation != "layer":
        result["basis_diagnostics"] = frozen_basis_diagnostics(
            basis_dim_of(bridge_spec), lora_dim, basis_seed_value, device
        )
    elif allocation == "layer":
        # One basis per layer block (each is orthonormal over its own block, and
        # the blocks are disjoint coordinate sets, so the three are mutually
        # orthogonal in the full space as well).
        result["basis_diagnostics"] = {
            brick: frozen_basis_diagnostics(
                basis_dim_of(bridge_spec),
                layer_blocks[block_index[brick]][1] - layer_blocks[block_index[brick]][0],
                basis_seed_value,
                device,
            )
            for brick in bricks
        }
    return result


def results_to_jsonable(result):
    if isinstance(result, dict):
        return {key: results_to_jsonable(value) for key, value in result.items() if key != "artifacts"}
    if isinstance(result, list):
        return [results_to_jsonable(value) for value in result]
    if isinstance(result, Path):
        return str(result)
    return result


def dump_result(result) -> str:
    return json.dumps(results_to_jsonable(result), indent=2, sort_keys=True)
