# Paper 7 (composition) — build status

**Complete and published (2026-08-03).** Manuscript `main.pdf`, 15 pages.
Public snapshot: `kortexa-ai/legolm.basis`, `arxiv7/`, alongside paper 3.

## How it builds

```bash
python -m src.figures7          # 4 PNGs -> figures7/
python -m src.render_arxiv7 --compile   # main.tex + artifacts + figures -> arxiv7/, then tectonic
```

`render_arxiv7.py` reads the three phase directories under `results/` when they
exist and falls back to `arxiv7/artifacts/` when they do not, so the public
snapshot re-renders the paper without the runs present. Both entry points share
the accessors in `render_arxiv7.py`, so a figure and a table can never disagree.

**Every number is rendered.** Nothing in `main.tex` is typed by hand and editing
it is reverted on the next render. The same per-run JSONs drive
`python -m src.report_disjoint`, which produces the run READMEs, so the
manuscript and the run reports read the same source.

## What is bundled

`artifacts/` — 32 per-run JSONs, promoted from the three gitignored result
directories:

| Source | Files | What they carry |
|---|---|---|
| `results/lfm230m-disjoint-20260802` | 9 | capacity pilots, the 2 BPB composition runs (the anti-metric table), disjoint/shared seeds 42 & 1042 |
| `results/lfm230m-disjoint-p2-20260803` | 13 | audio power run, seed completion, pairwise (IA/IV/AV), alpha arms, the dose-response, the 4 collapsed-router arms |
| `results/lfm230m-decisive-20260803` | 10 | layer partition at seeds 42 & 1042, the 8-seed task-conditioned router grid |

The two `summary.json` roll-ups are deliberately not bundled: they are
aggregates of the per-run files, and the renderer reads the per-run files.

## Figures

| File | Role |
|---|---|
| `figures/paper7_dose_response.png` | the money figure — retention against cos, ~7 degrees of tolerance |
| `figures/paper7_retention_vs_cos.png` | every merged cell in the paper, all arms, one axis |
| `figures/paper7_layer_partition.png` | the falsification: perfect geometry, dead probes |
| `figures/paper7_router_escape.png` | escape/collapse bimodality across 8 seeds |

Matplotlib, Okabe–Ito palette shared with `src/figures.py`, 300 dpi.
`matplotlib` is a declared dependency for exactly this reason.

## Scope, as published

LFM 2.5 230M only; no scale point. Two powered probes (IMU at 600 steps, audio
at 1800); vision participates as a context brick and is never probed. The
memory+confidence confabulation endpoint is **deferred** — see `PROGRAM.md`,
"Pending: 7b", for what it requires before it can run.

## Not in this paper, registered elsewhere

The router-basin experiment (`PROGRAM.md`, "Pending: 7c") decides whether the
constructive section ever becomes a method. Until it runs, paper 7's selection
section is an existence proof plus a named open problem, and the draft says so
in those words.
