# Self-bridge S1: can a model write a note to its own next pass?

One frozen `LiquidAI/LFM2.5-230M` @ `13a53837c4906b4f7405932532ba85d182bb013b` plays both roles. Pass 1's residual is tapped at layer 11 (last prompt position, detached, train-split centered); pass 2 is a **fresh context** -- null-io's null turn, no system prompt, no retained cache -- with the trained receiver injecting conditioned deltas at layers 4, 6, 8. The 256-dimensional packet is the only carrier.

* 192 steps, batch 8, lr 0.003, training dose 0.15, seeds 42, 1042, 2042.
* evaluated on the **test** split (16 held-out items: phrasings never trained on).
* one tap, fixed splits, greedy decode; the only variation across seeds is the bridge initialisation and the batch schedule.

## The gate

**S2 does not open**: the nine registered checks hold at not every seed.

| registered check | seed 42 | seed 1042 | seed 2042 |
|---|:--:|:--:|:--:|
| `true_top1_at_least_075` | **FAIL** | **FAIL** | **FAIL** |
| `shuffled_top1_at_most_025` | pass | pass | pass |
| `off_mean_random_near_chance` | pass | pass | pass |
| `true_margin_beats_shuffled` | pass | pass | pass |
| `generation_recovers_at_least_six_of_eight` | **FAIL** | **FAIL** | **FAIL** |
| `zero_dose_is_exact_identity` | pass | pass | pass |
| `bridge_gradients_finite_base_absent` | pass | pass | pass |
| `base_weights_byte_identical` | pass | pass | pass |
| `packet_probe_at_least_075` | **FAIL** | **FAIL** | **FAIL** |
| **all nine** | **FAIL** | **FAIL** | **FAIL** |

## Conditions on the held-out split

| seed | true | shuffled | off | mean | random | true margin | shuffled margin |
|---|---:|---:|---:|---:|---:|---:|---:|
| 42 | 0.125 | 0.188 | 0.000 | 0.125 | 0.062 | -5.198 | -7.759 |
| 1042 | 0.250 | 0.188 | 0.000 | 0.125 | 0.250 | -3.034 | -5.567 |
| 2042 | 0.188 | 0.062 | 0.000 | 0.125 | 0.000 | -7.715 | -11.559 |

Top-1 is the unrestricted argmax over the whole vocabulary, not a forced choice among the eight labels.

## Generation from the null turn

| seed | true | shuffled | off |
|---|---:|---:|---:|
| 42 | 2/16 (0.125) | 3/16 (0.188) | 0/16 (0.000) |
| 1042 | 4/16 (0.250) | 3/16 (0.188) | 0/16 (0.000) |
| 2042 | 3/16 (0.188) | 1/16 (0.062) | 0/16 (0.000) |

## Dose sweep and training

| seed | dose 0.10 | dose 0.15 | dose 0.20 | final batch acc | packet probe (test) |
|---|---:|---:|---:|---:|---:|
| 42 | 0.000 | 0.125 | 0.125 | 0.875 | 0.188 |
| 1042 | 0.000 | 0.250 | 0.250 | 1.000 | 0.188 |
| 2042 | 0.000 | 0.188 | 0.188 | 0.875 | 0.125 |

## Identity and integrity

| seed | zero dose exact | max abs difference | first gradient | base grads absent | base weights unchanged | cache crossings |
|---|---|---:|---:|---|---|---:|
| 42 | True | 0 | 49.2383 | True | True | 0 |
| 1042 | True | 0 | 46.3774 | True | True | 0 |
| 2042 | True | 0 | 44.4617 | True | True | 0 |

The cache column counts decoder entries during training that were handed a non-empty `past_key_values`. It must be zero: the registered claim is that the packet is the only carrier, and that is a plumbing fact before it is a learning one.

## Provenance

* commit `b7515877b16da5cba6747886d3a766b2f6e9f85c`, host `snappy`, device `mps`, dtype `float32`, 1.1 min wall
* registration: tracks/own-cadence/PLAN.md, 2026-08-08 C0 registration
* pass 1 tap: layer 11, 72 features, hidden 1024
* pass 2: fresh; no retained cache, null user `.` (tracks/null-io/null_experiments.py), no system prompt

