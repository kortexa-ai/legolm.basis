from __future__ import annotations

import argparse
import json
from pathlib import Path

# Consolidate a directory of single-experiment CLI outputs (the basis sweep)
# into a suite-style summary.json so the paper-2 renderer can follow the same
# single-artifact discipline as paper 1. Budgets and bridge specs vary per run
# and are recorded inside each result; the filename stem is the run name and
# is kept as source_file for traceability.


def group_of(name: str) -> str:
    for prefix, group in (
        ("task-", "task"),
        ("diversity-", "diversity"),
        ("compose-", "composition"),
        ("bridge-", "benchmark"),
        ("constant-", "controls"),
        ("shuffled-", "controls"),
        ("random-", "controls"),
    ):
        if name.startswith(prefix):
            return group
    return "other"


def main() -> None:
    parser = argparse.ArgumentParser(description="Aggregate loose experiment JSONs into a summary artifact")
    parser.add_argument("sweep_dir", type=Path)
    parser.add_argument("--output", type=Path, default=None, help="Defaults to <sweep_dir>/summary.json")
    parser.add_argument("--checkpoint", default="hf:LiquidAI/LFM2.5-230M")
    args = parser.parse_args()

    results = {}
    skipped = []
    for path in sorted(args.sweep_dir.glob("*.json")):
        if path.name == "summary.json":
            continue
        try:
            result = json.loads(path.read_text())
        except json.JSONDecodeError:
            skipped.append(path.name)
            continue
        if not isinstance(result, dict) or "experiment" not in result:
            skipped.append(path.name)
            continue
        name = path.stem
        results[name] = {
            "name": name,
            "group": group_of(name),
            "source_file": path.name,
            "result": result,
        }

    groups: dict[str, list[str]] = {}
    for name, payload in results.items():
        groups.setdefault(payload["group"], []).append(name)

    summary = {
        "metadata": {
            "checkpoint": args.checkpoint,
            "sweep_dir": str(args.sweep_dir),
            "note": (
                "Heterogeneous sweep: budgets, seeds, bridge specs, and basis_lr_scale vary per run "
                "and are recorded in each result (fields: steps, bridge, basis_lr_scale). "
                "Run names encode the configuration."
            ),
        },
        "summary": {"count": len(results), "groups": {k: sorted(v) for k, v in sorted(groups.items())}},
        "results": results,
    }
    output = args.output or (args.sweep_dir / "summary.json")
    output.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(f"Wrote {output}: {len(results)} results, groups {[f'{k}:{len(v)}' for k, v in sorted(groups.items())]}")
    if skipped:
        print(f"Skipped (not experiment results): {skipped}")


if __name__ == "__main__":
    main()
