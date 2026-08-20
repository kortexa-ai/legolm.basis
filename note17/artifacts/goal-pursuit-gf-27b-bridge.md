# gf-27b-bridge-27b

Host machine `smarty`, device `cuda`, dtype `bfloat16`, 1375.752 s. Registration: tracks/goal-pursuit/PLAN.md, GF-27B bridge registration (2026-08-16 morning).

**Scope.** trained doors only, no behavioural claim; the 27B behavioural GF eval is a separate later registration.

| quantity | value |
|---|---|
| hidden size | 5120 |
| layers | 64 |
| SOURCE_LAYER_27B | 51 (0.797 of depth) |
| recorded prior layer | 51 (0.79 of depth) |
| INJECT_LAYERS_27B | [19, 29, 40] |
| training dose | 0.15 (0 halvings) |
| steps run | 192 |

## Phase 1 — the tap scan

the depth-proportional prior carried down the ladder (the 0.8B tapped 19 of 24); the 230M's own scan later moved its tap to layer 12 of 14, which is why this rung scans.

Selection rule: best held-out accuracy; ties by train accuracy, then by closeness to the recorded prior, then by shallower layer. Probe: 300 full-batch Adam steps at 0.01, on the CPU in float32.

| layer | depth | prior? | train acc | held-out acc | held-out correct | train loss |
|---:|---:|:---:|---:|---:|---:|---:|
| 3 | 0.047 |  | 1.00 | 1.00 | 4/4 | 0.0000 |
| 11 | 0.172 |  | 1.00 | 1.00 | 4/4 | 0.0000 |
| 19 | 0.297 |  | 1.00 | 1.00 | 4/4 | 0.0000 |
| 27 | 0.422 |  | 1.00 | 1.00 | 4/4 | 0.0000 |
| 35 | 0.547 |  | 1.00 | 1.00 | 4/4 | 0.0000 |
| 43 | 0.672 |  | 1.00 | 1.00 | 4/4 | 0.0000 |
| 51 <- selected | 0.797 | **yes** | 1.00 | 1.00 | 4/4 | 0.0000 |
| 59 | 0.922 |  | 1.00 | 1.00 | 4/4 | 0.0000 |

## Phase 2 — placement and the coherence gate

Fractions [0.29, 0.46, 0.63] -> raw [19, 29, 40] -> layers [19, 29, 40] (deduplicated: False).

Gate rule: degenerate iff fewer than 10 distinct tokens or a word 3-gram repeated more than 4 times. Start dose 0.15, surviving dose 0.15 after 0 halving(s) of at most 3.

The gate bridge is UNTRAINED: only `fit_source_statistics` ran on the train taps. The prompt, verbatim:

```text
You are on a small errand. Pick exactly one action as JSON. Allowed tools: look, open, done. Places: shelf, box, drawer, pond, cabinet, basket, chest, jar. Respond with exactly one compact JSON object and no markdown fences. Valid examples: {"tool":"look","args":{"place":"shelf"}} or {"tool":"open","args":{"place":"box"}} or {"tool":"done","args":{"item":"amber key"}}. done submits the item you retrieved and ends the errand.

So far:
1. You are at the shelf.

What do you do next? One JSON action.
```

### Gate attempt 1 — dose 0.15 — PASS

distinct tokens 43 (floor 10), max word 3-gram repeats 1 (ceiling 4).

Packet decode:

```text
We need answer user's request: choose exactly one action JSON. Need likely look at shelf? We are at shelf. Need compact JSON no markdown. Need valid. Could be {"tool":"look","args":{"place":"shelf"}}. Need final only JSON.
</think>

{"tool":"look","args":{"place":"
```

No-packet decode:

```text
We need answer user's request: choose exactly one action as JSON, no markdown. We are at shelf. Allowed tools look, open, done. Places: shelf, box, drawer, pond, cabinet, basket, chest, jar. Need likely look at shelf first. So output {"tool":"look","args":{"
```

## Phase 3 — training

run_g1's recipe as gf_focus reproduces it, with the FOCUS bridge in the goal bridge's slot and the constant bridge second on one rng stream; goal_text=None throughout for both bridges (GF's registered deviation, carried); the auxiliary head is a 2-way focus classifier on the bus; done is never a training target for the focus bridge.

192 steps, batch 8, lr 0.003, AdamW wd 0.0, grad clip 1.0, dose 0.15, injection `conditioned` at [19, 29, 40], seed 42.

Wall projection at step 8: 3.394 s/step -> 0.362 h for both bridges against a 10.0 h budget; steps 192 -> 192 (cut: False).

| arm | step | loss | token accuracy | grad norm |
|---|---:|---:|---:|---:|
| focus | 1 | 2.1173 | 0.7891 | 12.4500 |
| focus | 32 | 0.0000 | 1.0000 | 0.0001 |
| focus | 64 | 0.0000 | 1.0000 | 0.0001 |
| focus | 96 | 0.0000 | 1.0000 | 0.0000 |
| focus | 128 | 0.0000 | 1.0000 | 0.0000 |
| focus | 160 | 0.0000 | 1.0000 | 0.0000 |
| focus | 192 | 0.0000 | 1.0000 | 0.0000 |
| constant | 1 | 1.4413 | 0.7978 | 10.7494 |
| constant | 32 | 0.0265 | 0.9853 | 0.0203 |
| constant | 64 | 0.0134 | 0.9853 | 0.0069 |
| constant | 96 | 0.0007 | 1.0000 | 0.0044 |
| constant | 128 | 0.0105 | 1.0000 | 0.0063 |
| constant | 160 | 0.0105 | 1.0000 | 0.0123 |
| constant | 192 | 0.0076 | 0.9926 | 0.0088 |

Focus bridge wall 650.989 s, constant bridge wall 649.818 s.

## Gates

| gate | result |
|---|---|
| held-out token accuracy [look] | 1.0 over 120 pairs (exact 1.0) |
| held-out token accuracy [open] | 1.0 over 60 pairs (exact 1.0) |
| aux on held-out taps | 4/4 — predicted ['look', 'look', 'open', 'open'], truth ['look', 'look', 'open', 'open'] |
| zero-dose bit-exactness | PASS |
| base weights byte-identical | PASS (taps True, focus True, constant True, end True) |

### Zero-dose transcripts

With a real packet at fraction 0.0:

```text
We need answer user's request: choose exactly one action as JSON, no markdown. We are at shelf. Allowed tools look, open, done. Places: shelf, box, drawer, pond, cabinet, basket, chest, jar. Need likely look at shelf first. So output {"tool":"look","args":{"
```

With no packet:

```text
We need answer user's request: choose exactly one action as JSON, no markdown. We are at shelf. Allowed tools look, open, done. Places: shelf, box, drawer, pond, cabinet, basket, chest, jar. Need likely look at shelf first. So output {"tool":"look","args":{"
```

## Checkpoints

| arm | path | sha256 |
|---|---|---|
| focus | `checkpoints/experiments/gf-focus-bridge-27b-s42.pt` | `ca951c55f3ee92b464ced526d084437fdb1be198faa2c78fe1ea9089a9eedb02` |
| constant | `checkpoints/experiments/gf-constant-bridge-27b-s42.pt` | `63538c124011388c714c780c927a5d6ba3c74b5c5535f7a7ad28dedd3a6a99ae` |

Canonical registered filenames: True.

