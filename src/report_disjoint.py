from __future__ import annotations

import argparse
import json
from pathlib import Path

# Render the Phase 3 v1/v2 (paper 7) tables straight from the run artifacts, so
# no number in the README or the write-up is ever typed by hand. Multiple result
# directories may be passed; the seed tables are meant to span the v1 and v2
# runs, which live in separate dated directories.


def load(directories: list[Path]) -> dict[str, dict]:
    results = {}
    for directory in directories:
        for path in sorted(directory.glob("*.json")):
            if path.name == "summary.json" or path.stem in results:
                continue
            try:
                results[path.stem] = json.loads(path.read_text())
            except json.JSONDecodeError:
                continue  # a run still in flight (empty redirect target)
    return results


def fmt(value: float, digits: int = 3) -> str:
    return f"{value:.{digits}f}"


def merge_columns(run: dict) -> list[str]:
    """Merge modes actually present in this run's probe results, in run order."""
    first = run["results"][next(iter(run["results"]))]["modes"]
    return [mode for mode in run.get("merge_modes", []) if mode in first]


def arm_of(run: dict) -> str:
    """Identity of a configuration, ignoring the seed — the row key for seed tables."""
    steps = run.get("task_steps_per_brick") or {}
    tag = "".join(brick[0].upper() for brick in run["bricks"])
    suffix = ""
    if steps and len(set(steps.values())) > 1:
        suffix = "-" + ",".join(f"{brick}{value}" for brick, value in sorted(steps.items()))
    return f"{tag} {run['bridge']} ({run['allocation']}){suffix}"


def compose_runs(runs: dict[str, dict]) -> list[tuple[str, dict]]:
    return [(name, runs[name]) for name in sorted(runs) if name.startswith("compose-task-")]


def spread(values: list[float]) -> str:
    if len(values) == 1:
        return f"{fmt(values[0])} (1 seed)"
    mean = sum(values) / len(values)
    return f"{fmt(mean)} ±{fmt((max(values) - min(values)) / 2)} (n={len(values)})"


def pilot_table(runs: dict[str, dict]) -> list[str]:
    rows = [name for name in runs if name.startswith(("pilot-", "power-"))]
    if not rows:
        return []
    lines = [
        "| run | modality | slice width | steps | rank-1 (true) | no_bridge | chance | n | train s |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for name in sorted(rows):
        run = runs[name]
        true = run["results"]["true"]
        no_bridge = run["results"].get("no_bridge", {}).get("rank1")
        width = name.split("-frozen-")[-1].split("-")[0]
        chance = 1 / 6 if run["modality"] == "imu" else 1 / 50
        lines.append(
            f"| {name} | {run['modality']} | {width} | {true.get('steps', '')} "
            f"| {fmt(true['rank1'])} | {'—' if no_bridge is None else fmt(no_bridge)} | {fmt(chance)} "
            f"| {true['count']} | {true['train_elapsed_s']:.0f} |"
        )
    return lines


def seed_table(runs: dict[str, dict]) -> list[str]:
    """Per-seed rank-1 and retention, grouped by arm x modality x merge."""
    grouped: dict[tuple[str, str, str], dict[int, tuple[float, float]]] = {}
    singles: dict[tuple[str, str], dict[int, float]] = {}
    for _, run in compose_runs(runs):
        arm = arm_of(run)
        for modality, payload in run["results"].items():
            singles.setdefault((arm, modality), {})[run["seed"]] = payload["modes"]["single"]["true"]["rank1"]
            for mode in merge_columns(run):
                grouped.setdefault((arm, modality, mode), {})[run["seed"]] = (
                    payload["modes"][mode]["true"]["rank1"],
                    payload["retention"][mode],
                )
    if not grouped:
        return []
    lines = [
        "| arm | modality | merge | seeds | single per seed | merged per seed | single | merged | retention |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for (arm, modality, mode), by_seed in sorted(grouped.items()):
        seeds = sorted(by_seed)
        single_values = [singles[(arm, modality)][seed] for seed in seeds]
        merged_values = [by_seed[seed][0] for seed in seeds]
        retentions = [by_seed[seed][1] for seed in seeds]
        lines.append(
            f"| {arm} | {modality} | {mode} | {','.join(str(seed) for seed in seeds)} "
            f"| {' / '.join(fmt(value) for value in single_values)} "
            f"| {' / '.join(fmt(value) for value in merged_values)} "
            f"| {spread(single_values)} | {spread(merged_values)} | {spread(retentions)} |"
        )
    return lines


def pairwise_table(runs: dict[str, dict]) -> list[str]:
    """Damage against the number of foreign bricks, and against the angle they open.

    `cos(sum, own)` is the covariate that actually moves: it is 1.0 when the
    foreign bricks contribute nothing and falls as their (orthogonal) deltas
    grow relative to the measured brick's own.
    """
    rows = []
    for name, run in compose_runs(runs):
        if "sum" not in merge_columns(run):
            continue
        n_foreign = len(run["bricks"]) - 1
        for modality, payload in run["results"].items():
            magnitudes = run.get("magnitudes", {}).get(modality, {})
            rows.append(
                (
                    modality,
                    n_foreign,
                    "+".join(sorted(brick for brick in run["bricks"] if brick != modality)) or "—",
                    name.removeprefix("compose-task-"),
                    magnitudes.get("sum_cos_own"),
                    magnitudes.get("own_l2"),
                    magnitudes.get("others_sum_l2"),
                    payload["modes"]["single"]["true"]["rank1"],
                    payload["modes"]["sum"]["true"]["rank1"],
                    payload["retention"]["sum"],
                    payload["modes"]["sum"].get("others_only", {}).get("rank1"),
                    payload["chance_rank1"],
                )
            )
    if not rows:
        return []
    lines = [
        "| modality | # foreign | foreign | run | cos(sum, own) | own L2 | others L2 "
        "| single | merged (sum) | retention | others_only | chance |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for row in sorted(rows, key=lambda item: (item[0], item[1], item[2], item[3])):
        modality, n_foreign, foreign, seed, cos, own, others, single, merged, retention, others_only, chance = row
        lines.append(
            f"| {modality} | {n_foreign} | {foreign} | {seed} "
            f"| {'—' if cos is None else f'{cos:.4f}'} | {'—' if own is None else f'{own:.2f}'} "
            f"| {'—' if others is None else f'{others:.2f}'} | {fmt(single)} | {fmt(merged)} "
            f"| {retention * 100:.1f}% | {'—' if others_only is None else fmt(others_only)} | {fmt(chance)} |"
        )
    return lines


def dose_table(runs: dict[str, dict]) -> list[str]:
    """Retention against cos(merged, own), swept by attenuating the foreign bricks.

    `beta-x` merges own + x*others, so beta-1 is exactly `sum` and beta-0 would
    be the single brick. Everything but the foreign contribution is held fixed,
    which makes this the controlled version of the pairwise comparison.
    """
    lines = [
        "| run | modality | merge | beta | cos(merged, own) | merged L2 | single | merged | retention | others_only |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    found = False
    for name, run in compose_runs(runs):
        modes = [mode for mode in merge_columns(run) if mode.startswith("beta-") or mode == "sum"]
        if not any(mode.startswith("beta-") for mode in modes):
            continue
        found = True
        for modality, payload in run["results"].items():
            magnitudes = run.get("magnitudes", {}).get(modality, {})
            single = payload["modes"]["single"]["true"]["rank1"]
            ordered = sorted(modes, key=lambda mode: 1.0 if mode == "sum" else float(mode.removeprefix("beta-")))
            for mode in ordered:
                beta = 1.0 if mode == "sum" else float(mode.removeprefix("beta-"))
                others_only = payload["modes"][mode].get("others_only", {}).get("rank1")
                lines.append(
                    f"| {name} | {modality} | {mode} | {beta:g} "
                    f"| {magnitudes.get(f'{mode}_cos_own', 0):.4f} | {magnitudes.get(f'{mode}_l2', 0):.2f} "
                    f"| {fmt(single)} | {fmt(payload['modes'][mode]['true']['rank1'])} "
                    f"| {payload['retention'][mode] * 100:.1f}% "
                    f"| {'—' if others_only is None else fmt(others_only)} |"
                )
    return lines if found else []


def layer_partition_table(runs: dict[str, dict]) -> list[str]:
    """The layer partition itself: which layers and which flat range each brick owns."""
    lines = [
        "| run | brick | layers | flat range | dims | share of D |",
        "|---|---|---|---|---|---|",
    ]
    found = False
    for name, run in compose_runs(runs):
        if run.get("allocation") != "layer":
            continue
        found = True
        bounds = run.get("layer_bounds") or []
        total = sum(run.get("layer_sizes") or []) or 1
        for index, brick in enumerate(run["bricks"]):
            start, end = run["layer_blocks"][brick]
            layer_span = f"{bounds[index]}–{bounds[index + 1] - 1}" if bounds else "—"
            lines.append(
                f"| {name} | {brick} | {layer_span} | [{start}, {end}) | {end - start} "
                f"| {(end - start) / total * 100:.1f}% |"
            )
    return lines if found else []


def layer_geometry_table(runs: dict[str, dict]) -> list[str]:
    """Site-local vs global geometry — the decisive pair for the layer arm.

    The phase-2 angle account read *globally* predicts failure here (the merged
    vector carries mass in coordinates this brick never writes, so the global
    cosine is well below the 0.99 the dose curve says is needed). Read
    *site-locally* it predicts ~100% retention, because the merged delta
    restricted to a brick's own layer block is exactly that brick's own delta.
    Retention in the last column picks the winner.
    """
    lines = [
        "| run | modality | merge | cos(merged, own) global | cos in own block "
        "| others in own block L2 | own outside block L2 | retention |",
        "|---|---|---|---|---|---|---|---|",
    ]
    found = False
    for name, run in compose_runs(runs):
        if run.get("allocation") != "layer":
            continue
        for modality, payload in run["results"].items():
            entry = run.get("magnitudes", {}).get(modality, {})
            if "layer_block" not in entry:
                continue
            found = True
            for mode in ["single"] + merge_columns(run):
                if f"{mode}_cos_own" not in entry:
                    continue
                retention = "1.000 (ref)" if mode == "single" else f"{payload['retention'][mode] * 100:.1f}%"
                lines.append(
                    f"| {name} | {modality} | {mode} | {entry[f'{mode}_cos_own']:.4f} "
                    f"| {entry.get(f'{mode}_cos_own_inblock', float('nan')):.7f} "
                    f"| {entry.get('others_in_own_block_l2', 0):.3e} "
                    f"| {entry.get('own_outside_block_l2', 0):.3e} | {retention} |"
                )
    return lines if found else []


def router_diagnostic_table(runs: dict[str, dict], tol: float = 1e-4) -> list[str]:
    """Did the router route, or did it learn a constant? One row per run x gate.

    The between-modality L1 gap decides first, because routing *is* answering
    differently when a different modality is asked. Only then does the
    within-modality dispersion say what kind of router it is:
      * gap ~ 0 — **modality-blind**: the same gate whichever brick owns the
        question, so it cannot route no matter how much it varies per example.
        This is the phase-2 collapse, and by the leak-free pool construction it
        is the *correct* answer to the question a feature-only router is asked:
        the ambient slots and the live slot are drawn from the same per-brick
        pool, so its input is identical across modalities and a modality-blind
        gate is its optimum.
      * gap large, `per_brick_std` ~ 0 — **task-routed**, constant within a
        modality: it routes off the task embedding alone.
      * gap large, `per_brick_std` > 0 — **task-routed and per-example**.
    Phase 2 could only catch the first because `per_brick_mean` happened to be
    byte-identical across modalities; this makes it a single-run verdict.
    """
    lines = [
        "| run | gate | lr | per-example std (max) | between-modality L1 gap | entropy mean / max "
        "| own-brick mass by modality | router verdict |",
        "|---|---|---|---|---|---|---|---|",
    ]
    found = False
    for name, run in compose_runs(runs):
        modes: dict[str, dict[str, dict]] = {}
        for modality, payload in run["results"].items():
            for mode, entry in (payload.get("gate_weights") or {}).items():
                modes.setdefault(mode, {})[modality] = entry
        for mode, per_modality in modes.items():
            entries = list(per_modality.values())
            if any("per_brick_std" not in entry for entry in entries):
                continue  # a phase-2 artifact, written before the dispersion stats existed
            found = True
            max_std = max(max(entry["per_brick_std"]) for entry in entries)
            gap = 0.0
            for left, right in zip(entries, entries[1:]):
                gap = max(
                    gap,
                    sum(abs(a - b) for a, b in zip(left["per_brick_mean"], right["per_brick_mean"])),
                )
            entropy = ", ".join(f"{entry['entropy_mean']:.4f}" for entry in entries)
            ceiling = entries[0]["entropy_max_possible"]
            masses = ", ".join(
                f"{modality} {entry['self_mean']:.4f}" for modality, entry in sorted(per_modality.items())
            )
            if mode == "gate-oracle":
                verdict = "oracle (one-hot by construction)"
            elif gap <= tol:
                verdict = "MODALITY-BLIND — cannot route"
                if max_std > tol:
                    verdict += " (varies per example, identically for both)"
            elif max_std > tol:
                verdict = "task-routed, per-example"
            else:
                verdict = "task-routed, constant within modality"
            lr = run.get("gate_stats", {}).get(mode, {}).get("lr")
            lines.append(
                f"| {name.removeprefix('compose-task-')} | {mode} | {'—' if lr is None else f'{lr:.1e}'} "
                f"| {max_std:.3e} | {gap:.3e} | {entropy} / {ceiling:.4f} | {masses} | {verdict} |"
            )
    return lines if found else []


def router_escape_table(runs: dict[str, dict], threshold: float = 0.80) -> list[str]:
    """Per seed: does the task-conditioned router escape collapse, and how often?

    The phase-3 v3 finding is that this is *bistable* — within a seed every
    lr x entropy cell agrees, and `load_ema_final` sits at one of two modes —
    so the reportable quantity is a rate over seeds, not a best cell. Every
    seed is counted; none is dropped.
    """
    rows = []
    for name, run in compose_runs(runs):
        # Only the phase-3 v3 grid, whose task routers name their own lr. Phase
        # 2's bare `gate-task` ran at the saturating 10x default and is a
        # different experiment, not another seed of this one.
        task_modes = [mode for mode in run.get("gate_modes", []) if mode.startswith("gate-task-lr-")]
        if len(task_modes) < 2:
            continue
        passing = [
            mode
            for mode in task_modes
            if all(payload["retention"][mode] >= threshold for payload in run["results"].values())
        ]
        stats = run.get("gate_stats", {})
        reference = "gate-task-lr-1" if "gate-task-lr-1" in stats else task_modes[0]
        load = stats.get(reference, {}).get("load_ema_final") or []
        own = {
            modality: payload.get("gate_weights", {}).get(reference, {}).get("self_mean")
            for modality, payload in run["results"].items()
        }
        rows.append(
            (
                run["seed"],
                f"| {run['seed']} | {len(passing)}/{len(task_modes)} "
                f"| {', '.join(f'{value:.3f}' for value in load)} "
                f"| {', '.join(f'{modality} {value:.4f}' for modality, value in sorted(own.items()) if value is not None)} "
                f"| {'escaped' if passing else 'COLLAPSED'} |"
            )
        )
    if not rows:
        return []
    escaped = sum(1 for _, line in rows if line.endswith("escaped |"))
    lines = [
        f"| seed | cells clearing {threshold:.0%} in both modalities | `load_ema_final` (imu, audio, vision) "
        "| own-brick mass at `gate-task-lr-1` | outcome |",
        "|---|---|---|---|---|",
    ]
    lines.extend(line for _, line in sorted(rows))
    lines.append(f"| **escape rate** | **{escaped}/{len(rows)} seeds** | | | |")
    return lines


def gate_weight_table(runs: dict[str, dict]) -> list[str]:
    lines = [
        "| run | modality | gate | own-brick mass (mean) | min | max | per-brick mean | merged (true) | retention |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    found = False
    for name, run in compose_runs(runs):
        for modality, payload in run["results"].items():
            for mode, entry in (payload.get("gate_weights") or {}).items():
                found = True
                per_brick = ", ".join(
                    f"{brick} {value:.3f}" for brick, value in zip(run["bricks"], entry["per_brick_mean"])
                )
                lines.append(
                    f"| {name} | {modality} | {mode} | {entry['self_mean']:.3f} | {entry['self_min']:.3f} "
                    f"| {entry['self_max']:.3f} | {per_brick} "
                    f"| {fmt(payload['modes'][mode]['true']['rank1'])} "
                    f"| {payload['retention'][mode] * 100:.1f}% |"
                )
    return lines if found else []


def probe_tables(runs: dict[str, dict]) -> list[str]:
    lines: list[str] = []
    for name, run in compose_runs(runs):
        steps = run.get("task_steps_per_brick") or {}
        step_note = (
            ", ".join(f"{brick} {value}" for brick, value in sorted(steps.items())) if steps else f"{run['task_steps']}"
        )
        lines.append("")
        lines.append(
            f"**{name}** — bridge `{run['bridge']}`, allocation `{run['allocation']}`, "
            f"bricks {run['bricks']}, slices {run.get('slices')}, "
            f"task steps ({step_note}) / {run['text_steps']} text steps, seed {run['seed']}"
        )
        columns = ["single"] + merge_columns(run)
        for modality, payload in run["results"].items():
            modes = payload["modes"]
            lines.append("")
            lines.append(
                f"_{modality} probe under merged weights_ (chance {fmt(payload['chance_rank1'])}, "
                f"{payload['modes']['single']['true']['count']} items, {payload['categories']} categories)"
            )
            lines.append("| condition | " + " | ".join(columns) + " |")
            lines.append("|---" * (len(columns) + 1) + "|")
            for condition in ("true", "shuffled", "random", "no_bridge", "others_only"):
                cells = []
                present = False
                for mode in columns:
                    entry = modes[mode].get(condition)
                    if entry is None:
                        cells.append("—")
                    else:
                        cells.append(fmt(entry["rank1"]))
                        present = True
                if present:
                    lines.append(f"| {condition} | " + " | ".join(cells) + " |")
            retention = payload["retention"]
            lines.append(
                "| **retention vs single** | 1.000 | "
                + " | ".join(fmt(retention[mode]) for mode in columns if mode != "single")
                + " |"
            )
        checks = run.get("coefficient_checks", {})
        if checks:
            lines.append("")
            lines.append("| modality | merge | coeff recovery ratio | coeff rel error |")
            lines.append("|---|---|---|---|")
            for modality, per_mode in checks.items():
                for mode, entry in per_mode.items():
                    lines.append(
                        f"| {modality} | {mode} | {entry['recovered_scale_ratio_mean']:.6f} "
                        f"| {entry['coefficient_rel_error_mean']:.2e} |"
                    )
        magnitudes = run.get("magnitudes", {})
        if magnitudes:
            merges = merge_columns(run)
            lines.append("")
            lines.append(
                "| modality | own L2 | others-sum L2 | "
                + " | ".join(f"{mode} L2 | cos({mode}, own)" for mode in merges)
                + " |"
            )
            lines.append("|---" * (3 + 2 * len(merges)) + "|")
            for modality, entry in magnitudes.items():
                cells = " | ".join(
                    f"{entry.get(f'{mode}_l2', 0):.4f} | {entry.get(f'{mode}_cos_own', 0):.4f}" for mode in merges
                )
                lines.append(
                    f"| {modality} | {entry.get('own_l2', 0):.4f} | {entry.get('others_sum_l2', 0):.4f} | {cells} |"
                )
        lines.append("")
        gate_note = f"; gates {run.get('gate_stats')}" if run.get("gate_stats") else ""
        lines.append(
            f"_runtime_: train {run['train_elapsed_s']:.0f}s, eval {run['eval_elapsed_s']:.0f}s; "
            f"trainable per brick {run['trainable_params_per_brick']}; "
            f"basis {run.get('basis_diagnostics', {})}{gate_note}"
        )
    return lines


def bpb_table(runs: dict[str, dict]) -> list[str]:
    names = sorted(name for name in runs if name.startswith("compose-") and not name.startswith("compose-task-"))
    if not names:
        return []
    lines = [
        "| run | allocation | per-brick singles (BPB gain) | singles mean | mean-merge | sum-merge "
        "| retention mean | retention sum |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for name in names:
        run = runs[name]
        singles = ", ".join(f"{brick} {entry['improvement']:+.4f}" for brick, entry in run["per_brick"].items())
        merges = run["merge_results"]
        lines.append(
            f"| {name} | {run.get('allocation')} | {singles} | {run['singles_mean_improvement']:+.4f} "
            f"| {merges['mean']['improvement']:+.4f} | {merges['sum']['improvement']:+.4f} "
            f"| {merges['mean']['retention_vs_singles_mean'] * 100:.1f}% "
            f"| {merges['sum']['retention_vs_singles_mean'] * 100:.1f}% |"
        )
        magnitudes = run.get("magnitudes", {})
        if magnitudes:
            lines.append(f"| ↳ magnitudes | | {magnitudes} | | | | | |")
    return lines


def gate_table(runs: dict[str, dict], threshold: float = 0.80) -> list[str]:
    """The registered gate, evaluated mechanically.

    Supported iff every task modality retains >= 80% of its own single-brick
    rank-1 under the merge while shuffled/random/no_bridge stay at chance
    (taken as within one 95% binomial half-width of 1/n_categories).
    """
    names = [name for name, _ in compose_runs(runs)]
    if not names:
        return []
    lines = [
        "| run | modality | single (true) | merge | merged (true) | retention | controls at chance? | verdict |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for name in names:
        run = runs[name]
        for modality, payload in run["results"].items():
            modes = payload["modes"]
            single = modes["single"]["true"]["rank1"]
            count = modes["single"]["true"]["count"]
            chance = payload["chance_rank1"]
            half_width = 1.96 * (chance * (1 - chance) / count) ** 0.5
            controls = []
            for condition in ("shuffled", "random", "no_bridge"):
                entry = modes["single"].get(condition)
                if entry is not None:
                    controls.append(entry["rank1"] <= chance + 2 * half_width)
            controls_ok = all(controls)
            for mode in merge_columns(run):
                merged = modes[mode]["true"]["rank1"]
                retention = payload["retention"][mode]
                verdict = "PASS" if (retention >= threshold and controls_ok) else "FAIL"
                if mode == "gate-oracle":
                    verdict += " (ceiling, not a result)"
                elif mode.startswith("beta-"):
                    # An attenuated merge is not a deployable composition rule;
                    # it is the dose-response knob. Flag it so a PASS here is
                    # never read as the registered gate being met.
                    verdict += f" (attenuated merge, beta={mode.removeprefix('beta-')})"
                lines.append(
                    f"| {name} | {modality} | {fmt(single)} | {mode} | {fmt(merged)} "
                    f"| {retention * 100:.1f}% | {'yes' if controls_ok else 'no'} | {verdict} |"
                )
    return lines


def gate_rollup(runs: dict[str, dict], threshold: float = 0.80) -> list[str]:
    """One row per run x merge: the gate is met only if EVERY modality clears it.

    The per-modality table can show a PASS that is an accident — a router that
    collapsed onto one brick scores 100% on that brick and nothing on the other
    — so the roll-up is the row that decides.
    """
    names = [name for name, _ in compose_runs(runs)]
    if not names:
        return []
    lines = [
        "| run | merge | per-modality retention | worst modality | verdict |",
        "|---|---|---|---|---|",
    ]
    for name in names:
        run = runs[name]
        for mode in merge_columns(run):
            per_modality = {
                modality: payload["retention"][mode] for modality, payload in run["results"].items()
            }
            worst = min(per_modality, key=per_modality.get)
            passed = all(value >= threshold for value in per_modality.values())
            note = " (ceiling)" if mode == "gate-oracle" else ""
            if mode.startswith("beta-"):
                note = " (attenuated merge)"
            lines.append(
                f"| {name.removeprefix('compose-task-')} | {mode} "
                f"| {', '.join(f'{modality} {value * 100:.1f}%' for modality, value in sorted(per_modality.items()))} "
                f"| {worst} ({per_modality[worst] * 100:.1f}%) | {'PASS' if passed else 'FAIL'}{note} |"
            )
    return lines


def main() -> None:
    parser = argparse.ArgumentParser(description="Render the disjoint-composition tables from artifacts")
    parser.add_argument("results_dir", type=Path, nargs="+")
    args = parser.parse_args()
    runs = load(args.results_dir)

    blocks = [
        ("## Capacity and power pilots", pilot_table(runs)),
        ("## Registered gate — roll-up (every modality must clear 80%)", gate_rollup(runs)),
        ("## Registered gate — per modality", gate_table(runs)),
        ("## Per-seed summary", seed_table(runs)),
        ("## Damage vs number of foreign bricks (sum merge)", pairwise_table(runs)),
        ("## Dose-response: retention vs cos(merged, own)", dose_table(runs)),
        ("## Layer partition (allocation `layer`)", layer_partition_table(runs)),
        ("## Site-local vs global geometry (allocation `layer`)", layer_geometry_table(runs)),
        ("## Task-conditioned router: escape rate across seeds", router_escape_table(runs)),
        ("## Did the router route, or learn a constant?", router_diagnostic_table(runs)),
        ("## Gate mass on the brick that owns the question", gate_weight_table(runs)),
        ("## Task probes under merged weights", probe_tables(runs)),
        ("## Secondary: BPB retention", bpb_table(runs)),
    ]
    for heading, lines in blocks:
        if lines:
            print(heading)
            print("\n".join(lines))
            print()


if __name__ == "__main__":
    main()
