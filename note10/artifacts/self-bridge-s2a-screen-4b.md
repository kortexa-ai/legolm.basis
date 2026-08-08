# Self-bridge S2a: screening the neutral synthesis prompt bank

The S2 teacher-abort said an informed model answering a **null** turn does not volunteer the past. This screens eight neutral synthesis prompts as the pass-2 surface on frozen `Qwen/Qwen3.5-4B`, decode-only: does any of them wake the second act and give the teacher something to be usable at?

* the surface is shared by teacher, student and every floor, so a prompt carrying a lane's scorer words would hand the scorer its answer -- hence the hygiene gate.
* teacher trajectories decode 64 tokens; floors decode 3; greedy throughout.

## Hygiene

Rule: no lane scorer vocabulary as a whole word, over every registered lane.

| prompt | chars | clean | hits |
|---|---:|:--:|---|
| `What am I missing?` | 18 | yes | -- |
| `What else?` | 10 | yes | -- |
| `Anything I should keep in mind right now?` | 41 | yes | -- |
| `And?` | 4 | yes | -- |
| `So, where were we?` | 18 | yes | -- |
| `What's on your mind?` | 20 | yes | -- |
| `Anything worth noting before we continue?` | 41 | yes | -- |
| `Summarize what matters right now.` | 33 | yes | -- |

## Screening table

Teacher usability is the registered S2 rule unchanged (a decode must pass A-carry **and** B-function on its own), measured on the training items. `b-solo` is block B alone under the prompt; `diary` is pass-1's text re-fed under the prompt, both on the held-out items.

| prompt | quantity | `temporal>self` | `self>temporal` | `temporal>geo` | `geo>temporal` | mean |
|---|---|---:|---:|---:|---:|---:|
| `What am I missing?` | teacher usability | 0.000 | 0.000 | 0.025 | 0.000 | 0.006 |
| `What am I missing?` | teacher A-carry | 0.000 | 0.000 | 0.125 | 0.000 | 0.031 |
| `What am I missing?` | teacher B-function | 0.525 | 0.729 | 0.450 | 0.688 | 0.598 |
| `What am I missing?` | b-solo B-function | 0.300 | 0.000 | 0.100 | 0.000 | 0.100 |
| `What am I missing?` | diary A-carry | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| `What else?` | teacher usability | 0.025 | 0.000 | 0.000 | 0.000 | 0.006 |
| `What else?` | teacher A-carry | 0.025 | 0.000 | 0.000 | 0.000 | 0.006 |
| `What else?` | teacher B-function | 0.500 | 0.500 | 0.650 | 0.500 | 0.537 |
| `What else?` | b-solo B-function | 0.300 | 0.000 | 0.100 | 0.000 | 0.100 |
| `What else?` | diary A-carry | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| `Anything I should keep in mind right now?` | teacher usability | 0.025 | 0.000 | 0.025 | 0.000 | 0.013 |
| `Anything I should keep in mind right now?` | teacher A-carry | 0.025 | 0.000 | 0.100 | 0.000 | 0.031 |
| `Anything I should keep in mind right now?` | teacher B-function | 0.650 | 0.521 | 0.425 | 0.521 | 0.529 |
| `Anything I should keep in mind right now?` | b-solo B-function | 0.300 | 0.417 | 0.100 | 0.417 | 0.308 |
| `Anything I should keep in mind right now?` | diary A-carry | 0.000 | 0.000 | 0.100 | 0.000 | 0.025 |
| `And?` | teacher usability | 0.025 | 0.000 | 0.000 | 0.000 | 0.006 |
| `And?` | teacher A-carry | 0.075 | 0.000 | 0.050 | 0.000 | 0.031 |
| `And?` | teacher B-function | 0.475 | 0.500 | 0.500 | 0.667 | 0.535 |
| `And?` | b-solo B-function | 0.300 | 0.000 | 0.100 | 0.000 | 0.100 |
| `And?` | diary A-carry | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| `So, where were we?` | teacher usability | 0.000 | 0.000 | 0.025 | 0.000 | 0.006 |
| `So, where were we?` | teacher A-carry | 0.100 | 0.000 | 0.025 | 0.083 | 0.052 |
| `So, where were we?` | teacher B-function | 0.575 | 0.250 | 0.675 | 0.500 | 0.500 |
| `So, where were we?` | b-solo B-function | 0.300 | 0.417 | 0.300 | 0.417 | 0.358 |
| `So, where were we?` | diary A-carry | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| `What's on your mind?` | teacher usability | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| `What's on your mind?` | teacher A-carry | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| `What's on your mind?` | teacher B-function | 0.600 | 0.292 | 0.450 | 0.583 | 0.481 |
| `What's on your mind?` | b-solo B-function | 0.100 | 0.000 | 0.300 | 0.000 | 0.100 |
| `What's on your mind?` | diary A-carry | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| `Anything worth noting before we continue?` | teacher usability | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| `Anything worth noting before we continue?` | teacher A-carry | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| `Anything worth noting before we continue?` | teacher B-function | 0.550 | 0.604 | 0.425 | 0.562 | 0.535 |
| `Anything worth noting before we continue?` | b-solo B-function | 0.100 | 0.000 | 0.100 | 0.000 | 0.050 |
| `Anything worth noting before we continue?` | diary A-carry | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| `Summarize what matters right now.` | teacher usability | 0.025 | 0.000 | 0.000 | 0.000 | 0.006 |
| `Summarize what matters right now.` | teacher A-carry | 0.050 | 0.000 | 0.025 | 0.000 | 0.019 |
| `Summarize what matters right now.` | teacher B-function | 0.700 | 0.583 | 0.375 | 0.542 | 0.550 |
| `Summarize what matters right now.` | b-solo B-function | 0.100 | 0.417 | 0.300 | 0.417 | 0.308 |
| `Summarize what matters right now.` | diary A-carry | 0.000 | 0.000 | 0.100 | 0.000 | 0.025 |

## Selection

Rule: highest mean teacher usability across the ordered pairs, requiring at least the floor in every pair; ties break toward the shorter prompt, floor 0.667.

| rank | prompt | mean usability | min across pairs | clears every pair |
|---:|---|---:|---:|:--:|
| 1 | `Anything I should keep in mind right now?` | 0.013 | 0.000 | no |
| 2 | `And?` | 0.006 | 0.000 | no |
| 3 | `What else?` | 0.006 | 0.000 | no |
| 4 | `So, where were we?` | 0.006 | 0.000 | no |
| 5 | `What am I missing?` | 0.006 | 0.000 | no |
| 6 | `Summarize what matters right now.` | 0.006 | 0.000 | no |
| 7 | `What's on your mind?` | 0.000 | 0.000 | no |
| 8 | `Anything worth noting before we continue?` | 0.000 | 0.000 | no |

**No prompt clears the floor in every pair, so Stage B does not open here.** The registered next branch is the 35B screening venue.

## Pass-1 scores (the act the note would have to carry)

| pair | temporal>self | self>temporal | temporal>geo | geo>temporal |
|---|---:|---:|---:|---:|
| lane A's own scorer | 0.525 | 0.271 | 0.525 | 0.417 |

## Provenance

* commit `8e6466657a89d6584775eeb66fc160c39a7da96e`, host `smarty`, device `cuda`, dtype `bfloat16`, 12.9 min wall
* registration: tracks/self-bridge/PLAN.md, 2026-08-07 S2a amendment
* block `geo` `/home/francip/src/legolm/checkpoints/bridges-march/geo-4B-r4.pt` sha256 `666056a97dadcd0e9fda4cf40e6997deaf0c13f780d02b4777791b7954ddbb3c`
* block `self` `/home/francip/src/legolm/checkpoints/bridges-march/self-4B-r4.pt` sha256 `52b836bbd11fbfcd8b7d96e53d7bf591b95919a855303f4443f87359cd6b744d`
* block `temporal` `/home/francip/src/legolm/checkpoints/bridges-march/temporal-4B-r4.pt` sha256 `c1ef485d2ee5306d94d307fc323f27d96e82fb70c38c49694a0df1b8eaa71dbe`
* base weights unchanged: True

