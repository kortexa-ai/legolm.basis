from __future__ import annotations

import argparse
import math
import shutil
import subprocess
from pathlib import Path
from typing import Any

from .render_arxiv import REPO_ROOT
from .report_disjoint import compose_runs, load

# Paper-7 renderer. Every number comes from the phase-1/2/3 composition
# artifacts, read by the same loader `src/report_disjoint.py` uses for the run
# READMEs, so the manuscript and the run reports cannot disagree. Nothing here
# is typed by hand; editing `arxiv7/main.tex` is reverted on the next render.

RESULT_DIRS = (
    REPO_ROOT / "results" / "lfm230m-disjoint-20260802",
    REPO_ROOT / "results" / "lfm230m-disjoint-p2-20260803",
    REPO_ROOT / "results" / "lfm230m-decisive-20260803",
)

ROUTER_SEEDS = (42, 1042, 2042, 3042, 4042, 5042, 6042, 7042)
GATE_THRESHOLD = 0.80


# --------------------------------------------------------------------------
# artifact accessors
# --------------------------------------------------------------------------


def artifact_dirs(explicit: list[Path] | None) -> list[Path]:
    """Prefer the live result directories; fall back to the bundled snapshot.

    The public snapshot ships `arxiv7/artifacts/` and gitignores `results/`, so
    the paper re-renders there without the runs being present.
    """
    if explicit:
        return explicit
    live = [path for path in RESULT_DIRS if path.exists()]
    return live if live else [REPO_ROOT / "arxiv7" / "artifacts"]


def fmt(value: float, digits: int = 3) -> str:
    return f"{value:.{digits}f}"


def pct(value: float, digits: int = 1) -> str:
    return f"{value * 100:.{digits}f}"


def probe(run: dict[str, Any], modality: str, mode: str, condition: str = "true") -> float:
    return float(run["results"][modality]["modes"][mode][condition]["rank1"])


def has_mode(run: dict[str, Any], modality: str, mode: str) -> bool:
    return mode in run["results"][modality]["modes"]


def ret(run: dict[str, Any], modality: str, mode: str) -> float:
    return float(run["results"][modality]["retention"][mode])


def mag(run: dict[str, Any], modality: str, key: str) -> float:
    return float(run["magnitudes"][modality][key])


def chance(run: dict[str, Any], modality: str) -> float:
    return float(run["results"][modality]["chance_rank1"])


def items(run: dict[str, Any], modality: str) -> int:
    return int(run["results"][modality]["modes"]["single"]["true"]["count"])


def gate_weights(run: dict[str, Any], modality: str, mode: str) -> dict[str, Any]:
    return run["results"][modality]["gate_weights"][mode]


def coeff(run: dict[str, Any], modality: str, mode: str, field: str) -> float:
    return float(run["coefficient_checks"][modality][mode][field])


def mean(values: list[float]) -> float:
    return sum(values) / len(values)


def half_spread(values: list[float]) -> float:
    return (max(values) - min(values)) / 2


def binomial_half_width(p: float, n: int) -> float:
    """95% normal-approximation half-width at rate p over n items."""
    return 1.96 * math.sqrt(p * (1 - p) / n)


def seed_runs(runs: dict[str, dict], prefix: str, seeds: tuple[int, ...]) -> list[dict[str, Any]]:
    return [runs[f"{prefix}{seed}"] for seed in seeds]


# --------------------------------------------------------------------------
# derived quantities
# --------------------------------------------------------------------------


def escape_summary(runs: dict[str, dict]) -> dict[str, Any]:
    """Per-seed router outcome, computed exactly as `report_disjoint` does.

    A seed *escapes* when at least one task-conditioned cell clears the
    registered gate in every measured modality; the reportable quantity is the
    rate over seeds, with no seed dropped.
    """
    rows = []
    task_modes: list[str] = []
    for seed in ROUTER_SEEDS:
        run = runs[f"compose-task-IAV-disjoint-768-router-seed{seed}"]
        task_modes = [mode for mode in run["gate_modes"] if mode.startswith("gate-task-lr-")]
        passing = [
            mode
            for mode in task_modes
            if all(payload["retention"][mode] >= GATE_THRESHOLD for payload in run["results"].values())
        ]
        load = run["gate_stats"]["gate-task-lr-1"]["load_ema_final"]
        rows.append(
            {
                "seed": seed,
                "run": run,
                "passing": passing,
                "n_cells": len(task_modes),
                "load": load,
                "own": {
                    modality: gate_weights(run, modality, "gate-task-lr-1")["self_mean"]
                    for modality in run["results"]
                },
                "escaped": bool(passing),
            }
        )
    escaped = [row for row in rows if row["escaped"]]
    per_cell = {
        mode: sum(1 for row in rows if mode in row["passing"]) for mode in task_modes
    }
    per_cell_escaped = {
        mode: sum(1 for row in escaped if mode in row["passing"]) for mode in task_modes
    }
    return {
        "rows": rows,
        "escaped": escaped,
        "collapsed": [row for row in rows if not row["escaped"]],
        "task_modes": task_modes,
        "per_cell": per_cell,
        "per_cell_escaped": per_cell_escaped,
        "best_cells": [mode for mode, count in per_cell.items() if count == max(per_cell.values())],
        "best_count": max(per_cell.values()),
        "worst_count": min(per_cell.values()),
    }


def null_gap(runs: dict[str, dict]) -> float:
    """Largest between-modality L1 gap of the feature-only router, over seeds."""
    worst = 0.0
    for seed in ROUTER_SEEDS:
        run = runs[f"compose-task-IAV-disjoint-768-router-seed{seed}"]
        means = [
            gate_weights(run, modality, "gate-learned-lr-1")["per_brick_mean"]
            for modality in sorted(run["results"])
        ]
        worst = max(worst, sum(abs(a - b) for a, b in zip(means[0], means[1])))
    return worst


def oracle_cells(runs: dict[str, dict]) -> tuple[int, int, float]:
    hit = 0
    total = 0
    worst = 1.0
    for seed in ROUTER_SEEDS:
        run = runs[f"compose-task-IAV-disjoint-768-router-seed{seed}"]
        for modality in run["results"]:
            total += 1
            value = ret(run, modality, "gate-oracle")
            worst = min(worst, value)
            if value >= 1.0:
                hit += 1
    return hit, total, worst


# --------------------------------------------------------------------------
# tables
# --------------------------------------------------------------------------


def pilot_table(runs: dict[str, dict]) -> str:
    rows = [
        ("IMU (6-way)", "pilot-task-imu-frozen-128", 128, 600),
        ("IMU (6-way)", "pilot-task-imu-frozen-256", 256, 600),
        ("Audio (50-way)", "pilot-task-audio-frozen-128", 128, 600),
        ("Audio (50-way)", "pilot-task-audio-frozen-256", 256, 600),
        ("Audio (50-way)", "power-task-audio-frozen-256-s1800", 256, 1800),
    ]
    lines = []
    for label, name, width, steps in rows:
        run = runs[name]
        true = run["results"]["true"]
        ch = 1 / 6 if run["modality"] == "imu" else 1 / 50
        lines.append(
            rf"{label} & {width} & {steps} & {fmt(true['rank1'], 3)} & {fmt(ch, 3)} \\"
        )
    return "\n".join(lines)


def seed_table(runs: dict[str, dict]) -> str:
    """Three seeds x two allocations, IMU (the powered probe at 600 steps)."""
    lines = []
    for label, prefix in (
        ("disjoint-768", "compose-task-IAV-disjoint-768-seed"),
        ("shared-256", "compose-task-IAV-shared-256-seed"),
    ):
        group = seed_runs(runs, prefix, (42, 1042, 2042))
        for mode in ("sum", "mean"):
            singles = [probe(run, "imu", "single") for run in group]
            merged = [probe(run, "imu", mode) for run in group]
            rets = [ret(run, "imu", mode) for run in group]
            lines.append(
                rf"{label} & {mode} & {fmt(mean(singles), 3)} $\pm$ {fmt(half_spread(singles), 3)} & "
                rf"{fmt(mean(merged), 3)} $\pm$ {fmt(half_spread(merged), 3)} & "
                rf"{pct(mean(rets))}\% $\pm$ {pct(half_spread(rets))}\% \\"
            )
    return "\n".join(lines)


def merge_rule_table(runs: dict[str, dict]) -> str:
    """Four merge rules on one run: same direction, 3x range of norms, same dead probe."""
    run = runs["compose-task-IAV-disjoint-768-audio1800-seed42"]
    lines = []
    for mode in ("mean", "alpha-rsqrtn", "alpha-norm", "sum"):
        lines.append(
            rf"\texttt{{{mode}}} & {fmt(mag(run, 'imu', f'{mode}_l2'), 2)} & "
            rf"{fmt(mag(run, 'imu', f'{mode}_cos_own'), 4)} & "
            rf"{fmt(probe(run, 'imu', mode), 3)} & {pct(ret(run, 'imu', mode))}\% & "
            rf"{fmt(probe(run, 'audio', mode), 3)} & {pct(ret(run, 'audio', mode))}\% \\"
        )
    return "\n".join(lines)


def pairwise_table(runs: dict[str, dict]) -> str:
    rows = [
        ("imu", "audio", "compose-task-IA-disjoint-512-seed42", 1),
        ("imu", "vision", "compose-task-IV-disjoint-512-seed42", 1),
        ("imu", "audio + vision", "compose-task-IAV-disjoint-768-audio1800-seed42", 2),
        ("audio", "imu", "compose-task-IA-disjoint-512-seed42", 1),
        ("audio", "vision", "compose-task-AV-disjoint-512-seed42", 1),
        ("audio", "imu + vision", "compose-task-IAV-disjoint-768-audio1800-seed42", 2),
    ]
    lines = []
    for modality, foreign, name, count in rows:
        run = runs[name]
        lines.append(
            rf"{modality} & {foreign} & {count} & {fmt(mag(run, modality, 'sum_cos_own'), 4)} & "
            rf"{fmt(mag(run, modality, 'own_l2'), 1)} & {fmt(mag(run, modality, 'others_sum_l2'), 1)} & "
            rf"{fmt(probe(run, modality, 'single'), 3)} & {fmt(probe(run, modality, 'sum'), 3)} & "
            rf"{pct(ret(run, modality, 'sum'))}\% \\"
        )
    return "\n".join(lines)


def dose_rows(runs: dict[str, dict]) -> list[tuple[str, float, float, float, float, float, float]]:
    run = runs["compose-task-IAV-disjoint-768-dose-seed42"]
    out = []
    for mode, beta in (
        ("beta-0.125", 0.125),
        ("beta-0.25", 0.25),
        ("beta-0.5", 0.5),
        ("beta-0.75", 0.75),
        ("sum", 1.0),
    ):
        out.append(
            (
                mode,
                beta,
                mag(run, "imu", f"{mode}_cos_own"),
                ret(run, "imu", mode),
                mag(run, "audio", f"{mode}_cos_own"),
                ret(run, "audio", mode),
            )
        )
    return out


def dose_table(runs: dict[str, dict]) -> str:
    lines = []
    for _, beta, cos_i, ret_i, cos_a, ret_a in dose_rows(runs):
        lines.append(
            rf"{beta:g} & {fmt(cos_i, 3)} & {math.degrees(math.acos(min(1.0, cos_i))):.1f}$^\circ$ & "
            rf"{pct(ret_i)}\% & {fmt(cos_a, 3)} & {pct(ret_a)}\% \\"
        )
    return "\n".join(lines)


def bpb_table(runs: dict[str, dict]) -> str:
    """The anti-metric table: BPB retention against the task probe it contradicts."""
    rows = [
        ("shared", "mean", "compose-IAV-shared-256-seed42", "compose-task-IAV-shared-256-seed42"),
        ("disjoint", "mean", "compose-IAV-disjoint-768-seed42", "compose-task-IAV-disjoint-768-seed42"),
        ("shared", "sum", "compose-IAV-shared-256-seed42", "compose-task-IAV-shared-256-seed42"),
        ("disjoint", "sum", "compose-IAV-disjoint-768-seed42", "compose-task-IAV-disjoint-768-seed42"),
    ]
    lines = []
    for alloc, mode, bpb_name, task_name in rows:
        bpb = runs[bpb_name]
        task = runs[task_name]
        lines.append(
            rf"{alloc} + \texttt{{{mode}}} & {fmt(bpb['magnitudes'][f'merged_{mode}_l2'], 1)} & "
            rf"{bpb['merge_results'][mode]['improvement']:+.4f} & "
            rf"{pct(bpb['merge_results'][mode]['retention_vs_singles_mean'])}\% & "
            rf"{fmt(probe(task, 'imu', mode), 3)} & {pct(ret(task, 'imu', mode))}\% \\"
        )
    return "\n".join(lines)


def layer_table(runs: dict[str, dict]) -> str:
    lines = []
    for seed in (42, 1042):
        layer = runs[f"compose-task-IAV-layer-256-seed{seed}"]
        full = runs[f"compose-task-IAV-disjoint-768-router-seed{seed}"]
        for modality in ("imu", "audio"):
            lines.append(
                rf"{seed} & {modality} & {fmt(probe(full, modality, 'single'), 3)} & "
                rf"{fmt(probe(layer, modality, 'single'), 3)} & "
                rf"{fmt(mag(layer, modality, 'sum_cos_own_inblock'), 7)} & "
                rf"{mag(layer, modality, 'others_in_own_block_l2'):.3e} & "
                rf"{fmt(probe(layer, modality, 'sum'), 3)} & "
                rf"{pct(ret(layer, modality, 'sum'))}\% & "
                rf"{fmt(probe(layer, modality, 'sum', 'others_only'), 3)} \\"
            )
    return "\n".join(lines)


def escape_table(runs: dict[str, dict]) -> str:
    summary = escape_summary(runs)
    lines = []
    for row in summary["rows"]:
        load = ", ".join(f"{value:.3f}" for value in row["load"])
        outcome = "escaped" if row["escaped"] else r"\textbf{collapsed}"
        lines.append(
            rf"{row['seed']} & {len(row['passing'])}/{row['n_cells']} & {load} & "
            rf"{row['own']['imu']:.3f} & {row['own']['audio']:.3f} & {outcome} \\"
        )
    return "\n".join(lines)


def collapse_family_table(runs: dict[str, dict]) -> str:
    """Phase-2's feature-conditioned router family: lambda and lr, all collapsed."""
    lam = runs["compose-task-IAV-disjoint-768-gate3-seed42"]
    lr = runs["compose-task-IAV-disjoint-768-gate4-seed42"]
    rows = [
        (lam, "gate-learned", r"$\lambda = 0$"),
        (lam, "gate-balanced-0.5", r"$\lambda = 0.5$"),
        (lam, "gate-balanced-2", r"$\lambda = 2$"),
        (lam, "gate-balanced-8", r"$\lambda = 8$"),
        (lr, "gate-lr-1", r"router lr $1\times$"),
        (lr, "gate-lr-0.1", r"router lr $0.1\times$"),
        (lr, "gate-lr-0.01", r"router lr $0.01\times$"),
    ]
    lines = []
    for run, mode, label in rows:
        masses = gate_weights(run, "imu", mode)["per_brick_mean"]
        gap = sum(
            abs(a - b)
            for a, b in zip(
                gate_weights(run, "imu", mode)["per_brick_mean"],
                gate_weights(run, "audio", mode)["per_brick_mean"],
            )
        )
        lines.append(
            rf"{label} & {', '.join(f'{value:.3f}' for value in masses)} & {gap:.1e} & "
            rf"{pct(ret(run, 'imu', mode))}\% & {pct(ret(run, 'audio', mode))}\% \\"
        )
    return "\n".join(lines)


# --------------------------------------------------------------------------
# manuscript
# --------------------------------------------------------------------------


def write_tex(runs: dict[str, dict], out_dir: Path) -> Path:
    d1 = runs["compose-task-IAV-disjoint-768-seed42"]
    powered = runs["compose-task-IAV-disjoint-768-audio1800-seed42"]
    shared1 = runs["compose-task-IAV-shared-256-seed42"]
    dose = runs["compose-task-IAV-disjoint-768-dose-seed42"]
    layer42 = runs["compose-task-IAV-layer-256-seed42"]
    layer1042 = runs["compose-task-IAV-layer-256-seed1042"]
    router42 = runs["compose-task-IAV-disjoint-768-router-seed42"]
    bpb_shared = runs["compose-IAV-shared-256-seed42"]
    bpb_disjoint = runs["compose-IAV-disjoint-768-seed42"]
    power_audio = runs["power-task-audio-frozen-256-s1800"]

    gate_pct = rf"{GATE_THRESHOLD * 100:.0f}\%"
    lora_dim = int(d1["lora_dim"])
    n_items = items(d1, "imu")
    chance_imu = chance(d1, "imu")
    chance_audio = chance(d1, "audio")
    hw_imu = binomial_half_width(chance_imu, n_items)
    hw_audio = binomial_half_width(chance_audio, n_items)
    params = d1["trainable_params_per_brick"]

    # weight-space verification
    rec_ratio = coeff(d1, "imu", "sum", "recovered_scale_ratio_mean")
    rec_err = coeff(d1, "imu", "sum", "coefficient_rel_error_mean")
    rec_mean = coeff(d1, "imu", "mean", "recovered_scale_ratio_mean")
    sh_ratio = coeff(shared1, "imu", "sum", "recovered_scale_ratio_mean")
    sh_err = coeff(shared1, "imu", "sum", "coefficient_rel_error_mean")
    own_l2 = mag(d1, "imu", "own_l2")
    others_l2 = mag(d1, "imu", "others_sum_l2")
    sum_l2 = mag(d1, "imu", "sum_l2")
    pythagoras = math.sqrt(own_l2**2 + others_l2**2)
    sh_own = mag(shared1, "imu", "own_l2")
    sh_others = mag(shared1, "imu", "others_sum_l2")
    sh_sum = mag(shared1, "imu", "sum_l2")
    sh_pythagoras = math.sqrt(sh_own**2 + sh_others**2)
    # phase-1/2 runs share one basis across bricks; the layer arm has one per brick
    basis_offdiag = float(d1["basis_diagnostics"]["max_offdiag_abs"])
    basis_dim = int(d1["basis_diagnostics"]["basis_dim"])

    # three-seed aggregates (IMU, the powered probe at 600 steps)
    dis_group = seed_runs(runs, "compose-task-IAV-disjoint-768-seed", (42, 1042, 2042))
    sh_group = seed_runs(runs, "compose-task-IAV-shared-256-seed", (42, 1042, 2042))
    dis_single = [probe(run, "imu", "single") for run in dis_group]
    dis_sum = [probe(run, "imu", "sum") for run in dis_group]
    dis_ret = [ret(run, "imu", "sum") for run in dis_group]
    sh_single = [probe(run, "imu", "single") for run in sh_group]
    sh_sum_probe = [probe(run, "imu", "sum") for run in sh_group]
    sh_ret = [ret(run, "imu", "sum") for run in sh_group]

    # powered audio
    audio_1800 = float(power_audio["results"]["true"]["rank1"])
    audio_600 = float(runs["pilot-task-audio-frozen-256"]["results"]["true"]["rank1"])
    audio_nobridge = float(power_audio["results"]["no_bridge"]["rank1"])
    audio_single = probe(powered, "audio", "single")
    audio_merged = probe(powered, "audio", "sum")
    audio_others_only = probe(powered, "audio", "sum", "others_only")
    imu_single_p = probe(powered, "imu", "single")
    imu_merged_p = probe(powered, "imu", "sum")
    imu_others_only = probe(powered, "imu", "sum", "others_only")

    # dose
    dose_first = dose_rows(runs)[0]
    dose_tol_deg = math.degrees(math.acos(min(1.0, dose_first[2])))
    dose_half = dose_rows(runs)[2]
    dose_half_deg = math.degrees(math.acos(min(1.0, dose_half[2])))

    # layer partition
    blocks = layer42["layer_blocks"]
    bounds = layer42["layer_bounds"]
    n_layers = len(layer42["layer_sizes"])
    layer_rec = coeff(layer42, "imu", "sum", "recovered_scale_ratio_mean")
    layer_rec_err = coeff(layer42, "imu", "sum", "coefficient_rel_error_mean")
    full42 = runs["compose-task-IAV-disjoint-768-router-seed42"]
    full1042 = runs["compose-task-IAV-disjoint-768-router-seed1042"]
    restrict_imu = probe(layer42, "imu", "single") / probe(full42, "imu", "single")
    restrict_audio = probe(layer42, "audio", "single") / probe(full42, "audio", "single")
    restrict_imu_1042 = probe(layer1042, "imu", "single") / probe(full1042, "imu", "single")
    restrict_audio_1042 = probe(layer1042, "audio", "single") / probe(full1042, "audio", "single")
    layer_global_cos = mag(layer42, "imu", "sum_cos_own")

    # selection
    summary = escape_summary(runs)
    n_escaped = len(summary["escaped"])
    n_seeds = len(summary["rows"])
    hit, total, oracle_worst = oracle_cells(runs)
    gap = null_gap(runs)
    escaped_load = [row["load"] for row in summary["escaped"]]
    collapsed_load = [row["load"] for row in summary["collapsed"]]
    escaped_audio_mass = [row["own"]["audio"] for row in summary["escaped"]]
    collapsed_audio_mass = [row["own"]["audio"] for row in summary["collapsed"]]
    best_cell_label = ", ".join(rf"\texttt{{{mode}}}" for mode in summary["best_cells"])
    best_escaped = max(summary["per_cell_escaped"][mode] for mode in summary["best_cells"])
    engaged_cos = mag(router42, "imu", "gate-task-lr-1_cos_own")
    engaged_l2 = mag(router42, "imu", "gate-task-lr-1_l2")
    engaged_own = mag(router42, "imu", "own_l2")
    imu_collapsed_ret = [
        ret(row["run"], "imu", mode) for row in summary["collapsed"] for mode in summary["task_modes"]
    ]
    audio_collapsed_ret = [
        ret(row["run"], "audio", mode) for row in summary["collapsed"] for mode in summary["task_modes"]
    ]
    collapsed_audio_single = [probe(row["run"], "audio", "single") for row in summary["collapsed"]]

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
\emergencystretch=2em  % long \texttt{{}} run names would otherwise overflow the margin
\hypersetup{{
  colorlinks=true,
  linkcolor=blue!60!black,
  citecolor=blue!60!black,
  urlcolor=blue!60!black,
  pdftitle={{Zero Weight-Space Interference Is Not Enough}},
  pdfauthor={{Franci Penov}},
}}
\graphicspath{{{{figures/}}}}
\title{{Zero Weight-Space Interference Is Not Enough:\\Behavioral Probes for Composing Sensor Bricks\\on a Frozen Language Model}}
\author{{Franci Penov \\ kortexa.ai \\ \texttt{{francip@kortexa.ai}}}}
\date{{2026-08-03}}

\begin{{document}}
\maketitle

\begin{{abstract}}
Modular adaptation promises that separately trained sensor adapters can be merged into one model that serves all of them. The standard evidence for a successful merge is an in-objective metric --- perplexity, bits-per-byte, or a single downstream score. We argue that such metrics certify nothing, and we build the instrument they are missing: each constituent's own out-of-objective behavioral probe, re-measured under the merged weights. On a frozen 230M-parameter language model with three sensor bricks (IMU, audio, vision) generated by conditional LoRA bridges, the instrument immediately separates the two: the merge with the best bits-per-byte retention we have ever recorded ({pct(bpb_shared['merge_results']['sum']['retention_vs_singles_mean'])}\%) has behaviorally dead probes, indistinguishable from the merge that scores {pct(bpb_disjoint['merge_results']['sum']['retention_vs_singles_mean'])}\%. With that instrument we report an exhaustive negative on additive composition. Allocating each brick a disjoint block of a shared frozen orthonormal basis makes the merge provably lossless --- projecting the merged delta back onto a brick's own block recovers its coefficients at ratio {fmt(rec_ratio, 6)} --- and it buys nothing: across three seeds, two allocations, and four merge rules spanning a {mag(powered, 'imu', 'sum_l2') / mag(powered, 'imu', 'mean_l2'):.0f}$\times$ range of norms, a six-way IMU probe worth {fmt(mean(dis_single), 3)} alone is worth {fmt(mean(dis_sum), 3)} merged against a {fmt(chance_imu, 3)} chance rate, and a powered fifty-way audio probe worth {fmt(audio_single, 3)} alone scores {fmt(audio_merged, 3)}. One foreign brick is as damaging as two, and a continuous dose-response shows the {gate_pct} retention gate is met only when foreign bricks are attenuated to $\cos \approx {fmt(dose_first[2], 2)}$ --- about {dose_tol_deg:.0f} degrees of tolerance. We then falsify our own mechanism: partitioning \emph{{layers}} instead of coefficients gives each brick perfect ownership of its sites ($\cos = {fmt(mag(layer42, 'imu', 'sum_cos_own_inblock'), 7)}$ in-block, zero foreign mass in-block) and retention is still {pct(ret(layer1042, 'audio', 'sum'))}--{pct(ret(layer42, 'imu', 'sum'))}\%, replicated at two seeds, with the merged probe equal to deleting the measured brick. The damage is cross-layer residual-stream interaction, not weight-space overlap. Finally, selection works where addition cannot: an oracle router recovers every brick's single-brick probe exactly ({hit}/{total} cells at {n_seeds} seeds), and a task-conditioned learned router reaches that ceiling exactly when it escapes a collapse basin --- which it does in {n_escaped} seeds of {n_seeds}, with no hyperparameter predicting which. We state the resulting open problem: make the escape selectable.
\end{{abstract}}

\section{{Introduction}}
A conditional LoRA bridge \cite{{penov2026bridges}} maps a frozen sensor encoder's features to per-input low-rank weight updates injected into a frozen language model, giving the model token-free awareness of an external signal. A follow-up study \cite{{penov2026basis}} reparameterized the bridge's output as $k$ coefficients over a basis of LoRA directions, and proved that coefficient-space composition is \emph{{identical}} to weight-space composition, since $\mathrm{{mean}}(c_i \cdot B) = \mathrm{{mean}}(c_i) \cdot B$. That located the failure in the merge operation and named an untested fix: give each modality its own block of a shared frozen orthonormal basis, so that weight-space interference is zero by construction. This paper runs that experiment, and everything the experiment forced afterwards.

The result is a negative, and the reason it is worth reporting is methodological. One claim connects this paper to its predecessors:

\begin{{quote}}
A metric computed in the space the intervention was optimized in certifies nothing. Certification requires an out-of-objective behavioral probe.
\end{{quote}}

Composition research is unusually exposed to this. Bits-per-byte, perplexity, and averaged benchmark scores are cheap to compute under a merge and they move for reasons that have nothing to do with whether the merged model can still \emph{{do}} what each constituent could do. Section~\ref{{sec:instrument}} makes that concrete in one table: the merge with the highest BPB retention in this program is behaviorally dead, and it is dead in exactly the same way as the merge with the worst BPB retention.

\paragraph{{Contributions.}}
\begin{{itemize}}
  \item \textbf{{An instrument}} (\S\ref{{sec:instrument}}): each constituent's own task probe re-measured under merged weights, against its single-brick score, the published feature controls, and an \texttt{{others\_only}} control that zeroes the measured brick inside the merge. Instantiated by an anti-metric result --- {pct(bpb_shared['merge_results']['sum']['retention_vs_singles_mean'])}\% BPB retention on probes at chance.
  \item \textbf{{An exhaustive additive negative}} (\S\ref{{sec:negative}}): provably lossless disjoint-sum composition is behaviorally dead across three seeds, two allocations and four merge rules; damage is presence-driven rather than count-driven, graded by angle, and a controlled dose-response bounds the tolerance at roughly {dose_tol_deg:.0f} degrees.
  \item \textbf{{A mechanism, correctly localized}} (\S\ref{{sec:mechanism}}): a layer-partitioned design that our own angle account predicted would retain $\sim$100\% instead retains {pct(ret(layer1042, 'audio', 'sum'))}--{pct(ret(layer42, 'imu', 'sum'))}\%, replicated at two seeds. The interference is cross-layer and downstream, not in the weights.
  \item \textbf{{Selection, honestly}} (\S\ref{{sec:selection}}): the routing ceiling is exact at every seed; the only learned mechanism that reaches it is bistable across seeds and must be handed the task identity. We report the escape rate rather than a method.
\end{{itemize}}

\section{{Setup}}
\label{{sec:setup}}
\paragraph{{Model and bricks.}}
The base model is LiquidAI LFM~2.5 230M, frozen, adapted through the published harness's HuggingFace checkpoint path \cite{{penov2026note}}. LoRA rank 4 on attention and MLP projections gives a flattened adaptation vector of $D = {lora_dim:,}$ dimensions. Three bricks are trained, each alone, by the ordinary recipe: two \emph{{task}} bricks with closed-set ranking probes --- IMU ({int(round(1 / chance_imu))}-way activities, chance {fmt(chance_imu, 3)}) and audio ({int(round(1 / chance_audio))}-way events, chance {fmt(chance_audio, 3)}) --- and one \emph{{context}} brick (vision) trained on the text objective, which has no label probe in this suite and therefore enters only through the damage it does. Trainable parameters per brick: {params['imu']:,} (IMU), {params['audio']:,} (audio).

\paragraph{{Shared frozen basis and allocations.}}
Each brick's bridge emits $k$ coefficients over a shared frozen orthonormal basis $B \in \mathbb{{R}}^{{k \times D}}$, built by Cholesky whitening of a seeded Gaussian ($\max |BB^\top - I|$ off-diagonal $\le {basis_offdiag:.1e}$ at $k = {basis_dim}$). The basis is a buffer, not a parameter: it is regenerated from its seed and never stored. Three allocations are compared. Under \textbf{{shared}} allocation all bricks write all $k$ rows. Under \textbf{{disjoint}} allocation brick $i$ writes only rows $[i \cdot k/n, (i{{+}}1) \cdot k/n)$, so no two bricks ever touch the same coordinate. Under \textbf{{layer}} allocation (\S\ref{{sec:mechanism}}) each brick gets its own basis over its own contiguous block of decoder layers.

\paragraph{{Merge rules.}}
\texttt{{sum}} adds every brick's delta; \texttt{{mean}} averages them; \texttt{{alpha-norm}} rescales the sum per item so its $L_2$ matches that item's own single-brick delta norm; \texttt{{alpha-rsqrtn}} is the variance-preserving $1/\sqrt{{n}}$ point; \texttt{{beta-}}$\beta$ applies $\mathrm{{own}} + \beta \cdot \mathrm{{others}}$, so $\beta = 1$ is exactly \texttt{{sum}}. The gated modes of \S\ref{{sec:selection}} apply a convex weight per brick, so a confident gate reproduces a single brick exactly and a uniform gate reproduces \texttt{{mean}}.

\paragraph{{Budgets and slice width.}}
Table~\ref{{tab:pilot}} sets the per-modality slice width from single-modality frozen probes. IMU is far stronger at width 256 than at 128 and audio is marginally better, so three modalities $\times$ 256 rows fixes $k_{{\mathrm{{total}}}} = 768$; the shared arm uses $k = 256$, which by prefix-stability of Cholesky whitening is literally the first 256 rows of the same basis. Budgets are the house standard: learning rate $10^{{-3}}$, 32{{,}}768 evaluation tokens, {n_items} stratified evaluation items per probe, 600 task steps for IMU and 300 text steps for vision. Audio at 600 steps is underpowered (Table~\ref{{tab:pilot}}); the registered fix is {int(power_audio['results']['true']['steps'])} steps, which lifts a single audio brick from {fmt(audio_600, 3)} to {fmt(audio_1800, 3)} against a {fmt(audio_nobridge, 3)} no-bridge baseline. Every behavioral claim below is scoped to the two \emph{{powered}} probes: IMU at 600 steps and audio at {int(power_audio['results']['true']['steps'])}. Vision was never powered as a probe and no behavioral claim is made about it.

\begin{{table}}[t]
\centering
\caption{{Single-modality frozen-basis probes that fix the slice width and the audio budget. Rank-1 accuracy, \texttt{{true}} condition; all controls sit at chance in every frozen run.}}
\label{{tab:pilot}}
\begin{{tabular}}{{lrrrr}}
\toprule
Probe & Slice width & Steps & Rank-1 & Chance \\
\midrule
{pilot_table(runs)}
\bottomrule
\end{{tabular}}
\end{{table}}

\paragraph{{Statistical hygiene.}}
Every probe is a closed-set ranking probe over {n_items} stratified evaluation items, so one item is {100 / n_items:.1f} points. The 95\% binomial half-width at the six-way chance rate is $\pm{fmt(hw_imu, 3)}$ and at the fifty-way rate $\pm{fmt(hw_audio, 3)}$. We never rank cells inside those bands: a merged IMU score anywhere between roughly {fmt(chance_imu - hw_imu, 2)} and {fmt(chance_imu + hw_imu, 2)} is ``at chance'' and its exact value carries no information. This is why the registered gate is set at {gate_pct} retention rather than at 95\%, and why the paper leans on three-seed aggregates, eight-seed rates, and the dose curve rather than on individual cells. Cells that rest on a single seed are labelled as such in every table and in the text.

\paragraph{{The registered gate.}}
Stated before any run: composition is \emph{{supported}} only if \textbf{{every}} measured task modality retains $\ge {gate_pct}$ of that same brick's single-brick rank-1 under the merge, with the \texttt{{shuffled}} / \texttt{{random}} / \texttt{{no\_bridge}} controls at chance. A cell where one modality clears and the other does not is a failure. This roll-up rule is unchanged across every arm in the paper.

\section{{The instrument, and why the usual metric is not one}}
\label{{sec:instrument}}
The composition instrument re-measures \emph{{each brick's own probe under the merged weights}}. Every cell is reported against four references: that brick's single-brick score, the published \texttt{{shuffled}} and \texttt{{random}} feature controls, \texttt{{no\_bridge}}, and --- the load-bearing one --- \texttt{{others\_only}}, which zeroes the measured brick's delta inside the merge and leaves the others. \texttt{{others\_only}} answers the question a retention percentage cannot: is the brick's contribution \emph{{diluted}}, or is it \emph{{inaudible}}?

Table~\ref{{tab:bpb}} is the reason the instrument had to be built. It reports bits-per-byte retention for the same three bricks merged four ways, beside the IMU task probe measured on the identical merges. BPB retention tracks exactly one thing --- how close the merged delta's norm lands to a single brick's --- and it orders the merges in a way that is not merely uninformative but actively inverted. Shared-plus-sum is the best composition BPB number this program has recorded; it gets there because a shared basis lets three coefficient vectors overlap so their sum stays near single-brick scale ({fmt(bpb_shared['magnitudes']['merged_sum_l2'], 1)} against a single brick's {fmt(mean([value for key, value in bpb_shared['magnitudes'].items() if key.startswith('single_')]), 1)}) instead of growing orthogonally to {fmt(bpb_disjoint['magnitudes']['merged_sum_l2'], 1)}, which is precisely what disjointness forces. And that ``winning'' merge has the same extinguished task probe as the merge that scores {pct(bpb_disjoint['merge_results']['sum']['retention_vs_singles_mean'])}\%: IMU {fmt(probe(shared1, 'imu', 'sum'), 3)} against {fmt(probe(d1, 'imu', 'sum'), 3)}, both at the {fmt(chance_imu, 3)} chance rate.

\begin{{table}}[t]
\centering
\caption{{The anti-metric result. BPB retention on the merged bricks (secondary metric, computed in the training objective) against the IMU task probe measured on the same merges (out-of-objective). A metric on which the behaviorally dead configuration scores {pct(bpb_shared['merge_results']['sum']['retention_vs_singles_mean'])}\% is not measuring composition. Single seed (42).}}
\label{{tab:bpb}}
\small
\begin{{tabular}}{{lrrrrr}}
\toprule
Merge & $\|\Delta_{{\mathrm{{merged}}}}\|$ & $\Delta$BPB & BPB retention & IMU rank-1 & IMU retention \\
\midrule
{bpb_table(runs)}
\bottomrule
\end{{tabular}}
\end{{table}}

\section{{The additive negative}}
\label{{sec:negative}}

\subsection{{The construction delivers, and it buys nothing}}
Disjoint allocation was designed to make weight-space interference zero, and it does, measurably. Projecting the merged delta back onto a brick's own block of the basis recovers that brick's coefficients at ratio {fmt(rec_ratio, 6)} with relative error {rec_err:.1e} under \texttt{{sum}} --- zero cross-terms and zero dilution --- against ratio {fmt(sh_ratio, 3)} at relative error {sh_err:.2f} for the shared arm, which is thoroughly contaminated. Under \texttt{{mean}} the same projection returns exactly $1/n$ ({fmt(rec_mean, 5)}), reproducing the dilution mechanism of prior work to four decimals. The norms confirm orthogonality independently: in the disjoint arm $\sqrt{{\|{{\mathrm{{own}}}}\|^2 + \|{{\mathrm{{others}}}}\|^2}} = \sqrt{{{fmt(own_l2, 2)}^2 + {fmt(others_l2, 2)}^2}} = {fmt(pythagoras, 2)} = \|{{\mathrm{{sum}}}}\|$ exactly, while in the shared arm {fmt(sh_pythagoras, 2)} $\ne$ {fmt(sh_sum, 2)}.

It buys nothing. Table~\ref{{tab:seeds}} gives three seeds of each allocation on the powered IMU probe. A brick worth {fmt(mean(dis_single), 3)} $\pm$ {fmt(half_spread(dis_single), 3)} alone is worth {fmt(mean(dis_sum), 3)} $\pm$ {fmt(half_spread(dis_sum), 3)} inside the three-way sum, against chance {fmt(chance_imu, 3)}: retention {pct(mean(dis_ret))}\%. The shared arm --- whose weight space is contaminated --- lands in the same place, {pct(mean(sh_ret))}\%. Every seed of every arm is at or below chance, and the spread across seeds is roughly a fifth of the distance to the gate. The probe is not degraded; it is extinguished, and the two arms are indistinguishable, which is the whole point: weight-space cleanliness is measurable, achievable, and behaviorally inert.

The \texttt{{others\_only}} control says what kind of failure this is. Deleting the measured brick from the merge entirely scores {fmt(imu_others_only, 3)} (IMU) and {fmt(audio_others_only, 3)} (audio) against merged scores of {fmt(imu_merged_p, 3)} and {fmt(audio_merged, 3)}. The brick's contribution is not diluted; it is inaudible.

\begin{{table}}[t]
\centering
\caption{{Three seeds (42, 1042, 2042) of each allocation on the six-way IMU probe, mean $\pm$ half-spread. Chance is {fmt(chance_imu, 3)}; the 95\% binomial half-width is $\pm{fmt(hw_imu, 3)}$. All controls at chance in every run.}}
\label{{tab:seeds}}
\begin{{tabular}}{{llrrr}}
\toprule
Allocation & Merge & Single rank-1 & Merged rank-1 & Retention \\
\midrule
{seed_table(runs)}
\bottomrule
\end{{tabular}}
\end{{table}}

\subsection{{Magnitude is excluded}}
Four merge rules on the same trained bricks span a {mag(powered, 'imu', 'sum_l2') / mag(powered, 'imu', 'mean_l2'):.0f}$\times$ range of merged norms, including one (\texttt{{alpha-norm}}) that matches the measured brick's own norm to four decimals ({fmt(mag(powered, 'imu', 'alpha-norm_l2'), 2)} against $\|\mathrm{{own}}\| = {fmt(mag(powered, 'imu', 'own_l2'), 2)}$). None recovers anything (Table~\ref{{tab:merges}}). The reason is in one column: all four are positive rescalings of the same vector, so all four share one $\cos(\mathrm{{merged}}, \mathrm{{own}})$. Magnitude was the only thing they varied, and magnitude does not matter. What is left is direction.

\begin{{table}}[t]
\centering
\caption{{Four merge rules, one set of trained bricks, seed 42 (single seed). All four are positive rescalings of the same merged direction, so $\cos$ is shared; the norms span {mag(powered, 'imu', 'sum_l2') / mag(powered, 'imu', 'mean_l2'):.0f}$\times$ and the probes are dead in all of them. Chance: IMU {fmt(chance_imu, 3)}, audio {fmt(chance_audio, 3)}.}}
\label{{tab:merges}}
\small
\begin{{tabular}}{{lrrrrrr}}
\toprule
Merge & $\|\Delta_{{\mathrm{{merged}}}}\|$ & $\cos(\mathrm{{merged}}, \mathrm{{own}})$ & IMU rank-1 & IMU ret. & Audio rank-1 & Audio ret. \\
\midrule
{merge_rule_table(runs)}
\bottomrule
\end{{tabular}}
\end{{table}}

\subsection{{Presence, not count --- and the angle grades it}}
Halving the number of foreign bricks changes nothing (Table~\ref{{tab:pairwise}}): audio goes to {fmt(probe(runs['compose-task-IA-disjoint-512-seed42'], 'audio', 'sum'), 3)} with one foreign brick and {fmt(audio_merged, 3)} with two; IMU retains {pct(ret(runs['compose-task-IA-disjoint-512-seed42'], 'imu', 'sum'))}\% against {pct(ret(powered, 'imu', 'sum'))}\%. One foreign brick is as fatal as two. What does move the number is the angle the foreign bricks open, which is set by their norm relative to the measured brick's: the small vision context brick ($\|\Delta\| \approx {fmt(mag(runs['compose-task-IV-disjoint-512-seed42'], 'imu', 'others_sum_l2'), 1)}$ against IMU's ${fmt(mag(runs['compose-task-IV-disjoint-512-seed42'], 'imu', 'own_l2'), 1)}$) leaves IMU at {pct(ret(runs['compose-task-IV-disjoint-512-seed42'], 'imu', 'sum'))}\% where audio leaves it at {pct(ret(runs['compose-task-IA-disjoint-512-seed42'], 'imu', 'sum'))}\%. Both modalities order the same way, and the covariate that predicts retention is $\cos$, not brick count. These rows are single-seed and are read as an ordering, not as point estimates.

\begin{{table}}[t]
\centering
\caption{{Damage against the number of foreign bricks and against the angle they open, sum merge, seed 42 (single seed), identical per-brick budgets. Retention is against each modality's own single-brick rank-1 in the same run.}}
\label{{tab:pairwise}}
\small
\begin{{tabular}}{{llrrrrrrr}}
\toprule
Measured & Foreign & \# & $\cos(\mathrm{{sum}}, \mathrm{{own}})$ & $\|\mathrm{{own}}\|$ & $\|\mathrm{{others}}\|$ & Single & Merged & Retention \\
\midrule
{pairwise_table(runs)}
\bottomrule
\end{{tabular}}
\end{{table}}

\subsection{{The dose-response}}
Comparing brick sets confounds ``how many foreign bricks'' with ``how large are they'', so the \texttt{{beta-}}$\beta$ merge attenuates the foreign contribution continuously and sweeps $\cos(\mathrm{{merged}}, \mathrm{{own}})$ with everything else held fixed. This is the paper's central measurement (Table~\ref{{tab:dose}}, Figure~\ref{{fig:dose}}). The registered {gate_pct} gate is met only at $\beta = {dose_first[1]:g}$, i.e. $\cos \approx {fmt(dose_first[2], 2)}$, i.e. with the foreign bricks attenuated to an eighth of their trained strength --- and even there only for IMU; the fifty-way audio probe is already down to {pct(dose_first[5])}\%. A brick tolerates roughly {dose_tol_deg:.0f} degrees of rotation of its adaptation before it starts losing its probe, and by {dose_half_deg:.0f} degrees it has lost about two thirds of it.

Two consequences. First, \emph{{no additive rule can work}}: at $\beta = 1$ every brick contributes at full strength by definition, and the curve is already on the floor. Second, the curve does not say composition is impossible --- it says the other bricks have to be \emph{{muted}}, which is a description of selection rather than of arithmetic. This single run is seed 42; the ordering it establishes is corroborated by the pairwise arm and by the three-seed table, but the curve itself is not replicated.

\begin{{table}}[t]
\centering
\caption{{Dose-response: retention against $\cos(\mathrm{{merged}}, \mathrm{{own}})$ under $\mathrm{{own}} + \beta \cdot \mathrm{{others}}$, seed 42 (single seed). $\beta = 1$ is \texttt{{sum}}; $\beta = 0$ would be the single brick. Angles are for IMU. Retention is against singles of {fmt(probe(dose, 'imu', 'single'), 3)} (IMU) and {fmt(probe(dose, 'audio', 'single'), 3)} (audio).}}
\label{{tab:dose}}
\begin{{tabular}}{{rrrrrr}}
\toprule
$\beta$ & $\cos$ (IMU) & angle & IMU retention & $\cos$ (audio) & Audio retention \\
\midrule
{dose_table(runs)}
\bottomrule
\end{{tabular}}
\end{{table}}

\begin{{figure}}[t]
\centering
\includegraphics[width=0.82\linewidth]{{paper7_dose_response.png}}
\caption{{The dose-response. Retention collapses within a few degrees of rotation: the registered {gate_pct} gate is cleared only at $\cos \approx {fmt(dose_first[2], 2)}$, and only by the six-way probe. Shaded band is the 95\% binomial half-width at each probe's chance rate over {n_items} items.}}
\label{{fig:dose}}
\end{{figure}}

\subsection{{The sharpest cell: a powered probe erased}}
Audio at {int(power_audio['results']['true']['steps'])} steps is not a weak modality but a short-changed one: single-brick rank-1 rises from {fmt(audio_600, 3)} to {fmt(audio_1800, 3)} against a {fmt(chance_audio, 3)} chance rate. Powered, it gives the starkest measurement in the paper. A brick that is right {int(round(audio_single * n_items))} times out of {n_items} on a fifty-way problem is right {int(round(audio_merged * n_items))} times inside the three-way disjoint sum --- strictly worse than deleting it, since \texttt{{others\_only}} scores {fmt(audio_others_only, 3)}. The controls behaved throughout: \texttt{{shuffled}}, \texttt{{random}} and \texttt{{no\_bridge}} sit at chance in every single-brick column, so the instrument is sound and the failure is real.

\begin{{figure}}[t]
\centering
\includegraphics[width=0.9\linewidth]{{paper7_retention_vs_cos.png}}
\caption{{Every merged cell in the paper, retention against $\cos(\mathrm{{merged}}, \mathrm{{own}})$, across allocations, merge rules, brick sets and seeds. The additive family occupies one region and one region only. Selection modes (stars at $\cos \approx 1$) are the only points above the gate, and the ones that fall below it are the collapsed router's cells.}}
\label{{fig:scatter}}
\end{{figure}}

\section{{Localizing the mechanism: a falsified prediction}}
\label{{sec:mechanism}}
The dose-response invited an obvious inference: if $\cos = 1$ is the only survivable regime, build a design where $\cos = 1$ holds at every site a brick writes. Coefficient-space partitioning cannot do that --- the basis spans every LoRA site, so each brick is off-axis everywhere it writes --- but \emph{{layer}} partitioning can. The model has {n_layers} decoder layers laid out layer-major in the flat vector, so a layer set is a contiguous flat range. The most equal contiguous three-way split is fixed by the architecture, not chosen: IMU layers {bounds[0]}--{bounds[1] - 1} ({blocks['imu'][1] - blocks['imu'][0]:,} dims, {(blocks['imu'][1] - blocks['imu'][0]) / lora_dim * 100:.1f}\%), audio layers {bounds[1]}--{bounds[2] - 1} ({blocks['audio'][1] - blocks['audio'][0]:,}, {(blocks['audio'][1] - blocks['audio'][0]) / lora_dim * 100:.1f}\%), vision layers {bounds[2]}--{bounds[3] - 1} ({blocks['vision'][1] - blocks['vision'][0]:,}, {(blocks['vision'][1] - blocks['vision'][0]) / lora_dim * 100:.1f}\%), each block holding exactly two of the six attention layers.

\paragraph{{Registered prediction.}}
The site-local angle account predicts $\sim$100\% retention, because $\cos(\mathrm{{merged}}, \mathrm{{own}})$ restricted to a brick's own block is $1.0$ by construction. The global angle account predicts retention at or below the phase-2 level. These differ by about 100 points, so the arm is decisive either way.

\paragraph{{The geometry came out as designed.}}
\begin{{itemize}}
  \item in-block $\cos(\mathrm{{merged}}, \mathrm{{own}}) = {fmt(mag(layer42, 'imu', 'sum_cos_own_inblock'), 7)}$ under both \texttt{{sum}} and \texttt{{mean}};
  \item \texttt{{others\_in\_own\_block}} $L_2 = {mag(layer42, 'imu', 'others_in_own_block_l2'):.3e}$ --- the other bricks put literally zero mass in the measured brick's sites;
  \item \texttt{{own\_outside\_block}} $L_2 = {mag(layer42, 'imu', 'own_outside_block_l2'):.3e}$ --- and the measured brick puts literally zero mass outside them;
  \item coefficient recovery through the block basis at ratio {fmt(layer_rec, 7)}, relative error {layer_rec_err:.1e}.
\end{{itemize}}
The control is clean: restricting a brick to a third of the sites costs almost nothing on its own --- IMU falls to {pct(restrict_imu)}\% of its full-layer single and audio \emph{{rises}} to {pct(restrict_audio)}\% at seed 42 ({pct(restrict_imu_1042)}\% and {pct(restrict_audio_1042)}\% at seed 1042). A third of the sites is not a capacity bottleneck at these budgets, so whatever happens to the merged probes is not an artifact of the partition.

\paragraph{{The prediction failed, and the failure replicates.}}
Retention is {pct(ret(layer42, 'imu', 'sum'))}\% (IMU) and {pct(ret(layer42, 'audio', 'sum'))}\% (audio) at seed 42, and {pct(ret(layer1042, 'imu', 'sum'))}\% and {pct(ret(layer1042, 'audio', 'sum'))}\% at seed 1042 (Table~\ref{{tab:layer}}, Figure~\ref{{fig:layer}}). Every cell of both seeds fails the registered gate with all controls at chance. The \texttt{{others\_only}} control reproduces verbatim under this perfect geometry: at both seeds the merged score equals \texttt{{others\_only}} to within one evaluation item, and at seed 1042 the merged IMU score is \emph{{below}} it. A brick can own its sites outright --- perfect direction, perfect magnitude, provably zero foreign mass anywhere it writes --- and still lose its probe the moment two other bricks are switched on at \emph{{other}} layers.

The global-angle account is not rescued either: layer partitioning lands at global $\cos \approx {fmt(layer_global_cos, 2)}$, where the dose curve predicts about {pct(ret(powered, 'imu', 'sum'))}\% for IMU, and observed retention is about twice that at seed 42 and level with it at seed 1042. Retention is therefore not a pure function of the global cosine either; the angle is a decent summary statistic \emph{{within}} a fixed allocation and does not transfer \emph{{across}} allocations.

What survives is the mechanism the failure implicates, and it should be stated in these words: \textbf{{the damage is cross-layer residual-stream interaction, not weight-space overlap}}. A probe reading out of the top of the stack runs its forward pass through every foreign adaptation installed anywhere along it, and that is enough to extinguish it. Disjoint sites do not protect a probe, because the interference is downstream of the sites.

Whether layer partitioning helps \emph{{at all}} is not resolved by two seeds and is not claimed. Against the matched full-layer comparator at seed 42 IMU goes {pct(ret(powered, 'imu', 'sum'))}\% $\to$ {pct(ret(layer42, 'imu', 'sum'))}\% and audio {pct(ret(powered, 'audio', 'sum'))}\% $\to$ {pct(ret(layer42, 'audio', 'sum'))}\%, which looks like a doubling; at seed 1042 the comparison is {pct(ret(full1042, 'imu', 'sum'))}\% against {pct(ret(layer1042, 'imu', 'sum'))}\%, which is indistinguishable. The defensible statement is that layer partitioning is at best a modest improvement, inside seed spread, and nowhere near the $\sim$100\% its own prediction required.

\begin{{table}}[t]
\centering
\caption{{The layer-partition falsification, both seeds. Each brick owns its sites exactly --- in-block $\cos = 1$, zero foreign mass in-block --- and the probe dies anyway, landing on \texttt{{others\_only}}. ``Full-layer single'' is the same brick trained at the same budget and seed without the site restriction.}}
\label{{tab:layer}}
\footnotesize
\begin{{tabular}}{{llrrrrrrr}}
\toprule
Seed & Probe & Full-layer & Restricted & In-block $\cos$ & Foreign in-block & Merged & Retention & \texttt{{others\_only}} \\
 & & single & single & & $L_2$ & (sum) & & \\
\midrule
{layer_table(runs)}
\bottomrule
\end{{tabular}}
\end{{table}}

\begin{{figure}}[t]
\centering
\includegraphics[width=0.92\linewidth]{{paper7_layer_partition.png}}
\caption{{The falsification in one panel. Left: the weight-space geometry is exactly as designed at both seeds. Right: the probes die anyway, landing on the \texttt{{others\_only}} control, roughly 70--95 points below the prediction the geometry licensed.}}
\label{{fig:layer}}
\end{{figure}}

\section{{Selection, stated honestly}}
\label{{sec:selection}}

\subsection{{The ceiling is exact and the feature-only null is provably blind}}
Routing each probe through only its own brick's weights --- a hard one-hot oracle over the coefficient heads --- reproduces the single-brick number exactly: retention {fmt(oracle_worst, 3)} in both modalities at all {n_seeds} seeds, {hit} cells of {total}, with $\cos(\mathrm{{merged}}, \mathrm{{own}}) = 1$ and $\|\mathrm{{merged}}\| = \|\mathrm{{own}}\|$. This is a ceiling, not a result, but it settles what the whole negative family left open: \textbf{{composition under this architecture is solvable}}. Having three bridges loaded damages no brick. Every point of loss in \S\ref{{sec:negative}} and \S\ref{{sec:mechanism}} is attributable to \emph{{adding the other bricks in}}, and a mechanism that declines to add them recovers 100\% of both modalities.

The complementary null is equally emphatic. Our gate protocol is leak-free by construction: the live slot and the ambient slots are drawn from the \emph{{same}} per-brick pool, so a router that sees only the concatenated sensor features has the same input distribution whichever modality is being asked. It therefore has no input-conditioned solution, and the measurement confirms the argument mechanically --- the feature-only router's between-modality $L_1$ gap is {gap:.3e} at every one of the {n_seeds} seeds, byte-identical gate vectors whichever brick owns the question, while its within-modality dispersion is nonzero. It is not a frozen constant; it is \emph{{modality-blind}}. That is the correct answer to the question it was asked, which means the earlier collapse of feature-conditioned routers was never an optimizer failure, and it means the only informative router in this family is a task-conditioned one.

For completeness, Table~\ref{{tab:collapse}} shows the feature-conditioned family swept over load-balancing weight and router learning rate. Load balancing only chooses \emph{{which}} brick the constant lands on; lowering the learning rate only slides the constant from one-hot toward uniform, and a uniform gate \emph{{is}} the mean merge. The apparent 100\% IMU cells are accidents of the constant pointing at IMU, which is exactly why the roll-up gate requires every modality to clear.

\begin{{table}}[t]
\centering
\caption{{The feature-conditioned router family, seed 42 (single seed). ``Gate mass'' is the mean convex weight over (imu, audio, vision); the $L_1$ gap is between the two measured modalities' mean gate vectors. Every row is a constant: the gap is at the numerical floor, so no row routes.}}
\label{{tab:collapse}}
\small
\begin{{tabular}}{{lrrrr}}
\toprule
Router & Gate mass (imu, audio, vision) & Between-modality $L_1$ & IMU ret. & Audio ret. \\
\midrule
{collapse_family_table(runs)}
\bottomrule
\end{{tabular}}
\end{{table}}

\subsection{{The task-conditioned router reaches the ceiling --- in {n_escaped} seeds of {n_seeds}}}
Given a learned embedding of \emph{{which task is being asked}}, the router can in principle route. At seed 42 it looked like a clean pass: five of six grid cells cleared the gate in both modalities. The registered replicate at seed 1042 \textbf{{reversed}} it: zero of six. That split changed the reportable quantity from ``does it pass'' to ``how often does it escape'', and eight seeds were run in total at an identical six-cell grid (router learning rate $\in \{{0.3, 1, 3\}} \times$ the bridge rate, with and without an entropy bonus). Table~\ref{{tab:escape}} and Figure~\ref{{fig:escape}} report every seed; none is dropped.

The escape rate is \textbf{{{n_escaped}/{n_seeds}}}. The two outcomes are close to bimodal rather than a continuum: escaped seeds land with \texttt{{load\_ema}} at $\approx$ [{mean([load[0] for load in escaped_load]):.2f}, {mean([load[1] for load in escaped_load]):.2f}, {mean([load[2] for load in escaped_load]):.2f}] over (imu, audio, vision) and own-brick mass {min(escaped_audio_mass):.2f}--{max(escaped_audio_mass):.2f} on audio; collapsed seeds land at $\approx$ [{mean([load[0] for load in collapsed_load]):.2f}, {mean([load[1] for load in collapsed_load]):.3f}, {mean([load[2] for load in collapsed_load]):.2f}] with audio's own mass at {min(collapsed_audio_mass):.3f}--{max(collapsed_audio_mass):.3f}. Only one seed sits between the modes, so the paper says ``close to bimodal'' rather than claiming a clean switch from eight points.

Three facts locate the failure in the training dynamic rather than in the configuration.

\begin{{enumerate}}
  \item \textbf{{The grid does not decide it.}} No cell is safe across seeds and none fails across seeds: the best cells ({best_cell_label}) clear {summary['best_count']}/{n_seeds} overall and {best_escaped}/{n_escaped} among the escaped seeds; the worst clear {summary['worst_count']}/{n_seeds}. The grid moves the result by a cell or two; the seed moves it by six.
  \item \textbf{{The bricks do not decide it.}} The collapsing seeds have audio bricks that are, if anything, better ({', '.join(fmt(value, 3) for value in collapsed_audio_single)} against seed 42's {fmt(probe(router42, 'audio', 'single'), 3)}), and the oracle reaches 100\% at every seed.
  \item \textbf{{The failure has a direction.}} It is always audio that is starved. Across the collapsed seeds' task-conditioned cells, IMU retention stays at {pct(min(imu_collapsed_ret))}--{pct(max(imu_collapsed_ret))}\% while audio falls to {pct(min(audio_collapsed_ret))}--{pct(max(audio_collapsed_ret))}\%. The router collapses onto the brick whose language-model loss moves most. Task conditioning weakens that attractor enough to escape it most of the time; it does not remove it.
\end{{enumerate}}

The entropy bonus does not fix it: at the collapsing seeds it raises per-example routing entropy and still routes to IMU in both modalities --- softmax temperature without separation --- and at seed 42 it was actively harmful at the highest learning rate, producing that seed's only failing task-conditioned cell.

What the escaped seeds show is worth keeping, because it is exact. When the router engages, $\cos(\mathrm{{merged}}, \mathrm{{own}}) = {fmt(engaged_cos, 4)}$ and $\|\mathrm{{merged}}\| = {fmt(engaged_l2, 2)}$ against $\|\mathrm{{own}}\| = {fmt(engaged_own, 2)}$, with retention at or above 100\% in both modalities. The router does not find a better way to \emph{{add}} the bricks; it \textbf{{mutes}} them, returning the merged delta to the $\cos \approx 1$ regime the dose-response identified as the only survivable one. The dose curve, the oracle, and the escaped router are three views of one fact. (Retention above 100\%, up to {pct(max(ret(row['run'], modality, mode) for row in summary['escaped'] for modality in ('imu', 'audio') for mode in summary['task_modes']))}\%, is noise: one item is {100 / n_items:.1f} points and a near-one-hot mixture differing by two items sits well inside that. The claim is ``recovers the single-brick number'', not ``beats it''.)

\begin{{table}}[t]
\centering
\caption{{Router escape across {n_seeds} seeds at an identical six-cell grid. ``Cells clearing'' counts task-conditioned cells that clear {gate_pct} in \emph{{every}} measured modality. \texttt{{load\_ema}} and own-brick mass are read at \texttt{{gate-task-lr-1}}. No seed is dropped.}}
\label{{tab:escape}}
\footnotesize
\begin{{tabular}}{{lrlrrl}}
\toprule
Seed & Cells clearing & \texttt{{load\_ema}} (imu, audio, vision) & Own mass (IMU) & Own mass (audio) & Outcome \\
\midrule
{escape_table(runs)}
\midrule
\multicolumn{{5}}{{l}}{{\textbf{{Escape rate}}}} & \textbf{{{n_escaped}/{n_seeds} seeds}} \\
\bottomrule
\end{{tabular}}
\end{{table}}

\begin{{figure}}[t]
\centering
\includegraphics[width=0.9\linewidth]{{paper7_router_escape.png}}
\caption{{The escape is close to bimodal and hyperparameter-independent. Left: end-of-training load EMA per seed --- either the router splits its load between the two task bricks, or it collapses onto IMU. Right: retention of both probes across all six grid cells of each seed; IMU survives everywhere, audio is either recovered or extinguished, and the cells within a seed agree.}}
\label{{fig:escape}}
\end{{figure}}

\subsection{{Two caveats that must travel together}}
\textbf{{First, the router is \emph{{given}} the task identity.}} It still has to learn, from the language-model loss alone with no supervision on brick identity, that this identity maps to a near-one-hot selection over coefficient heads --- and when it escapes, it does, in {int(router42['gate_steps'])} steps. But it should be described for what it is: a \emph{{learned oracle}}, not a system that infers from the sensor stream which brick is relevant. Under this construction the sensor stream \emph{{cannot}} carry that signal, by design, and the modality-blind null proves it at all {n_seeds} seeds with a between-modality $L_1$ gap of {gap:.3e}.

\textbf{{Second, it fails outright in a quarter of the seeds, and nothing in the grid predicts which.}} A mechanism that reaches the ceiling on {n_escaped} seeds and chance on {n_seeds - n_escaped}, with no hyperparameter selecting between them, is a result --- but it is not yet a method.

So the honest form: \textbf{{selection-based composition is exactly right when it engages, recovering each brick's single-brick probe to the item, and the only learned mechanism we found for engaging it collapses onto the loudest brick in {n_seeds - n_escaped} seeds of {n_seeds}}}. This section is an existence proof plus a named open problem, not a recipe. Anything stronger would be a claim built on a seed --- which is exactly what the seed-42 run would have supported and the seed-1042 run refuted.

\section{{The open problem}}
\label{{sec:open}}
Addition is closed. Every additive rule we can construct fails, including the two that were designed to be interference-free by construction, and the mechanism is now localized somewhere addition cannot reach. Routing is the road, and the specific obstacle is not architectural but dynamical: \textbf{{make the router's escape selectable}}. The escape is bimodal, hyperparameter-independent and directional --- it collapses onto the brick whose loss moves most --- which points at the optimization schedule rather than the architecture. Three concrete candidates: per-brick loss normalization, so no expert can win the race to saturation; a warmup in which each expert is trained alone before the router is allowed to mix; and explicit routing supervision, which trades the ``learned'' claim for a working system and would establish the upper bound the unsupervised version is chasing. A second open question follows immediately from the collapse mechanism: the escape rate should degrade with the number of experts, so three or four probed modalities is the test that says whether {n_escaped}/{n_seeds} is a floor or a ceiling.

\section{{Related Work}}
Weight-space merging is a mature literature that this paper's instrument reads differently. Task arithmetic \cite{{ilharco2023task}} composes fine-tuned models by adding task vectors; TIES-merging \cite{{yadav2023ties}} resolves sign conflicts and trims low-magnitude entries before summing; DARE \cite{{yu2024dare}} shows delta parameters are extremely redundant and rescales after random dropping; model soups \cite{{wortsman2022soups}} average weights of models fine-tuned from a common initialization. LoRA-specific composition includes LoraHub \cite{{huang2024lorahub}}, which learns per-task mixing coefficients over a library of adapters. All of these report in-objective or aggregate downstream metrics --- average accuracy over a task set, or the merged model's score on each task's own benchmark. Our contribution is orthogonal to the merge rules and lies in the measurement: \emph{{each constituent's own behavioral probe, re-measured under the merge, against an \texttt{{others\_only}} control}}. That instrument is what converts ``retention is 94.7\%'' into ``the probe is at chance'', and it is what makes the disjoint-allocation negative interpretable rather than merely disappointing.

The interference we measure is also distinct from what the merging literature usually models. TIES and DARE both treat interference as a \emph{{parameter-space}} phenomenon --- sign disagreement and magnitude swamping in shared coordinates --- and both mitigate it by editing coordinates. Our disjoint and layer allocations remove that phenomenon entirely, by construction and by measurement, and the behavioral damage survives unchanged, which localizes it downstream in the residual stream.

The routing half connects to mixture-of-experts. Sparse expert routing and its load-balancing pathologies are well documented \cite{{shazeer2017moe,fedus2022switch}}: a router that collapses onto a subset of experts, starving the rest, is the classical imbalance failure, and the standard remedy is an auxiliary load-balancing loss. We observe exactly that pathology in an unusual setting --- three experts, two tasks, a router over \emph{{adapter coefficient heads}} rather than over feed-forward blocks --- and we report that the standard remedy does not work here: the balance penalty pinned within 1\% of its theoretical maximum only chooses \emph{{which}} expert the constant lands on. What does work, when it works, is conditioning the router on task identity, which is closer to the per-task mixing of LoraHub than to per-token MoE routing; and what remains open is the bistability, which the MoE literature's expert-choice and warmup remedies are the natural next place to look.

Finally, the conditional bridge itself and its basis reparameterization are prior work of ours \cite{{penov2026bridges,penov2026note,penov2026basis}}; the composition negative reported at the end of \cite{{penov2026basis}} is what this paper set out to fix.

\section{{Limitations}}
\textbf{{One model, one scale.}} Every number is on LFM 2.5 230M. ``Six degrees of rotation costs you the probe'' is exactly the sort of claim that could soften with model size, and no scale point above 230M is reported here.
\textbf{{Two probed bricks.}} Routing over two task bricks plus one context brick is the easiest routing problem that is not trivial, and n = 2 turns out to be bistable; the paper does not overclaim from it.
\textbf{{Vision is never probed.}} The suite has no vision label probe, so vision enters as a context brick trained on the text objective and is measured only through the damage it does. All behavioral claims are scoped to IMU and to audio at {int(power_audio['results']['true']['steps'])} steps.
\textbf{{{n_items} evaluation items per probe.}} One item is {100 / n_items:.1f} points and the 95\% binomial half-width at the six-way chance rate is $\pm{fmt(hw_imu, 3)}$; differences below about five points are not resolvable, and no ranking is claimed inside that band.
\textbf{{Single-seed cells.}} The dose-response curve, the pairwise decomposition, the four-merge-rule table and the collapsed-router family are seed 42 only, and are labelled as such wherever they appear. The three-seed and eight-seed aggregates carry the load-bearing claims.
\textbf{{The layer partition is contiguous and balanced by flat size.}} Interleaved and capacity-matched partitions are unexplored; what is falsified is the pure-angle prediction, not every conceivable site partition.
\textbf{{The router is task-conditioned and its escape is seed-determined.}} See \S\ref{{sec:selection}}; these two caveats are load-bearing and neither can be dropped.

\section{{Conclusion}}
We built the measurement that composition research is missing --- each constituent's own out-of-objective probe under the merged weights --- and it changes what the results say. A merge that is provably lossless in weight space, verified to a coefficient recovery ratio of {fmt(rec_ratio, 6)}, is behaviorally dead; a merge that scores {pct(bpb_shared['merge_results']['sum']['retention_vs_singles_mean'])}\% on the in-objective metric is dead in exactly the same way. The tolerance for adding a foreign adaptation is about {dose_tol_deg:.0f} degrees, so no additive rule survives, and when we built the one design our own angle account said should work --- perfect ownership of disjoint sites --- it failed at two seeds, which localizes the damage as cross-layer residual-stream interaction rather than weight-space overlap. What does work is not arithmetic but selection: an oracle recovers every brick exactly at every seed, and a task-conditioned learned router reaches that ceiling precisely when it escapes a collapse basin, in {n_escaped} seeds of {n_seeds}. The headline is the one the whole paper is built around: \textbf{{zero weight-space interference is not enough}}. The next problem is not a better merge rule; it is making the escape selectable.

\section*{{Reproducibility Statement}}
Every number in this manuscript is rendered from the bundled run artifacts by the repository's renderer (\texttt{{src/render\_arxiv7.py}}); the figures are rendered from the same artifacts by \texttt{{src/figures7.py}}. The artifacts in \texttt{{arxiv7/artifacts/}} are the raw per-run JSON written by the harness, and the same files drive the per-run reports produced by \texttt{{python -m src.report\_disjoint}}, so the manuscript and the run reports cannot disagree. Editing \texttt{{arxiv7/main.tex}} by hand is reverted on the next render. Code, artifacts, and the exact render pipeline: \url{{https://github.com/kortexa-ai/legolm.basis}}.

\bibliographystyle{{plain}}
\bibliography{{references}}
\end{{document}}
"""
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "main.tex"
    target.write_text(tex.strip() + "\n")
    return target


def bundle_artifacts(dirs: list[Path], out_dir: Path) -> int:
    """Copy every artifact the renderer reads into the manuscript directory.

    These files are published, so a run that recorded an absolute path would
    carry a home directory into a public repository. The composition artifacts
    record no filesystem paths at all; this fails loudly if that ever changes,
    rather than shipping one.
    """
    dest = out_dir / "artifacts"
    dest.mkdir(parents=True, exist_ok=True)
    copied = 0
    for directory in dirs:
        for path in sorted(directory.glob("*.json")):
            if path.name == "summary.json":
                continue  # a roll-up of the per-run files, not read by the renderer
            text = path.read_text()
            if str(Path.home()) in text:
                raise SystemExit(f"{path} records an absolute home path; sanitize before bundling")
            shutil.copy2(path, dest / path.name)
            copied += 1
    return copied


def main() -> None:
    parser = argparse.ArgumentParser(description="Render the composition paper from the run artifacts")
    parser.add_argument("--results", type=Path, nargs="*", default=None)
    parser.add_argument("--output-dir", type=Path, default=REPO_ROOT / "arxiv7")
    parser.add_argument("--figures-dir", type=Path, default=REPO_ROOT / "figures7")
    parser.add_argument("--compile", action="store_true")
    args = parser.parse_args()

    dirs = artifact_dirs(args.results)
    runs = load(dirs)
    if not compose_runs(runs):
        raise SystemExit(f"No composition artifacts found in {[str(path) for path in dirs]}")
    tex = write_tex(runs, args.output_dir)
    print(f"Wrote {tex} from {len(runs)} artifacts in {[str(path) for path in dirs]}")
    if dirs != [args.output_dir / "artifacts"]:
        print(f"Bundled {bundle_artifacts(dirs, args.output_dir)} artifacts")
    if args.figures_dir.exists():
        fig_dst = args.output_dir / "figures"
        fig_dst.mkdir(parents=True, exist_ok=True)
        for png in args.figures_dir.glob("paper7_*.png"):
            shutil.copy2(png, fig_dst / png.name)
    if args.compile:
        subprocess.run(
            ["tectonic", "-X", "compile", "main.tex", "--keep-intermediates", "--keep-logs"],
            cwd=args.output_dir,
            check=True,
        )


if __name__ == "__main__":
    main()
