from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw

from .figures import PALETTE, PLOT_BOTTOM, PLOT_LEFT, PLOT_RIGHT, PLOT_TOP, axes, bar_chart, blank, text
from .render_arxiv import load_summary, r
from .render_arxiv2 import bridge_params, simp, stask, task_std

# Paper-2 figures, rendered from the same three artifacts as the manuscript.


def capacity_figure(sweep, dense, out: Path) -> None:
    dense_params = int(r(dense, "bridge-imu")["trainable_params"])
    labels = [f"dense\n{dense_params / 1e6:.0f}M params"]
    values = [float(r(dense, "diversity-imu-l0.00")["improvement"])]
    for k in (4, 16, 64, 256):
        params = bridge_params(sweep, k)
        labels.append(f"basis-{k}\n{params / 1e6:.1f}M params")
        values.append(simp(sweep, f"diversity-imu-l0.00-basis-{k}"))
    colors = [PALETTE["gray"], PALETTE["sky"], PALETTE["blue"], PALETTE["green"], PALETTE["purple"]]
    bar_chart(
        out / "paper2_capacity.png",
        "Compression is free: BPB improvement vs bridge size",
        "IMU, standard budget; labels rounded to 4 decimals, bar heights exact",
        labels,
        values,
        colors,
    )


def audio_budget_figure(sweep, dense, out: Path) -> None:
    frozen_2400 = (
        stask(sweep, "task-audio-basis-256-s2400-blr0")
        + stask(sweep, "task-audio-basis-256-s2400-blr0-seed1042")
        + stask(sweep, "task-audio-basis-256-s2400-blr0-seed2042")
    ) / 3
    series = [
        ("dense (199M)", PALETTE["gray"], [(600, task_std(dense, "audio")), (1200, stask(sweep, "task-audio-dense-s1200")), (2400, stask(sweep, "task-audio-dense-s2400"))]),
        ("basis-256 trained (198M)", PALETTE["blue"], [(600, stask(sweep, "task-audio-basis-256")), (1200, stask(sweep, "task-audio-basis-256-s1200")), (2400, stask(sweep, "task-audio-basis-256-s2400"))]),
        ("basis-256 frozen (181k trainable)", PALETTE["green"], [(1200, stask(sweep, "task-audio-basis-256-s1200-blr0")), (2400, frozen_2400)]),
    ]
    img, draw = blank(
        "Frozen basis reaches dense-level conditioning at ~2x steps",
        "Fifty-way audio task, rank-1 accuracy (chance 0.02); frozen point at 2400 is a three-seed mean",
    )
    ymin, ymax = 0.0, 0.5
    axes(img, draw, ymin, ymax, "Rank-1 accuracy ↑")
    xmin, xmax = 500, 2500

    def px(x):
        return int(PLOT_LEFT + (x - xmin) / (xmax - xmin) * (PLOT_RIGHT - PLOT_LEFT))

    def py(y):
        return int(PLOT_BOTTOM - (y - ymin) / (ymax - ymin) * (PLOT_BOTTOM - PLOT_TOP))

    for x in (600, 1200, 2400):
        text(draw, (px(x), PLOT_BOTTOM + 45), str(x), 25, anchor="mm")
    text(draw, ((PLOT_LEFT + PLOT_RIGHT) // 2, PLOT_BOTTOM + 95), "Task-probe training steps", 28, fill=PALETTE["gray"], anchor="mm")

    for idx, (label, color, points) in enumerate(series):
        coords = [(px(x), py(y)) for x, y in points]
        if len(coords) > 1:
            draw.line(coords, fill=color, width=6)
        for (cx, cy), (_, y) in zip(coords, points):
            draw.ellipse((cx - 12, cy - 12, cx + 12, cy + 12), fill=color, outline=PALETTE["dark"], width=3)
            text(draw, (cx, cy - 26), f"{y:.2f}", 23, anchor="ms", bold=True)
        legend_y = PLOT_TOP + 20 + idx * 42
        draw.line((PLOT_LEFT + 30, legend_y, PLOT_LEFT + 90, legend_y), fill=color, width=6)
        text(draw, (PLOT_LEFT + 105, legend_y), label, 26, anchor="lm")
    out.mkdir(parents=True, exist_ok=True)
    img.save(out / "paper2_audio_budget.png", dpi=(300, 300))


def main() -> None:
    parser = argparse.ArgumentParser(description="Render paper-2 figures from the three artifacts")
    parser.add_argument("--sweep", type=Path, default=Path("results/lfm230m-basis-sweep-20260702/summary.json"))
    parser.add_argument("--dense", type=Path, default=Path("results/lfm230m-standard-20260701/summary.json"))
    parser.add_argument("--output-dir", type=Path, default=Path("figures2"))
    args = parser.parse_args()
    sweep = load_summary(args.sweep)
    dense = load_summary(args.dense)
    capacity_figure(sweep, dense, args.output_dir)
    audio_budget_figure(sweep, dense, args.output_dir)
    print(f"Wrote figures to {args.output_dir}")


if __name__ == "__main__":
    main()
