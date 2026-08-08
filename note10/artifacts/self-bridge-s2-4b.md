# Self-bridge S2: block-act carry at 4B

One frozen `Qwen/Qwen3.5-4B` in both roles. Pass 1 asks lane A's question with block A active and the emitter taps layer 19 at the last position of the pass-1 exchange; pass 2 is a **fresh context** -- null turn, block B active, no retained cache -- with the trained receiver injecting at layers 7, 11, 15. The packet is the only thing that crosses.

* objective: v1.10 forward-KL distillation; teacher = two-turn history + block B; 384 steps (the registration is silent on steps; 384 is the v1.10 lineage default), batch 8, dose 0.15.
* seeds 42, 1042, 2042; blocks from `/home/francip/src/legolm/checkpoints/bridges-march` (March vintage), sha256s in the provenance section.
* 95% Wilson half-widths; greedy decode; deterministic given the checkpoints.

## Verdict

**Reading: teacher-abort.** S3 does not open.

* `temporal>self` -- **aborted**: teacher survival below the registered two-thirds floor. Teacher survival 0.000 (A-carry 0.025, B-function 0.600); floors measured anyway -- untrained 0.000, diary 0.000, B-solo 0.100.
* `self>temporal` -- **aborted**: teacher survival below the registered two-thirds floor. Teacher survival 0.000 (A-carry 0.000, B-function 0.625); floors measured anyway -- untrained 0.000, diary 0.000, B-solo 0.000.
* `temporal>geo` -- **aborted**: teacher survival below the registered two-thirds floor. Teacher survival 0.000 (A-carry 0.050, B-function 0.375); floors measured anyway -- untrained 0.200, diary 0.000, B-solo 0.000.
* `geo>temporal` -- **aborted**: teacher survival below the registered two-thirds floor. Teacher survival 0.000 (A-carry 0.000, B-function 0.604); floors measured anyway -- untrained 0.000, diary 0.000, B-solo 0.000.

## Per pair, per seed

| pair | seed | A-carry | untrained floor | text-note floor | B-function | B-solo | retention | shuffled | gate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|:--:|

## Dose curves (A-carry / B-function)

| pair | seed | 0.10 | 0.15 | 0.20 | 0.25 | 0.30 |
|---|---:|---:|---:|---:|---:|---:|

## The in-band floors

`untrained-carry` is the sequential-composition cell re-measured here -- pass 1 under A, the swap, pass 2 over the retained cache. `text-note` is the diary: pass 1's words re-fed into a fresh context under B. `b-solo` is B alone on the null turn. None of them depends on a packet, so they are measured whether or not a pair trains.

| pair | untrained A-carry | diary A-carry | B-solo function | diary B-function |
|---|---:|---:|---:|---:|
| `temporal>self` | 0/10 (0.000) | 0/10 (0.000) | 1/10 (0.100) | 2/10 (0.200) |
| `self>temporal` | 0/12 (0.000) | 0/12 (0.000) | 0/12 (0.000) | 0/12 (0.000) |
| `temporal>geo` | 2/10 (0.200) | 0/10 (0.000) | 0/10 (0.000) | 1/10 (0.100) |
| `geo>temporal` | 0/12 (0.000) | 0/12 (0.000) | 0/12 (0.000) | 5/12 (0.417) |

## Teacher usability

The registered rule: a teacher decode that fails A-carry or B-function on its own excludes that item, and under two-thirds survival the pair does not train. The two halves are reported separately because they move independently.

| pair | usable | survival | A-carry | B-function | median words | turn run-on | pass-1 score |
|---|---:|---:|---:|---:|---:|---:|---:|
| `temporal>self` | 0/40 | 0.000 | 0.025 | 0.600 | 9 | 17/40 | 0.525 |
| `self>temporal` | 0/48 | 0.000 | 0.000 | 0.625 | 4 | 8/48 | 0.271 |
| `temporal>geo` | 0/40 | 0.000 | 0.050 | 0.375 | 25 | 26/40 | 0.525 |
| `geo>temporal` | 0/48 | 0.000 | 0.000 | 0.604 | 4 | 16/48 | 0.417 |

## Integrity

| pair | seed | zero-dose exact | max abs diff | base weights | training cache crossings | eval cache crossings |
|---|---:|---|---:|---|---:|---:|

Cache-crossing columns count decoder entries handed a non-empty `past_key_values` during the packet path. They must be zero: the untrained-carry floor deliberately uses a cache and is measured outside the guarded region.

## Provenance

* commit `1ed9175f9438e72473631e723653e2d228bc3f2e`, host `smarty`, device `cuda`, dtype `bfloat16`, 0.05 h wall
* registration: tracks/self-bridge/PLAN.md, 2026-08-07 S2 registration
* block `geo` `/home/francip/src/legolm/checkpoints/bridges-march/geo-4B-r4.pt` sha256 `666056a97dadcd0e9fda4cf40e6997deaf0c13f780d02b4777791b7954ddbb3c`
* block `self` `/home/francip/src/legolm/checkpoints/bridges-march/self-4B-r4.pt` sha256 `52b836bbd11fbfcd8b7d96e53d7bf591b95919a855303f4443f87359cd6b744d`
* block `temporal` `/home/francip/src/legolm/checkpoints/bridges-march/temporal-4B-r4.pt` sha256 `c1ef485d2ee5306d94d307fc323f27d96e82fb70c38c49694a0df1b8eaa71dbe`
* LoRA r4-attn, 32 modules, 786,432 dims

