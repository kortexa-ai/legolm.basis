# Self-bridge S1: can a model write a note to its own next pass?

One frozen `Qwen/Qwen3.5-0.8B` @ `2fc06364715b967f1860aea9cf38778875588b17` plays both roles. Pass 1's residual is tapped at layer 19 (last prompt position, detached, train-split centered); pass 2 is a **fresh context** -- null-io's null turn, no system prompt, no retained cache -- with the trained receiver injecting conditioned deltas at layers 7, 11, 15. The 256-dimensional packet is the only carrier.

* 192 steps, batch 8, lr 0.003, training dose 0.15, seeds 42, 1042, 2042.
* evaluated on the **test** split (16 held-out items: phrasings never trained on).
* one tap, fixed splits, greedy decode; the only variation across seeds is the bridge initialisation and the batch schedule.

## The gate

**S2 opens**: the nine registered checks hold at every seed.

| registered check | seed 42 | seed 1042 | seed 2042 |
|---|:--:|:--:|:--:|
| `true_top1_at_least_075` | pass | pass | pass |
| `shuffled_top1_at_most_025` | pass | pass | pass |
| `off_mean_random_near_chance` | pass | pass | pass |
| `true_margin_beats_shuffled` | pass | pass | pass |
| `generation_recovers_at_least_six_of_eight` | pass | pass | pass |
| `zero_dose_is_exact_identity` | pass | pass | pass |
| `bridge_gradients_finite_base_absent` | pass | pass | pass |
| `base_weights_byte_identical` | pass | pass | pass |
| `packet_probe_at_least_075` | pass | pass | pass |
| **all nine** | **pass** | **pass** | **pass** |

## Conditions on the held-out split

| seed | true | shuffled | off | mean | random | true margin | shuffled margin |
|---|---:|---:|---:|---:|---:|---:|---:|
| 42 | 1.000 | 0.000 | 0.000 | 0.125 | 0.000 | +11.221 | -13.400 |
| 1042 | 1.000 | 0.000 | 0.000 | 0.125 | 0.188 | +10.960 | -13.479 |
| 2042 | 1.000 | 0.000 | 0.000 | 0.125 | 0.000 | +12.424 | -15.278 |

Top-1 is the unrestricted argmax over the whole vocabulary, not a forced choice among the eight labels.

## Generation from the null turn

| seed | true | shuffled | off |
|---|---:|---:|---:|
| 42 | 16/16 (1.000) | 0/16 (0.000) | 0/16 (0.000) |
| 1042 | 16/16 (1.000) | 0/16 (0.000) | 0/16 (0.000) |
| 2042 | 16/16 (1.000) | 0/16 (0.000) | 0/16 (0.000) |

## Dose sweep and training

| seed | dose 0.10 | dose 0.15 | dose 0.20 | final batch acc | packet probe (test) |
|---|---:|---:|---:|---:|---:|
| 42 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| 1042 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| 2042 | 0.000 | 1.000 | 0.875 | 1.000 | 1.000 |

## Identity and integrity

| seed | zero dose exact | max abs difference | first gradient | base grads absent | base weights unchanged | cache crossings |
|---|---|---:|---:|---|---|---:|
| 42 | True | 0 | 16.3718 | True | True | 0 |
| 1042 | True | 0 | 15.3775 | True | True | 0 |
| 2042 | True | 0 | 16.7412 | True | True | 0 |

The cache column counts decoder entries during training that were handed a non-empty `past_key_values`. It must be zero: the registered claim is that the packet is the only carrier, and that is a plumbing fact before it is a learning one.

## Provenance

* commit `81b32ea0724bd63a2ffd7b710949d2f1e38f530e`, host `snappy`, device `mps`, dtype `float32`, 11.6 min wall
* registration: tracks/self-bridge/PLAN.md, 2026-08-06 S1 registration
* pass 1 tap: layer 19, 72 features, hidden 1024
* pass 2: fresh; no retained cache, null user `.` (tracks/null-io/null_experiments.py), no system prompt

