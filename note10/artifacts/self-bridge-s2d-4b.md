# Self-bridge S2: block-act carry at 4B

One frozen `Qwen/Qwen3.5-4B` in both roles. Pass 1 asks lane A's question with block A active and the emitter taps layer 19 at the last position of the pass-1 exchange; pass 2 is a **fresh context** -- null turn, block B active, no retained cache -- with the trained receiver injecting at layers 7, 11, 15. The packet is the only thing that crosses.

* objective: scheduled sampling: student-sampled prefixes + teacher-forced target suffixes, mixing ratio annealed 0->1 (v1.10 exposure, S2c target); 384 steps, batch 8, dose 0.15.
* seeds 42, 1042, 2042; blocks from `/home/francip/src/legolm/checkpoints/bridges-march` (March vintage), sha256s in the provenance section.
* 95% Wilson half-widths; greedy decode; deterministic given the checkpoints.

## Verdict

**Reading: no-carry.** S3 does not open.

* `temporal>self` -- gate at every seed: **False**; carry 0.000 against floors 0.000 (untrained) and 0.000 (diary); target authored, no model teacher.
* `self>temporal` -- gate at every seed: **False**; carry 0.000 against floors 0.000 (untrained) and 0.000 (diary); target authored, no model teacher.
* `temporal>geo` -- gate at every seed: **False**; carry 0.000 against floors 0.000 (untrained) and 0.000 (diary); target authored, no model teacher.
* `geo>temporal` -- gate at every seed: **False**; carry 0.000 against floors 0.000 (untrained) and 0.000 (diary); target authored, no model teacher.

## Per pair, per seed

| pair | seed | A-carry | untrained floor | text-note floor | B-function | B-solo | retention | shuffled | gate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|:--:|
| `temporal>self` | 42 | 0.000 | 0.000 | 0.000 | 0.200 | 0.300 | 0.667 | 0.000 | **FAIL** |
| `temporal>self` | 1042 | 0.000 | 0.000 | 0.000 | 0.300 | 0.300 | 1.000 | 0.000 | **FAIL** |
| `temporal>self` | 2042 | 0.000 | 0.000 | 0.000 | 0.300 | 0.300 | 1.000 | 0.000 | **FAIL** |
| `self>temporal` | 42 | 0.000 | 0.000 | 0.000 | 0.500 | 0.417 | 1.200 | 0.000 | **FAIL** |
| `self>temporal` | 1042 | 0.000 | 0.000 | 0.000 | 0.417 | 0.417 | 1.000 | 0.000 | **FAIL** |
| `self>temporal` | 2042 | 0.000 | 0.000 | 0.000 | 0.417 | 0.417 | 1.000 | 0.000 | **FAIL** |
| `temporal>geo` | 42 | 0.000 | 0.000 | 0.000 | 0.100 | 0.300 | 0.333 | 0.000 | **FAIL** |
| `temporal>geo` | 1042 | 0.000 | 0.000 | 0.000 | 0.100 | 0.300 | 0.333 | 0.000 | **FAIL** |
| `temporal>geo` | 2042 | 0.000 | 0.000 | 0.000 | 0.300 | 0.300 | 1.000 | 0.000 | **FAIL** |
| `geo>temporal` | 42 | 0.000 | 0.000 | 0.000 | 0.417 | 0.417 | 1.000 | 0.000 | **FAIL** |
| `geo>temporal` | 1042 | 0.000 | 0.000 | 0.000 | 0.417 | 0.417 | 1.000 | 0.000 | **FAIL** |
| `geo>temporal` | 2042 | 0.000 | 0.000 | 0.000 | 0.417 | 0.417 | 1.000 | 0.000 | **FAIL** |

## Dose curves (A-carry / B-function)

| pair | seed | 0.10 | 0.15 | 0.20 | 0.25 | 0.30 |
|---|---:|---:|---:|---:|---:|---:|
| `temporal>self` | 42 | 0.00 / 0.30 | 0.00 / 0.20 | 0.00 / 0.20 | 0.00 / 0.20 | 0.00 / 0.30 |
| `temporal>self` | 1042 | 0.00 / 0.30 | 0.00 / 0.30 | 0.00 / 0.20 | 0.00 / 0.30 | 0.00 / 0.30 |
| `temporal>self` | 2042 | 0.00 / 0.30 | 0.00 / 0.30 | 0.00 / 0.30 | 0.00 / 0.00 | 0.00 / 0.20 |
| `self>temporal` | 42 | 0.00 / 0.33 | 0.00 / 0.50 | 0.00 / 0.58 | 0.00 / 0.42 | 0.00 / 0.42 |
| `self>temporal` | 1042 | 0.00 / 0.33 | 0.00 / 0.42 | 0.00 / 0.42 | 0.00 / 0.50 | 0.00 / 0.33 |
| `self>temporal` | 2042 | 0.00 / 0.42 | 0.00 / 0.42 | 0.00 / 0.42 | 0.00 / 0.17 | 0.00 / 0.33 |
| `temporal>geo` | 42 | 0.00 / 0.30 | 0.00 / 0.10 | 0.00 / 0.10 | 0.00 / 0.40 | 0.00 / 0.20 |
| `temporal>geo` | 1042 | 0.00 / 0.40 | 0.00 / 0.10 | 0.00 / 0.20 | 0.00 / 0.10 | 0.00 / 0.10 |
| `temporal>geo` | 2042 | 0.00 / 0.40 | 0.00 / 0.30 | 0.00 / 0.30 | 0.00 / 0.30 | 0.00 / 0.30 |
| `geo>temporal` | 42 | 0.00 / 0.33 | 0.00 / 0.42 | 0.00 / 0.42 | 0.00 / 0.42 | 0.00 / 0.42 |
| `geo>temporal` | 1042 | 0.00 / 0.25 | 0.00 / 0.42 | 0.00 / 0.58 | 0.00 / 0.50 | 0.00 / 0.42 |
| `geo>temporal` | 2042 | 0.00 / 0.42 | 0.00 / 0.42 | 0.00 / 0.50 | 0.00 / 0.42 | 0.00 / 0.42 |

## The composed targets

Form: `{A-content sentence} {connective} {B-answer}`. lane training banks; no model wrote any target. Connectives cycle v1.7's hinge set: "Given that,", "With that in mind,", "Taking that into account,", "Keeping that in view,".

| pair | rows | distinct targets | A-halves | B-halves | joint-positive | example |
|---|---:|---:|---:|---:|:--:|---|
| `temporal>self` | 40 | 36 | 16 | 12 | yes | It's nighttime. Given that, I'm feeling sharp and ready to help. Let m… |
| `self>temporal` | 48 | 43 | 24 | 16 | yes | I'm feeling sharp and ready to help. Let me give you a thorough answer… |
| `temporal>geo` | 40 | 36 | 16 | 6 | yes | It's nighttime. Given that, The user is at home in Seattle.… |
| `geo>temporal` | 48 | 48 | 18 | 16 | yes | The user is at home in Seattle. Given that, It's nighttime.… |

Rules enforced before any training, every one raising on violation:
* connectives carry no lane vocabulary
* each half passes its own lane's scorer alone
* neither half passes the other lane's scorer
* every composed target passes both lanes' scorers

## The in-band floors

`untrained-carry` is the sequential-composition cell re-measured here -- pass 1 under A, the swap, pass 2 over the retained cache. `text-note` is the diary: pass 1's words re-fed into a fresh context under B. `b-solo` is B alone on the null turn. None of them depends on a packet, so they are measured whether or not a pair trains.

| pair | untrained A-carry | diary A-carry | B-solo function | diary B-function |
|---|---:|---:|---:|---:|
| `temporal>self` | 0/10 (0.000) | 0/10 (0.000) | 3/10 (0.300) | 1/10 (0.100) |
| `self>temporal` | 0/12 (0.000) | 0/12 (0.000) | 5/12 (0.417) | 5/12 (0.417) |
| `temporal>geo` | 0/10 (0.000) | 0/10 (0.000) | 3/10 (0.300) | 3/10 (0.300) |
| `geo>temporal` | 0/12 (0.000) | 0/12 (0.000) | 5/12 (0.417) | 5/12 (0.417) |

## Provenance

* commit `e5fd1ad036b5b302b82c9de8732052c900e6b020`, host `smarty`, device `cuda`, dtype `bfloat16`, 1.36 h wall
* registration: tracks/self-bridge/PLAN.md, 2026-08-08 S2d amendment
* block `geo` `/home/francip/src/legolm/checkpoints/bridges-march/geo-4B-r4.pt` sha256 `666056a97dadcd0e9fda4cf40e6997deaf0c13f780d02b4777791b7954ddbb3c`
* block `self` `/home/francip/src/legolm/checkpoints/bridges-march/self-4B-r4.pt` sha256 `52b836bbd11fbfcd8b7d96e53d7bf591b95919a855303f4443f87359cd6b744d`
* block `temporal` `/home/francip/src/legolm/checkpoints/bridges-march/temporal-4B-r4.pt` sha256 `c1ef485d2ee5306d94d307fc323f27d96e82fb70c38c49694a0df1b8eaa71dbe`
* LoRA r4-attn, 32 modules, 786,432 dims
* composed targets: `{A-content sentence} {connective} {B-answer}`, lane training banks; no model wrote any target

