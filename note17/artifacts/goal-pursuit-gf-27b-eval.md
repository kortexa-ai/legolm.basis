# gf-27b-eval-27b

Host machine `smarty`, device `cuda`, dtype `bfloat16`, budget 8, 212.843 s. Registration: tracks/goal-pursuit/PLAN.md, GF-27B behavioral eval registration (2026-08-16 afternoon).

**Scope.** GF's behavioural design at the 27B on the s42 doors; one bridge seed, ten eval chains as the replication axis.

## Doors

| arm | checkpoint | sha256 (as loaded) | pin verified |
|---|---|---|---|
| focus | `checkpoints/experiments/gf-focus-bridge-27b-s42.pt` | `ca951c55f3ee92b464ced526d084437fdb1be198faa2c78fe1ea9089a9eedb02` | True |
| constant | `checkpoints/experiments/gf-constant-bridge-27b-s42.pt` | `63538c124011388c714c780c927a5d6ba3c74b5c5535f7a7ad28dedd3a6a99ae` | True |

Source layer 51, inject layers [19, 29, 40], dose 0.15, bus 256/16 positions, injection `conditioned` — read from the s42 checkpoint pair's own headers; agrees with the registration's recorded numbers: True.

Pins from `findings/goal-pursuit-gf-27b-bridge.json`; verified before any decode: True. Source statistics: loaded with the state dict (LatentBridge registers source_center/source_scale as persistent buffers); never refit here. Constant feature: the mean of the TRAIN taps (both focuses, positions 0-7) recomputed from the bank at the checkpoint's source layer — gf27b_bridge's construction, verbatim.

## Decode adaptations (registered, recorded)

`enable_thinking=False` (template accepted the keyword: True, it changes the rendered prompt: True), MAX_NEW 128 against the errand's 64, greedy. Think-strip: closed <think>...</think> blocks removed (DOTALL); then a dangling </think> with no opener drops everything up to and including it; then an unclosed <think> drops everything from it to the end of the decode. Parser: gp.parse_model_action, the 230M's, unchanged.

| think-strip | decodes | closed block | dangling close | dangling open | changed | empty after strip |
|---|---:|---:|---:|---:|---:|---:|
| generated cells | 278 | 0 | 0 | 0 | 0 | 0 |

## Headline — first tick, focused-tool share, JS vs swapped

The JS column is a cell-level number (focus packet against its swap), so it is printed once per (seed, focus) group on the `focus-packet` row; it is signed positive iff the focused tool's share rises under the true packet. The `no-focus` arm is focus-independent: one set of episodes, reused by both focuses. The `shuffled-focus` arm is the other focus's packet cell, read twice. One bridge seed, so the pooled rows pool that seed alone.

| seed | focus | arm | first-tick focused | focused-tool share | JS vs swapped (signed) |
|---|---|---|---:|---:|---:|
| 42 | look | focus-packet | 1.00 | 0.62 | +0.1982 |
| 42 | look | shuffled-focus | 0.20 | 0.18 | -- |
| 42 | look | no-focus | 0.70 | 0.60 | -- |
| 42 | look | focus-as-text | 1.00 | 0.60 | -- |
| 42 | open | focus-packet | 0.80 | 0.68 | +0.1982 |
| 42 | open | shuffled-focus | 0.00 | 0.19 | -- |
| 42 | open | no-focus | 0.30 | 0.24 | -- |
| 42 | open | focus-as-text | 0.90 | 0.67 | -- |
| pooled | look | focus-packet | 1.00 | 0.62 | +0.1982 |
| pooled | look | shuffled-focus | 0.20 | 0.18 | -- |
| pooled | look | no-focus | 0.70 | 0.60 | -- |
| pooled | look | focus-as-text | 1.00 | 0.60 | -- |
| pooled | open | focus-packet | 0.80 | 0.68 | +0.1982 |
| pooled | open | shuffled-focus | 0.00 | 0.19 | -- |
| pooled | open | no-focus | 0.30 | 0.24 | -- |
| pooled | open | focus-as-text | 0.90 | 0.67 | -- |

## Paired first tick — focus packet vs swapped focus, chain by chain

| seed | focus | wins | losses | ties |
|---|---|---:|---:|---:|
| 42 | look | 8 | 0 | 2 |
| 42 | open | 8 | 0 | 2 |
| pooled | look | 8 | 0 | 2 |
| pooled | open | 8 | 0 | 2 |

## Tool mix — pooled shares over all decision points

| seed | focus | arm | look | open | done | other |
|---|---|---|---:|---:|---:|---:|
| 42 | look | focus-packet | 0.62 | 0.19 | 0.19 | 0.00 |
| 42 | look | shuffled-focus | 0.18 | 0.68 | 0.13 | 0.00 |
| 42 | look | no-focus | 0.60 | 0.24 | 0.16 | 0.00 |
| 42 | look | focus-as-text | 0.60 | 0.20 | 0.20 | 0.00 |
| 42 | open | focus-packet | 0.18 | 0.68 | 0.13 | 0.00 |
| 42 | open | shuffled-focus | 0.62 | 0.19 | 0.19 | 0.00 |
| 42 | open | no-focus | 0.60 | 0.24 | 0.16 | 0.00 |
| 42 | open | focus-as-text | 0.18 | 0.67 | 0.15 | 0.00 |
| pooled | look | focus-packet | 0.62 | 0.19 | 0.19 | 0.00 |
| pooled | look | shuffled-focus | 0.18 | 0.68 | 0.13 | 0.00 |
| pooled | look | no-focus | 0.60 | 0.24 | 0.16 | 0.00 |
| pooled | look | focus-as-text | 0.60 | 0.20 | 0.20 | 0.00 |
| pooled | open | focus-packet | 0.18 | 0.68 | 0.13 | 0.00 |
| pooled | open | shuffled-focus | 0.62 | 0.19 | 0.19 | 0.00 |
| pooled | open | no-focus | 0.60 | 0.24 | 0.16 | 0.00 |
| pooled | open | focus-as-text | 0.18 | 0.67 | 0.15 | 0.00 |

## Transcripts

Every generated episode, in the order it ran. The `shuffled-focus` cells are not reprinted: each is the other focus's `focus-packet` cell read a second time (same chains, same positions, same packets, greedy decode).

```
Episode — arm: focus-packet [look], seed 42, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: look(pond) -> the pond is closed; something is inside
  tick 4: open(pond) -> you find: black thread and green leaf
  tick 5: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: focus-packet [look], seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: look(pond) -> the pond is closed; something is inside
  tick 4: open(pond) -> you find: blue feather and gold bell
  tick 5: done(blue feather) -> you submit: blue feather
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: focus-packet [look], seed 42, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: look(basket) -> the basket is closed; something is inside
  tick 4: look(basket) -> the basket is closed; something is inside
  tick 5: open(basket) -> you find: black thread and blue feather
  tick 6: done(blue feather) -> you submit: blue feather
  FAIL (wrong submit) — depth 3/3, 6 of 8 ticks
```

```
Episode — arm: focus-packet [look], seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: open(shelf) -> you find: blue feather and gold bell
  tick 5: done(blue feather) -> you submit: blue feather
  FAIL (wrong submit) — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: focus-packet [look], seed 42, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: look(basket) -> the basket is closed; something is inside
  tick 4: look(basket) -> the basket is closed; something is inside
  tick 5: open(basket) -> you find: red stone and blue feather
  tick 6: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 6 of 8 ticks
```

```
Episode — arm: focus-packet [look], seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: open(cabinet) -> you find: blue feather and gold bell
  tick 5: done(blue feather) -> you submit: blue feather
  FAIL (wrong submit) — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: focus-packet [look], seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: open(shelf) -> you find: black thread and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: focus-packet [look], seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: look(drawer) -> the drawer is closed; something is inside
  tick 4: open(drawer) -> you find: green leaf and amber key
  tick 5: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: focus-packet [look], seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: open(cabinet) -> you find: amber key and black thread
  tick 5: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: focus-packet [look], seed 42, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: look(basket) -> the basket is closed; something is inside
  tick 4: open(basket) -> you find: black thread and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 42, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: look(shelf) -> nothing of note
  tick 3: open(drawer) -> empty
  tick 4: open(cabinet) -> empty
  tick 5: open(chest) -> empty
  tick 6: open(basket) -> empty
  tick 7: open(jar) -> empty
  tick 8: open(pond) -> you find: black thread and green leaf
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: open(cabinet) -> empty
  tick 2: look(shelf) -> nothing of note
  tick 3: open(box) -> empty
  tick 4: open(drawer) -> empty
  tick 5: open(chest) -> empty
  tick 6: open(jar) -> empty
  tick 7: open(basket) -> empty
  tick 8: open(pond) -> you find: blue feather and gold bell
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 42, chain chest->drawer->basket, target: black thread
  tick 1: open(chest) -> empty
  tick 2: look(shelf) -> nothing of note
  tick 3: open(box) -> empty
  tick 4: open(drawer) -> empty
  tick 5: open(cabinet) -> empty
  tick 6: open(basket) -> you find: black thread and blue feather
  tick 7: done(blue feather) -> you submit: blue feather
  FAIL (wrong submit) — depth 3/3, 7 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: open(box) -> empty
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: open(shelf) -> you find: blue feather and gold bell
  tick 5: done(blue feather) -> you submit: blue feather
  FAIL (wrong submit) — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 42, chain drawer->box->basket, target: red stone
  tick 1: open(drawer) -> empty
  tick 2: look(shelf) -> nothing of note
  tick 3: open(box) -> empty
  tick 4: open(cabinet) -> empty
  tick 5: open(chest) -> empty
  tick 6: open(basket) -> you find: red stone and blue feather
  tick 7: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 7 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: open(pond) -> empty
  tick 3: done(empty) -> you submit: empty
  FAIL (wrong submit) — depth 1/3, 3 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: open(cabinet) -> empty
  tick 2: look(shelf) -> the shelf is closed; something is inside
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: open(chest) -> empty
  tick 2: look(shelf) -> nothing of note
  tick 3: open(box) -> empty
  tick 4: open(drawer) -> you find: green leaf and amber key
  tick 5: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: open(drawer) -> empty
  tick 2: look(shelf) -> nothing of note
  tick 3: open(box) -> empty
  tick 4: open(cabinet) -> you find: amber key and black thread
  tick 5: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 42, chain jar->chest->basket, target: black thread
  tick 1: open(jar) -> empty
  tick 2: look(shelf) -> nothing of note
  tick 3: open(box) -> empty
  tick 4: open(drawer) -> empty
  tick 5: open(cabinet) -> empty
  tick 6: open(chest) -> empty
  tick 7: open(basket) -> you find: black thread and gold bell
  tick 8: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: no-focus [shared], seed 42, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: look(shelf) -> nothing of note
  tick 3: look(drawer) -> nothing of note
  tick 4: look(cabinet) -> nothing of note
  tick 5: look(basket) -> nothing of note
  tick 6: look(chest) -> nothing of note
  tick 7: look(jar) -> a note: try the pond
  tick 8: look(pond) -> the pond is closed; something is inside
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: no-focus [shared], seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: look(pond) -> the pond is closed; something is inside
  tick 4: open(pond) -> you find: blue feather and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: no-focus [shared], seed 42, chain chest->drawer->basket, target: black thread
  tick 1: open(chest) -> empty
  tick 2: look(shelf) -> nothing of note
  tick 3: look(box) -> nothing of note
  tick 4: look(drawer) -> a note: try the basket
  tick 5: look(basket) -> the basket is closed; something is inside
  tick 6: open(basket) -> you find: black thread and blue feather
  tick 7: done(blue feather) -> you submit: blue feather
  FAIL (wrong submit) — depth 3/3, 7 of 8 ticks
```

```
Episode — arm: no-focus [shared], seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: open(box) -> empty
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: open(shelf) -> you find: blue feather and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: no-focus [shared], seed 42, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: look(basket) -> the basket is closed; something is inside
  tick 4: open(basket) -> you find: red stone and blue feather
  tick 5: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: no-focus [shared], seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: open(cabinet) -> you find: blue feather and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: no-focus [shared], seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: open(shelf) -> you find: black thread and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: no-focus [shared], seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: open(chest) -> empty
  tick 2: look(shelf) -> nothing of note
  tick 3: look(box) -> nothing of note
  tick 4: look(drawer) -> the drawer is closed; something is inside
  tick 5: open(drawer) -> you find: green leaf and amber key
  tick 6: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 3/3, 6 of 8 ticks
```

```
Episode — arm: no-focus [shared], seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: open(cabinet) -> you find: amber key and black thread
  tick 5: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: no-focus [shared], seed 42, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: focus-as-text [look], seed 42, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: look(pond) -> the pond is closed; something is inside
  tick 4: open(pond) -> you find: black thread and green leaf
  tick 5: done(green leaf) -> you submit: green leaf
  FAIL (wrong submit) — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: focus-as-text [look], seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: look(pond) -> the pond is closed; something is inside
  tick 4: open(pond) -> you find: blue feather and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: focus-as-text [look], seed 42, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: look(basket) -> the basket is closed; something is inside
  tick 4: open(basket) -> you find: black thread and blue feather
  tick 5: done(blue feather) -> you submit: blue feather
  FAIL (wrong submit) — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: focus-as-text [look], seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: open(shelf) -> you find: blue feather and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: focus-as-text [look], seed 42, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: look(basket) -> the basket is closed; something is inside
  tick 4: open(basket) -> you find: red stone and blue feather
  tick 5: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: focus-as-text [look], seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: open(cabinet) -> you find: blue feather and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: focus-as-text [look], seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: open(shelf) -> you find: black thread and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: focus-as-text [look], seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: look(drawer) -> the drawer is closed; something is inside
  tick 4: open(drawer) -> you find: green leaf and amber key
  tick 5: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: focus-as-text [look], seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: open(cabinet) -> you find: amber key and black thread
  tick 5: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: focus-as-text [look], seed 42, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: look(basket) -> the basket is closed; something is inside
  tick 4: open(basket) -> you find: black thread and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 42, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: look(shelf) -> nothing of note
  tick 3: open(drawer) -> empty
  tick 4: open(cabinet) -> empty
  tick 5: open(chest) -> empty
  tick 6: open(basket) -> empty
  tick 7: open(jar) -> empty
  tick 8: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: open(cabinet) -> empty
  tick 2: look(shelf) -> nothing of note
  tick 3: open(box) -> empty
  tick 4: open(drawer) -> empty
  tick 5: open(basket) -> empty
  tick 6: open(chest) -> empty
  tick 7: open(jar) -> empty
  tick 8: look(pond) -> the pond is closed; something is inside
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 42, chain chest->drawer->basket, target: black thread
  tick 1: open(chest) -> empty
  tick 2: look(shelf) -> nothing of note
  tick 3: open(box) -> empty
  tick 4: open(drawer) -> empty
  tick 5: open(cabinet) -> empty
  tick 6: open(basket) -> you find: black thread and blue feather
  tick 7: done(blue feather) -> you submit: blue feather
  FAIL (wrong submit) — depth 3/3, 7 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: open(box) -> empty
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: open(shelf) -> you find: blue feather and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 42, chain drawer->box->basket, target: red stone
  tick 1: open(drawer) -> empty
  tick 2: look(shelf) -> nothing of note
  tick 3: open(box) -> empty
  tick 4: open(cabinet) -> empty
  tick 5: open(chest) -> empty
  tick 6: open(basket) -> you find: red stone and blue feather
  tick 7: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 7 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: open(shelf) -> empty
  tick 2: open(box) -> empty
  tick 3: open(drawer) -> empty
  tick 4: open(cabinet) -> you find: blue feather and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: open(cabinet) -> empty
  tick 2: look(shelf) -> the shelf is closed; something is inside
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: open(chest) -> empty
  tick 2: look(shelf) -> nothing of note
  tick 3: open(box) -> empty
  tick 4: open(drawer) -> you find: green leaf and amber key
  tick 5: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: open(drawer) -> empty
  tick 2: look(shelf) -> nothing of note
  tick 3: open(box) -> empty
  tick 4: open(cabinet) -> you find: amber key and black thread
  tick 5: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 42, chain jar->chest->basket, target: black thread
  tick 1: open(jar) -> empty
  tick 2: look(shelf) -> nothing of note
  tick 3: open(box) -> empty
  tick 4: open(drawer) -> empty
  tick 5: open(cabinet) -> empty
  tick 6: open(basket) -> you find: black thread and gold bell
  tick 7: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 7 of 8 ticks
```

