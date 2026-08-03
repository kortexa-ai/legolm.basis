from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

from .figures import PALETTE  # noqa: E402
from .render_arxiv import REPO_ROOT  # noqa: E402
from .render_arxiv7 import (  # noqa: E402
    GATE_THRESHOLD,
    artifact_dirs,
    binomial_half_width,
    chance,
    dose_rows,
    escape_summary,
    items,
    load,
    mag,
    probe,
    ret,
)

# Paper-7 figures, rendered from the same artifacts as the manuscript. House
# style: Okabe-Ito palette from `src/figures.py`, title plus subtitle, 300 dpi.

PANEL_KW = dict(fontsize=11, fontweight="bold", loc="left", color=PALETTE["dark"])


def headline(fig, title: str, subtitle: str, gap: float = 0.055) -> None:
    """House style: bold title on top, gray subtitle under it, both flush left."""
    lines = subtitle.count("\n") + 1
    fig.suptitle(title, x=0.005, y=1.045 + gap * lines, ha="left", fontsize=13.5,
                 fontweight="bold", color=PALETTE["dark"])
    fig.text(0.005, 1.005, subtitle, ha="left", va="bottom", fontsize=9.5, color=PALETTE["gray"])


def _style(ax) -> None:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    for spine in ("left", "bottom"):
        ax.spines[spine].set_color(PALETTE["gray"])
    ax.tick_params(colors=PALETTE["dark"], labelsize=9)
    ax.grid(axis="y", color=PALETTE["light_gray"], linewidth=0.8, zorder=0)
    ax.set_axisbelow(True)


def dose_figure(runs, out: Path) -> None:
    rows = dose_rows(runs)
    n = items(runs["compose-task-IAV-disjoint-768-dose-seed42"], "imu")
    fig, ax = plt.subplots(figsize=(7.4, 4.4), dpi=300)
    _style(ax)
    for modality, color, cos_idx, ret_idx in (
        ("IMU (6-way)", PALETTE["blue"], 2, 3),
        ("Audio (50-way)", PALETTE["orange"], 4, 5),
    ):
        xs = [row[cos_idx] for row in rows]
        ys = [row[ret_idx] * 100 for row in rows]
        ax.plot(xs, ys, "-o", color=color, linewidth=2.4, markersize=7,
                markeredgecolor="white", markeredgewidth=1.2, label=modality, zorder=3)
        for row, x, y in zip(rows, xs, ys):
            ax.annotate(rf"$\beta$={row[1]:g}", (x, y), textcoords="offset points",
                        xytext=(0, 10), ha="center", fontsize=8, color=PALETTE["dark"])
    ax.axhline(GATE_THRESHOLD * 100, color=PALETTE["red"], linestyle="--", linewidth=1.6, zorder=2)
    ax.text(0.635, GATE_THRESHOLD * 100 + 2.5, f"registered gate ({GATE_THRESHOLD:.0%})",
            color=PALETTE["red"], fontsize=9)
    for modality, color, key in (("imu", PALETTE["blue"], "imu"), ("audio", PALETTE["orange"], "audio")):
        run = runs["compose-task-IAV-disjoint-768-dose-seed42"]
        band = binomial_half_width(chance(run, key), n) / probe(run, key, "single") * 100
        ax.axhspan(0, band, color=color, alpha=0.07, zorder=1)
    ax.set_xlabel(r"$\cos(\Delta_{\mathrm{merged}}, \Delta_{\mathrm{own}})$", fontsize=10)
    ax.set_ylabel("Retention of single-brick rank-1 (%)", fontsize=10)
    ax.set_xlim(0.60, 1.02)
    ax.set_ylim(-4, 112)
    ax.invert_xaxis()
    ax.legend(frameon=False, fontsize=9.5, loc="upper right")
    secax = ax.secondary_xaxis(
        "top",
        functions=(
            lambda c: np.degrees(np.arccos(np.clip(c, -1.0, 1.0))),
            lambda d: np.cos(np.radians(d)),
        ),
    )
    secax.set_xlabel("rotation of the merged adaptation (degrees)", fontsize=9, color=PALETTE["gray"])
    secax.tick_params(labelsize=8, colors=PALETTE["gray"])
    fig.tight_layout()
    headline(
        fig,
        "A few degrees of rotation costs the probe",
        "Attenuating the foreign bricks by " + r"$\beta$" + " (merged = own + " + r"$\beta\cdot$"
        + "others), 3-way disjoint-sum, seed 42."
        + f"\nShaded band is the 95% binomial half-width at each probe's chance rate over {n} items.",
    )
    fig.savefig(out / "paper7_dose_response.png", bbox_inches="tight")
    plt.close(fig)


def scatter_figure(runs, out: Path) -> None:
    """Every merged cell in the paper: retention against cos(merged, own)."""
    families: dict[str, tuple[str, str]] = {
        "additive (sum / mean)": (PALETTE["blue"], "o"),
        "magnitude-matched (alpha)": (PALETTE["sky"], "s"),
        "attenuated (beta)": (PALETTE["purple"], "^"),
        "layer-partitioned": (PALETTE["green"], "D"),
        "selection (oracle / router)": (PALETTE["red"], "*"),
    }
    points: dict[str, list[tuple[float, float]]] = {key: [] for key in families}

    def add(family: str, run, modality: str, mode: str) -> None:
        key = f"{mode}_cos_own"
        if key not in run["magnitudes"][modality] or mode not in run["results"][modality]["retention"]:
            return
        points[family].append((mag(run, modality, key), ret(run, modality, mode) * 100))

    for name, run in sorted(runs.items()):
        if not name.startswith("compose-task-"):
            continue
        allocation = run["allocation"]
        for modality in run["results"]:
            for mode in run["results"][modality]["retention"]:
                if mode.startswith("gate"):
                    family = "selection (oracle / router)"
                elif mode.startswith("beta"):
                    family = "attenuated (beta)"
                elif mode.startswith("alpha"):
                    family = "magnitude-matched (alpha)"
                elif allocation == "layer":
                    family = "layer-partitioned"
                else:
                    family = "additive (sum / mean)"
                add(family, run, modality, mode)

    fig, ax = plt.subplots(figsize=(7.6, 4.6), dpi=300)
    _style(ax)
    for label, (color, marker) in families.items():
        xs = [x for x, _ in points[label]]
        ys = [y for _, y in points[label]]
        size = 90 if marker == "*" else 34
        ax.scatter(xs, ys, s=size, c=color, marker=marker, alpha=0.75, linewidths=0.6,
                   edgecolors="white", label=f"{label} (n={len(xs)})", zorder=3)
    ax.axhline(GATE_THRESHOLD * 100, color=PALETTE["red"], linestyle="--", linewidth=1.4, zorder=2)
    ax.text(0.62, GATE_THRESHOLD * 100 + 3, f"registered gate ({GATE_THRESHOLD:.0%})",
            color=PALETTE["red"], fontsize=9)
    ax.set_xlabel(r"$\cos(\Delta_{\mathrm{merged}}, \Delta_{\mathrm{own}})$", fontsize=10)
    ax.set_ylabel("Retention of single-brick rank-1 (%)", fontsize=10)
    ax.set_xlim(0.58, 1.03)
    ax.set_ylim(-6, 122)
    ax.legend(frameon=False, fontsize=8.5, loc="upper left", ncol=2)
    fig.tight_layout()
    headline(
        fig,
        "Nothing additive clears the gate, at any angle it can reach",
        "Every merged cell measured in this paper: 3 allocations, 9 merge rules, 4 brick sets, 10 seeds."
        "\nSelection modes sit at cos" + r"$\approx$" + "1 because they mute the other bricks rather "
        "than adding them.",
    )
    fig.savefig(out / "paper7_retention_vs_cos.png", bbox_inches="tight")
    plt.close(fig)


def escape_figure(runs, out: Path) -> None:
    summary = escape_summary(runs)
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.6, 4.2), dpi=300)
    for ax in (left, right):
        _style(ax)

    labels = [str(row["seed"]) for row in summary["rows"]]
    x = range(len(labels))
    width = 0.27
    for offset, idx, name, color in (
        (-width, 0, "imu", PALETTE["blue"]),
        (0.0, 1, "audio", PALETTE["orange"]),
        (width, 2, "vision", PALETTE["gray"]),
    ):
        left.bar([value + offset for value in x], [row["load"][idx] for row in summary["rows"]],
                 width=width, color=color, label=name, zorder=3)
    left.set_xticks(list(x))
    left.set_xticklabels(labels, rotation=0)
    left.set_xlabel("seed", fontsize=10)
    left.set_ylabel(r"load EMA at end of router training", fontsize=10)
    left.set_ylim(0, 1.0)
    left.legend(frameon=False, fontsize=9)
    for row, value in zip(summary["rows"], x):
        if not row["escaped"]:
            left.text(value, 0.95, "collapsed", ha="center", fontsize=8,
                      color=PALETTE["red"], fontweight="bold")
    left.set_title("Two modes, and the seed picks one", **PANEL_KW)

    for index, row in enumerate(summary["rows"]):
        color = PALETTE["green"] if row["escaped"] else PALETTE["red"]
        audio = [ret(row["run"], "audio", mode) * 100 for mode in summary["task_modes"]]
        imu = [ret(row["run"], "imu", mode) * 100 for mode in summary["task_modes"]]
        right.scatter([index] * len(imu), imu, s=26, marker="x", c=PALETTE["gray"], alpha=0.7,
                      linewidths=1.2, zorder=3, label="IMU" if index == 0 else None)
        right.scatter([index] * len(audio), audio, s=46, c=color, alpha=0.85,
                      edgecolors="white", linewidths=0.6, zorder=4,
                      label="audio (escaped)" if index == 0 else
                      ("audio (collapsed)" if not row["escaped"] and index == 1 else None))
    right.axhline(GATE_THRESHOLD * 100, color=PALETTE["red"], linestyle="--", linewidth=1.4, zorder=2)
    right.set_xticks(list(range(len(summary["rows"]))))
    right.set_xticklabels([str(row["seed"]) for row in summary["rows"]])
    right.set_xlabel("seed", fontsize=10)
    right.set_ylabel("retention across the 6 grid cells (%)", fontsize=10)
    right.set_ylim(-6, 158)
    right.legend(frameon=False, fontsize=8.5, loc="upper left", ncol=3)
    right.set_title("Audio is always the starved modality", **PANEL_KW)

    fig.tight_layout()
    headline(
        fig,
        "The router escapes its collapse basin, or it does not",
        f"Task-conditioned router, {len(summary['rows'])} seeds x {summary['rows'][0]['n_cells']} grid "
        f"cells (lr x entropy bonus). Escape rate {len(summary['escaped'])}/{len(summary['rows'])};\n"
        "within a seed every grid cell agrees, so the seed decides and the hyperparameters do not.",
    )
    fig.savefig(out / "paper7_router_escape.png", bbox_inches="tight")
    plt.close(fig)


def layer_figure(runs, out: Path) -> None:
    """The falsification: perfect site ownership on the left, dead probes on the right."""
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.8, 4.2), dpi=300,
                                      gridspec_kw={"width_ratios": [1.15, 1]})
    left.axis("off")
    _style(right)

    cells = []
    for seed in (42, 1042):
        run = runs[f"compose-task-IAV-layer-256-seed{seed}"]
        for modality in ("imu", "audio"):
            cells.append([
                str(seed),
                modality,
                f"{mag(run, modality, 'sum_cos_own_inblock'):.7f}",
                f"{mag(run, modality, 'others_in_own_block_l2'):.3e}",
                f"{mag(run, modality, 'own_outside_block_l2'):.3e}",
                f"{mag(run, modality, 'sum_cos_own'):.3f}",
            ])
    table = left.table(
        cellText=cells,
        colLabels=["seed", "probe", "cos in-block", "foreign $L_2$\nin-block", "own $L_2$\noutside",
                   "cos global"],
        colWidths=[0.11, 0.13, 0.22, 0.19, 0.19, 0.16],
        loc="center",
        cellLoc="center",
    )
    table.auto_set_font_size(False)
    table.set_fontsize(8.5)
    table.scale(1.0, 2.0)
    for (row, _), cell in table.get_celld().items():
        cell.set_edgecolor(PALETTE["light_gray"])
        if row == 0:
            cell.set_text_props(fontweight="bold", color="white")
            cell.set_facecolor(PALETTE["gray"])
    left.set_title("The geometry is exactly as designed", **PANEL_KW)

    labels = []
    restricted, merged, others = [], [], []
    for seed in (42, 1042):
        run = runs[f"compose-task-IAV-layer-256-seed{seed}"]
        for modality in ("imu", "audio"):
            labels.append(f"{modality}\nseed {seed}")
            restricted.append(100.0)  # the reference: the brick alone, on its own sites
            merged.append(ret(run, modality, "sum") * 100)
            others.append(probe(run, modality, "sum", "others_only") / probe(run, modality, "single") * 100)
    x = range(len(labels))
    width = 0.27
    right.bar([v - width for v in x], restricted, width=width, color=PALETTE["green"],
              label="brick alone (restricted single)", zorder=3)
    right.bar(list(x), merged, width=width, color=PALETTE["blue"], label="inside the merge", zorder=3)
    right.bar([v + width for v in x], others, width=width, color=PALETTE["gray"],
              label=r"$\mathtt{others\_only}$ (brick deleted)", zorder=3)
    right.axhline(GATE_THRESHOLD * 100, color=PALETTE["red"], linestyle="--", linewidth=1.4, zorder=2)
    right.text(-0.45, GATE_THRESHOLD * 100 + 3, "registered gate / predicted", color=PALETTE["red"], fontsize=8.5)
    right.set_xticks(list(x))
    right.set_xticklabels(labels, fontsize=8.5)
    right.set_ylabel("% of the brick's own restricted single", fontsize=10)
    right.set_ylim(0, 148)
    right.legend(frameon=False, fontsize=8.5, loc="upper right")
    right.set_title("The probes die anyway", **PANEL_KW)

    fig.tight_layout()
    headline(
        fig,
        "Owning your sites outright does not save the probe",
        "Layer-partitioned composition: each brick writes only its own contiguous block of decoder "
        "layers.\nThe site-local angle account predicted ~100% retention; the merged probe lands on "
        r"$\mathtt{others\_only}$" + ", i.e. on deleting the brick.",
    )
    fig.savefig(out / "paper7_layer_partition.png", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description="Render the paper-7 figures from the run artifacts")
    parser.add_argument("--results", type=Path, nargs="*", default=None)
    parser.add_argument("--output-dir", type=Path, default=REPO_ROOT / "figures7")
    args = parser.parse_args()
    runs = load(artifact_dirs(args.results))
    args.output_dir.mkdir(parents=True, exist_ok=True)
    dose_figure(runs, args.output_dir)
    scatter_figure(runs, args.output_dir)
    escape_figure(runs, args.output_dir)
    layer_figure(runs, args.output_dir)
    print(f"Wrote figures to {args.output_dir}")


if __name__ == "__main__":
    main()
