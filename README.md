# Two Regimes of Compressed Conditioning: Basis-Mixture Bridges

Code, artifacts, and manuscript for the basis-mixture bridges paper
(`arxiv2/main.pdf`). A conditional LoRA bridge's dense output layer is
reparameterized as k coefficients over a basis of LoRA directions; two useful
regimes emerge, separated by a span threshold that scales with task complexity:

- **Trained small basis** (k=16): 16x fewer bridge parameters, equal-or-better
  language-modeling gain, six-way task conditioning at parity — and the
  diversity–quality tradeoff dissolves.
- **Frozen seeded basis** (k=256): only the 181k-parameter coefficient head
  trains (0.09% of the dense bridge; the basis is reconstructible from an RNG
  seed), reaching dense-level fifty-way conditioning at ~2x the training steps.

**Every number in the manuscript renders from three bundled artifacts**
(`arxiv2/summary-sweep.json`, `arxiv2/summary-dense.json`,
`arxiv2/summary-dense-scaling.json`) via `paper-render-arxiv2`; figures via
`python -m src.figures2`.

## Reproduce

```bash
./setup.sh                      # data, tokenizer, sensor caches (see paper-1 README sections below)
# a basis experiment, e.g. the trained k=16 bridge on IMU:
paper-run bridge --modality imu --checkpoint hf:LiquidAI/LFM2.5-230M --bridge basis-16
# the frozen regime:
paper-run task-eval --modality audio --checkpoint hf:LiquidAI/LFM2.5-230M \
  --bridge basis-256 --basis-lr-scale 0 --steps 2400
```

The harness is the conditional-LoRA-bridges suite
([kortexa-ai/legolm.paper](https://github.com/kortexa-ai/legolm.paper)),
extended with `--bridge {dense,basis-<k>}` and `--basis-lr-scale`; the `hf:`
checkpoint adapter and its fidelity notes are documented in the 230M
replication note bundled with that repository. This repository is a
self-contained snapshot: the original paper's manuscript (`arxiv/`),
the replication note (`note/`), and their artifacts are included unchanged.

Checkpoints are stored with Git LFS: run `git lfs pull` after cloning.

## License

MIT (see LICENSE).
