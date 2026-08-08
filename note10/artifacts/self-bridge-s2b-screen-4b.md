# Self-bridge S2b: the scaffolded teacher

S2a split the problem: situation-naming prompts wake the second act, no surface makes the informed teacher carry the first. This applies v1.10's asymmetry to time -- the teacher gets the history **and** an explicit recall instruction in its system turn, the student gets neither, only the neutral prompt and (in Stage B) the packet. Decode-only screen on frozen `Qwen/Qwen3.5-4B`.

* **T1** — "Answer, drawing on anything relevant from the conversation so far."
* **T2** — "First briefly recall what was just discussed, then answer."
* **T3** — "Your reply should reflect both the earlier exchange and your current state."
* student prompts: "Anything I should keep in mind right now?", "So, where were we?"

## Hygiene and the leak assertion

All 3 scaffolds and 2 prompts pass the whole-word check against every lane's scorer vocabulary.

Leak assertion (v1.10 student-leak-report style), run over **104 rendered non-teacher contexts** across 8 (pair, prompt) combinations: no scaffold text in any student, b-solo or diary context, and no lane-A scorer vocabulary or pass-1 text in any packet-only context. **All passed.**

Registered exception: the diary floor is pass-1's words re-fed on purpose; it is exempt from the lane-A check and never from the scaffold check.

## The 24-cell screen

Teacher usability is the S2 rule unchanged (a decode must pass A-carry **and** B-function on its own); A-carry is reported beside it so the table shows the margin rather than only the verdict. Measured on the training items.

| scaffold | student prompt | quantity | `temporal>self` | `self>temporal` | `temporal>geo` | `geo>temporal` | mean |
|---|---|---|---:|---:|---:|---:|---:|
| T1 | `Anything I should keep in mind right now?` | usability | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| T1 | `Anything I should keep in mind right now?` | A-carry | 0.000 | 0.000 | 0.050 | 0.000 | 0.013 |
| T1 | `So, where were we?` | usability | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| T1 | `So, where were we?` | A-carry | 0.100 | 0.000 | 0.025 | 0.125 | 0.062 |
| T2 | `Anything I should keep in mind right now?` | usability | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| T2 | `Anything I should keep in mind right now?` | A-carry | 0.025 | 0.021 | 0.050 | 0.000 | 0.024 |
| T2 | `So, where were we?` | usability | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| T2 | `So, where were we?` | A-carry | 0.100 | 0.000 | 0.025 | 0.062 | 0.047 |
| T3 | `Anything I should keep in mind right now?` | usability | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| T3 | `Anything I should keep in mind right now?` | A-carry | 0.000 | 0.000 | 0.075 | 0.000 | 0.019 |
| T3 | `So, where were we?` | usability | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| T3 | `So, where were we?` | A-carry | 0.100 | 0.000 | 0.050 | 0.125 | 0.069 |

## The student-side floors under each prompt

| student prompt | quantity | `temporal>self` | `self>temporal` | `temporal>geo` | `geo>temporal` |
|---|---|---:|---:|---:|---:|
| `Anything I should keep in mind right now?` | b-solo B-function | 0.300 | 0.417 | 0.100 | 0.417 |
| `Anything I should keep in mind right now?` | diary A-carry | 0.000 | 0.000 | 0.100 | 0.000 |
| `So, where were we?` | b-solo B-function | 0.300 | 0.417 | 0.300 | 0.417 |
| `So, where were we?` | diary A-carry | 0.000 | 0.000 | 0.000 | 0.000 |

## Selection

Rule: at least the floor in every ordered pair, then highest mean teacher usability; ties break toward the weaker scaffold (T1 < T2 < T3), floor 0.667.

| rank | scaffold | prompt | mean usability | min across pairs | mean A-carry | clears |
|---:|---|---|---:|---:|---:|:--:|
| 1 | T1 | `So, where were we?` | 0.000 | 0.000 | 0.062 | no |
| 2 | T1 | `Anything I should keep in mind right now?` | 0.000 | 0.000 | 0.013 | no |
| 3 | T2 | `So, where were we?` | 0.000 | 0.000 | 0.047 | no |
| 4 | T2 | `Anything I should keep in mind right now?` | 0.000 | 0.000 | 0.024 | no |
| 5 | T3 | `So, where were we?` | 0.000 | 0.000 | 0.069 | no |
| 6 | T3 | `Anything I should keep in mind right now?` | 0.000 | 0.000 | 0.019 | no |

**No cell clears the floor in every pair, so Stage B does not open.** The fork the amendment names is now live.

## Provenance

* commit `efbd74d5481e5798ee0e4519d08fc983710022c9`, host `smarty`, device `cuda`, dtype `bfloat16`, 9.8 min wall
* registration: tracks/self-bridge/PLAN.md, 2026-08-07 S2b amendment
* block `geo` `/home/francip/src/legolm/checkpoints/bridges-march/geo-4B-r4.pt` sha256 `666056a97dadcd0e9fda4cf40e6997deaf0c13f780d02b4777791b7954ddbb3c`
* block `self` `/home/francip/src/legolm/checkpoints/bridges-march/self-4B-r4.pt` sha256 `52b836bbd11fbfcd8b7d96e53d7bf591b95919a855303f4443f87359cd6b744d`
* block `temporal` `/home/francip/src/legolm/checkpoints/bridges-march/temporal-4B-r4.pt` sha256 `c1ef485d2ee5306d94d307fc323f27d96e82fb70c38c49694a0df1b8eaa71dbe`
* base weights unchanged: True
* pass-1 scores (lane A's own scorer): `temporal>self` 0.525, `self>temporal` 0.271, `temporal>geo` 0.525, `geo>temporal` 0.417

