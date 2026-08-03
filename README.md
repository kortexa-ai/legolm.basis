# Basis-mixture bridges, and what happens when you compose them

Two papers built on the same harness, both self-contained here.

| Manuscript | Paper | Renderer |
|---|---|---|
| `arxiv2/main.pdf` | Two Regimes of Compressed Conditioning: Basis-Mixture Bridges | `src/render_arxiv2.py`, `src/figures2.py` |
| `arxiv7/main.pdf` | Zero Weight-Space Interference Is Not Enough | `src/render_arxiv7.py`, `src/figures7.py` |

In both, **every number in the manuscript renders from the bundled artifacts**.
The prose lives in the renderer, not in `main.tex`; editing the `.tex` is
reverted on the next render.

## Two Regimes of Compressed Conditioning (`arxiv2/`)

A conditional LoRA bridge's dense output layer is reparameterized as k
coefficients over a basis of LoRA directions; two useful regimes emerge,
separated by a span threshold that scales with task complexity:

- **Trained small basis** (k=16): 16x fewer bridge parameters, equal-or-better
  language-modeling gain, six-way task conditioning at parity — and the
  diversity–quality tradeoff dissolves.
- **Frozen seeded basis** (k=256): only the 181k-parameter coefficient head
  trains (0.09% of the dense bridge; the basis is reconstructible from an RNG
  seed), reaching dense-level fifty-way conditioning at ~2x the training steps.

Artifacts: `arxiv2/summary-sweep.json`, `arxiv2/summary-dense.json`,
`arxiv2/summary-dense-scaling.json`.

```bash
python -m src.figures2
python -m src.render_arxiv2 --compile
```

```bash
./setup.sh                      # data, tokenizer, sensor caches (see paper-1 README sections below)
# a basis experiment, e.g. the trained k=16 bridge on IMU:
paper-run bridge --modality imu --checkpoint hf:LiquidAI/LFM2.5-230M --bridge basis-16
# the frozen regime:
paper-run task-eval --modality audio --checkpoint hf:LiquidAI/LFM2.5-230M \
  --bridge basis-256 --basis-lr-scale 0 --steps 2400
```

## Zero Weight-Space Interference Is Not Enough (`arxiv7/`)

Paper 2 closed by proving that coefficient-space composition is identical to
weight-space composition, and named the untested fix: give each modality its own
disjoint block of a shared frozen orthonormal basis, so weight-space
interference is zero by construction. This paper runs that, and everything it
forced afterwards.

The construction delivers exactly what it promises — the merged delta projects
back onto a brick's own block at coefficient recovery ratio **1.000006** — and
it buys nothing behaviorally. That gap is only visible with the right
instrument, which is the paper's first contribution: **each constituent's own
out-of-objective task probe, re-measured under the merged weights**, against an
`others_only` control that deletes the measured brick from the merge. Measured
that way, the merge with the best bits-per-byte retention in the program (94.7%)
has probes sitting at chance, indistinguishable from the merge scoring −106.5%.

- **Addition is closed.** Dead across 3 seeds, 2 allocations and 4 merge rules
  spanning a 3x range of norms; one foreign brick is as damaging as two; a
  controlled dose-response puts the whole tolerance at about 7 degrees of
  rotation.
- **The mechanism is not where we thought.** A layer-partitioned design gives
  each brick perfect ownership of its sites (in-block cos 1.0000000, provably
  zero foreign mass in-block) and the probes die anyway, at two seeds. The
  damage is cross-layer residual-stream interaction, not weight-space overlap.
- **Selection works; engaging it is the open problem.** An oracle router recovers
  every brick exactly (16/16 cells over 8 seeds). A task-conditioned learned
  router reaches that ceiling precisely when it escapes a collapse basin — which
  it does in 6 seeds of 8, with no hyperparameter predicting which, and only
  when handed the task identity.

Artifacts: `arxiv7/artifacts/` — 32 per-run JSONs, the same files that render the
run reports via `python -m src.report_disjoint`. Build status and scope:
`arxiv7/STATUS.md`. The three sessions that produced them ran end to end from
`./run_disjoint_v1.sh`, `./run_disjoint_p2.sh` and `./run_decisive.sh`, which
carry every arm's registered rationale in their comments.

```bash
python -m src.figures7
python -m src.render_arxiv7 --compile     # reads arxiv7/artifacts/ directly
```

```bash
COMMON="--checkpoint hf:LiquidAI/LFM2.5-230M --eval-tokens 32768 --sensor-limit 64
        --task-bricks imu,audio --context-bricks vision
        --task-steps 600 --task-steps-per-brick audio=1800 --text-steps 300
        --max-eval-items 64 --seed 42"

# the additive negative: each brick trained alone, then re-probed under the merge
paper-run compose-task $COMMON --bridge basis-disjoint-768 --allocation disjoint \
  --merge-modes sum,mean,alpha-norm,alpha-rsqrtn --conditions true,shuffled,random

# the dose-response (the money figure)
paper-run compose-task $COMMON --bridge basis-disjoint-768 --allocation disjoint \
  --merge-modes beta-0.125,beta-0.25,beta-0.5,beta-0.75,sum --conditions true

# the layer partition
paper-run compose-task $COMMON --bridge basis-frozen-256 --allocation layer \
  --merge-modes sum,mean --conditions true,shuffled,random

# the router grid (one seed of the eight)
paper-run compose-task $COMMON --bridge basis-disjoint-768 --allocation disjoint \
  --merge-modes sum --gate-steps 600 --conditions true \
  --gate-modes gate-oracle,gate-learned-lr-1,gate-task-lr-0.3,gate-task-lr-1,gate-task-lr-3,gate-task-lr-0.3-ent0.1,gate-task-lr-1-ent0.1,gate-task-lr-3-ent0.1
```

## Harness

The harness is the conditional-LoRA-bridges suite
([kortexa-ai/legolm.paper](https://github.com/kortexa-ai/legolm.paper)),
extended with `--bridge {dense,basis-<k>,basis-frozen-<k>,basis-disjoint-<k>}`,
`--basis-lr-scale`, `--allocation {shared,disjoint,layer}`, the `compose-task`
instrument and its gate modes; the `hf:` checkpoint adapter and its fidelity
notes are documented in the 230M replication note bundled with that repository.
This repository is a self-contained snapshot: the original paper's manuscript
(`arxiv/`), the replication note (`note/`), and their artifacts are included
unchanged.

One note on reproduction across the two papers. The harness here is the version
the composition runs used, in which `run_task_eval`'s training loop was
extracted into `_train_task_bridge` so a merged brick and a solo brick train
through literally the same code. Re-running the earlier `task-imu-basis-16`
config through it reproduces every control exactly and lands the `true`
condition at 0.84 against the published 0.91 — MPS kernel nondeterminism across
a 600-step run on a newer torch, well inside that config's own published
three-seed spread of 0.67–0.91. The arithmetic is unchanged; the bundled
artifacts are the originals either way.

Checkpoints are stored with Git LFS: run `git lfs pull` after cloning.

## License

MIT (see LICENSE).
