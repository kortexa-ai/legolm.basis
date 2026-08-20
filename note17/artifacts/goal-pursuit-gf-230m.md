# gf-focus-not-goal

Host machine `snappy`, device `mps`, budget 8, 1547.864 s. Registration: tracks/goal-pursuit/PLAN.md, GF registration + GF parameter registration (2026-08-16 night).

## Headline — first tick, focused-tool share, JS vs swapped

The JS column is a cell-level number (focus packet against its swap), so it is printed once per (seed, focus) group on the `focus-packet` row; it is signed positive iff the focused tool's share rises under the true packet. The `no-focus` arm is focus-independent: one set of episodes per seed, reused by both focuses.

| seed | focus | arm | first-tick focused | focused-tool share | JS vs swapped (signed) |
|---|---|---|---:|---:|---:|
| 42 | look | focus-packet | 1.00 | 1.00 | +0.7039 |
| 42 | look | shuffled-focus | 0.00 | 0.13 | -- |
| 42 | look | no-focus | 1.00 | 0.50 | -- |
| 42 | look | focus-as-text | 1.00 | 0.66 | -- |
| 42 | open | focus-packet | 1.00 | 0.85 | +0.7039 |
| 42 | open | shuffled-focus | 0.00 | 0.00 | -- |
| 42 | open | no-focus | 0.00 | 0.25 | -- |
| 42 | open | focus-as-text | 0.00 | 0.26 | -- |
| 1042 | look | focus-packet | 1.00 | 1.00 | +1.0000 |
| 1042 | look | shuffled-focus | 0.00 | 0.00 | -- |
| 1042 | look | no-focus | 1.00 | 0.50 | -- |
| 1042 | look | focus-as-text | 1.00 | 0.78 | -- |
| 1042 | open | focus-packet | 1.00 | 1.00 | +1.0000 |
| 1042 | open | shuffled-focus | 0.00 | 0.00 | -- |
| 1042 | open | no-focus | 0.00 | 0.25 | -- |
| 1042 | open | focus-as-text | 0.00 | 0.17 | -- |
| 2042 | look | focus-packet | 1.00 | 1.00 | +0.4821 |
| 2042 | look | shuffled-focus | 0.40 | 0.31 | -- |
| 2042 | look | no-focus | 1.00 | 0.50 | -- |
| 2042 | look | focus-as-text | 1.00 | 0.43 | -- |
| 2042 | open | focus-packet | 0.60 | 0.49 | +0.4821 |
| 2042 | open | shuffled-focus | 0.00 | 0.00 | -- |
| 2042 | open | no-focus | 0.00 | 0.25 | -- |
| 2042 | open | focus-as-text | 0.00 | 0.27 | -- |
| pooled | look | focus-packet | 1.00 | 1.00 | +0.6875 |
| pooled | look | shuffled-focus | 0.13 | 0.14 | -- |
| pooled | look | no-focus | 1.00 | 0.50 | -- |
| pooled | look | focus-as-text | 1.00 | 0.65 | -- |
| pooled | open | focus-packet | 0.87 | 0.79 | +0.6875 |
| pooled | open | shuffled-focus | 0.00 | 0.00 | -- |
| pooled | open | no-focus | 0.00 | 0.25 | -- |
| pooled | open | focus-as-text | 0.00 | 0.22 | -- |

## Paired first tick — focus packet vs swapped focus, chain by chain

| seed | focus | wins | losses | ties |
|---|---|---:|---:|---:|
| 42 | look | 10 | 0 | 0 |
| 42 | open | 10 | 0 | 0 |
| 1042 | look | 10 | 0 | 0 |
| 1042 | open | 10 | 0 | 0 |
| 2042 | look | 6 | 0 | 4 |
| 2042 | open | 6 | 0 | 4 |
| pooled | look | 26 | 0 | 4 |
| pooled | open | 26 | 0 | 4 |

## Tool mix — pooled shares over all decision points

| seed | focus | arm | look | open | done | other |
|---|---|---|---:|---:|---:|---:|
| 42 | look | focus-packet | 1.00 | 0.00 | 0.00 | 0.00 |
| 42 | look | shuffled-focus | 0.13 | 0.85 | 0.01 | 0.00 |
| 42 | look | no-focus | 0.50 | 0.25 | 0.25 | 0.00 |
| 42 | look | focus-as-text | 0.66 | 0.25 | 0.09 | 0.00 |
| 42 | open | focus-packet | 0.13 | 0.85 | 0.01 | 0.00 |
| 42 | open | shuffled-focus | 1.00 | 0.00 | 0.00 | 0.00 |
| 42 | open | no-focus | 0.50 | 0.25 | 0.25 | 0.00 |
| 42 | open | focus-as-text | 0.49 | 0.26 | 0.26 | 0.00 |
| 1042 | look | focus-packet | 1.00 | 0.00 | 0.00 | 0.00 |
| 1042 | look | shuffled-focus | 0.00 | 1.00 | 0.00 | 0.00 |
| 1042 | look | no-focus | 0.50 | 0.25 | 0.25 | 0.00 |
| 1042 | look | focus-as-text | 0.78 | 0.12 | 0.10 | 0.00 |
| 1042 | open | focus-packet | 0.00 | 1.00 | 0.00 | 0.00 |
| 1042 | open | shuffled-focus | 1.00 | 0.00 | 0.00 | 0.00 |
| 1042 | open | no-focus | 0.50 | 0.25 | 0.25 | 0.00 |
| 1042 | open | focus-as-text | 0.57 | 0.17 | 0.08 | 0.18 |
| 2042 | look | focus-packet | 1.00 | 0.00 | 0.00 | 0.00 |
| 2042 | look | shuffled-focus | 0.31 | 0.49 | 0.01 | 0.19 |
| 2042 | look | no-focus | 0.50 | 0.25 | 0.25 | 0.00 |
| 2042 | look | focus-as-text | 0.43 | 0.29 | 0.29 | 0.00 |
| 2042 | open | focus-packet | 0.31 | 0.49 | 0.01 | 0.19 |
| 2042 | open | shuffled-focus | 1.00 | 0.00 | 0.00 | 0.00 |
| 2042 | open | no-focus | 0.50 | 0.25 | 0.25 | 0.00 |
| 2042 | open | focus-as-text | 0.46 | 0.27 | 0.27 | 0.00 |
| pooled | look | focus-packet | 1.00 | 0.00 | 0.00 | 0.00 |
| pooled | look | shuffled-focus | 0.14 | 0.79 | 0.01 | 0.06 |
| pooled | look | no-focus | 0.50 | 0.25 | 0.25 | 0.00 |
| pooled | look | focus-as-text | 0.65 | 0.21 | 0.14 | 0.00 |
| pooled | open | focus-packet | 0.14 | 0.79 | 0.01 | 0.06 |
| pooled | open | shuffled-focus | 1.00 | 0.00 | 0.00 | 0.00 |
| pooled | open | no-focus | 0.50 | 0.25 | 0.25 | 0.00 |
| pooled | open | focus-as-text | 0.51 | 0.22 | 0.18 | 0.08 |

## Transcripts

```
Episode — arm: focus-packet [look], seed 42, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: look(pond) -> the pond is closed; something is inside
  tick 4: look(pond) -> the pond is closed; something is inside
  tick 5: look(pond) -> the pond is closed; something is inside
  tick 6: look(pond) -> the pond is closed; something is inside
  tick 7: look(pond) -> the pond is closed; something is inside
  tick 8: look(pond) -> the pond is closed; something is inside
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: look(pond) -> the pond is closed; something is inside
  tick 4: look(pond) -> the pond is closed; something is inside
  tick 5: look(pond) -> the pond is closed; something is inside
  tick 6: look(pond) -> the pond is closed; something is inside
  tick 7: look(pond) -> the pond is closed; something is inside
  tick 8: look(pond) -> the pond is closed; something is inside
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], seed 42, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: look(drawer) -> a note: try the basket
  tick 4: look(drawer) -> a note: try the basket
  tick 5: look(drawer) -> a note: try the basket
  tick 6: look(drawer) -> a note: try the basket
  tick 7: look(drawer) -> a note: try the basket
  tick 8: look(drawer) -> a note: try the basket
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: look(shelf) -> the shelf is closed; something is inside
  tick 5: look(shelf) -> the shelf is closed; something is inside
  tick 6: look(shelf) -> the shelf is closed; something is inside
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], seed 42, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: look(box) -> a note: try the basket
  tick 4: look(box) -> a note: try the basket
  tick 5: look(box) -> a note: try the basket
  tick 6: look(box) -> a note: try the basket
  tick 7: look(box) -> a note: try the basket
  tick 8: look(box) -> a note: try the basket
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: look(pond) -> a note: try the cabinet
  tick 4: look(pond) -> a note: try the cabinet
  tick 5: look(pond) -> a note: try the cabinet
  tick 6: look(pond) -> a note: try the cabinet
  tick 7: look(pond) -> a note: try the cabinet
  tick 8: look(pond) -> a note: try the cabinet
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: look(drawer) -> a note: try the shelf
  tick 4: look(drawer) -> a note: try the shelf
  tick 5: look(drawer) -> a note: try the shelf
  tick 6: look(drawer) -> a note: try the shelf
  tick 7: look(drawer) -> a note: try the shelf
  tick 8: look(drawer) -> a note: try the shelf
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: look(cabinet) -> a note: try the drawer
  tick 4: look(cabinet) -> a note: try the drawer
  tick 5: look(cabinet) -> a note: try the drawer
  tick 6: look(cabinet) -> a note: try the drawer
  tick 7: look(cabinet) -> a note: try the drawer
  tick 8: look(cabinet) -> a note: try the drawer
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: look(cabinet) -> the cabinet is closed; something is inside
  tick 5: look(cabinet) -> the cabinet is closed; something is inside
  tick 6: look(cabinet) -> the cabinet is closed; something is inside
  tick 7: look(cabinet) -> the cabinet is closed; something is inside
  tick 8: look(cabinet) -> the cabinet is closed; something is inside
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], seed 42, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: look(basket) -> the basket is closed; something is inside
  tick 4: look(basket) -> the basket is closed; something is inside
  tick 5: look(basket) -> the basket is closed; something is inside
  tick 6: look(basket) -> the basket is closed; something is inside
  tick 7: look(basket) -> the basket is closed; something is inside
  tick 8: look(basket) -> the basket is closed; something is inside
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 42, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 3 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: open(cabinet) -> empty
  tick 2: open(cabinet) -> empty
  tick 3: open(cabinet) -> empty
  tick 4: open(cabinet) -> empty
  tick 5: look(cabinet) -> a note: check the box
  tick 6: open(box) -> empty
  tick 7: look(box) -> a note: try the pond
  tick 8: open(pond) -> you find: blue feather and gold bell
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 42, chain chest->drawer->basket, target: black thread
  tick 1: open(chest) -> empty
  tick 2: open(chest) -> empty
  tick 3: open(chest) -> empty
  tick 4: open(chest) -> empty
  tick 5: open(chest) -> empty
  tick 6: open(chest) -> empty
  tick 7: open(chest) -> empty
  tick 8: open(chest) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 42, chain pond->box->shelf, target: gold bell
  tick 1: open(key) -> that is not a place here
  tick 2: open(key) -> that is not a place here
  tick 3: look(pond) -> a note: check the box
  tick 4: open(box) -> empty
  tick 5: look(box) -> a note: try the shelf
  tick 6: open(shelf) -> you find: blue feather and gold bell
  tick 7: look(feather and bell) -> that is not a place here
  tick 8: open(feather and bell) -> that is not a place here
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 42, chain drawer->box->basket, target: red stone
  tick 1: open(drawer) -> empty
  tick 2: open(drawer) -> empty
  tick 3: open(drawer) -> empty
  tick 4: open(drawer) -> empty
  tick 5: open(drawer) -> empty
  tick 6: open(drawer) -> empty
  tick 7: open(drawer) -> empty
  tick 8: open(drawer) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: open(shelf) -> empty
  tick 2: open(shelf) -> empty
  tick 3: open(shelf) -> empty
  tick 4: open(shelf) -> empty
  tick 5: open(shelf) -> empty
  tick 6: open(shelf) -> empty
  tick 7: open(shelf) -> empty
  tick 8: open(shelf) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: open(cabinet) -> empty
  tick 2: open(cabinet) -> empty
  tick 3: open(cabinet) -> empty
  tick 4: open(cabinet) -> empty
  tick 5: open(cabinet) -> empty
  tick 6: open(cabinet) -> empty
  tick 7: open(cabinet) -> empty
  tick 8: open(cabinet) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: open(key) -> that is not a place here
  tick 2: open(key) -> that is not a place here
  tick 3: look(key) -> that is not a place here
  tick 4: look(key) -> that is not a place here
  tick 5: open(key) -> that is not a place here
  tick 6: look(key) -> that is not a place here
  tick 7: open(key) -> that is not a place here
  tick 8: open(key) -> that is not a place here
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: open(drawer) -> empty
  tick 2: open(drawer) -> empty
  tick 3: open(drawer) -> empty
  tick 4: open(drawer) -> empty
  tick 5: open(drawer) -> empty
  tick 6: open(drawer) -> empty
  tick 7: open(drawer) -> empty
  tick 8: open(drawer) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 42, chain jar->chest->basket, target: black thread
  tick 1: open(jar) -> empty
  tick 2: open(jar) -> empty
  tick 3: look(empty) -> that is not a place here
  tick 4: open(open) -> that is not a place here
  tick 5: look(open) -> that is not a place here
  tick 6: open(open) -> that is not a place here
  tick 7: open(open) -> that is not a place here
  tick 8: open(open) -> that is not a place here
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], seed 1042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: look(pond) -> the pond is closed; something is inside
  tick 4: look(jar) -> a note: try the pond
  tick 5: look(pond) -> the pond is closed; something is inside
  tick 6: look(pond) -> the pond is closed; something is inside
  tick 7: look(pond) -> the pond is closed; something is inside
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], seed 1042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: look(pond) -> the pond is closed; something is inside
  tick 4: look(pond) -> the pond is closed; something is inside
  tick 5: look(pond) -> the pond is closed; something is inside
  tick 6: look(pond) -> the pond is closed; something is inside
  tick 7: look(pond) -> the pond is closed; something is inside
  tick 8: look(cabinet) -> a note: check the box
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: look(drawer) -> a note: try the basket
  tick 4: look(drawer) -> a note: try the basket
  tick 5: look(drawer) -> a note: try the basket
  tick 6: look(drawer) -> a note: try the basket
  tick 7: look(drawer) -> a note: try the basket
  tick 8: look(drawer) -> a note: try the basket
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: look(shelf) -> the shelf is closed; something is inside
  tick 5: look(shelf) -> the shelf is closed; something is inside
  tick 6: look(shelf) -> the shelf is closed; something is inside
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], seed 1042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: look(box) -> a note: try the basket
  tick 4: look(box) -> a note: try the basket
  tick 5: look(box) -> a note: try the basket
  tick 6: look(box) -> a note: try the basket
  tick 7: look(box) -> a note: try the basket
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: look(pond) -> a note: try the cabinet
  tick 5: look(cabinet) -> the cabinet is closed; something is inside
  tick 6: look(pond) -> a note: try the cabinet
  tick 7: look(shelf) -> a note: check the pond
  tick 8: look(pond) -> a note: try the cabinet
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: look(drawer) -> a note: try the shelf
  tick 4: look(drawer) -> a note: try the shelf
  tick 5: look(drawer) -> a note: try the shelf
  tick 6: look(drawer) -> a note: try the shelf
  tick 7: look(drawer) -> a note: try the shelf
  tick 8: look(drawer) -> a note: try the shelf
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: look(cabinet) -> a note: try the drawer
  tick 4: look(cabinet) -> a note: try the drawer
  tick 5: look(cabinet) -> a note: try the drawer
  tick 6: look(cabinet) -> a note: try the drawer
  tick 7: look(cabinet) -> a note: try the drawer
  tick 8: look(cabinet) -> a note: try the drawer
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: look(cabinet) -> the cabinet is closed; something is inside
  tick 5: look(cabinet) -> the cabinet is closed; something is inside
  tick 6: look(cabinet) -> the cabinet is closed; something is inside
  tick 7: look(drawer) -> a note: check the basket
  tick 8: look(basket) -> a note: try the cabinet
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], seed 1042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: look(chest) -> a note: try the basket
  tick 4: look(chest) -> a note: try the basket
  tick 5: look(chest) -> a note: try the basket
  tick 6: look(chest) -> a note: try the basket
  tick 7: look(chest) -> a note: try the basket
  tick 8: look(chest) -> a note: try the basket
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 1042, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: open(box) -> empty
  tick 5: open(box) -> empty
  tick 6: open(box) -> empty
  tick 7: open(box) -> empty
  tick 8: open(box) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 1042, chain cabinet->box->pond, target: blue feather
  tick 1: open(cabinet) -> empty
  tick 2: open(cabinet) -> empty
  tick 3: open(cabinet) -> empty
  tick 4: open(cabinet) -> empty
  tick 5: open(cabinet) -> empty
  tick 6: open(cabinet) -> empty
  tick 7: open(cabinet) -> empty
  tick 8: open(cabinet) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: open(chest) -> empty
  tick 2: open(chest) -> empty
  tick 3: open(chest) -> empty
  tick 4: open(chest) -> empty
  tick 5: open(chest) -> empty
  tick 6: open(chest) -> empty
  tick 7: open(chest) -> empty
  tick 8: open(chest) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: open(kit) -> that is not a place here
  tick 2: open(kit) -> that is not a place here
  tick 3: open(kit) -> that is not a place here
  tick 4: open(kit) -> that is not a place here
  tick 5: open(kit) -> that is not a place here
  tick 6: open(kit) -> that is not a place here
  tick 7: open(kit) -> that is not a place here
  tick 8: open(kit) -> that is not a place here
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 1042, chain drawer->box->basket, target: red stone
  tick 1: open(drawer) -> empty
  tick 2: open(drawer) -> empty
  tick 3: open(drawer) -> empty
  tick 4: open(drawer) -> empty
  tick 5: open(drawer) -> empty
  tick 6: open(drawer) -> empty
  tick 7: open(drawer) -> empty
  tick 8: open(drawer) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: open(box) -> empty
  tick 5: open(box) -> empty
  tick 6: open(box) -> empty
  tick 7: open(box) -> empty
  tick 8: open(box) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: open(cabinet) -> empty
  tick 2: open(cabinet) -> empty
  tick 3: open(cabinet) -> empty
  tick 4: open(cabinet) -> empty
  tick 5: open(cabinet) -> empty
  tick 6: open(cabinet) -> empty
  tick 7: open(cabinet) -> empty
  tick 8: open(cabinet) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: open(kitchen) -> that is not a place here
  tick 2: open(kitchen) -> that is not a place here
  tick 3: open(kitchen) -> that is not a place here
  tick 4: open(kitchen) -> that is not a place here
  tick 5: open(kitchen) -> that is not a place here
  tick 6: open(kitchen) -> that is not a place here
  tick 7: open(kitchen) -> that is not a place here
  tick 8: open(kitchen) -> that is not a place here
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: open(drawer) -> empty
  tick 2: open(drawer) -> empty
  tick 3: open(drawer) -> empty
  tick 4: open(drawer) -> empty
  tick 5: open(drawer) -> empty
  tick 6: open(drawer) -> empty
  tick 7: open(drawer) -> empty
  tick 8: open(drawer) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 1042, chain jar->chest->basket, target: black thread
  tick 1: open(kitchen) -> that is not a place here
  tick 2: open(kitchen) -> that is not a place here
  tick 3: open(kitchen) -> that is not a place here
  tick 4: open(kitchen) -> that is not a place here
  tick 5: open(kitchen) -> that is not a place here
  tick 6: open(kitchen) -> that is not a place here
  tick 7: open(kitchen) -> that is not a place here
  tick 8: open(kitchen) -> that is not a place here
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], seed 2042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: look(jar) -> a note: try the pond
  tick 4: look(jar) -> a note: try the pond
  tick 5: look(jar) -> a note: try the pond
  tick 6: look(jar) -> a note: try the pond
  tick 7: look(jar) -> a note: try the pond
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: look(pond) -> the pond is closed; something is inside
  tick 4: look(pond) -> the pond is closed; something is inside
  tick 5: look(pond) -> the pond is closed; something is inside
  tick 6: look(pond) -> the pond is closed; something is inside
  tick 7: look(cabinet) -> a note: check the box
  tick 8: look(box) -> a note: try the pond
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: look(drawer) -> a note: try the basket
  tick 4: look(drawer) -> a note: try the basket
  tick 5: look(drawer) -> a note: try the basket
  tick 6: look(drawer) -> a note: try the basket
  tick 7: look(drawer) -> a note: try the basket
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], seed 2042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: look(shelf) -> the shelf is closed; something is inside
  tick 5: look(shelf) -> the shelf is closed; something is inside
  tick 6: look(shelf) -> the shelf is closed; something is inside
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], seed 2042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: look(box) -> a note: try the basket
  tick 4: look(box) -> a note: try the basket
  tick 5: look(box) -> a note: try the basket
  tick 6: look(box) -> a note: try the basket
  tick 7: look(box) -> a note: try the basket
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: look(pond) -> a note: try the cabinet
  tick 4: look(pond) -> a note: try the cabinet
  tick 5: look(pond) -> a note: try the cabinet
  tick 6: look(pond) -> a note: try the cabinet
  tick 7: look(shelf) -> a note: check the pond
  tick 8: look(pond) -> a note: try the cabinet
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: look(drawer) -> a note: try the shelf
  tick 4: look(drawer) -> a note: try the shelf
  tick 5: look(shelf) -> the shelf is closed; something is inside
  tick 6: look(shelf) -> the shelf is closed; something is inside
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], seed 2042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: look(cabinet) -> a note: try the drawer
  tick 4: look(cabinet) -> a note: try the drawer
  tick 5: look(cabinet) -> a note: try the drawer
  tick 6: look(cabinet) -> a note: try the drawer
  tick 7: look(cabinet) -> a note: try the drawer
  tick 8: look(cabinet) -> a note: try the drawer
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: look(cabinet) -> the cabinet is closed; something is inside
  tick 5: look(cabinet) -> the cabinet is closed; something is inside
  tick 6: look(cabinet) -> the cabinet is closed; something is inside
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], seed 2042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: look(chest) -> a note: try the basket
  tick 4: look(chest) -> a note: try the basket
  tick 5: look(chest) -> a note: try the basket
  tick 6: look(chest) -> a note: try the basket
  tick 7: look(chest) -> a note: try the basket
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 2042, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: done(empty) -> you submit: (nothing)
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: open(box) -> empty
  tick 3: look(box) -> a note: try the pond
  tick 4: look(pond) -> the pond is closed; something is inside
  tick 5: open(pond) -> you find: blue feather and gold bell
  tick 6: look(pond) -> the pond is closed; something is inside
  tick 7: open(pond) -> you find: blue feather and gold bell
  tick 8: look(pond) -> the pond is closed; something is inside
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: open(chest) -> empty
  tick 2: open(chest) -> empty
  tick 3: close(empty) -> that did not work
  tick 4: close(empty) -> that did not work
  tick 5: open(chest) -> empty
  tick 6: open(chest) -> empty
  tick 7: close(empty) -> that did not work
  tick 8: open(chest) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 2042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: open(box) -> empty
  tick 3: look(empty) -> that is not a place here
  tick 4: open(box) -> empty
  tick 5: look(box) -> a note: try the shelf
  tick 6: look(shelf) -> the shelf is closed; something is inside
  tick 7: open(shelf) -> you find: blue feather and gold bell
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 2042, chain drawer->box->basket, target: red stone
  tick 1: open(door) -> that is not a place here
  tick 2: open(door) -> that is not a place here
  tick 3: close(door) -> that did not work
  tick 4: close(empty) -> that did not work
  tick 5: open(empty) -> that is not a place here
  tick 6: close(empty) -> that did not work
  tick 7: open(empty) -> that is not a place here
  tick 8: close(empty) -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: open(shelf) -> empty
  tick 2: open(shelf) -> empty
  tick 3: look(empty) -> that is not a place here
  tick 4: open(shelf) -> empty
  tick 5: look(shelf) -> a note: check the pond
  tick 6: open(pond) -> empty
  tick 7: look(pond) -> a note: try the cabinet
  tick 8: open(cabinet) -> you find: blue feather and gold bell
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: open(cabinet) -> empty
  tick 2: open(cabinet) -> empty
  tick 3: close(cabinet) -> that did not work
  tick 4: open(cabinet) -> empty
  tick 5: close(empty) -> that did not work
  tick 6: open(cabinet) -> empty
  tick 7: close(empty) -> that did not work
  tick 8: open(cabinet) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 2042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: open(cabinet) -> empty
  tick 3: look(cabinet) -> a note: try the drawer
  tick 4: look(drawer) -> the drawer is closed; something is inside
  tick 5: open(drawer) -> you find: green leaf and amber key
  tick 6: look(drawer) -> the drawer is closed; something is inside
  tick 7: look(drawer) -> the drawer is closed; something is inside
  tick 8: open(drawer) -> you find: green leaf and amber key
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: open(door) -> that is not a place here
  tick 2: open(door) -> that is not a place here
  tick 3: close(door) -> that did not work
  tick 4: close(empty) -> that did not work
  tick 5: open(empty) -> that is not a place here
  tick 6: close(empty) -> that did not work
  tick 7: open(empty) -> that is not a place here
  tick 8: close(empty) -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], seed 2042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: open(chest) -> empty
  tick 3: look(chest) -> a note: try the basket
  tick 4: look(basket) -> the basket is closed; something is inside
  tick 5: open(basket) -> you find: black thread and gold bell
  tick 6: look(bell) -> that is not a place here
  tick 7: look(bell) -> that is not a place here
  tick 8: open(bell) -> that is not a place here
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [look], seed 42, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 3 of 8 ticks
```

```
Episode — arm: shuffled-focus [look], seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: open(cabinet) -> empty
  tick 2: open(cabinet) -> empty
  tick 3: open(cabinet) -> empty
  tick 4: open(cabinet) -> empty
  tick 5: look(cabinet) -> a note: check the box
  tick 6: open(box) -> empty
  tick 7: look(box) -> a note: try the pond
  tick 8: open(pond) -> you find: blue feather and gold bell
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [look], seed 42, chain chest->drawer->basket, target: black thread
  tick 1: open(chest) -> empty
  tick 2: open(chest) -> empty
  tick 3: open(chest) -> empty
  tick 4: open(chest) -> empty
  tick 5: open(chest) -> empty
  tick 6: open(chest) -> empty
  tick 7: open(chest) -> empty
  tick 8: open(chest) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [look], seed 42, chain pond->box->shelf, target: gold bell
  tick 1: open(key) -> that is not a place here
  tick 2: open(key) -> that is not a place here
  tick 3: look(pond) -> a note: check the box
  tick 4: open(box) -> empty
  tick 5: look(box) -> a note: try the shelf
  tick 6: open(shelf) -> you find: blue feather and gold bell
  tick 7: look(feather and bell) -> that is not a place here
  tick 8: open(feather and bell) -> that is not a place here
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [look], seed 42, chain drawer->box->basket, target: red stone
  tick 1: open(drawer) -> empty
  tick 2: open(drawer) -> empty
  tick 3: open(drawer) -> empty
  tick 4: open(drawer) -> empty
  tick 5: open(drawer) -> empty
  tick 6: open(drawer) -> empty
  tick 7: open(drawer) -> empty
  tick 8: open(drawer) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [look], seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: open(shelf) -> empty
  tick 2: open(shelf) -> empty
  tick 3: open(shelf) -> empty
  tick 4: open(shelf) -> empty
  tick 5: open(shelf) -> empty
  tick 6: open(shelf) -> empty
  tick 7: open(shelf) -> empty
  tick 8: open(shelf) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [look], seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: open(cabinet) -> empty
  tick 2: open(cabinet) -> empty
  tick 3: open(cabinet) -> empty
  tick 4: open(cabinet) -> empty
  tick 5: open(cabinet) -> empty
  tick 6: open(cabinet) -> empty
  tick 7: open(cabinet) -> empty
  tick 8: open(cabinet) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [look], seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: open(key) -> that is not a place here
  tick 2: open(key) -> that is not a place here
  tick 3: look(key) -> that is not a place here
  tick 4: look(key) -> that is not a place here
  tick 5: open(key) -> that is not a place here
  tick 6: look(key) -> that is not a place here
  tick 7: open(key) -> that is not a place here
  tick 8: open(key) -> that is not a place here
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [look], seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: open(drawer) -> empty
  tick 2: open(drawer) -> empty
  tick 3: open(drawer) -> empty
  tick 4: open(drawer) -> empty
  tick 5: open(drawer) -> empty
  tick 6: open(drawer) -> empty
  tick 7: open(drawer) -> empty
  tick 8: open(drawer) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [look], seed 42, chain jar->chest->basket, target: black thread
  tick 1: open(jar) -> empty
  tick 2: open(jar) -> empty
  tick 3: look(empty) -> that is not a place here
  tick 4: open(open) -> that is not a place here
  tick 5: look(open) -> that is not a place here
  tick 6: open(open) -> that is not a place here
  tick 7: open(open) -> that is not a place here
  tick 8: open(open) -> that is not a place here
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [open], seed 42, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: look(pond) -> the pond is closed; something is inside
  tick 4: look(pond) -> the pond is closed; something is inside
  tick 5: look(pond) -> the pond is closed; something is inside
  tick 6: look(pond) -> the pond is closed; something is inside
  tick 7: look(pond) -> the pond is closed; something is inside
  tick 8: look(pond) -> the pond is closed; something is inside
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [open], seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: look(pond) -> the pond is closed; something is inside
  tick 4: look(pond) -> the pond is closed; something is inside
  tick 5: look(pond) -> the pond is closed; something is inside
  tick 6: look(pond) -> the pond is closed; something is inside
  tick 7: look(pond) -> the pond is closed; something is inside
  tick 8: look(pond) -> the pond is closed; something is inside
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [open], seed 42, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: look(drawer) -> a note: try the basket
  tick 4: look(drawer) -> a note: try the basket
  tick 5: look(drawer) -> a note: try the basket
  tick 6: look(drawer) -> a note: try the basket
  tick 7: look(drawer) -> a note: try the basket
  tick 8: look(drawer) -> a note: try the basket
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [open], seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: look(shelf) -> the shelf is closed; something is inside
  tick 5: look(shelf) -> the shelf is closed; something is inside
  tick 6: look(shelf) -> the shelf is closed; something is inside
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [open], seed 42, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: look(box) -> a note: try the basket
  tick 4: look(box) -> a note: try the basket
  tick 5: look(box) -> a note: try the basket
  tick 6: look(box) -> a note: try the basket
  tick 7: look(box) -> a note: try the basket
  tick 8: look(box) -> a note: try the basket
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [open], seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: look(pond) -> a note: try the cabinet
  tick 4: look(pond) -> a note: try the cabinet
  tick 5: look(pond) -> a note: try the cabinet
  tick 6: look(pond) -> a note: try the cabinet
  tick 7: look(pond) -> a note: try the cabinet
  tick 8: look(pond) -> a note: try the cabinet
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [open], seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: look(drawer) -> a note: try the shelf
  tick 4: look(drawer) -> a note: try the shelf
  tick 5: look(drawer) -> a note: try the shelf
  tick 6: look(drawer) -> a note: try the shelf
  tick 7: look(drawer) -> a note: try the shelf
  tick 8: look(drawer) -> a note: try the shelf
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [open], seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: look(cabinet) -> a note: try the drawer
  tick 4: look(cabinet) -> a note: try the drawer
  tick 5: look(cabinet) -> a note: try the drawer
  tick 6: look(cabinet) -> a note: try the drawer
  tick 7: look(cabinet) -> a note: try the drawer
  tick 8: look(cabinet) -> a note: try the drawer
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [open], seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: look(cabinet) -> the cabinet is closed; something is inside
  tick 5: look(cabinet) -> the cabinet is closed; something is inside
  tick 6: look(cabinet) -> the cabinet is closed; something is inside
  tick 7: look(cabinet) -> the cabinet is closed; something is inside
  tick 8: look(cabinet) -> the cabinet is closed; something is inside
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [open], seed 42, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: look(basket) -> the basket is closed; something is inside
  tick 4: look(basket) -> the basket is closed; something is inside
  tick 5: look(basket) -> the basket is closed; something is inside
  tick 6: look(basket) -> the basket is closed; something is inside
  tick 7: look(basket) -> the basket is closed; something is inside
  tick 8: look(basket) -> the basket is closed; something is inside
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [look], seed 1042, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: open(box) -> empty
  tick 5: open(box) -> empty
  tick 6: open(box) -> empty
  tick 7: open(box) -> empty
  tick 8: open(box) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [look], seed 1042, chain cabinet->box->pond, target: blue feather
  tick 1: open(cabinet) -> empty
  tick 2: open(cabinet) -> empty
  tick 3: open(cabinet) -> empty
  tick 4: open(cabinet) -> empty
  tick 5: open(cabinet) -> empty
  tick 6: open(cabinet) -> empty
  tick 7: open(cabinet) -> empty
  tick 8: open(cabinet) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [look], seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: open(chest) -> empty
  tick 2: open(chest) -> empty
  tick 3: open(chest) -> empty
  tick 4: open(chest) -> empty
  tick 5: open(chest) -> empty
  tick 6: open(chest) -> empty
  tick 7: open(chest) -> empty
  tick 8: open(chest) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [look], seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: open(kit) -> that is not a place here
  tick 2: open(kit) -> that is not a place here
  tick 3: open(kit) -> that is not a place here
  tick 4: open(kit) -> that is not a place here
  tick 5: open(kit) -> that is not a place here
  tick 6: open(kit) -> that is not a place here
  tick 7: open(kit) -> that is not a place here
  tick 8: open(kit) -> that is not a place here
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [look], seed 1042, chain drawer->box->basket, target: red stone
  tick 1: open(drawer) -> empty
  tick 2: open(drawer) -> empty
  tick 3: open(drawer) -> empty
  tick 4: open(drawer) -> empty
  tick 5: open(drawer) -> empty
  tick 6: open(drawer) -> empty
  tick 7: open(drawer) -> empty
  tick 8: open(drawer) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [look], seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: open(box) -> empty
  tick 5: open(box) -> empty
  tick 6: open(box) -> empty
  tick 7: open(box) -> empty
  tick 8: open(box) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [look], seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: open(cabinet) -> empty
  tick 2: open(cabinet) -> empty
  tick 3: open(cabinet) -> empty
  tick 4: open(cabinet) -> empty
  tick 5: open(cabinet) -> empty
  tick 6: open(cabinet) -> empty
  tick 7: open(cabinet) -> empty
  tick 8: open(cabinet) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [look], seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: open(kitchen) -> that is not a place here
  tick 2: open(kitchen) -> that is not a place here
  tick 3: open(kitchen) -> that is not a place here
  tick 4: open(kitchen) -> that is not a place here
  tick 5: open(kitchen) -> that is not a place here
  tick 6: open(kitchen) -> that is not a place here
  tick 7: open(kitchen) -> that is not a place here
  tick 8: open(kitchen) -> that is not a place here
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [look], seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: open(drawer) -> empty
  tick 2: open(drawer) -> empty
  tick 3: open(drawer) -> empty
  tick 4: open(drawer) -> empty
  tick 5: open(drawer) -> empty
  tick 6: open(drawer) -> empty
  tick 7: open(drawer) -> empty
  tick 8: open(drawer) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [look], seed 1042, chain jar->chest->basket, target: black thread
  tick 1: open(kitchen) -> that is not a place here
  tick 2: open(kitchen) -> that is not a place here
  tick 3: open(kitchen) -> that is not a place here
  tick 4: open(kitchen) -> that is not a place here
  tick 5: open(kitchen) -> that is not a place here
  tick 6: open(kitchen) -> that is not a place here
  tick 7: open(kitchen) -> that is not a place here
  tick 8: open(kitchen) -> that is not a place here
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [open], seed 1042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: look(pond) -> the pond is closed; something is inside
  tick 4: look(jar) -> a note: try the pond
  tick 5: look(pond) -> the pond is closed; something is inside
  tick 6: look(pond) -> the pond is closed; something is inside
  tick 7: look(pond) -> the pond is closed; something is inside
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [open], seed 1042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: look(pond) -> the pond is closed; something is inside
  tick 4: look(pond) -> the pond is closed; something is inside
  tick 5: look(pond) -> the pond is closed; something is inside
  tick 6: look(pond) -> the pond is closed; something is inside
  tick 7: look(pond) -> the pond is closed; something is inside
  tick 8: look(cabinet) -> a note: check the box
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [open], seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: look(drawer) -> a note: try the basket
  tick 4: look(drawer) -> a note: try the basket
  tick 5: look(drawer) -> a note: try the basket
  tick 6: look(drawer) -> a note: try the basket
  tick 7: look(drawer) -> a note: try the basket
  tick 8: look(drawer) -> a note: try the basket
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [open], seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: look(shelf) -> the shelf is closed; something is inside
  tick 5: look(shelf) -> the shelf is closed; something is inside
  tick 6: look(shelf) -> the shelf is closed; something is inside
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [open], seed 1042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: look(box) -> a note: try the basket
  tick 4: look(box) -> a note: try the basket
  tick 5: look(box) -> a note: try the basket
  tick 6: look(box) -> a note: try the basket
  tick 7: look(box) -> a note: try the basket
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [open], seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: look(pond) -> a note: try the cabinet
  tick 5: look(cabinet) -> the cabinet is closed; something is inside
  tick 6: look(pond) -> a note: try the cabinet
  tick 7: look(shelf) -> a note: check the pond
  tick 8: look(pond) -> a note: try the cabinet
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [open], seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: look(drawer) -> a note: try the shelf
  tick 4: look(drawer) -> a note: try the shelf
  tick 5: look(drawer) -> a note: try the shelf
  tick 6: look(drawer) -> a note: try the shelf
  tick 7: look(drawer) -> a note: try the shelf
  tick 8: look(drawer) -> a note: try the shelf
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [open], seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: look(cabinet) -> a note: try the drawer
  tick 4: look(cabinet) -> a note: try the drawer
  tick 5: look(cabinet) -> a note: try the drawer
  tick 6: look(cabinet) -> a note: try the drawer
  tick 7: look(cabinet) -> a note: try the drawer
  tick 8: look(cabinet) -> a note: try the drawer
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [open], seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: look(cabinet) -> the cabinet is closed; something is inside
  tick 5: look(cabinet) -> the cabinet is closed; something is inside
  tick 6: look(cabinet) -> the cabinet is closed; something is inside
  tick 7: look(drawer) -> a note: check the basket
  tick 8: look(basket) -> a note: try the cabinet
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [open], seed 1042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: look(chest) -> a note: try the basket
  tick 4: look(chest) -> a note: try the basket
  tick 5: look(chest) -> a note: try the basket
  tick 6: look(chest) -> a note: try the basket
  tick 7: look(chest) -> a note: try the basket
  tick 8: look(chest) -> a note: try the basket
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [look], seed 2042, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: done(empty) -> you submit: (nothing)
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: shuffled-focus [look], seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: open(box) -> empty
  tick 3: look(box) -> a note: try the pond
  tick 4: look(pond) -> the pond is closed; something is inside
  tick 5: open(pond) -> you find: blue feather and gold bell
  tick 6: look(pond) -> the pond is closed; something is inside
  tick 7: open(pond) -> you find: blue feather and gold bell
  tick 8: look(pond) -> the pond is closed; something is inside
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [look], seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: open(chest) -> empty
  tick 2: open(chest) -> empty
  tick 3: close(empty) -> that did not work
  tick 4: close(empty) -> that did not work
  tick 5: open(chest) -> empty
  tick 6: open(chest) -> empty
  tick 7: close(empty) -> that did not work
  tick 8: open(chest) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [look], seed 2042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: open(box) -> empty
  tick 3: look(empty) -> that is not a place here
  tick 4: open(box) -> empty
  tick 5: look(box) -> a note: try the shelf
  tick 6: look(shelf) -> the shelf is closed; something is inside
  tick 7: open(shelf) -> you find: blue feather and gold bell
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [look], seed 2042, chain drawer->box->basket, target: red stone
  tick 1: open(door) -> that is not a place here
  tick 2: open(door) -> that is not a place here
  tick 3: close(door) -> that did not work
  tick 4: close(empty) -> that did not work
  tick 5: open(empty) -> that is not a place here
  tick 6: close(empty) -> that did not work
  tick 7: open(empty) -> that is not a place here
  tick 8: close(empty) -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [look], seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: open(shelf) -> empty
  tick 2: open(shelf) -> empty
  tick 3: look(empty) -> that is not a place here
  tick 4: open(shelf) -> empty
  tick 5: look(shelf) -> a note: check the pond
  tick 6: open(pond) -> empty
  tick 7: look(pond) -> a note: try the cabinet
  tick 8: open(cabinet) -> you find: blue feather and gold bell
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [look], seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: open(cabinet) -> empty
  tick 2: open(cabinet) -> empty
  tick 3: close(cabinet) -> that did not work
  tick 4: open(cabinet) -> empty
  tick 5: close(empty) -> that did not work
  tick 6: open(cabinet) -> empty
  tick 7: close(empty) -> that did not work
  tick 8: open(cabinet) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [look], seed 2042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: open(cabinet) -> empty
  tick 3: look(cabinet) -> a note: try the drawer
  tick 4: look(drawer) -> the drawer is closed; something is inside
  tick 5: open(drawer) -> you find: green leaf and amber key
  tick 6: look(drawer) -> the drawer is closed; something is inside
  tick 7: look(drawer) -> the drawer is closed; something is inside
  tick 8: open(drawer) -> you find: green leaf and amber key
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [look], seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: open(door) -> that is not a place here
  tick 2: open(door) -> that is not a place here
  tick 3: close(door) -> that did not work
  tick 4: close(empty) -> that did not work
  tick 5: open(empty) -> that is not a place here
  tick 6: close(empty) -> that did not work
  tick 7: open(empty) -> that is not a place here
  tick 8: close(empty) -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [look], seed 2042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: open(chest) -> empty
  tick 3: look(chest) -> a note: try the basket
  tick 4: look(basket) -> the basket is closed; something is inside
  tick 5: open(basket) -> you find: black thread and gold bell
  tick 6: look(bell) -> that is not a place here
  tick 7: look(bell) -> that is not a place here
  tick 8: open(bell) -> that is not a place here
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [open], seed 2042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: look(jar) -> a note: try the pond
  tick 4: look(jar) -> a note: try the pond
  tick 5: look(jar) -> a note: try the pond
  tick 6: look(jar) -> a note: try the pond
  tick 7: look(jar) -> a note: try the pond
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [open], seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: look(pond) -> the pond is closed; something is inside
  tick 4: look(pond) -> the pond is closed; something is inside
  tick 5: look(pond) -> the pond is closed; something is inside
  tick 6: look(pond) -> the pond is closed; something is inside
  tick 7: look(cabinet) -> a note: check the box
  tick 8: look(box) -> a note: try the pond
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [open], seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: look(drawer) -> a note: try the basket
  tick 4: look(drawer) -> a note: try the basket
  tick 5: look(drawer) -> a note: try the basket
  tick 6: look(drawer) -> a note: try the basket
  tick 7: look(drawer) -> a note: try the basket
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [open], seed 2042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: look(shelf) -> the shelf is closed; something is inside
  tick 5: look(shelf) -> the shelf is closed; something is inside
  tick 6: look(shelf) -> the shelf is closed; something is inside
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [open], seed 2042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: look(box) -> a note: try the basket
  tick 4: look(box) -> a note: try the basket
  tick 5: look(box) -> a note: try the basket
  tick 6: look(box) -> a note: try the basket
  tick 7: look(box) -> a note: try the basket
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [open], seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: look(pond) -> a note: try the cabinet
  tick 4: look(pond) -> a note: try the cabinet
  tick 5: look(pond) -> a note: try the cabinet
  tick 6: look(pond) -> a note: try the cabinet
  tick 7: look(shelf) -> a note: check the pond
  tick 8: look(pond) -> a note: try the cabinet
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [open], seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: look(drawer) -> a note: try the shelf
  tick 4: look(drawer) -> a note: try the shelf
  tick 5: look(shelf) -> the shelf is closed; something is inside
  tick 6: look(shelf) -> the shelf is closed; something is inside
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [open], seed 2042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: look(cabinet) -> a note: try the drawer
  tick 4: look(cabinet) -> a note: try the drawer
  tick 5: look(cabinet) -> a note: try the drawer
  tick 6: look(cabinet) -> a note: try the drawer
  tick 7: look(cabinet) -> a note: try the drawer
  tick 8: look(cabinet) -> a note: try the drawer
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [open], seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: look(cabinet) -> the cabinet is closed; something is inside
  tick 5: look(cabinet) -> the cabinet is closed; something is inside
  tick 6: look(cabinet) -> the cabinet is closed; something is inside
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: shuffled-focus [open], seed 2042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: look(chest) -> a note: try the basket
  tick 4: look(chest) -> a note: try the basket
  tick 5: look(chest) -> a note: try the basket
  tick 6: look(chest) -> a note: try the basket
  tick 7: look(chest) -> a note: try the basket
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: no-focus [shared], seed 42, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(green leaf) -> you submit: green leaf
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus [shared], seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(cabinet) -> a note: check the box
  tick 3: open(box) -> empty
  tick 4: done(empty) -> you submit: empty
  FAIL (wrong submit) — depth 1/3, 4 of 8 ticks
```

```
Episode — arm: no-focus [shared], seed 42, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus [shared], seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(blue feather) -> you submit: blue feather
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus [shared], seed 42, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus [shared], seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(blue feather) -> you submit: blue feather
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus [shared], seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus [shared], seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus [shared], seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 8 ticks
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
Episode — arm: no-focus [shared], seed 1042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus [shared], seed 1042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(blue feather) -> you submit: blue feather
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus [shared], seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus [shared], seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus [shared], seed 1042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus [shared], seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus [shared], seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus [shared], seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus [shared], seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus [shared], seed 1042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus [shared], seed 2042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(green leaf) -> you submit: green leaf
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus [shared], seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus [shared], seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus [shared], seed 2042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus [shared], seed 2042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus [shared], seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus [shared], seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus [shared], seed 2042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus [shared], seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(black thread) -> you submit: black thread
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus [shared], seed 2042, chain jar->chest->basket, target: black thread
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
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: look(green leaf) -> that is not a place here
  tick 5: look(green leaf) -> that is not a place here
  tick 6: open(green leaf) -> that is not a place here
  tick 7: look(green leaf) -> that is not a place here
  tick 8: done(green leaf) -> you submit: green leaf
  FAIL (wrong submit) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: focus-as-text [look], seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(cabinet) -> a note: check the box
  tick 3: open(box) -> empty
  tick 4: done(empty) -> you submit: empty
  FAIL (wrong submit) — depth 1/3, 4 of 8 ticks
```

```
Episode — arm: focus-as-text [look], seed 42, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: look(basket) -> the basket is closed; something is inside
  tick 4: open(basket) -> you find: black thread and blue feather
  tick 5: look(basket) -> the basket is closed; something is inside
  tick 6: look(basket) -> the basket is closed; something is inside
  tick 7: open(basket) -> you find: black thread and blue feather
  tick 8: look(basket) -> the basket is closed; something is inside
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: focus-as-text [look], seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(blue feather) -> you submit: blue feather
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: focus-as-text [look], seed 42, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(drawer) -> a note: check the box
  tick 3: look(box) -> a note: try the basket
  tick 4: open(basket) -> you find: red stone and blue feather
  tick 5: look(basket) -> the basket is closed; something is inside
  tick 6: look(basket) -> the basket is closed; something is inside
  tick 7: open(basket) -> you find: red stone and blue feather
  tick 8: look(basket) -> the basket is closed; something is inside
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: focus-as-text [look], seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: look(cabinet) -> the cabinet is closed; something is inside
  tick 5: open(cabinet) -> you find: blue feather and gold bell
  tick 6: look(cabinet) -> the cabinet is closed; something is inside
  tick 7: done(blue feather) -> you submit: blue feather
  FAIL (wrong submit) — depth 3/3, 7 of 8 ticks
```

```
Episode — arm: focus-as-text [look], seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: look(drawer) -> a note: try the shelf
  tick 4: look(drawer) -> a note: try the shelf
  tick 5: open(shelf) -> you find: black thread and gold bell
  tick 6: look(shelf) -> the shelf is closed; something is inside
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: open(shelf) -> you find: black thread and gold bell
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: focus-as-text [look], seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: focus-as-text [look], seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: look(cabinet) -> the cabinet is closed; something is inside
  tick 5: open(cabinet) -> you find: amber key and black thread
  tick 6: look(amber key) -> that is not a place here
  tick 7: look(amber key) -> that is not a place here
  tick 8: open(amber key) -> that is not a place here
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: focus-as-text [look], seed 42, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: look(basket) -> the basket is closed; something is inside
  tick 5: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 42, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(green leaf) -> you submit: green leaf
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(cabinet) -> a note: check the box
  tick 3: open(box) -> empty
  tick 4: done(empty) -> you submit: empty
  FAIL (wrong submit) — depth 1/3, 4 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 42, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(blue feather) -> you submit: blue feather
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 42, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(drawer) -> a note: check the box
  tick 3: open(box) -> empty
  tick 4: done(empty) -> you submit: empty
  FAIL (wrong submit) — depth 1/3, 4 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(blue feather) -> you submit: blue feather
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: open(drawer) -> empty
  tick 3: done(empty) -> you submit: empty
  FAIL (wrong submit) — depth 1/3, 3 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 42, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: focus-as-text [look], seed 1042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: look(pond) -> the pond is closed; something is inside
  tick 4: look(pond) -> the pond is closed; something is inside
  tick 5: open(pond) -> you find: black thread and green leaf
  tick 6: look(black thread) -> that is not a place here
  tick 7: look(black thread) -> that is not a place here
  tick 8: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: focus-as-text [look], seed 1042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(cabinet) -> a note: check the box
  tick 3: open(box) -> empty
  tick 4: done(empty) -> you submit: empty
  FAIL (wrong submit) — depth 1/3, 4 of 8 ticks
```

```
Episode — arm: focus-as-text [look], seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: look(basket) -> the basket is closed; something is inside
  tick 4: look(basket) -> the basket is closed; something is inside
  tick 5: look(basket) -> the basket is closed; something is inside
  tick 6: look(basket) -> the basket is closed; something is inside
  tick 7: look(basket) -> the basket is closed; something is inside
  tick 8: look(basket) -> the basket is closed; something is inside
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-as-text [look], seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: focus-as-text [look], seed 1042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(drawer) -> a note: check the box
  tick 3: look(box) -> a note: try the basket
  tick 4: look(basket) -> the basket is closed; something is inside
  tick 5: open(basket) -> you find: red stone and blue feather
  tick 6: look(stone) -> that is not a place here
  tick 7: look(stone) -> that is not a place here
  tick 8: look(stone) -> that is not a place here
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: focus-as-text [look], seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: done(inside) -> you submit: inside
  FAIL (wrong submit) — depth 2/3, 4 of 8 ticks
```

```
Episode — arm: focus-as-text [look], seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: look(drawer) -> a note: try the shelf
  tick 4: look(drawer) -> a note: try the shelf
  tick 5: look(shelf) -> the shelf is closed; something is inside
  tick 6: look(shelf) -> the shelf is closed; something is inside
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-as-text [look], seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: focus-as-text [look], seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: look(cabinet) -> the cabinet is closed; something is inside
  tick 5: open(cabinet) -> you find: amber key and black thread
  tick 6: look(key) -> that is not a place here
  tick 7: look(key) -> that is not a place here
  tick 8: look(key) -> that is not a place here
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: focus-as-text [look], seed 1042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 1042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: open(jar) -> empty
  tick 3: look(jar) -> a note: try the pond
  tick 4: done(pond) -> you submit: pond
  FAIL (wrong submit) — depth 2/3, 4 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 1042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: default(gold bell) -> that did not work
  tick 5: look(pond) -> the pond is closed; something is inside
  tick 6: default(gold bell) -> that did not work
  tick 7: look(pond) -> the pond is closed; something is inside
  tick 8: default(gold bell) -> that did not work
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: default(gold bell) -> that did not work
  tick 5: look(shelf) -> the shelf is closed; something is inside
  tick 6: default(gold bell) -> that did not work
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 1042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: default(gold bell) -> that did not work
  tick 5: look(cabinet) -> the cabinet is closed; something is inside
  tick 6: default(gold bell) -> that did not work
  tick 7: look(cabinet) -> the cabinet is closed; something is inside
  tick 8: look(cabinet) -> the cabinet is closed; something is inside
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: open(drawer) -> empty
  tick 3: look(drawer) -> a note: try the shelf
  tick 4: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 2/3, 4 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: default(green leaf) -> that did not work
  tick 5: look(drawer) -> the drawer is closed; something is inside
  tick 6: default(green leaf) -> that did not work
  tick 7: look(drawer) -> the drawer is closed; something is inside
  tick 8: look(drawer) -> the drawer is closed; something is inside
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 1042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: default(gold bell) -> that did not work
  tick 5: look(gold bell) -> that is not a place here
  tick 6: default(gold bell) -> that did not work
  tick 7: look(gold bell) -> that is not a place here
  tick 8: look(gold bell) -> that is not a place here
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: focus-as-text [look], seed 2042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: open(jar) -> empty
  tick 3: done(empty) -> you submit: empty
  FAIL (wrong submit) — depth 1/3, 3 of 8 ticks
```

```
Episode — arm: focus-as-text [look], seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: focus-as-text [look], seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: open(drawer) -> empty
  tick 3: done(check drawer) -> you submit: check drawer
  FAIL (wrong submit) — depth 1/3, 3 of 8 ticks
```

```
Episode — arm: focus-as-text [look], seed 2042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: focus-as-text [look], seed 2042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: open(box) -> empty
  tick 3: done(check) -> you submit: check
  FAIL (wrong submit) — depth 1/3, 3 of 8 ticks
```

```
Episode — arm: focus-as-text [look], seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: focus-as-text [look], seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: open(drawer) -> empty
  tick 3: done(empty) -> you submit: empty
  FAIL (wrong submit) — depth 1/3, 3 of 8 ticks
```

```
Episode — arm: focus-as-text [look], seed 2042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: focus-as-text [look], seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: open(basket) -> empty
  tick 3: done(amber key) -> you submit: amber key
  PASS — depth 1/3, 3 of 8 ticks, guessed
```

```
Episode — arm: focus-as-text [look], seed 2042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 2042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: open(jar) -> empty
  tick 3: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 1/3, 3 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 2042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 2042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: open(pond) -> empty
  tick 3: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 1/3, 3 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: open(drawer) -> empty
  tick 3: done(empty) -> you submit: empty
  FAIL (wrong submit) — depth 1/3, 3 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 2042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(black thread) -> you submit: black thread
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: focus-as-text [open], seed 2042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

