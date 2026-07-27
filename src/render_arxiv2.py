from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path
from typing import Any

from .render_arxiv import REPO_ROOT, copy_summary, fmt, load_summary, r, stats

# Paper-2 renderer. Every number comes from three artifacts: the basis-sweep
# summary (heterogeneous runs, names encode config), the LFM standard suite
# (dense references), and the LFM 10x suite (long-budget dense audio point).

DENSE_PARAMS = None  # read from the dense artifact at render time


def sres(sweep: dict[str, Any], name: str) -> dict[str, Any]:
    entry = sweep["results"].get(name)
    if not entry:
        raise KeyError(f"Missing sweep result: {name}")
    return entry["result"]


def simp(sweep: dict[str, Any], name: str) -> float:
    return float(sres(sweep, name)["improvement"])


def scos(sweep: dict[str, Any], name: str) -> float:
    return float(sres(sweep, name)["heldout_probe"]["cross_input_cosine_mean"])


def stask(sweep: dict[str, Any], name: str, condition: str = "true", field: str = "rank1") -> float:
    return float(sres(sweep, name)["results"][condition][field])


def task_std(payload: dict[str, Any], modality: str, condition: str = "true", field: str = "rank1") -> float:
    return float(r(payload, f"task-{modality}")["results"][condition][field])


def bridge_params(sweep: dict[str, Any], k: int) -> int:
    return int(sres(sweep, f"diversity-imu-l0.00-basis-{k}")["trainable_params"])


def frozen_trainable(sweep: dict[str, Any], k: int) -> int:
    res = sres(sweep, f"diversity-imu-l0.00-basis-{k}") if k != 64 else sres(sweep, f"constant-imu-basis-{k}")
    return int(res["trainable_params"]) - k * int(res["lora_dim"])


def capacity_table(sweep: dict[str, Any], dense: dict[str, Any], dense_params: int) -> str:
    d_bridge = float(r(dense, "diversity-imu-l0.00")["improvement"])
    d_const = float(r(dense, "constant-imu")["improvement"])
    d_cos = float(r(dense, "diversity-imu-l0.00")["heldout_probe"]["cross_input_cosine_mean"])
    lines = [
        rf"dense & {dense_params:,} & 100\% & {fmt(d_bridge, sign=True)} & {fmt(d_const, sign=True)} & {fmt(d_cos, 2)} \\"
    ]
    for k in (4, 16, 64, 256):
        params = bridge_params(sweep, k)
        lines.append(
            rf"basis-{k} & {params:,} & {params / dense_params * 100:.1f}\% & "
            rf"{fmt(simp(sweep, f'diversity-imu-l0.00-basis-{k}'), sign=True)} & "
            rf"{fmt(simp(sweep, f'constant-imu-basis-{k}'), sign=True)} & "
            rf"{fmt(scos(sweep, f'diversity-imu-l0.00-basis-{k}'), 2)} \\"
        )
    return "\n".join(lines)


def imu_task_table(sweep: dict[str, Any], dense: dict[str, Any]) -> str:
    dense_seeds = [
        task_std(dense, "imu"),
        stask(sweep, "task-imu-dense-seed1042"),
        stask(sweep, "task-imu-dense-seed2042"),
    ]
    b16_seeds = [
        stask(sweep, "task-imu-basis-16"),
        stask(sweep, "task-imu-basis-16-seed1042"),
        stask(sweep, "task-imu-basis-16-seed2042"),
    ]
    rows = [
        ("dense (trained)", dense_seeds),
        ("basis-16 (trained)", b16_seeds),
        ("basis-64 (trained)", [stask(sweep, "task-imu-basis-64")]),
        ("basis-256 (trained)", [stask(sweep, "task-imu-basis-256")]),
        ("basis-16 (frozen)", [stask(sweep, "task-imu-basis-16-blr0")]),
        ("basis-64 (frozen)", [stask(sweep, "task-imu-basis-64-blr0")]),
        ("basis-256 (frozen)", [stask(sweep, "task-imu-basis-256-blr0")]),
    ]
    lines = []
    for label, seeds in rows:
        per_seed = ", ".join(fmt(v, 2) for v in seeds)
        mean = sum(seeds) / len(seeds)
        lines.append(rf"{label} & {per_seed} & {fmt(mean, 2)} \\")
    return "\n".join(lines)


def lambda_table(sweep: dict[str, Any], dense: dict[str, Any]) -> str:
    lines = []
    for lam, dense_name, sweep_name in (
        (0.0, "diversity-imu-l0.00", "diversity-imu-l0.00-basis-16"),
        (0.05, "diversity-imu-l0.05", "diversity-imu-l0.05-basis-16"),
        (0.1, "diversity-imu-l0.10", "diversity-imu-l0.10-basis-16"),
        (0.2, "diversity-imu-l0.20", "diversity-imu-l0.20-basis-16"),
    ):
        dres = r(dense, dense_name)
        lines.append(
            rf"{lam:.2f} & {fmt(dres['improvement'], sign=True)} & "
            rf"{fmt(dres['heldout_probe']['cross_input_cosine_mean'], 2)} & "
            rf"{fmt(simp(sweep, sweep_name), sign=True)} & "
            rf"{fmt(scos(sweep, sweep_name), 2)} \\"
        )
    return "\n".join(lines)


def audio_budget_table(sweep: dict[str, Any], dense: dict[str, Any]) -> str:
    frozen_2400 = [
        stask(sweep, "task-audio-basis-256-s2400-blr0"),
        stask(sweep, "task-audio-basis-256-s2400-blr0-seed1042"),
        stask(sweep, "task-audio-basis-256-s2400-blr0-seed2042"),
    ]
    frozen_mean = sum(frozen_2400) / len(frozen_2400)
    rows = [
        ("600", fmt(task_std(dense, "audio"), 2), fmt(stask(sweep, "task-audio-basis-256"), 2), "--"),
        ("1200", fmt(stask(sweep, "task-audio-dense-s1200"), 2), fmt(stask(sweep, "task-audio-basis-256-s1200"), 2), fmt(stask(sweep, "task-audio-basis-256-s1200-blr0"), 2)),
        (
            "2400",
            fmt(stask(sweep, "task-audio-dense-s2400"), 2),
            fmt(stask(sweep, "task-audio-basis-256-s2400"), 2),
            rf"{fmt(frozen_mean, 2)} ({', '.join(fmt(v, 2) for v in frozen_2400)})",
        ),
    ]
    return "\n".join(rf"{steps} & {d} & {t} & {f} \\" for steps, d, t, f in rows)


def composition_table(sweep: dict[str, Any], dense: dict[str, Any]) -> str:
    def retention(get):
        singles = [get(tag) for tag in ("V", "A", "I")]
        triple = get("VAI")
        return sum(singles) / 3, triple, triple / (sum(singles) / 3)

    d_s, d_t, d_r = retention(lambda tag: float(r(dense, f"compose-{tag}")["improvement"]))
    t_s, t_t, t_r = retention(lambda tag: simp(sweep, f"compose-{tag}-basis-16"))
    f_s, f_t, f_r = retention(lambda tag: simp(sweep, f"compose-{tag}-basis-256-blr0"))
    lines = []
    for label, s, t, ratio in (
        ("dense", d_s, d_t, d_r),
        ("basis-16 (trained)", t_s, t_t, t_r),
        ("basis-256 (frozen)", f_s, f_t, f_r),
    ):
        lines.append(rf"{label} & {fmt(s, sign=True)} & {fmt(t, sign=True)} & {ratio * 100:.0f}\% \\")
    return "\n".join(lines)


def write_tex(sweep: dict[str, Any], dense: dict[str, Any], scaling: dict[str, Any], out_dir: Path) -> Path:
    st = stats(dense)
    dense_params = int(r(dense, "bridge-imu")["trainable_params"])
    lora_dim = int(r(dense, "bridge-imu")["lora_dim"])
    p16 = bridge_params(sweep, 16)
    fro256 = frozen_trainable(sweep, 256)
    fro64 = frozen_trainable(sweep, 64)
    b16_bpb = [
        simp(sweep, "diversity-imu-l0.00-basis-16"),
        simp(sweep, "bridge-imu-basis-16-seed1042"),
        simp(sweep, "bridge-imu-basis-16-seed2042"),
    ]
    b16_mean = sum(b16_bpb) / 3
    b16_spread = max(b16_bpb) - min(b16_bpb)
    dense_repro_imu = float(r(dense, "repro-imu")["mean_improvement"])
    imu_dense_mean = (task_std(dense, "imu") + stask(sweep, "task-imu-dense-seed1042") + stask(sweep, "task-imu-dense-seed2042")) / 3
    imu_b16_mean = (stask(sweep, "task-imu-basis-16") + stask(sweep, "task-imu-basis-16-seed1042") + stask(sweep, "task-imu-basis-16-seed2042")) / 3
    frozen_2400_mean = (
        stask(sweep, "task-audio-basis-256-s2400-blr0")
        + stask(sweep, "task-audio-basis-256-s2400-blr0-seed1042")
        + stask(sweep, "task-audio-basis-256-s2400-blr0-seed2042")
    ) / 3
    b16_l20 = simp(sweep, "diversity-imu-l0.20-basis-16")
    b16_l0 = simp(sweep, "diversity-imu-l0.00-basis-16")
    b16_cos20 = scos(sweep, "diversity-imu-l0.20-basis-16")
    dense_l0 = float(r(dense, "diversity-imu-l0.00")["improvement"])
    dense_l10 = float(r(dense, "diversity-imu-l0.10")["improvement"])
    dense_cos10 = float(r(dense, "diversity-imu-l0.10")["heldout_probe"]["cross_input_cosine_mean"])
    audio_dense_6000 = task_std(scaling, "audio")

    tex = rf"""
\ifdefined\XeTeXrevision\else\pdfoutput=1\fi
\documentclass[11pt]{{article}}
\usepackage[margin=1in]{{geometry}}
\usepackage{{graphicx}}
\usepackage{{booktabs}}
\usepackage{{amsmath}}
\usepackage{{amssymb}}
\usepackage{{xcolor}}
\usepackage{{hyperref}}
\usepackage{{microtype}}
\hypersetup{{
  colorlinks=true,
  linkcolor=blue!60!black,
  citecolor=blue!60!black,
  urlcolor=blue!60!black,
  pdftitle={{Two Regimes of Compressed Conditioning: Basis-Mixture Bridges for Frozen Language Models}},
  pdfauthor={{Franci Penov}},
}}
\graphicspath{{{{figures/}}}}
\title{{Two Regimes of Compressed Conditioning:\\Basis-Mixture Bridges for Frozen Language Models}}
\author{{Franci Penov \\ kortexa.ai \\ \texttt{{francip@kortexa.ai}}}}
\date{{2026-07-03}}

\begin{{document}}
\maketitle

\begin{{abstract}}
Conditional LoRA bridges condition a frozen language model on an external sensor stream by generating per-input low-rank weight updates, but the generating hypernetwork is dominated by one dense output layer that scales with the adapted model. We reparameterize that output as $k$ coefficients over a learned basis of LoRA directions and characterize the design space on a pretrained 230M-parameter model with capacity-matched controls, task-aligned probes, and weight-space diversity probes. Two regimes emerge. With a small \emph{{trained}} basis ($k{{=}}16$; {dense_params / p16:.0f}$\times$ fewer parameters), the bridge matches the dense hypernetwork's language-modeling gain and its six-way task conditioning, and the diversity--quality tradeoff dissolves: cross-input cosine of generated weights falls from {fmt(scos(sweep, 'diversity-imu-l0.00-basis-16'), 2)} to {fmt(b16_cos20, 2)} with no loss of language-modeling improvement, where the dense bridge pays for every increment. With a large \emph{{frozen}} basis ($k{{=}}256$, reconstructible from a random seed), only {fro256:,} parameters ({fro256 / dense_params * 100:.2f}\% of dense) train, and the bridge reaches the dense model's hard-task conditioning at roughly twice the training steps. At the standard budget that step-for-parameter trade applies to every basis size we tested on the fifty-way task. A span threshold separates the regimes, and it scales with task complexity: a frozen random subspace of 64 directions supports six-way IMU conditioning but is at chance on fifty-way audio, where 256 directions succeed. We also report what fails: accelerating basis training destabilizes it; training the basis above the span threshold is mildly harmful; and composing bridges by coefficient averaging inherits the sub-additivity of weight averaging. The obstacle is the merge operation, not the representation.
\end{{abstract}}

\section{{Introduction}}
A conditional LoRA bridge \cite{{penov2026bridges}} maps features from a frozen sensor encoder to per-input Low-Rank Adaptation (LoRA) parameters injected into a frozen language model, giving the model an ambient, token-free awareness of an external signal. The original study established an evaluation discipline (language-modeling metrics cannot certify conditioning; capacity-matched controls and task-aligned probes can) and named its scaling bottleneck: the bridge's final linear layer emits the full flattened LoRA vector, so its parameter count grows with the adapted model. On the 230M-parameter model used here, the dense bridge has {dense_params / 1e6:.0f}M parameters against a {lora_dim:,}-dimensional LoRA vector \cite{{penov2026note}}.

This paper attacks that bottleneck by construction. The bridge's output layer is replaced by a coefficient head: the hypernetwork emits $k$ coefficients $c$, and the generated weights are $w = c \cdot B$ for a $k \times D$ basis $B$ of LoRA directions. Compression is trivial by construction; the cost is not. That cost has a structure: a \emph{{span threshold}} in $k$, scaling with task complexity, that separates two operating regimes with qualitatively different economics. Contributions:
\begin{{itemize}}
  \item \textbf{{A trained-basis regime}} ($k$ small): {dense_params / p16:.0f}$\times$ fewer bridge parameters with language-modeling gains slightly above dense ({fmt(b16_mean, sign=True)} vs {fmt(dense_repro_imu, sign=True)} on IMU, three seeds each) and six-way task conditioning at parity ({fmt(imu_b16_mean, 2)} vs {fmt(imu_dense_mean, 2)} mean rank-1); on the fifty-way task, small trained bases share the step-for-parameter trade quantified below. In this regime the diversity--quality tradeoff reported for dense bridges dissolves.
  \item \textbf{{A frozen-basis regime}} ($k$ large): with the basis frozen at its random orthonormal initialization (reconstructible from an RNG seed, so never stored), only the coefficient head trains ({fro256:,} parameters, {fro256 / dense_params * 100:.2f}\% of dense), reaching dense-level conditioning on a fifty-way task at roughly $2\times$ the steps.
  \item \textbf{{The span threshold}} separating them, measured at two task complexities, plus three informative negatives: faster basis learning rates destabilize training, basis training above the threshold is mildly harmful, and coefficient-space composition inherits weight-space sub-additivity exactly.
\end{{itemize}}
All experiments use the published bridge harness and its controls unchanged \cite{{penov2026bridges,penov2026note}}; the reparameterization is the only manipulated variable.

\section{{Method}}
\paragraph{{Dense bridge (baseline).}}
The published bridge maps a sensor feature $f$ through a small trunk to a 256-dimensional representation $h$, then through a dense output layer to the flattened LoRA vector $w \in \mathbb{{R}}^D$, applied per input to the frozen model's attention and MLP projections at rank 4. The output layer holds $257 \cdot D$ of the bridge's parameters, {dense_params / 1e6:.0f}M of them at $D = {lora_dim:,}$.

\paragraph{{Basis-mixture bridge.}}
We replace the output layer with a coefficient head $h \mapsto c \in \mathbb{{R}}^k$ and a basis $B \in \mathbb{{R}}^{{k \times D}}$, generating $w = c \cdot B$. $B$ is initialized with orthonormal rows; the head is initialized near zero, so generated weights start near zero exactly as in the dense bridge. Parameters: $kD$ for the basis plus a fixed $\sim$115k-parameter trunk and a head with $257 \cdot k$ parameters, running from {bridge_params(sweep, 4) / 1e6:.1f}M at $k{{=}}4$ to {bridge_params(sweep, 256) / 1e6:.0f}M at $k{{=}}256$.

\paragraph{{Frozen variant.}}
Setting the basis learning rate to zero freezes $B$ at initialization. The basis then never needs storage, since it is a deterministic function of the seed, and the trainable footprint collapses to the trunk and head: {frozen_trainable(sweep, 16):,} parameters at $k{{=}}16$, {fro64:,} at $k{{=}}64$, {fro256:,} at $k{{=}}256$.

\paragraph{{Controls and probes.}}
All of the original study's instruments apply unchanged: the capacity-matched constant-feature control (the same bridge trained on a fixed input) isolates trainable capacity from conditioning; task-aligned ranking probes measure whether generated weights carry input identity (six-way IMU activities, chance 0.17; fifty-way audio events, chance 0.02); the held-out weight-space probe measures cross-input cosine of generated weights (lower = more input-dependent).

\section{{Setup}}
The base model is LiquidAI LFM~2.5 230M, adapted through the harness's HuggingFace checkpoint path; porting details (LoRA target mapping, byte-exact bits-per-byte across tokenizers, sequence-start handling) are documented in the accompanying replication note \cite{{penov2026note}}, which also establishes the dense reference values used throughout. Standard budget: 300 benchmark steps (batch 8) and 600 task-probe steps (batch 4), learning rate $10^{{-3}}$, seed 42 (three seeds where stated); audio task runs extend to 1200 and 2400 steps where budget is the variable under study. BPB improvements are measured against the frozen baseline on a fixed 32{{,}}768-token validation stream.

\section{{Results}}

\subsection{{Capacity: compression is free at every $k$}}
Table~\ref{{tab:capacity}} and Figure~\ref{{fig:capacity}} sweep $k$ at the standard budget on IMU. Every basis bridge matches or exceeds the dense bridge's BPB improvement, including $k{{=}}4$ at {bridge_params(sweep, 4) / dense_params * 100:.1f}\% of its parameters, and the three-seed spread at $k{{=}}16$ is {b16_spread:.4f}. The capacity/conditioning decomposition survives reparameterization: the constant-feature control matches the true-feature bridge at every $k$, so BPB gains remain attributable to capacity, not sensing, exactly as in the dense case. The $k{{=}}256$ row doubles as an equal-size control: it has {bridge_params(sweep, 256) / dense_params * 100:.1f}\% of the dense parameter count with the same behavior profile as the other basis rows, so the differences documented below are structural, not size effects.

\begin{{table}}[t]
\centering
\caption{{Capacity sweep on IMU at the standard budget (seed 42; $k{{=}}16$ BPB confirmed over three seeds). Constant = capacity-matched control. Cross-cos = cross-input cosine of generated weights at $\lambda = 0$ (1.0 = fully input-independent).}}
\label{{tab:capacity}}
\begin{{tabular}}{{lrrrrr}}
\toprule
Bridge & Params & \% dense & $\Delta$BPB & Constant & Cross-cos \\
\midrule
{capacity_table(sweep, dense, dense_params)}
\bottomrule
\end{{tabular}}
\end{{table}}


\begin{{figure}}[t]
\centering
\includegraphics[width=0.82\linewidth]{{paper2_capacity.png}}
\caption{{BPB improvement vs.\ bridge parameterization (IMU, standard budget). Every basis size matches or exceeds the dense bridge; labels round to four decimals while bar heights are exact.}}
\label{{fig:capacity}}
\end{{figure}}

\subsection{{Task conditioning: parity for trained bases}}
Table~\ref{{tab:imutask}} reports the six-way IMU probe. The trained $k{{=}}16$ bridge averages {fmt(imu_b16_mean, 2)} rank-1 over three seeds against the dense bridge's {fmt(imu_dense_mean, 2)}; every control (no-bridge, shuffled, random features) sits at chance in every run. Seed spread is wide for both (dense {fmt(task_std(dense, 'imu'), 2)}--{fmt(stask(sweep, 'task-imu-dense-seed2042'), 2)}; basis-16 {fmt(stask(sweep, 'task-imu-basis-16-seed2042'), 2)}--{fmt(stask(sweep, 'task-imu-basis-16'), 2)}), and single-seed values for $k{{=}}64$ and $k{{=}}256$ fall inside it: we detect no systematic dependence of easy-task conditioning on $k$ for trained bases. The fifty-way audio probe separates the parameterizations more sharply at the standard budget: trained bases reach {fmt(stask(sweep, "task-audio-basis-16"), 2)} ($k{{=}}16$), {fmt(stask(sweep, "task-audio-basis-64"), 2)} ($k{{=}}64$), and {fmt(stask(sweep, "task-audio-basis-256"), 2)} ($k{{=}}256$) against the dense bridge's {fmt(task_std(dense, "audio"), 2)}: well above chance, well below dense. Section~\ref{{sec:span}} shows this gap closing with training budget for $k{{=}}256$; we did not budget-extend the smaller $k$.

\begin{{table}}[t]
\centering
\caption{{Six-way IMU task probe (rank-1 accuracy, chance 0.17), true-feature condition; all controls at chance in every run. Frozen rows use the basis at random initialization.}}
\label{{tab:imutask}}
\begin{{tabular}}{{lll}}
\toprule
Bridge & Per-seed rank-1 & Mean \\
\midrule
{imu_task_table(sweep, dense)}
\bottomrule
\end{{tabular}}
\end{{table}}

\subsection{{The diversity--quality tradeoff dissolves in coefficient space}}
For dense bridges, enforcing input-dependent weights costs language-modeling quality: at $\lambda = 0.10$ the dense bridge gives up {fmt(dense_l0 - dense_l10, 4)} BPB to reach cross-input cosine {fmt(dense_cos10, 2)}, and the original small-model study reported complete erasure at the strongest penalty. Table~\ref{{tab:lambda}} shows the trained $k{{=}}16$ bridge escaping the tradeoff entirely: cosine falls monotonically from {fmt(scos(sweep, 'diversity-imu-l0.00-basis-16'), 2)} to {fmt(b16_cos20, 2)}, giving near-orthogonal per-input weights, while $\Delta$BPB stays within noise of its unregularized value ({fmt(b16_l20, sign=True)} vs {fmt(b16_l0, sign=True)}). In a 16-dimensional coefficient space, input-dependence and text quality stop competing: the basis can orient its few directions so that both objectives are satisfiable at once. The frozen variant does not share this property (its diversity cost ratio resembles the dense bridge's), so free diversity is specifically a property of \emph{{trained}} low-dimensional coefficient spaces.

\begin{{table}}[t]
\centering
\caption{{Diversity sweep on IMU (standard budget, seed 42): the dense bridge trades BPB for input-dependence; the trained basis-16 bridge does not.}}
\label{{tab:lambda}}
\begin{{tabular}}{{rrrrr}}
\toprule
 & \multicolumn{{2}}{{c}}{{dense}} & \multicolumn{{2}}{{c}}{{basis-16 (trained)}} \\
$\lambda$ & $\Delta$BPB & Cross-cos & $\Delta$BPB & Cross-cos \\
\midrule
{lambda_table(sweep, dense)}
\bottomrule
\end{{tabular}}
\end{{table}}

\subsection{{The span threshold and the frozen regime}}
\label{{sec:span}}
The frozen rows of Table~\ref{{tab:imutask}} and the audio results in Table~\ref{{tab:budget}} locate the paper's central structure. A frozen random basis of 16 directions supports nothing: the IMU probe is at chance ({fmt(stask(sweep, 'task-imu-basis-16-blr0'), 2)}) and even the capacity gain vanishes ($\Delta$BPB {fmt(simp(sweep, 'diversity-imu-l0.10-basis-16-blr0'), sign=True)} under regularization). Sixteen random directions in a {lora_dim:,}-dimensional weight space almost surely span nothing useful, and below this threshold the basis \emph{{must}} be learned. At $k{{=}}64$ the frozen basis supports the six-way task ({fmt(stask(sweep, 'task-imu-basis-64-blr0'), 2)}) but is at chance on the fifty-way one ({fmt(stask(sweep, 'task-audio-basis-64-s1200-blr0'), 2)} at 1200 steps). At $k{{=}}256$ it supports both. The threshold scales with the task's complexity rather than being a constant of the architecture: the random subspace must be wide enough to intersect the directions the task requires.

Above the threshold, freezing is an advantage rather than a compromise. Table~\ref{{tab:budget}} and Figure~\ref{{fig:budget}} track the fifty-way audio probe across training budgets: the frozen $k{{=}}256$ bridge reaches {fmt(frozen_2400_mean, 2)} mean rank-1 at 2400 steps (three seeds), the level the dense bridge reaches at 1200 ({fmt(stask(sweep, 'task-audio-dense-s1200'), 2)}). That is dense-level conditioning at $\sim$$2\times$ the steps from {fro256 / dense_params * 100:.2f}\% of the trainable parameters, with the basis reproducible from a seed rather than stored. The same table shows the trained $k{{=}}256$ basis \emph{{trailing}} its own frozen variant at 2400 steps ({fmt(stask(sweep, 'task-audio-basis-256-s2400'), 2)} vs {fmt(frozen_2400_mean, 2)}): above the span threshold, a churning basis is a moving target for the coefficient head, and stationarity wins. The dense bridge continues to improve with budget ({fmt(stask(sweep, 'task-audio-dense-s2400'), 2)} at 2400; {fmt(audio_dense_6000, 2)} at 6000 in the replication note's $10\times$ suite \cite{{penov2026note}}), so the frozen regime buys its parameter economy with training compute, not with a performance ceiling we could detect.

\begin{{table}}[t]
\centering
\caption{{Fifty-way audio task probe (rank-1, chance 0.02) vs.\ training budget, seed 42 except where noted. The frozen $k{{=}}256$ value at 2400 steps is a three-seed mean (per-seed values in parentheses).}}
\label{{tab:budget}}
\begin{{tabular}}{{rlll}}
\toprule
Steps & dense & basis-256 (trained) & basis-256 (frozen) \\
\midrule
{audio_budget_table(sweep, dense)}
\bottomrule
\end{{tabular}}
\end{{table}}


\begin{{figure}}[t]
\centering
\includegraphics[width=0.82\linewidth]{{paper2_audio_budget.png}}
\caption{{Fifty-way audio conditioning vs.\ training budget. The frozen $k{{=}}256$ bridge (181k trainable parameters) reaches at 2400 steps the level the dense bridge (199M) reaches at 1200; the trained basis trails its own frozen variant.}}
\label{{fig:budget}}
\end{{figure}}

\subsection{{What does not work}}
\label{{sec:negative}}
\paragraph{{Accelerating the basis.}}
If the frozen regime's $2\times$ step cost came from a slowly-rotating basis, raising the basis learning rate should recover it. The opposite happens: at 1200 audio steps, scaling the basis learning rate by $3\times$ drops rank-1 from {fmt(stask(sweep, 'task-audio-basis-256-s1200'), 2)} to {fmt(stask(sweep, 'task-audio-basis-256-s1200-blr3'), 2)}, and $10\times$ to {fmt(stask(sweep, 'task-audio-basis-256-s1200-blr10'), 2)}, near chance. The coefficient head learns against the basis; making the basis move faster destroys the target it is learning to address. Consistent with this, the frozen basis at the same budget matches the trained one ({fmt(stask(sweep, 'task-audio-basis-256-s1200-blr0'), 2)} vs {fmt(stask(sweep, 'task-audio-basis-256-s1200'), 2)}): basis training contributes nothing above the span threshold, and the head does all the work.

\paragraph{{Composition by coefficient averaging.}}
With a shared basis, averaging generated weights is algebraically identical to averaging coefficients ($\mathrm{{mean}}(c_i B) = \mathrm{{mean}}(c_i) B$), so the harness's additive-merge composition directly tests coefficient-space composition. Table~\ref{{tab:compose}}: it inherits the dense bridge's sub-additivity, slightly worse. The interference comes from the averaging operation, which dilutes each constituent's contribution regardless of the space it is expressed in. (The frozen row's low absolute values reflect its $2\times$ budget law: the 150-step bricks are under-trained, so its retention should be read with caution.) Constructive composition needs a different merge, not a different representation; we return to this in the discussion.

\begin{{table}}[t]
\centering
\caption{{Additive-merge composition (BPB improvement; vision+audio+IMU triple vs.\ mean of singles; 150 steps/brick, standard protocol).}}
\label{{tab:compose}}
\begin{{tabular}}{{lrrr}}
\toprule
Bridge & Singles mean & Triple & Retention \\
\midrule
{composition_table(sweep, dense)}
\bottomrule
\end{{tabular}}
\end{{table}}

\section{{Related Work}}
Static-coefficient random-basis adaptation is well established: PRANC \cite{{nooralinejad2023pranc}} trains coefficients over seed-reconstructible pseudo-random basis networks; NOLA \cite{{koohpayegani2024nola}} applies the idea to LoRA factors; VeRA \cite{{kopiczko2024vera}} shares one frozen random matrix pair across layers with trained per-layer scalings; RandLoRA \cite{{albert2025randlora}} scales many frozen random low-rank matrices to full-rank updates; VB-LoRA \cite{{li2024vblora}} mixes from a shared \emph{{learned}} vector bank. All train coefficients once per task. Input-conditioned mixing exists over \emph{{trained}} factors: TopLoRA \cite{{li2025toplora}} generates per-token diagonal coefficients modulating learned per-module LoRA factors --- the closest prior work to ours --- HydraLoRA \cite{{tian2024hydralora}} routes per sample over trained expert heads, and the mixture-of-LoRA-experts line routes per token \cite{{wu2024mole}}. Hypernetworks that generate adapters condition on task descriptions or exemplars rather than individual inputs: HyperTuning \cite{{phang2022hypertuning}}, Text-to-LoRA \cite{{charakorn2025texttolora}}. Against all three lines, our setting combines a frozen \emph{{random}} shared basis with coefficients generated \emph{{per input}} by a hypernetwork --- and conditioned on an external sensor stream rather than the text itself \cite{{penov2026bridges}}. To our knowledge no prior work occupies this intersection, and none reports an analog of the span threshold, the free-diversity property of trained low-dimensional coefficient spaces, or capacity-vs-conditioning probes for generated weights. LoRA composition via learned per-task mixing (LoraHub \cite{{huang2024lorahub}}) contrasts with our per-input merge negative; tying and factor-freezing for parameter economy appear in Tied-LoRA \cite{{renduchintala2024tiedlora}} and LoRA-XS \cite{{balazy2024loraxs}}.

\section{{Discussion}}
The two regimes answer different engineering questions. When bridge quality and conditioning fidelity dominate (a deployed always-on sensor with a modest parameter budget), the trained small basis dominates the dense bridge on the axes we measured for single-sensor deployment: {dense_params / p16:.0f}$\times$ smaller, language-modeling gain slightly higher, six-way conditioning at parity, and diversity regularization free. It still shares the family's step-for-parameter trade on harder tasks and, like every parameterization tested, composes sub-additively. When parameter and storage economy dominate (many sensors, many model versions, over-the-air updates), the frozen seeded basis reduces the entire sensor-specific artifact to a $\sim${fro256 / 1000:.0f}k-parameter head plus a seed, at the cost of a task-complexity-dependent minimum $k$ and roughly doubled training. The span threshold gives the selection rule: estimate task complexity, size $k$ with margin, freeze if $k$ clears the threshold, train the basis if it cannot.

The composition negative sharpens the agenda the original paper left open. Since the interference comes from the merge operation rather than the representation, the shared frozen basis becomes an asset rather than a fix: it makes \emph{{disjoint coefficient allocation}} trivial (each modality claims its own block of an orthonormal basis, making weight-space interference zero by construction), and it makes task-level composition probes the right instrument, since BPB retention mostly measures adaptation magnitude surviving a mean. Both are mechanical extensions of the present harness.

\section{{Limitations}}
All results are on one pretrained base model and two sensor task complexities; the span threshold is bracketed ($16 < k^* \le 64$ for six-way IMU, $64 < k^* \le 256$ for fifty-way audio), not mapped. Task probes beyond $k{{=}}16$ and the $\lambda$ sweep are single-seed; the IMU probe's own seed spread is wide, so per-$k$ differences on the easy task should not be over-read. The frozen regime's $2\times$ step law is measured at one task and bracketed budgets. BPB retention is a weak composition metric, used here only to show the negative transfers across parameterizations. Conclusions about scale inherit the caveats of the replication note \cite{{penov2026note}}, including the pretraining-vs-scale confound.

\section{{Conclusion}}
Reparameterizing a conditional LoRA bridge's output as coefficients over a basis of LoRA directions turns its main scaling liability into a design space with two useful regimes: a trained low-dimensional regime that compresses {dense_params / p16:.0f}$\times$ while dissolving the diversity--quality tradeoff, and a frozen seeded regime that reduces the trainable and storable footprint to a coefficient head at {fro256 / dense_params * 100:.2f}\% of the dense bridge, for a measured $2\times$ training cost. A span threshold that grows with task complexity separates the regimes and gives practitioners a selection rule. The failures are as instructive as the successes: the basis should be stationary or absent, not fast, and composition fails in coefficient space exactly as it does in weight space. That locates the problem in the merge operation, and makes disjoint allocation over a shared frozen basis the next constructive step.

\section*{{Reproducibility Statement}}
All experiments run through the published bridge harness with the basis parameterization selected by \texttt{{--bridge basis-<k>}} and the frozen variant by \texttt{{--basis-lr-scale 0}}. Every number in this manuscript is rendered from three bundled artifacts (the basis-sweep summary and the two dense reference suites) by the repository's renderer; run names in the sweep artifact encode each experiment's configuration. Code, artifacts, and the exact render pipeline: \url{{https://github.com/kortexa-ai/legolm.basis}}.

\bibliographystyle{{plain}}
\bibliography{{references}}
\end{{document}}
"""
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "main.tex"
    target.write_text(tex.strip() + "\n")
    return target


def main() -> None:
    parser = argparse.ArgumentParser(description="Render the basis-mixture paper from three artifacts")
    parser.add_argument("--sweep", type=Path, default=REPO_ROOT / "results" / "lfm230m-basis-sweep-20260702" / "summary.json")
    parser.add_argument("--dense", type=Path, default=REPO_ROOT / "results" / "lfm230m-standard-20260701" / "summary.json")
    parser.add_argument("--dense-scaling", type=Path, default=REPO_ROOT / "results" / "lfm230m-scaling-20260701" / "summary.json")
    parser.add_argument("--output-dir", type=Path, default=REPO_ROOT / "arxiv2")
    parser.add_argument("--figures-dir", type=Path, default=REPO_ROOT / "figures2")
    parser.add_argument("--compile", action="store_true")
    args = parser.parse_args()

    sweep = load_summary(args.sweep)
    dense = load_summary(args.dense)
    scaling = load_summary(args.dense_scaling)
    tex = write_tex(sweep, dense, scaling, args.output_dir)
    print(f"Wrote {tex}")
    for src_path, name in ((args.sweep, "summary-sweep.json"), (args.dense, "summary-dense.json"), (args.dense_scaling, "summary-dense-scaling.json")):
        copy_summary(src_path, args.output_dir, name)
    if args.figures_dir.exists():
        fig_dst = args.output_dir / "figures"
        fig_dst.mkdir(parents=True, exist_ok=True)
        for png in args.figures_dir.glob("paper2_*.png"):
            shutil.copy2(png, fig_dst / png.name)
    if args.compile:
        subprocess.run(["tectonic", "-X", "compile", "main.tex", "--keep-intermediates", "--keep-logs"], cwd=args.output_dir, check=True)


if __name__ == "__main__":
    main()
