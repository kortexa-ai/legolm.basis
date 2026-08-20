# gf2-dose-dial

Host machine `snappy`, device `mps`, budget 8, 2256.439 s. Registration: tracks/goal-pursuit/PLAN.md, GF-2 registration — the dose dial (2026-08-16 morning).

The GF bridge pair, reproduced per seed by the registered recipe (training dose untouched at 0.15); the ONLY swept knob is the generate-time delivery fraction. The `no-focus` row is the fixed habitual reference at the trained dose 0.15 — it is not swept. With two focuses the shuffled arm at a dose IS the other focus's packet at that dose, so each cell is generated once and read by both arms.

## The preregistered selector — GF-3's bias dose

Rule: largest swept dose with pooled true-packet focused share <= 0.85 for BOTH focuses and pooled true-packet done share >= 0.05.

**VERDICT: null — no swept dose satisfies both clauses.** No dose in 0.15, 0.1, 0.075, 0.05, 0.03, 0.015 keeps the focused share at or below 0.85 for both focuses while leaving the done share at or above 0.05.

Recorded beside it, the strict-literal variant that reads BOTH clauses off the union mix: null.

| dose | look share | open share | union done share | focused clause | done clause | selected |
|---|---:|---:|---:|---|---|---|
| 0.15 | 1.00 | 0.79 | 0.00 | fail | fail | no |
| 0.1 | 0.54 | 0.38 | 0.02 | pass | fail | no |
| 0.075 | 0.51 | 0.30 | 0.02 | pass | fail | no |
| 0.05 | 1.00 | 0.32 | 0.03 | fail | fail | no |
| 0.03 | 0.95 | 0.35 | 0.01 | fail | fail | no |
| 0.015 | 0.79 | 0.33 | 0.00 | pass | fail | no |

## Headline — one table per focus, rows are doses

Focused-tool share, signed JS against the SAME-dose shuffled arm (positive iff the focused tool's share rises under the true packet), first-tick focused rate, the done share and the repertoire count (tool categories above 0.05) — all under the true packet.

### focus: look

| dose | seed | focused share | JS vs swapped (signed) | first-tick focused | done share | repertoire |
|---|---|---:|---:|---:|---:|---:|
| 0.15 | 42 | 1.00 | +0.7039 | 1.00 | 0.00 | 1 |
| 0.15 | 1042 | 1.00 | +1.0000 | 1.00 | 0.00 | 1 |
| 0.15 | 2042 | 1.00 | +0.4821 | 1.00 | 0.00 | 1 |
| 0.15 | pooled | 1.00 | +0.6875 | 1.00 | 0.00 | 1 |
| 0.1 | 42 | 0.66 | +0.4633 | 0.50 | 0.00 | 3 |
| 0.1 | 1042 | 0.00 | +0.0000 | 0.00 | 0.00 | 1 |
| 0.1 | 2042 | 0.96 | +1.0000 | 0.70 | 0.00 | 1 |
| 0.1 | pooled | 0.54 | +0.3995 | 0.40 | 0.00 | 3 |
| 0.075 | 42 | 0.20 | -0.0148 | 0.20 | 0.00 | 3 |
| 0.075 | 1042 | 0.33 | +0.2044 | 1.00 | 0.00 | 2 |
| 0.075 | 2042 | 1.00 | +0.4591 | 1.00 | 0.00 | 1 |
| 0.075 | pooled | 0.51 | +0.0999 | 0.73 | 0.00 | 3 |
| 0.05 | 42 | 1.00 | +0.0982 | 1.00 | 0.00 | 1 |
| 0.05 | 1042 | 1.00 | +0.4427 | 1.00 | 0.00 | 1 |
| 0.05 | 2042 | 1.00 | +0.5742 | 1.00 | 0.00 | 1 |
| 0.05 | pooled | 1.00 | +0.3070 | 1.00 | 0.00 | 1 |
| 0.03 | 42 | 0.96 | +0.1079 | 0.70 | 0.00 | 1 |
| 0.03 | 1042 | 0.89 | +0.1931 | 0.70 | 0.00 | 2 |
| 0.03 | 2042 | 1.00 | +0.1520 | 1.00 | 0.00 | 1 |
| 0.03 | pooled | 0.95 | +0.1424 | 0.80 | 0.00 | 1 |
| 0.015 | 42 | 0.72 | +0.0015 | 0.20 | 0.00 | 3 |
| 0.015 | 1042 | 0.69 | +0.0060 | 0.20 | 0.00 | 2 |
| 0.015 | 2042 | 0.96 | +0.1126 | 0.90 | 0.00 | 1 |
| 0.015 | pooled | 0.79 | +0.0182 | 0.43 | 0.00 | 2 |

### focus: open

| dose | seed | focused share | JS vs swapped (signed) | first-tick focused | done share | repertoire |
|---|---|---:|---:|---:|---:|---:|
| 0.15 | 42 | 0.85 | +0.7039 | 1.00 | 0.01 | 2 |
| 0.15 | 1042 | 1.00 | +1.0000 | 1.00 | 0.00 | 1 |
| 0.15 | 2042 | 0.49 | +0.4821 | 0.60 | 0.01 | 3 |
| 0.15 | pooled | 0.79 | +0.6875 | 0.87 | 0.01 | 3 |
| 0.1 | 42 | 0.70 | +0.4633 | 0.80 | 0.00 | 2 |
| 0.1 | 1042 | 0.00 | +0.0000 | 0.00 | 0.00 | 1 |
| 0.1 | 2042 | 0.57 | +1.0000 | 1.00 | 0.43 | 2 |
| 0.1 | pooled | 0.38 | +0.3995 | 0.60 | 0.05 | 3 |
| 0.075 | 42 | 0.45 | +0.0148 | 0.20 | 0.00 | 3 |
| 0.075 | 1042 | 0.05 | +0.2044 | 0.00 | 0.00 | 1 |
| 0.075 | 2042 | 0.50 | +0.4591 | 0.70 | 0.17 | 3 |
| 0.075 | pooled | 0.30 | +0.0999 | 0.30 | 0.03 | 3 |
| 0.05 | 42 | 0.15 | +0.0982 | 0.20 | 0.03 | 2 |
| 0.05 | 1042 | 0.38 | +0.4427 | 0.90 | 0.00 | 3 |
| 0.05 | 2042 | 0.51 | +0.5742 | 0.90 | 0.26 | 3 |
| 0.05 | pooled | 0.32 | +0.3070 | 0.67 | 0.06 | 4 |
| 0.03 | 42 | 0.22 | +0.1079 | 0.90 | 0.01 | 3 |
| 0.03 | 1042 | 0.57 | +0.1931 | 0.90 | 0.00 | 2 |
| 0.03 | 2042 | 0.23 | +0.1520 | 0.80 | 0.05 | 2 |
| 0.03 | pooled | 0.35 | +0.1424 | 0.87 | 0.02 | 2 |
| 0.015 | 42 | 0.25 | +0.0015 | 0.80 | 0.00 | 3 |
| 0.015 | 1042 | 0.40 | +0.0060 | 0.80 | 0.00 | 2 |
| 0.015 | 2042 | 0.33 | +0.1126 | 0.80 | 0.00 | 2 |
| 0.015 | pooled | 0.33 | +0.0182 | 0.80 | 0.00 | 2 |

## The fixed habitual reference — no-focus at the trained dose

| seed | look share | open share | first-tick look | first-tick open | done share | repertoire |
|---|---:|---:|---:|---:|---:|---:|
| 42 | 0.50 | 0.25 | 1.00 | 0.00 | 0.25 | 3 |
| 1042 | 0.50 | 0.25 | 1.00 | 0.00 | 0.25 | 3 |
| 2042 | 0.50 | 0.25 | 1.00 | 0.00 | 0.25 | 3 |
| pooled | 0.50 | 0.25 | 1.00 | 0.00 | 0.25 | 3 |

## Paired first tick — focus packet vs the same-dose shuffled focus, chain by chain

| dose | seed | focus | wins | losses | ties |
|---|---|---|---:|---:|---:|
| 0.15 | 42 | look | 10 | 0 | 0 |
| 0.15 | 1042 | look | 10 | 0 | 0 |
| 0.15 | 2042 | look | 6 | 0 | 4 |
| 0.15 | pooled | look | 26 | 0 | 4 |
| 0.15 | 42 | open | 10 | 0 | 0 |
| 0.15 | 1042 | open | 10 | 0 | 0 |
| 0.15 | 2042 | open | 6 | 0 | 4 |
| 0.15 | pooled | open | 26 | 0 | 4 |
| 0.1 | 42 | look | 5 | 0 | 5 |
| 0.1 | 1042 | look | 0 | 0 | 10 |
| 0.1 | 2042 | look | 7 | 0 | 3 |
| 0.1 | pooled | look | 12 | 0 | 18 |
| 0.1 | 42 | open | 5 | 0 | 5 |
| 0.1 | 1042 | open | 0 | 0 | 10 |
| 0.1 | 2042 | open | 10 | 0 | 0 |
| 0.1 | pooled | open | 15 | 0 | 15 |
| 0.075 | 42 | look | 1 | 2 | 7 |
| 0.075 | 1042 | look | 10 | 0 | 0 |
| 0.075 | 2042 | look | 7 | 0 | 3 |
| 0.075 | pooled | look | 18 | 2 | 10 |
| 0.075 | 42 | open | 2 | 0 | 8 |
| 0.075 | 1042 | open | 0 | 0 | 10 |
| 0.075 | 2042 | open | 7 | 0 | 3 |
| 0.075 | pooled | open | 9 | 0 | 21 |
| 0.05 | 42 | look | 2 | 0 | 8 |
| 0.05 | 1042 | look | 9 | 0 | 1 |
| 0.05 | 2042 | look | 9 | 0 | 1 |
| 0.05 | pooled | look | 20 | 0 | 10 |
| 0.05 | 42 | open | 2 | 0 | 8 |
| 0.05 | 1042 | open | 9 | 0 | 1 |
| 0.05 | 2042 | open | 9 | 0 | 1 |
| 0.05 | pooled | open | 20 | 0 | 10 |
| 0.03 | 42 | look | 6 | 0 | 4 |
| 0.03 | 1042 | look | 6 | 0 | 4 |
| 0.03 | 2042 | look | 8 | 0 | 2 |
| 0.03 | pooled | look | 20 | 0 | 10 |
| 0.03 | 42 | open | 6 | 0 | 4 |
| 0.03 | 1042 | open | 6 | 0 | 4 |
| 0.03 | 2042 | open | 8 | 0 | 2 |
| 0.03 | pooled | open | 20 | 0 | 10 |
| 0.015 | 42 | look | 0 | 0 | 10 |
| 0.015 | 1042 | look | 0 | 0 | 10 |
| 0.015 | 2042 | look | 7 | 0 | 3 |
| 0.015 | pooled | look | 7 | 0 | 23 |
| 0.015 | 42 | open | 0 | 0 | 10 |
| 0.015 | 1042 | open | 0 | 0 | 10 |
| 0.015 | 2042 | open | 7 | 0 | 3 |
| 0.015 | pooled | open | 7 | 0 | 23 |

## Tool mix — pooled shares over all decision points, true packet

| dose | focus | look | open | done | other |
|---|---|---:|---:|---:|---:|
| 0.15 | look | 1.00 | 0.00 | 0.00 | 0.00 |
| 0.15 | open | 0.14 | 0.79 | 0.01 | 0.06 |
| 0.1 | look | 0.54 | 0.06 | 0.00 | 0.40 |
| 0.1 | open | 0.00 | 0.38 | 0.05 | 0.57 |
| 0.075 | look | 0.51 | 0.15 | 0.00 | 0.35 |
| 0.075 | open | 0.19 | 0.30 | 0.03 | 0.48 |
| 0.05 | look | 1.00 | 0.00 | 0.00 | 0.00 |
| 0.05 | open | 0.51 | 0.32 | 0.06 | 0.12 |
| 0.03 | look | 0.95 | 0.05 | 0.00 | 0.00 |
| 0.03 | open | 0.60 | 0.35 | 0.02 | 0.03 |
| 0.015 | look | 0.79 | 0.19 | 0.00 | 0.02 |
| 0.015 | open | 0.65 | 0.33 | 0.00 | 0.02 |
| 0.15 | no-focus | 0.50 | 0.25 | 0.25 | 0.00 |

## Transcripts

```
Episode — arm: no-focus, dose 0.15, seed 42, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(green leaf) -> you submit: green leaf
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus, dose 0.15, seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(cabinet) -> a note: check the box
  tick 3: open(box) -> empty
  tick 4: done(empty) -> you submit: empty
  FAIL (wrong submit) — depth 1/3, 4 of 8 ticks
```

```
Episode — arm: no-focus, dose 0.15, seed 42, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus, dose 0.15, seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(blue feather) -> you submit: blue feather
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus, dose 0.15, seed 42, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus, dose 0.15, seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(blue feather) -> you submit: blue feather
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus, dose 0.15, seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus, dose 0.15, seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus, dose 0.15, seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus, dose 0.15, seed 42, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus, dose 0.15, seed 1042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus, dose 0.15, seed 1042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(blue feather) -> you submit: blue feather
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus, dose 0.15, seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus, dose 0.15, seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus, dose 0.15, seed 1042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus, dose 0.15, seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus, dose 0.15, seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus, dose 0.15, seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus, dose 0.15, seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus, dose 0.15, seed 1042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus, dose 0.15, seed 2042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(green leaf) -> you submit: green leaf
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus, dose 0.15, seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus, dose 0.15, seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus, dose 0.15, seed 2042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus, dose 0.15, seed 2042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus, dose 0.15, seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus, dose 0.15, seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus, dose 0.15, seed 2042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus, dose 0.15, seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(black thread) -> you submit: black thread
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: no-focus, dose 0.15, seed 2042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.15, seed 42, chain box->jar->pond, target: black thread
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
Episode — arm: focus-packet [look], dose 0.15, seed 42, chain cabinet->box->pond, target: blue feather
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
Episode — arm: focus-packet [look], dose 0.15, seed 42, chain chest->drawer->basket, target: black thread
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
Episode — arm: focus-packet [look], dose 0.15, seed 42, chain pond->box->shelf, target: gold bell
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
Episode — arm: focus-packet [look], dose 0.15, seed 42, chain drawer->box->basket, target: red stone
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
Episode — arm: focus-packet [look], dose 0.15, seed 42, chain shelf->pond->cabinet, target: gold bell
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
Episode — arm: focus-packet [look], dose 0.15, seed 42, chain cabinet->drawer->shelf, target: gold bell
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
Episode — arm: focus-packet [look], dose 0.15, seed 42, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: focus-packet [look], dose 0.15, seed 42, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: focus-packet [look], dose 0.15, seed 42, chain jar->chest->basket, target: black thread
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
Episode — arm: focus-packet [open], dose 0.15, seed 42, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 3 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.15, seed 42, chain cabinet->box->pond, target: blue feather
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
Episode — arm: focus-packet [open], dose 0.15, seed 42, chain chest->drawer->basket, target: black thread
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
Episode — arm: focus-packet [open], dose 0.15, seed 42, chain pond->box->shelf, target: gold bell
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
Episode — arm: focus-packet [open], dose 0.15, seed 42, chain drawer->box->basket, target: red stone
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
Episode — arm: focus-packet [open], dose 0.15, seed 42, chain shelf->pond->cabinet, target: gold bell
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
Episode — arm: focus-packet [open], dose 0.15, seed 42, chain cabinet->drawer->shelf, target: gold bell
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
Episode — arm: focus-packet [open], dose 0.15, seed 42, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: focus-packet [open], dose 0.15, seed 42, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: focus-packet [open], dose 0.15, seed 42, chain jar->chest->basket, target: black thread
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
Episode — arm: focus-packet [look], dose 0.1, seed 42, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: nothing() -> that did not work
  tick 5: open(box) -> empty
  tick 6: open(box) -> empty
  tick 7: nothing() -> that did not work
  tick 8: open(box) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.1, seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: remember() -> that did not work
  tick 2: look(cabinet) -> a note: check the box
  tick 3: look(box) -> a note: try the pond
  tick 4: look(pond) -> the pond is closed; something is inside
  tick 5: look(cabinet) -> a note: check the box
  tick 6: nothing() -> that did not work
  tick 7: look(cabinet) -> a note: check the box
  tick 8: look(cabinet) -> a note: check the box
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.1, seed 42, chain chest->drawer->basket, target: black thread
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
Episode — arm: focus-packet [look], dose 0.1, seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: look(shelf) -> the shelf is closed; something is inside
  tick 5: look(shelf) -> the shelf is closed; something is inside
  tick 6: nothing() -> that did not work
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.1, seed 42, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(drawer) -> a note: check the box
  tick 3: look(drawer) -> a note: check the box
  tick 4: look(drawer) -> a note: check the box
  tick 5: look(drawer) -> a note: check the box
  tick 6: look(drawer) -> a note: check the box
  tick 7: look(drawer) -> a note: check the box
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.1, seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: look(pond) -> a note: try the cabinet
  tick 4: look(pond) -> a note: try the cabinet
  tick 5: look(pond) -> a note: try the cabinet
  tick 6: nothing() -> that did not work
  tick 7: look(pond) -> a note: try the cabinet
  tick 8: look(shelf) -> a note: check the pond
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.1, seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: remember() -> that did not work
  tick 2: look(cabinet) -> a note: check the drawer
  tick 3: look(drawer) -> a note: try the shelf
  tick 4: look(drawer) -> a note: try the shelf
  tick 5: look(drawer) -> a note: try the shelf
  tick 6: look(drawer) -> a note: try the shelf
  tick 7: look(drawer) -> a note: try the shelf
  tick 8: look(drawer) -> a note: try the shelf
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.1, seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: open(chest) -> empty
  tick 2: open(chest) -> empty
  tick 3: open(chest) -> empty
  tick 4: look(chest) -> a note: check the cabinet
  tick 5: look(cabinet) -> a note: try the drawer
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.1, seed 42, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: focus-packet [look], dose 0.1, seed 42, chain jar->chest->basket, target: black thread
  tick 1: open(jar) -> empty
  tick 2: open(jar) -> empty
  tick 3: open(jar) -> empty
  tick 4: nothing() -> that did not work
  tick 5: open(jar) -> empty
  tick 6: open(jar) -> empty
  tick 7: nothing() -> that did not work
  tick 8: open(jar) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.1, seed 42, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: open(box) -> empty
  tick 5: open(box) -> empty
  tick 6: open(box) -> empty
  tick 7: nothing() -> that did not work
  tick 8: open(box) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.1, seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: nothing() -> that did not work
  tick 2: open(cabinet) -> empty
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  tick 6: remember() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.1, seed 42, chain chest->drawer->basket, target: black thread
  tick 1: open(chest) -> empty
  tick 2: open(chest) -> empty
  tick 3: open(chest) -> empty
  tick 4: open(chest) -> empty
  tick 5: open(box) -> empty
  tick 6: nothing() -> that did not work
  tick 7: open(box) -> empty
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.1, seed 42, chain pond->box->shelf, target: gold bell
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: open(box) -> empty
  tick 5: open(box) -> empty
  tick 6: open(box) -> empty
  tick 7: nothing() -> that did not work
  tick 8: open(box) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.1, seed 42, chain drawer->box->basket, target: red stone
  tick 1: open(drawer) -> empty
  tick 2: open(drawer) -> empty
  tick 3: open(drawer) -> empty
  tick 4: open(drawer) -> empty
  tick 5: open(drawer) -> empty
  tick 6: nothing() -> that did not work
  tick 7: open(drawer) -> empty
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.1, seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: open(box) -> empty
  tick 5: open(box) -> empty
  tick 6: open(box) -> empty
  tick 7: nothing() -> that did not work
  tick 8: open(box) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.1, seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: nothing() -> that did not work
  tick 2: open(cabinet) -> empty
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: open(cabinet) -> empty
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: open(cabinet) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.1, seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: open(chest) -> empty
  tick 2: open(chest) -> empty
  tick 3: open(chest) -> empty
  tick 4: open(chest) -> empty
  tick 5: open(chest) -> empty
  tick 6: nothing() -> that did not work
  tick 7: open(chest) -> empty
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.1, seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: open(drawer) -> empty
  tick 2: open(drawer) -> empty
  tick 3: open(drawer) -> empty
  tick 4: open(drawer) -> empty
  tick 5: open(drawer) -> empty
  tick 6: nothing() -> that did not work
  tick 7: open(drawer) -> empty
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.1, seed 42, chain jar->chest->basket, target: black thread
  tick 1: open(jar) -> empty
  tick 2: open(jar) -> empty
  tick 3: open(jar) -> empty
  tick 4: open(jar) -> empty
  tick 5: open(jar) -> empty
  tick 6: open(jar) -> empty
  tick 7: nothing() -> that did not work
  tick 8: open(jar) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.075, seed 42, chain box->jar->pond, target: black thread
  tick 1: remember() -> that did not work
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
Episode — arm: focus-packet [look], dose 0.075, seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: remember() -> that did not work
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
Episode — arm: focus-packet [look], dose 0.075, seed 42, chain chest->drawer->basket, target: black thread
  tick 1: remember() -> that did not work
  tick 2: removed(chest) -> that did not work
  tick 3: remove() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  tick 6: remove(chest) -> that did not work
  tick 7: remove() -> that did not work
  tick 8: remove() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.075, seed 42, chain pond->box->shelf, target: gold bell
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
Episode — arm: focus-packet [look], dose 0.075, seed 42, chain drawer->box->basket, target: red stone
  tick 1: remember() -> that did not work
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
Episode — arm: focus-packet [look], dose 0.075, seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: look(pond) -> a note: try the cabinet
  tick 4: look(pond) -> a note: try the cabinet
  tick 5: look(pond) -> a note: try the cabinet
  tick 6: look(pond) -> a note: try the cabinet
  tick 7: look(shelf) -> a note: check the pond
  tick 8: look(shelf) -> a note: check the pond
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.075, seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: remember() -> that did not work
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
Episode — arm: focus-packet [look], dose 0.075, seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: remember() -> that did not work
  tick 2: removed(chest) -> that did not work
  tick 3: remove() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  tick 6: remove(chest) -> that did not work
  tick 7: remove() -> that did not work
  tick 8: remove() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.075, seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: remember() -> that did not work
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
Episode — arm: focus-packet [look], dose 0.075, seed 42, chain jar->chest->basket, target: black thread
  tick 1: remember() -> that did not work
  tick 2: removed(jar) -> that did not work
  tick 3: remove() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  tick 6: remove(jar) -> that did not work
  tick 7: remove(amber key) -> that did not work
  tick 8: remove(jar) -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.075, seed 42, chain box->jar->pond, target: black thread
  tick 1: remember() -> that did not work
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: open(box) -> empty
  tick 5: open(box) -> empty
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: open(box) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.075, seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: look(box) -> a note: try the pond
  tick 5: look(pond) -> the pond is closed; something is inside
  tick 6: nothing() -> that did not work
  tick 7: look(pond) -> the pond is closed; something is inside
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.075, seed 42, chain chest->drawer->basket, target: black thread
  tick 1: remember() -> that did not work
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: open(box) -> empty
  tick 5: open(box) -> empty
  tick 6: nothing() -> that did not work
  tick 7: open(box) -> empty
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.075, seed 42, chain pond->box->shelf, target: gold bell
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: nothing() -> that did not work
  tick 5: look(pond) -> a note: check the box
  tick 6: look(box) -> a note: try the shelf
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.075, seed 42, chain drawer->box->basket, target: red stone
  tick 1: remember() -> that did not work
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: open(box) -> empty
  tick 5: open(box) -> empty
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: open(box) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.075, seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: look(cabinet) -> the cabinet is closed; something is inside
  tick 5: look(cabinet) -> the cabinet is closed; something is inside
  tick 6: look(cabinet) -> the cabinet is closed; something is inside
  tick 7: look(shelf) -> a note: check the pond
  tick 8: look(pond) -> a note: try the cabinet
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.075, seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: remember() -> that did not work
  tick 2: open(cabinet) -> empty
  tick 3: open(cabinet) -> empty
  tick 4: open(cabinet) -> empty
  tick 5: open(cabinet) -> empty
  tick 6: open(cabinet) -> empty
  tick 7: nothing() -> that did not work
  tick 8: open(cabinet) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.075, seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: look(drawer) -> the drawer is closed; something is inside
  tick 4: look(drawer) -> the drawer is closed; something is inside
  tick 5: look(drawer) -> the drawer is closed; something is inside
  tick 6: look(drawer) -> the drawer is closed; something is inside
  tick 7: look(drawer) -> the drawer is closed; something is inside
  tick 8: look(drawer) -> the drawer is closed; something is inside
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.075, seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: remember() -> that did not work
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: open(box) -> empty
  tick 5: open(box) -> empty
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: open(box) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.075, seed 42, chain jar->chest->basket, target: black thread
  tick 1: open(jar) -> empty
  tick 2: open(jar) -> empty
  tick 3: open(jar) -> empty
  tick 4: nothing() -> that did not work
  tick 5: open(jar) -> empty
  tick 6: open(jar) -> empty
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.05, seed 42, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: look(jar) -> a note: try the pond
  tick 4: look(shelf) -> nothing of note
  tick 5: look(shelf) -> nothing of note
  tick 6: look(shelf) -> nothing of note
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.05, seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(cabinet) -> a note: check the box
  tick 3: look(cabinet) -> a note: check the box
  tick 4: look(cabinet) -> a note: check the box
  tick 5: look(cabinet) -> a note: check the box
  tick 6: look(cabinet) -> a note: check the box
  tick 7: look(cabinet) -> a note: check the box
  tick 8: look(cabinet) -> a note: check the box
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.05, seed 42, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: look(drawer) -> a note: try the basket
  tick 4: look(drawer) -> a note: try the basket
  tick 5: look(drawer) -> a note: try the basket
  tick 6: look(drawer) -> a note: try the basket
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.05, seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(pond) -> a note: check the box
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: look(shelf) -> the shelf is closed; something is inside
  tick 5: look(shelf) -> the shelf is closed; something is inside
  tick 6: look(shelf) -> the shelf is closed; something is inside
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.05, seed 42, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(drawer) -> a note: check the box
  tick 3: look(drawer) -> a note: check the box
  tick 4: look(drawer) -> a note: check the box
  tick 5: look(drawer) -> a note: check the box
  tick 6: look(drawer) -> a note: check the box
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.05, seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(shelf) -> a note: check the pond
  tick 3: look(shelf) -> a note: check the pond
  tick 4: look(shelf) -> a note: check the pond
  tick 5: look(shelf) -> a note: check the pond
  tick 6: look(shelf) -> a note: check the pond
  tick 7: look(shelf) -> a note: check the pond
  tick 8: look(shelf) -> a note: check the pond
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.05, seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: look(drawer) -> a note: try the shelf
  tick 4: look(drawer) -> a note: try the shelf
  tick 5: look(cabinet) -> a note: check the drawer
  tick 6: look(cabinet) -> a note: check the drawer
  tick 7: look(cabinet) -> a note: check the drawer
  tick 8: look(cabinet) -> a note: check the drawer
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.05, seed 42, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: focus-packet [look], dose 0.05, seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: look(basket) -> a note: try the cabinet
  tick 4: look(drawer) -> a note: check the basket
  tick 5: look(drawer) -> a note: check the basket
  tick 6: look(drawer) -> a note: check the basket
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.05, seed 42, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: look(chest) -> a note: try the basket
  tick 4: look(chest) -> a note: try the basket
  tick 5: look(chest) -> a note: try the basket
  tick 6: look(chest) -> a note: try the basket
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.05, seed 42, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: look(pond) -> the pond is closed; something is inside
  tick 4: look(pond) -> the pond is closed; something is inside
  tick 5: open(box) -> empty
  tick 6: open(box) -> empty
  tick 7: open(box) -> empty
  tick 8: open(box) -> empty
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.05, seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(cabinet) -> a note: check the box
  tick 3: look(cabinet) -> a note: check the box
  tick 4: look(cabinet) -> a note: check the box
  tick 5: look(cabinet) -> a note: check the box
  tick 6: look(cabinet) -> a note: check the box
  tick 7: look(cabinet) -> a note: check the box
  tick 8: look(cabinet) -> a note: check the box
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.05, seed 42, chain chest->drawer->basket, target: black thread
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
Episode — arm: focus-packet [open], dose 0.05, seed 42, chain pond->box->shelf, target: gold bell
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 4 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.05, seed 42, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(drawer) -> a note: check the box
  tick 3: look(drawer) -> a note: check the box
  tick 4: look(drawer) -> a note: check the box
  tick 5: look(drawer) -> a note: check the box
  tick 6: look(drawer) -> a note: check the box
  tick 7: look(drawer) -> a note: check the box
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.05, seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: look(cabinet) -> the cabinet is closed; something is inside
  tick 5: look(cabinet) -> the cabinet is closed; something is inside
  tick 6: look(shelf) -> a note: check the pond
  tick 7: look(shelf) -> a note: check the pond
  tick 8: look(shelf) -> a note: check the pond
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.05, seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: open(drawer) -> empty
  tick 3: open(drawer) -> empty
  tick 4: look(shelf) -> the shelf is closed; something is inside
  tick 5: look(drawer) -> a note: try the shelf
  tick 6: look(shelf) -> the shelf is closed; something is inside
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.05, seed 42, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: focus-packet [open], dose 0.05, seed 42, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: focus-packet [open], dose 0.05, seed 42, chain jar->chest->basket, target: black thread
  tick 1: open(jar) -> empty
  tick 2: open(jar) -> empty
  tick 3: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 3 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.03, seed 42, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: look(box) -> a note: check the jar
  tick 3: look(jar) -> a note: try the pond
  tick 4: look(jar) -> a note: try the pond
  tick 5: look(shelf) -> nothing of note
  tick 6: look(shelf) -> nothing of note
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.03, seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(cabinet) -> a note: check the box
  tick 3: look(cabinet) -> a note: check the box
  tick 4: look(cabinet) -> a note: check the box
  tick 5: look(cabinet) -> a note: check the box
  tick 6: look(cabinet) -> a note: check the box
  tick 7: look(cabinet) -> a note: check the box
  tick 8: look(cabinet) -> a note: check the box
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.03, seed 42, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: look(drawer) -> a note: try the basket
  tick 4: look(drawer) -> a note: try the basket
  tick 5: look(drawer) -> a note: try the basket
  tick 6: look(drawer) -> a note: try the basket
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.03, seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(pond) -> a note: check the box
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: look(shelf) -> the shelf is closed; something is inside
  tick 5: look(shelf) -> the shelf is closed; something is inside
  tick 6: look(shelf) -> the shelf is closed; something is inside
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.03, seed 42, chain drawer->box->basket, target: red stone
  tick 1: open(box) -> empty
  tick 2: look(drawer) -> a note: check the box
  tick 3: look(drawer) -> a note: check the box
  tick 4: look(drawer) -> a note: check the box
  tick 5: look(drawer) -> a note: check the box
  tick 6: look(drawer) -> a note: check the box
  tick 7: look(drawer) -> a note: check the box
  tick 8: look(drawer) -> a note: check the box
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.03, seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(shelf) -> a note: check the pond
  tick 3: look(shelf) -> a note: check the pond
  tick 4: look(shelf) -> a note: check the pond
  tick 5: look(shelf) -> a note: check the pond
  tick 6: look(shelf) -> a note: check the pond
  tick 7: look(shelf) -> a note: check the pond
  tick 8: look(shelf) -> a note: check the pond
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.03, seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: look(drawer) -> a note: try the shelf
  tick 4: look(cabinet) -> a note: check the drawer
  tick 5: look(cabinet) -> a note: check the drawer
  tick 6: look(cabinet) -> a note: check the drawer
  tick 7: look(cabinet) -> a note: check the drawer
  tick 8: look(cabinet) -> a note: check the drawer
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.03, seed 42, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: focus-packet [look], dose 0.03, seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: open(box) -> empty
  tick 2: look(drawer) -> a note: check the basket
  tick 3: look(drawer) -> a note: check the basket
  tick 4: look(drawer) -> a note: check the basket
  tick 5: look(drawer) -> a note: check the basket
  tick 6: look(drawer) -> a note: check the basket
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.03, seed 42, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: look(chest) -> a note: try the basket
  tick 4: look(chest) -> a note: try the basket
  tick 5: look(chest) -> a note: try the basket
  tick 6: look(chest) -> a note: try the basket
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.03, seed 42, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: look(box) -> a note: check the jar
  tick 3: look(jar) -> a note: try the pond
  tick 4: look(jar) -> a note: try the pond
  tick 5: look(jar) -> a note: try the pond
  tick 6: look(jar) -> a note: try the pond
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.03, seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: open(cabinet) -> empty
  tick 2: open(cabinet) -> empty
  tick 3: open(cabinet) -> empty
  tick 4: open(cabinet) -> empty
  tick 5: look(cabinet) -> a note: check the box
  tick 6: look(cabinet) -> a note: check the box
  tick 7: look(cabinet) -> a note: check the box
  tick 8: look(cabinet) -> a note: check the box
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.03, seed 42, chain chest->drawer->basket, target: black thread
  tick 1: open(box) -> empty
  tick 2: look(chest) -> a note: check the drawer
  tick 3: look(drawer) -> a note: try the basket
  tick 4: look(shelf) -> nothing of note
  tick 5: look(shelf) -> nothing of note
  tick 6: look(shelf) -> nothing of note
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.03, seed 42, chain pond->box->shelf, target: gold bell
  tick 1: open(box) -> empty
  tick 2: look(shelf) -> the shelf is closed; something is inside
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: look(shelf) -> the shelf is closed; something is inside
  tick 5: look(shelf) -> the shelf is closed; something is inside
  tick 6: look(shelf) -> the shelf is closed; something is inside
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.03, seed 42, chain drawer->box->basket, target: red stone
  tick 1: open(box) -> empty
  tick 2: look(drawer) -> a note: check the box
  tick 3: look(drawer) -> a note: check the box
  tick 4: look(drawer) -> a note: check the box
  tick 5: look(drawer) -> a note: check the box
  tick 6: look(drawer) -> a note: check the box
  tick 7: look(drawer) -> a note: check the box
  tick 8: look(drawer) -> a note: check the box
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.03, seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(shelf) -> a note: check the pond
  tick 3: look(shelf) -> a note: check the pond
  tick 4: look(shelf) -> a note: check the pond
  tick 5: look(shelf) -> a note: check the pond
  tick 6: look(shelf) -> a note: check the pond
  tick 7: look(shelf) -> a note: check the pond
  tick 8: look(shelf) -> a note: check the pond
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.03, seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: open(cabinet) -> empty
  tick 2: open(cabinet) -> empty
  tick 3: open(cabinet) -> empty
  tick 4: open(cabinet) -> empty
  tick 5: look(cabinet) -> a note: check the drawer
  tick 6: look(drawer) -> a note: try the shelf
  tick 7: look(drawer) -> a note: try the shelf
  tick 8: look(drawer) -> a note: try the shelf
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.03, seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: open(box) -> empty
  tick 2: look(chest) -> a note: check the cabinet
  tick 3: look(cabinet) -> a note: try the drawer
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  tick 6: remember(amber key) -> that did not work
  tick 7: remember(amber key) -> that did not work
  tick 8: remember(amber key) -> that did not work
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.03, seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: open(box) -> empty
  tick 2: look(drawer) -> a note: check the basket
  tick 3: look(drawer) -> a note: check the basket
  tick 4: look(drawer) -> a note: check the basket
  tick 5: look(drawer) -> a note: check the basket
  tick 6: look(drawer) -> a note: check the basket
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.03, seed 42, chain jar->chest->basket, target: black thread
  tick 1: open(jar) -> empty
  tick 2: open(jar) -> empty
  tick 3: open(jar) -> empty
  tick 4: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 4 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.015, seed 42, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: look(box) -> a note: check the jar
  tick 5: look(shelf) -> nothing of note
  tick 6: look(shelf) -> nothing of note
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.015, seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: open(cabinet) -> empty
  tick 2: open(cabinet) -> empty
  tick 3: open(cabinet) -> empty
  tick 4: look(cabinet) -> a note: check the box
  tick 5: look(cabinet) -> a note: check the box
  tick 6: look(cabinet) -> a note: check the box
  tick 7: look(cabinet) -> a note: check the box
  tick 8: look(cabinet) -> a note: check the box
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.015, seed 42, chain chest->drawer->basket, target: black thread
  tick 1: open(box) -> empty
  tick 2: look(chest) -> a note: check the drawer
  tick 3: look(chest) -> a note: check the drawer
  tick 4: look(shelf) -> nothing of note
  tick 5: look(shelf) -> nothing of note
  tick 6: look(shelf) -> nothing of note
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.015, seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(pond) -> a note: check the box
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: look(shelf) -> the shelf is closed; something is inside
  tick 5: look(shelf) -> the shelf is closed; something is inside
  tick 6: look(shelf) -> the shelf is closed; something is inside
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.015, seed 42, chain drawer->box->basket, target: red stone
  tick 1: open(box) -> empty
  tick 2: look(drawer) -> a note: check the box
  tick 3: look(drawer) -> a note: check the box
  tick 4: look(drawer) -> a note: check the box
  tick 5: look(drawer) -> a note: check the box
  tick 6: look(drawer) -> a note: check the box
  tick 7: look(drawer) -> a note: check the box
  tick 8: look(drawer) -> a note: check the box
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.015, seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(shelf) -> a note: check the pond
  tick 3: look(shelf) -> a note: check the pond
  tick 4: look(shelf) -> a note: check the pond
  tick 5: look(shelf) -> a note: check the pond
  tick 6: look(shelf) -> a note: check the pond
  tick 7: look(shelf) -> a note: check the pond
  tick 8: look(shelf) -> a note: check the pond
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.015, seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: open(cabinet) -> empty
  tick 2: open(cabinet) -> empty
  tick 3: open(cabinet) -> empty
  tick 4: look(cabinet) -> a note: check the drawer
  tick 5: look(cabinet) -> a note: check the drawer
  tick 6: look(cabinet) -> a note: check the drawer
  tick 7: look(cabinet) -> a note: check the drawer
  tick 8: look(cabinet) -> a note: check the drawer
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.015, seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: open(box) -> empty
  tick 2: look(chest) -> a note: check the cabinet
  tick 3: look(cabinet) -> a note: try the drawer
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  tick 6: remember(amber key) -> that did not work
  tick 7: remember(amber key) -> that did not work
  tick 8: remember(amber key) -> that did not work
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.015, seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: open(box) -> empty
  tick 2: look(drawer) -> a note: check the basket
  tick 3: look(drawer) -> a note: check the basket
  tick 4: look(drawer) -> a note: check the basket
  tick 5: look(drawer) -> a note: check the basket
  tick 6: look(drawer) -> a note: check the basket
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.015, seed 42, chain jar->chest->basket, target: black thread
  tick 1: open(jar) -> empty
  tick 2: open(jar) -> empty
  tick 3: open(jar) -> empty
  tick 4: open(jar) -> empty
  tick 5: look(jar) -> a note: check the chest
  tick 6: look(chest) -> a note: try the basket
  tick 7: look(chest) -> a note: try the basket
  tick 8: look(chest) -> a note: try the basket
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.015, seed 42, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: open(box) -> empty
  tick 5: look(shelf) -> nothing of note
  tick 6: look(shelf) -> nothing of note
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.015, seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: open(cabinet) -> empty
  tick 2: open(cabinet) -> empty
  tick 3: open(cabinet) -> empty
  tick 4: open(cabinet) -> empty
  tick 5: look(cabinet) -> a note: check the box
  tick 6: look(cabinet) -> a note: check the box
  tick 7: look(cabinet) -> a note: check the box
  tick 8: look(cabinet) -> a note: check the box
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.015, seed 42, chain chest->drawer->basket, target: black thread
  tick 1: open(box) -> empty
  tick 2: look(chest) -> a note: check the drawer
  tick 3: look(chest) -> a note: check the drawer
  tick 4: look(shelf) -> nothing of note
  tick 5: look(shelf) -> nothing of note
  tick 6: look(shelf) -> nothing of note
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.015, seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(pond) -> a note: check the box
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: look(shelf) -> the shelf is closed; something is inside
  tick 5: look(shelf) -> the shelf is closed; something is inside
  tick 6: look(shelf) -> the shelf is closed; something is inside
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.015, seed 42, chain drawer->box->basket, target: red stone
  tick 1: open(box) -> empty
  tick 2: look(drawer) -> a note: check the box
  tick 3: look(drawer) -> a note: check the box
  tick 4: look(drawer) -> a note: check the box
  tick 5: look(drawer) -> a note: check the box
  tick 6: look(drawer) -> a note: check the box
  tick 7: look(drawer) -> a note: check the box
  tick 8: look(drawer) -> a note: check the box
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.015, seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(shelf) -> a note: check the pond
  tick 3: look(shelf) -> a note: check the pond
  tick 4: look(shelf) -> a note: check the pond
  tick 5: look(shelf) -> a note: check the pond
  tick 6: look(shelf) -> a note: check the pond
  tick 7: look(shelf) -> a note: check the pond
  tick 8: look(shelf) -> a note: check the pond
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.015, seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: open(cabinet) -> empty
  tick 2: open(cabinet) -> empty
  tick 3: open(cabinet) -> empty
  tick 4: open(cabinet) -> empty
  tick 5: look(cabinet) -> a note: check the drawer
  tick 6: look(cabinet) -> a note: check the drawer
  tick 7: look(cabinet) -> a note: check the drawer
  tick 8: look(cabinet) -> a note: check the drawer
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.015, seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: open(box) -> empty
  tick 2: look(chest) -> a note: check the cabinet
  tick 3: look(cabinet) -> a note: try the drawer
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  tick 6: remember(amber key) -> that did not work
  tick 7: remember(amber key) -> that did not work
  tick 8: remember(amber key) -> that did not work
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.015, seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: open(box) -> empty
  tick 2: look(drawer) -> a note: check the basket
  tick 3: look(drawer) -> a note: check the basket
  tick 4: look(drawer) -> a note: check the basket
  tick 5: look(drawer) -> a note: check the basket
  tick 6: look(drawer) -> a note: check the basket
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.015, seed 42, chain jar->chest->basket, target: black thread
  tick 1: open(jar) -> empty
  tick 2: open(jar) -> empty
  tick 3: open(jar) -> empty
  tick 4: open(jar) -> empty
  tick 5: look(jar) -> a note: check the chest
  tick 6: look(chest) -> a note: try the basket
  tick 7: look(chest) -> a note: try the basket
  tick 8: look(chest) -> a note: try the basket
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.15, seed 1042, chain box->jar->pond, target: black thread
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
Episode — arm: focus-packet [look], dose 0.15, seed 1042, chain cabinet->box->pond, target: blue feather
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
Episode — arm: focus-packet [look], dose 0.15, seed 1042, chain chest->drawer->basket, target: black thread
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
Episode — arm: focus-packet [look], dose 0.15, seed 1042, chain pond->box->shelf, target: gold bell
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
Episode — arm: focus-packet [look], dose 0.15, seed 1042, chain drawer->box->basket, target: red stone
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
Episode — arm: focus-packet [look], dose 0.15, seed 1042, chain shelf->pond->cabinet, target: gold bell
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
Episode — arm: focus-packet [look], dose 0.15, seed 1042, chain cabinet->drawer->shelf, target: gold bell
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
Episode — arm: focus-packet [look], dose 0.15, seed 1042, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: focus-packet [look], dose 0.15, seed 1042, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: focus-packet [look], dose 0.15, seed 1042, chain jar->chest->basket, target: black thread
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
Episode — arm: focus-packet [open], dose 0.15, seed 1042, chain box->jar->pond, target: black thread
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
Episode — arm: focus-packet [open], dose 0.15, seed 1042, chain cabinet->box->pond, target: blue feather
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
Episode — arm: focus-packet [open], dose 0.15, seed 1042, chain chest->drawer->basket, target: black thread
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
Episode — arm: focus-packet [open], dose 0.15, seed 1042, chain pond->box->shelf, target: gold bell
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
Episode — arm: focus-packet [open], dose 0.15, seed 1042, chain drawer->box->basket, target: red stone
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
Episode — arm: focus-packet [open], dose 0.15, seed 1042, chain shelf->pond->cabinet, target: gold bell
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
Episode — arm: focus-packet [open], dose 0.15, seed 1042, chain cabinet->drawer->shelf, target: gold bell
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
Episode — arm: focus-packet [open], dose 0.15, seed 1042, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: focus-packet [open], dose 0.15, seed 1042, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: focus-packet [open], dose 0.15, seed 1042, chain jar->chest->basket, target: black thread
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
Episode — arm: focus-packet [look], dose 0.1, seed 1042, chain box->jar->pond, target: black thread
  tick 1: nothing() -> that did not work
  tick 2: nothing() -> that did not work
  tick 3: nothing() -> that did not work
  tick 4: nothing() -> that did not work
  tick 5: nothing() -> that did not work
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.1, seed 1042, chain cabinet->box->pond, target: blue feather
  tick 1: nothing() -> that did not work
  tick 2: nothing() -> that did not work
  tick 3: nothing() -> that did not work
  tick 4: nothing() -> that did not work
  tick 5: nothing() -> that did not work
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.1, seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: nothing() -> that did not work
  tick 2: nothing() -> that did not work
  tick 3: nothing() -> that did not work
  tick 4: nothing() -> that did not work
  tick 5: nothing() -> that did not work
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.1, seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: nothing() -> that did not work
  tick 2: nothing() -> that did not work
  tick 3: nothing() -> that did not work
  tick 4: nothing() -> that did not work
  tick 5: nothing() -> that did not work
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.1, seed 1042, chain drawer->box->basket, target: red stone
  tick 1: nothing() -> that did not work
  tick 2: nothing() -> that did not work
  tick 3: nothing() -> that did not work
  tick 4: nothing() -> that did not work
  tick 5: nothing() -> that did not work
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.1, seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: nothing() -> that did not work
  tick 2: nothing() -> that did not work
  tick 3: nothing() -> that did not work
  tick 4: nothing() -> that did not work
  tick 5: nothing() -> that did not work
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.1, seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: nothing() -> that did not work
  tick 2: nothing() -> that did not work
  tick 3: nothing() -> that did not work
  tick 4: nothing() -> that did not work
  tick 5: nothing() -> that did not work
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.1, seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: nothing() -> that did not work
  tick 2: nothing() -> that did not work
  tick 3: nothing() -> that did not work
  tick 4: nothing() -> that did not work
  tick 5: nothing() -> that did not work
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.1, seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: nothing() -> that did not work
  tick 2: nothing() -> that did not work
  tick 3: nothing() -> that did not work
  tick 4: nothing() -> that did not work
  tick 5: nothing() -> that did not work
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.1, seed 1042, chain jar->chest->basket, target: black thread
  tick 1: nothing() -> that did not work
  tick 2: nothing() -> that did not work
  tick 3: nothing() -> that did not work
  tick 4: nothing() -> that did not work
  tick 5: nothing() -> that did not work
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.1, seed 1042, chain box->jar->pond, target: black thread
  tick 1: nothing() -> that did not work
  tick 2: nothing() -> that did not work
  tick 3: nothing() -> that did not work
  tick 4: nothing() -> that did not work
  tick 5: nothing() -> that did not work
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.1, seed 1042, chain cabinet->box->pond, target: blue feather
  tick 1: nothing() -> that did not work
  tick 2: nothing() -> that did not work
  tick 3: nothing() -> that did not work
  tick 4: nothing() -> that did not work
  tick 5: nothing() -> that did not work
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.1, seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: nothing() -> that did not work
  tick 2: nothing() -> that did not work
  tick 3: nothing() -> that did not work
  tick 4: nothing() -> that did not work
  tick 5: nothing() -> that did not work
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.1, seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: nothing() -> that did not work
  tick 2: nothing() -> that did not work
  tick 3: nothing() -> that did not work
  tick 4: nothing() -> that did not work
  tick 5: nothing() -> that did not work
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.1, seed 1042, chain drawer->box->basket, target: red stone
  tick 1: nothing() -> that did not work
  tick 2: nothing() -> that did not work
  tick 3: nothing() -> that did not work
  tick 4: nothing() -> that did not work
  tick 5: nothing() -> that did not work
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.1, seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: nothing() -> that did not work
  tick 2: nothing() -> that did not work
  tick 3: nothing() -> that did not work
  tick 4: nothing() -> that did not work
  tick 5: nothing() -> that did not work
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.1, seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: nothing() -> that did not work
  tick 2: nothing() -> that did not work
  tick 3: nothing() -> that did not work
  tick 4: nothing() -> that did not work
  tick 5: nothing() -> that did not work
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.1, seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: nothing() -> that did not work
  tick 2: nothing() -> that did not work
  tick 3: nothing() -> that did not work
  tick 4: nothing() -> that did not work
  tick 5: nothing() -> that did not work
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.1, seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: nothing() -> that did not work
  tick 2: nothing() -> that did not work
  tick 3: nothing() -> that did not work
  tick 4: nothing() -> that did not work
  tick 5: nothing() -> that did not work
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.1, seed 1042, chain jar->chest->basket, target: black thread
  tick 1: nothing() -> that did not work
  tick 2: nothing() -> that did not work
  tick 3: nothing() -> that did not work
  tick 4: nothing() -> that did not work
  tick 5: nothing() -> that did not work
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.075, seed 1042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: nothing() -> that did not work
  tick 4: nothing() -> that did not work
  tick 5: look(jar) -> a note: try the pond
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.075, seed 1042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(cabinet) -> a note: check the box
  tick 3: nothing() -> that did not work
  tick 4: nothing() -> that did not work
  tick 5: look(cabinet) -> a note: check the box
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.075, seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: nothing() -> that did not work
  tick 3: look(drawer) -> a note: try the basket
  tick 4: nothing() -> that did not work
  tick 5: nothing() -> that did not work
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.075, seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: nothing() -> that did not work
  tick 3: nothing() -> that did not work
  tick 4: nothing() -> that did not work
  tick 5: nothing() -> that did not work
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.075, seed 1042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(drawer) -> a note: check the box
  tick 3: nothing() -> that did not work
  tick 4: look(drawer) -> a note: check the box
  tick 5: look(drawer) -> a note: check the box
  tick 6: nothing() -> that did not work
  tick 7: look(drawer) -> a note: check the box
  tick 8: look(drawer) -> a note: check the box
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.075, seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: nothing() -> that did not work
  tick 3: look(pond) -> a note: try the cabinet
  tick 4: nothing() -> that did not work
  tick 5: nothing() -> that did not work
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.075, seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: nothing() -> that did not work
  tick 4: look(drawer) -> a note: try the shelf
  tick 5: look(drawer) -> a note: try the shelf
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.075, seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: nothing() -> that did not work
  tick 3: nothing() -> that did not work
  tick 4: nothing() -> that did not work
  tick 5: nothing() -> that did not work
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.075, seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: nothing() -> that did not work
  tick 4: nothing() -> that did not work
  tick 5: look(drawer) -> a note: check the basket
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.075, seed 1042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: nothing() -> that did not work
  tick 3: nothing() -> that did not work
  tick 4: nothing() -> that did not work
  tick 5: nothing() -> that did not work
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.075, seed 1042, chain box->jar->pond, target: black thread
  tick 1: nothing() -> that did not work
  tick 2: open(box) -> empty
  tick 3: nothing() -> that did not work
  tick 4: nothing() -> that did not work
  tick 5: nothing() -> that did not work
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.075, seed 1042, chain cabinet->box->pond, target: blue feather
  tick 1: nothing() -> that did not work
  tick 2: nothing() -> that did not work
  tick 3: nothing() -> that did not work
  tick 4: nothing() -> that did not work
  tick 5: nothing() -> that did not work
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.075, seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: nothing() -> that did not work
  tick 2: nothing() -> that did not work
  tick 3: nothing() -> that did not work
  tick 4: nothing() -> that did not work
  tick 5: nothing() -> that did not work
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.075, seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: nothing() -> that did not work
  tick 2: nothing() -> that did not work
  tick 3: nothing() -> that did not work
  tick 4: nothing() -> that did not work
  tick 5: nothing() -> that did not work
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.075, seed 1042, chain drawer->box->basket, target: red stone
  tick 1: nothing() -> that did not work
  tick 2: open(box) -> empty
  tick 3: nothing() -> that did not work
  tick 4: nothing() -> that did not work
  tick 5: nothing() -> that did not work
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.075, seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: nothing() -> that did not work
  tick 2: nothing() -> that did not work
  tick 3: nothing() -> that did not work
  tick 4: nothing() -> that did not work
  tick 5: nothing() -> that did not work
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.075, seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: nothing() -> that did not work
  tick 2: open(box) -> empty
  tick 3: nothing() -> that did not work
  tick 4: nothing() -> that did not work
  tick 5: nothing() -> that did not work
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.075, seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: nothing() -> that did not work
  tick 2: nothing() -> that did not work
  tick 3: nothing() -> that did not work
  tick 4: nothing() -> that did not work
  tick 5: nothing() -> that did not work
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.075, seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: nothing() -> that did not work
  tick 2: open(box) -> empty
  tick 3: nothing() -> that did not work
  tick 4: nothing() -> that did not work
  tick 5: nothing() -> that did not work
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.075, seed 1042, chain jar->chest->basket, target: black thread
  tick 1: nothing() -> that did not work
  tick 2: nothing() -> that did not work
  tick 3: nothing() -> that did not work
  tick 4: nothing() -> that did not work
  tick 5: nothing() -> that did not work
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.05, seed 1042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: look(jar) -> a note: try the pond
  tick 4: look(shelf) -> nothing of note
  tick 5: look(shelf) -> nothing of note
  tick 6: look(shelf) -> nothing of note
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.05, seed 1042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(cabinet) -> a note: check the box
  tick 3: look(cabinet) -> a note: check the box
  tick 4: look(cabinet) -> a note: check the box
  tick 5: look(cabinet) -> a note: check the box
  tick 6: look(cabinet) -> a note: check the box
  tick 7: look(cabinet) -> a note: check the box
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.05, seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: look(drawer) -> a note: try the basket
  tick 4: look(drawer) -> a note: try the basket
  tick 5: look(drawer) -> a note: try the basket
  tick 6: look(drawer) -> a note: try the basket
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.05, seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(pond) -> a note: check the box
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: look(shelf) -> the shelf is closed; something is inside
  tick 5: look(shelf) -> the shelf is closed; something is inside
  tick 6: look(shelf) -> the shelf is closed; something is inside
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.05, seed 1042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(drawer) -> a note: check the box
  tick 3: look(drawer) -> a note: check the box
  tick 4: look(drawer) -> a note: check the box
  tick 5: look(drawer) -> a note: check the box
  tick 6: look(drawer) -> a note: check the box
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.05, seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(shelf) -> a note: check the pond
  tick 3: look(shelf) -> a note: check the pond
  tick 4: look(shelf) -> a note: check the pond
  tick 5: look(shelf) -> a note: check the pond
  tick 6: look(shelf) -> a note: check the pond
  tick 7: look(shelf) -> a note: check the pond
  tick 8: look(shelf) -> a note: check the pond
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.05, seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: look(drawer) -> a note: try the shelf
  tick 4: look(cabinet) -> a note: check the drawer
  tick 5: look(cabinet) -> a note: check the drawer
  tick 6: look(cabinet) -> a note: check the drawer
  tick 7: look(cabinet) -> a note: check the drawer
  tick 8: look(cabinet) -> a note: check the drawer
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.05, seed 1042, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: focus-packet [look], dose 0.05, seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: look(basket) -> a note: try the cabinet
  tick 4: look(drawer) -> a note: check the basket
  tick 5: look(drawer) -> a note: check the basket
  tick 6: look(shelf) -> nothing of note
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.05, seed 1042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: look(chest) -> a note: try the basket
  tick 4: look(chest) -> a note: try the basket
  tick 5: look(chest) -> a note: try the basket
  tick 6: look(chest) -> a note: try the basket
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.05, seed 1042, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: nothing() -> that did not work
  tick 5: open(box) -> empty
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.05, seed 1042, chain cabinet->box->pond, target: blue feather
  tick 1: open(cabinet) -> empty
  tick 2: open(cabinet) -> empty
  tick 3: open(cabinet) -> empty
  tick 4: nothing() -> that did not work
  tick 5: look(cabinet) -> a note: check the box
  tick 6: look(cabinet) -> a note: check the box
  tick 7: look(cabinet) -> a note: check the box
  tick 8: look(cabinet) -> a note: check the box
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.05, seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: nothing() -> that did not work
  tick 5: open(box) -> empty
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.05, seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: nothing() -> that did not work
  tick 4: nothing() -> that did not work
  tick 5: look(pond) -> a note: check the box
  tick 6: look(pond) -> a note: check the box
  tick 7: look(pond) -> a note: check the box
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.05, seed 1042, chain drawer->box->basket, target: red stone
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: nothing() -> that did not work
  tick 5: look(drawer) -> a note: check the box
  tick 6: look(drawer) -> a note: check the box
  tick 7: look(drawer) -> a note: check the box
  tick 8: look(drawer) -> a note: check the box
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.05, seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: look(cabinet) -> the cabinet is closed; something is inside
  tick 5: look(shelf) -> a note: check the pond
  tick 6: look(shelf) -> a note: check the pond
  tick 7: look(shelf) -> a note: check the pond
  tick 8: look(shelf) -> a note: check the pond
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.05, seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: open(cabinet) -> empty
  tick 2: open(cabinet) -> empty
  tick 3: open(cabinet) -> empty
  tick 4: nothing() -> that did not work
  tick 5: open(cabinet) -> empty
  tick 6: open(cabinet) -> empty
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.05, seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: nothing() -> that did not work
  tick 4: nothing() -> that did not work
  tick 5: look(chest) -> a note: check the cabinet
  tick 6: look(cabinet) -> a note: try the drawer
  tick 7: look(cabinet) -> a note: try the drawer
  tick 8: look(cabinet) -> a note: try the drawer
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.05, seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: nothing() -> that did not work
  tick 5: look(drawer) -> a note: check the basket
  tick 6: look(basket) -> a note: try the cabinet
  tick 7: look(cabinet) -> the cabinet is closed; something is inside
  tick 8: look(cabinet) -> the cabinet is closed; something is inside
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.05, seed 1042, chain jar->chest->basket, target: black thread
  tick 1: open(jar) -> empty
  tick 2: open(jar) -> empty
  tick 3: open(jar) -> empty
  tick 4: nothing() -> that did not work
  tick 5: nothing() -> that did not work
  tick 6: open(box) -> empty
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.03, seed 1042, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: look(box) -> a note: check the jar
  tick 5: look(jar) -> a note: try the pond
  tick 6: look(jar) -> a note: try the pond
  tick 7: look(jar) -> a note: try the pond
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.03, seed 1042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(cabinet) -> a note: check the box
  tick 3: look(cabinet) -> a note: check the box
  tick 4: look(cabinet) -> a note: check the box
  tick 5: look(cabinet) -> a note: check the box
  tick 6: look(cabinet) -> a note: check the box
  tick 7: look(cabinet) -> a note: check the box
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.03, seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: look(drawer) -> a note: try the basket
  tick 4: look(drawer) -> a note: try the basket
  tick 5: look(drawer) -> a note: try the basket
  tick 6: look(drawer) -> a note: try the basket
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.03, seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(pond) -> a note: check the box
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: look(shelf) -> the shelf is closed; something is inside
  tick 5: look(shelf) -> the shelf is closed; something is inside
  tick 6: look(shelf) -> the shelf is closed; something is inside
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.03, seed 1042, chain drawer->box->basket, target: red stone
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: look(drawer) -> a note: check the box
  tick 5: look(drawer) -> a note: check the box
  tick 6: look(drawer) -> a note: check the box
  tick 7: look(drawer) -> a note: check the box
  tick 8: look(drawer) -> a note: check the box
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.03, seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(shelf) -> a note: check the pond
  tick 3: look(shelf) -> a note: check the pond
  tick 4: look(shelf) -> a note: check the pond
  tick 5: look(shelf) -> a note: check the pond
  tick 6: look(shelf) -> a note: check the pond
  tick 7: look(shelf) -> a note: check the pond
  tick 8: look(shelf) -> a note: check the pond
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.03, seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: look(drawer) -> a note: try the shelf
  tick 4: look(cabinet) -> a note: check the drawer
  tick 5: look(cabinet) -> a note: check the drawer
  tick 6: look(cabinet) -> a note: check the drawer
  tick 7: look(cabinet) -> a note: check the drawer
  tick 8: look(cabinet) -> a note: check the drawer
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.03, seed 1042, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: focus-packet [look], dose 0.03, seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: look(drawer) -> a note: check the basket
  tick 5: look(drawer) -> a note: check the basket
  tick 6: look(drawer) -> a note: check the basket
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.03, seed 1042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: look(chest) -> a note: try the basket
  tick 4: look(chest) -> a note: try the basket
  tick 5: look(chest) -> a note: try the basket
  tick 6: look(chest) -> a note: try the basket
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.03, seed 1042, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: open(box) -> empty
  tick 5: open(box) -> empty
  tick 6: open(box) -> empty
  tick 7: open(box) -> empty
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.03, seed 1042, chain cabinet->box->pond, target: blue feather
  tick 1: open(cabinet) -> empty
  tick 2: open(cabinet) -> empty
  tick 3: open(cabinet) -> empty
  tick 4: open(cabinet) -> empty
  tick 5: look(cabinet) -> a note: check the box
  tick 6: look(cabinet) -> a note: check the box
  tick 7: look(cabinet) -> a note: check the box
  tick 8: look(cabinet) -> a note: check the box
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.03, seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: open(box) -> empty
  tick 5: look(chest) -> a note: check the drawer
  tick 6: look(drawer) -> a note: try the basket
  tick 7: look(drawer) -> a note: try the basket
  tick 8: look(drawer) -> a note: try the basket
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.03, seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: look(pond) -> a note: check the box
  tick 5: look(pond) -> a note: check the box
  tick 6: look(pond) -> a note: check the box
  tick 7: look(pond) -> a note: check the box
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.03, seed 1042, chain drawer->box->basket, target: red stone
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: open(box) -> empty
  tick 5: look(drawer) -> a note: check the box
  tick 6: look(drawer) -> a note: check the box
  tick 7: look(drawer) -> a note: check the box
  tick 8: look(drawer) -> a note: check the box
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.03, seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(shelf) -> a note: check the pond
  tick 3: look(shelf) -> a note: check the pond
  tick 4: look(shelf) -> a note: check the pond
  tick 5: look(shelf) -> a note: check the pond
  tick 6: look(shelf) -> a note: check the pond
  tick 7: look(shelf) -> a note: check the pond
  tick 8: look(shelf) -> a note: check the pond
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.03, seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: open(cabinet) -> empty
  tick 2: open(cabinet) -> empty
  tick 3: open(cabinet) -> empty
  tick 4: open(cabinet) -> empty
  tick 5: open(cabinet) -> empty
  tick 6: open(cabinet) -> empty
  tick 7: open(box) -> empty
  tick 8: open(box) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.03, seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: open(box) -> empty
  tick 5: look(chest) -> a note: check the cabinet
  tick 6: look(cabinet) -> a note: try the drawer
  tick 7: look(cabinet) -> a note: try the drawer
  tick 8: look(cabinet) -> a note: try the drawer
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.03, seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: open(box) -> empty
  tick 5: look(drawer) -> a note: check the basket
  tick 6: look(basket) -> a note: try the cabinet
  tick 7: look(basket) -> a note: try the cabinet
  tick 8: look(basket) -> a note: try the cabinet
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.03, seed 1042, chain jar->chest->basket, target: black thread
  tick 1: open(jar) -> empty
  tick 2: open(jar) -> empty
  tick 3: open(jar) -> empty
  tick 4: open(jar) -> empty
  tick 5: open(jar) -> empty
  tick 6: open(jar) -> empty
  tick 7: open(jar) -> empty
  tick 8: open(jar) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.015, seed 1042, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: look(box) -> a note: check the jar
  tick 5: look(shelf) -> nothing of note
  tick 6: look(shelf) -> nothing of note
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.015, seed 1042, chain cabinet->box->pond, target: blue feather
  tick 1: open(cabinet) -> empty
  tick 2: open(cabinet) -> empty
  tick 3: open(cabinet) -> empty
  tick 4: look(cabinet) -> a note: check the box
  tick 5: look(cabinet) -> a note: check the box
  tick 6: look(cabinet) -> a note: check the box
  tick 7: look(cabinet) -> a note: check the box
  tick 8: look(cabinet) -> a note: check the box
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.015, seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: look(chest) -> a note: check the drawer
  tick 5: look(dinner) -> that is not a place here
  tick 6: look(dinner) -> that is not a place here
  tick 7: look(dinner) -> that is not a place here
  tick 8: look(dinner) -> that is not a place here
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.015, seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(pond) -> a note: check the box
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: look(shelf) -> the shelf is closed; something is inside
  tick 5: look(shelf) -> the shelf is closed; something is inside
  tick 6: look(shelf) -> the shelf is closed; something is inside
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.015, seed 1042, chain drawer->box->basket, target: red stone
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: look(drawer) -> a note: check the box
  tick 5: look(drawer) -> a note: check the box
  tick 6: look(drawer) -> a note: check the box
  tick 7: look(drawer) -> a note: check the box
  tick 8: look(drawer) -> a note: check the box
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.015, seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(shelf) -> a note: check the pond
  tick 3: look(shelf) -> a note: check the pond
  tick 4: look(shelf) -> a note: check the pond
  tick 5: look(shelf) -> a note: check the pond
  tick 6: look(shelf) -> a note: check the pond
  tick 7: look(shelf) -> a note: check the pond
  tick 8: look(shelf) -> a note: check the pond
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.015, seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: open(cabinet) -> empty
  tick 2: open(cabinet) -> empty
  tick 3: open(cabinet) -> empty
  tick 4: look(cabinet) -> a note: check the drawer
  tick 5: look(cabinet) -> a note: check the drawer
  tick 6: look(cabinet) -> a note: check the drawer
  tick 7: look(cabinet) -> a note: check the drawer
  tick 8: look(cabinet) -> a note: check the drawer
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.015, seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: look(chest) -> a note: check the cabinet
  tick 5: look(cabinet) -> a note: try the drawer
  tick 6: look(cabinet) -> a note: try the drawer
  tick 7: look(cabinet) -> a note: try the drawer
  tick 8: look(cabinet) -> a note: try the drawer
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.015, seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: look(drawer) -> a note: check the basket
  tick 5: look(drawer) -> a note: check the basket
  tick 6: look(drawer) -> a note: check the basket
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.015, seed 1042, chain jar->chest->basket, target: black thread
  tick 1: open(jar) -> empty
  tick 2: open(jar) -> empty
  tick 3: open(jar) -> empty
  tick 4: open(jar) -> empty
  tick 5: look(jar) -> a note: check the chest
  tick 6: look(chest) -> a note: try the basket
  tick 7: look(chest) -> a note: try the basket
  tick 8: look(chest) -> a note: try the basket
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.015, seed 1042, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: open(box) -> empty
  tick 5: look(shelf) -> nothing of note
  tick 6: look(shelf) -> nothing of note
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.015, seed 1042, chain cabinet->box->pond, target: blue feather
  tick 1: open(cabinet) -> empty
  tick 2: open(cabinet) -> empty
  tick 3: open(cabinet) -> empty
  tick 4: open(cabinet) -> empty
  tick 5: look(cabinet) -> a note: check the box
  tick 6: look(cabinet) -> a note: check the box
  tick 7: look(cabinet) -> a note: check the box
  tick 8: look(cabinet) -> a note: check the box
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.015, seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: open(box) -> empty
  tick 5: look(chest) -> a note: check the drawer
  tick 6: look(dinner) -> that is not a place here
  tick 7: look(dinner) -> that is not a place here
  tick 8: look(dinner) -> that is not a place here
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.015, seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(pond) -> a note: check the box
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: look(shelf) -> the shelf is closed; something is inside
  tick 5: look(shelf) -> the shelf is closed; something is inside
  tick 6: look(shelf) -> the shelf is closed; something is inside
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.015, seed 1042, chain drawer->box->basket, target: red stone
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: open(box) -> empty
  tick 5: look(shelf) -> nothing of note
  tick 6: look(shelf) -> nothing of note
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.015, seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(shelf) -> a note: check the pond
  tick 3: look(shelf) -> a note: check the pond
  tick 4: look(shelf) -> a note: check the pond
  tick 5: look(shelf) -> a note: check the pond
  tick 6: look(shelf) -> a note: check the pond
  tick 7: look(shelf) -> a note: check the pond
  tick 8: look(shelf) -> a note: check the pond
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.015, seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: open(cabinet) -> empty
  tick 2: open(cabinet) -> empty
  tick 3: open(cabinet) -> empty
  tick 4: open(cabinet) -> empty
  tick 5: look(cabinet) -> a note: check the drawer
  tick 6: look(cabinet) -> a note: check the drawer
  tick 7: look(cabinet) -> a note: check the drawer
  tick 8: look(cabinet) -> a note: check the drawer
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.015, seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: open(box) -> empty
  tick 5: look(chest) -> a note: check the cabinet
  tick 6: look(cabinet) -> a note: try the drawer
  tick 7: look(cabinet) -> a note: try the drawer
  tick 8: look(cabinet) -> a note: try the drawer
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.015, seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: open(box) -> empty
  tick 5: look(shelf) -> nothing of note
  tick 6: look(shelf) -> nothing of note
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.015, seed 1042, chain jar->chest->basket, target: black thread
  tick 1: open(jar) -> empty
  tick 2: open(jar) -> empty
  tick 3: open(jar) -> empty
  tick 4: open(jar) -> empty
  tick 5: look(jar) -> a note: check the chest
  tick 6: look(chest) -> a note: try the basket
  tick 7: look(chest) -> a note: try the basket
  tick 8: look(chest) -> a note: try the basket
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.15, seed 2042, chain box->jar->pond, target: black thread
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
Episode — arm: focus-packet [look], dose 0.15, seed 2042, chain cabinet->box->pond, target: blue feather
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
Episode — arm: focus-packet [look], dose 0.15, seed 2042, chain chest->drawer->basket, target: black thread
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
Episode — arm: focus-packet [look], dose 0.15, seed 2042, chain pond->box->shelf, target: gold bell
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
Episode — arm: focus-packet [look], dose 0.15, seed 2042, chain drawer->box->basket, target: red stone
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
Episode — arm: focus-packet [look], dose 0.15, seed 2042, chain shelf->pond->cabinet, target: gold bell
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
Episode — arm: focus-packet [look], dose 0.15, seed 2042, chain cabinet->drawer->shelf, target: gold bell
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
Episode — arm: focus-packet [look], dose 0.15, seed 2042, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: focus-packet [look], dose 0.15, seed 2042, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: focus-packet [look], dose 0.15, seed 2042, chain jar->chest->basket, target: black thread
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
Episode — arm: focus-packet [open], dose 0.15, seed 2042, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: done(empty) -> you submit: (nothing)
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.15, seed 2042, chain cabinet->box->pond, target: blue feather
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
Episode — arm: focus-packet [open], dose 0.15, seed 2042, chain chest->drawer->basket, target: black thread
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
Episode — arm: focus-packet [open], dose 0.15, seed 2042, chain pond->box->shelf, target: gold bell
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
Episode — arm: focus-packet [open], dose 0.15, seed 2042, chain drawer->box->basket, target: red stone
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
Episode — arm: focus-packet [open], dose 0.15, seed 2042, chain shelf->pond->cabinet, target: gold bell
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
Episode — arm: focus-packet [open], dose 0.15, seed 2042, chain cabinet->drawer->shelf, target: gold bell
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
Episode — arm: focus-packet [open], dose 0.15, seed 2042, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: focus-packet [open], dose 0.15, seed 2042, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: focus-packet [open], dose 0.15, seed 2042, chain jar->chest->basket, target: black thread
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
Episode — arm: focus-packet [look], dose 0.1, seed 2042, chain box->jar->pond, target: black thread
  tick 1: remember() -> that did not work
  tick 2: look(box) -> a note: check the jar
  tick 3: look(jar) -> a note: try the pond
  tick 4: look(jar) -> a note: try the pond
  tick 5: look(jar) -> a note: try the pond
  tick 6: look(jar) -> a note: try the pond
  tick 7: look(jar) -> a note: try the pond
  tick 8: look(jar) -> a note: try the pond
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.1, seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(cabinet) -> a note: check the box
  tick 3: look(cabinet) -> a note: check the box
  tick 4: look(cabinet) -> a note: check the box
  tick 5: look(cabinet) -> a note: check the box
  tick 6: look(cabinet) -> a note: check the box
  tick 7: look(cabinet) -> a note: check the box
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.1, seed 2042, chain chest->drawer->basket, target: black thread
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
Episode — arm: focus-packet [look], dose 0.1, seed 2042, chain pond->box->shelf, target: gold bell
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
Episode — arm: focus-packet [look], dose 0.1, seed 2042, chain drawer->box->basket, target: red stone
  tick 1: remember() -> that did not work
  tick 2: look(drawer) -> a note: check the box
  tick 3: look(drawer) -> a note: check the box
  tick 4: look(drawer) -> a note: check the box
  tick 5: look(drawer) -> a note: check the box
  tick 6: look(drawer) -> a note: check the box
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.1, seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: look(pond) -> a note: try the cabinet
  tick 4: look(pond) -> a note: try the cabinet
  tick 5: look(pond) -> a note: try the cabinet
  tick 6: look(pond) -> a note: try the cabinet
  tick 7: look(shelf) -> a note: check the pond
  tick 8: look(shelf) -> a note: check the pond
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.1, seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: look(drawer) -> a note: try the shelf
  tick 4: look(drawer) -> a note: try the shelf
  tick 5: look(drawer) -> a note: try the shelf
  tick 6: look(drawer) -> a note: try the shelf
  tick 7: look(drawer) -> a note: try the shelf
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.1, seed 2042, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: focus-packet [look], dose 0.1, seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: remember() -> that did not work
  tick 2: look(drawer) -> a note: check the basket
  tick 3: look(basket) -> a note: try the cabinet
  tick 4: look(basket) -> a note: try the cabinet
  tick 5: look(cabinet) -> the cabinet is closed; something is inside
  tick 6: look(cabinet) -> the cabinet is closed; something is inside
  tick 7: look(cabinet) -> the cabinet is closed; something is inside
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.1, seed 2042, chain jar->chest->basket, target: black thread
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
Episode — arm: focus-packet [open], dose 0.1, seed 2042, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.1, seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: open(cabinet) -> empty
  tick 2: open(cabinet) -> empty
  tick 3: done(amber key) -> you submit: (nothing)
  FAIL (wrong submit) — depth 0/3, 3 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.1, seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: open(box) -> empty
  tick 2: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.1, seed 2042, chain pond->box->shelf, target: gold bell
  tick 1: open(box) -> empty
  tick 2: done(empty) -> you submit: (nothing)
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.1, seed 2042, chain drawer->box->basket, target: red stone
  tick 1: open(drawer) -> empty
  tick 2: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.1, seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: open(box) -> empty
  tick 2: done(empty) -> you submit: (nothing)
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.1, seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: open(cabinet) -> empty
  tick 2: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.1, seed 2042, chain chest->cabinet->drawer, target: green leaf
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: done(empty) -> you submit: (nothing)
  FAIL (wrong submit) — depth 0/3, 3 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.1, seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: open(drawer) -> empty
  tick 2: done(amber key) -> you submit: amber key
  PASS — depth 0/3, 2 of 8 ticks, guessed
```

```
Episode — arm: focus-packet [open], dose 0.1, seed 2042, chain jar->chest->basket, target: black thread
  tick 1: open(jar) -> empty
  tick 2: open(jar) -> empty
  tick 3: done(empty) -> you submit: (nothing)
  FAIL (wrong submit) — depth 0/3, 3 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.075, seed 2042, chain box->jar->pond, target: black thread
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
Episode — arm: focus-packet [look], dose 0.075, seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(cabinet) -> a note: check the box
  tick 3: look(cabinet) -> a note: check the box
  tick 4: look(cabinet) -> a note: check the box
  tick 5: look(cabinet) -> a note: check the box
  tick 6: look(cabinet) -> a note: check the box
  tick 7: look(cabinet) -> a note: check the box
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.075, seed 2042, chain chest->drawer->basket, target: black thread
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
Episode — arm: focus-packet [look], dose 0.075, seed 2042, chain pond->box->shelf, target: gold bell
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
Episode — arm: focus-packet [look], dose 0.075, seed 2042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(drawer) -> a note: check the box
  tick 3: look(drawer) -> a note: check the box
  tick 4: look(drawer) -> a note: check the box
  tick 5: look(drawer) -> a note: check the box
  tick 6: look(drawer) -> a note: check the box
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.075, seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: look(pond) -> a note: try the cabinet
  tick 4: look(pond) -> a note: try the cabinet
  tick 5: look(pond) -> a note: try the cabinet
  tick 6: look(pond) -> a note: try the cabinet
  tick 7: look(shelf) -> a note: check the pond
  tick 8: look(shelf) -> a note: check the pond
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.075, seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: look(drawer) -> a note: try the shelf
  tick 4: look(drawer) -> a note: try the shelf
  tick 5: look(drawer) -> a note: try the shelf
  tick 6: look(drawer) -> a note: try the shelf
  tick 7: look(cabinet) -> a note: check the drawer
  tick 8: look(drawer) -> a note: try the shelf
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.075, seed 2042, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: focus-packet [look], dose 0.075, seed 2042, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: focus-packet [look], dose 0.075, seed 2042, chain jar->chest->basket, target: black thread
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
Episode — arm: focus-packet [open], dose 0.075, seed 2042, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.075, seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: open(box) -> empty
  tick 3: look(cabinet) -> a note: check the box
  tick 4: look(cabinet) -> a note: check the box
  tick 5: open(box) -> empty
  tick 6: look(cabinet) -> a note: check the box
  tick 7: look(cabinet) -> a note: check the box
  tick 8: look(cabinet) -> a note: check the box
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.075, seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: open(box) -> empty
  tick 2: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.075, seed 2042, chain pond->box->shelf, target: gold bell
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 3 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.075, seed 2042, chain drawer->box->basket, target: red stone
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 3 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.075, seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 3 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.075, seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: open(cabinet) -> empty
  tick 2: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.075, seed 2042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: look(cabinet) -> a note: try the drawer
  tick 4: open(drawer) -> you find: green leaf and amber key
  tick 5: open(drawer) -> you find: green leaf and amber key
  tick 6: open(drawer) -> you find: green leaf and amber key
  tick 7: open(drawer) -> you find: green leaf and amber key
  tick 8: open(drawer) -> you find: green leaf and amber key
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.075, seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: done(amber key) -> you submit: amber key
  PASS — depth 0/3, 3 of 8 ticks, guessed
```

```
Episode — arm: focus-packet [open], dose 0.075, seed 2042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: open(chest) -> empty
  tick 3: open(chest) -> empty
  tick 4: look(chest) -> a note: try the basket
  tick 5: open(basket) -> you find: black thread and gold bell
  tick 6: look(basket) -> the basket is closed; something is inside
  tick 7: look(basket) -> the basket is closed; something is inside
  tick 8: look(basket) -> the basket is closed; something is inside
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.05, seed 2042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: look(jar) -> a note: try the pond
  tick 4: look(shelf) -> nothing of note
  tick 5: look(shelf) -> nothing of note
  tick 6: look(shelf) -> nothing of note
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.05, seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(cabinet) -> a note: check the box
  tick 3: look(cabinet) -> a note: check the box
  tick 4: look(cabinet) -> a note: check the box
  tick 5: look(cabinet) -> a note: check the box
  tick 6: look(cabinet) -> a note: check the box
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.05, seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: look(drawer) -> a note: try the basket
  tick 4: look(drawer) -> a note: try the basket
  tick 5: look(drawer) -> a note: try the basket
  tick 6: look(drawer) -> a note: try the basket
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.05, seed 2042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(pond) -> a note: check the box
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: look(shelf) -> the shelf is closed; something is inside
  tick 5: look(shelf) -> the shelf is closed; something is inside
  tick 6: look(shelf) -> the shelf is closed; something is inside
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.05, seed 2042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(drawer) -> a note: check the box
  tick 3: look(drawer) -> a note: check the box
  tick 4: look(drawer) -> a note: check the box
  tick 5: look(drawer) -> a note: check the box
  tick 6: look(shelf) -> nothing of note
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.05, seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: look(shelf) -> a note: check the pond
  tick 4: look(shelf) -> a note: check the pond
  tick 5: look(shelf) -> a note: check the pond
  tick 6: look(shelf) -> a note: check the pond
  tick 7: look(shelf) -> a note: check the pond
  tick 8: look(shelf) -> a note: check the pond
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.05, seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: look(drawer) -> a note: try the shelf
  tick 4: look(drawer) -> a note: try the shelf
  tick 5: look(cabinet) -> a note: check the drawer
  tick 6: look(cabinet) -> a note: check the drawer
  tick 7: look(cabinet) -> a note: check the drawer
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.05, seed 2042, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: focus-packet [look], dose 0.05, seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: look(basket) -> a note: try the cabinet
  tick 4: look(shelf) -> nothing of note
  tick 5: look(shelf) -> nothing of note
  tick 6: look(shelf) -> nothing of note
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.05, seed 2042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: look(chest) -> a note: try the basket
  tick 4: look(chest) -> a note: try the basket
  tick 5: look(chest) -> a note: try the basket
  tick 6: look(chest) -> a note: try the basket
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.05, seed 2042, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 3 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.05, seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: open(cabinet) -> empty
  tick 2: open(cabinet) -> empty
  tick 3: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 3 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.05, seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 3 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.05, seed 2042, chain pond->box->shelf, target: gold bell
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 3 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.05, seed 2042, chain drawer->box->basket, target: red stone
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 3 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.05, seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: look(cabinet) -> the cabinet is closed; something is inside
  tick 5: look(cabinet) -> the cabinet is closed; something is inside
  tick 6: look(cabinet) -> the cabinet is closed; something is inside
  tick 7: look(shelf) -> a note: check the pond
  tick 8: look(shelf) -> a note: check the pond
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.05, seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: open(cabinet) -> empty
  tick 2: open(cabinet) -> empty
  tick 3: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 3 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.05, seed 2042, chain chest->cabinet->drawer, target: green leaf
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 3 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.05, seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: done(amber key) -> you submit: amber key
  PASS — depth 0/3, 3 of 8 ticks, guessed
```

```
Episode — arm: focus-packet [open], dose 0.05, seed 2042, chain jar->chest->basket, target: black thread
  tick 1: open(jar) -> empty
  tick 2: open(jar) -> empty
  tick 3: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 3 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.03, seed 2042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: look(jar) -> a note: try the pond
  tick 4: look(shelf) -> nothing of note
  tick 5: look(shelf) -> nothing of note
  tick 6: look(shelf) -> nothing of note
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.03, seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(cabinet) -> a note: check the box
  tick 3: look(cabinet) -> a note: check the box
  tick 4: look(cabinet) -> a note: check the box
  tick 5: look(cabinet) -> a note: check the box
  tick 6: look(cabinet) -> a note: check the box
  tick 7: look(cabinet) -> a note: check the box
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.03, seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: look(drawer) -> a note: try the basket
  tick 4: look(drawer) -> a note: try the basket
  tick 5: look(drawer) -> a note: try the basket
  tick 6: look(drawer) -> a note: try the basket
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.03, seed 2042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(pond) -> a note: check the box
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: look(shelf) -> the shelf is closed; something is inside
  tick 5: look(shelf) -> the shelf is closed; something is inside
  tick 6: look(shelf) -> the shelf is closed; something is inside
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.03, seed 2042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(drawer) -> a note: check the box
  tick 3: look(drawer) -> a note: check the box
  tick 4: look(drawer) -> a note: check the box
  tick 5: look(drawer) -> a note: check the box
  tick 6: look(drawer) -> a note: check the box
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.03, seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(shelf) -> a note: check the pond
  tick 3: look(shelf) -> a note: check the pond
  tick 4: look(shelf) -> a note: check the pond
  tick 5: look(shelf) -> a note: check the pond
  tick 6: look(shelf) -> a note: check the pond
  tick 7: look(shelf) -> a note: check the pond
  tick 8: look(shelf) -> a note: check the pond
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.03, seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: look(drawer) -> a note: try the shelf
  tick 4: look(cabinet) -> a note: check the drawer
  tick 5: look(cabinet) -> a note: check the drawer
  tick 6: look(cabinet) -> a note: check the drawer
  tick 7: look(cabinet) -> a note: check the drawer
  tick 8: look(cabinet) -> a note: check the drawer
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.03, seed 2042, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: focus-packet [look], dose 0.03, seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: look(drawer) -> a note: check the basket
  tick 4: look(drawer) -> a note: check the basket
  tick 5: look(drawer) -> a note: check the basket
  tick 6: look(shelf) -> nothing of note
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.03, seed 2042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: look(chest) -> a note: try the basket
  tick 4: look(chest) -> a note: try the basket
  tick 5: look(chest) -> a note: try the basket
  tick 6: look(chest) -> a note: try the basket
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.03, seed 2042, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 3 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.03, seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: open(cabinet) -> empty
  tick 2: open(cabinet) -> empty
  tick 3: open(cabinet) -> empty
  tick 4: open(cabinet) -> empty
  tick 5: look(cabinet) -> a note: check the box
  tick 6: look(cabinet) -> a note: check the box
  tick 7: look(cabinet) -> a note: check the box
  tick 8: look(cabinet) -> a note: check the box
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.03, seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: open(box) -> empty
  tick 2: look(chest) -> a note: check the drawer
  tick 3: look(drawer) -> a note: try the basket
  tick 4: look(shelf) -> nothing of note
  tick 5: look(shelf) -> nothing of note
  tick 6: look(shelf) -> nothing of note
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.03, seed 2042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(pond) -> a note: check the box
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: look(shelf) -> the shelf is closed; something is inside
  tick 5: look(shelf) -> the shelf is closed; something is inside
  tick 6: look(shelf) -> the shelf is closed; something is inside
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.03, seed 2042, chain drawer->box->basket, target: red stone
  tick 1: open(box) -> empty
  tick 2: look(drawer) -> a note: check the box
  tick 3: look(drawer) -> a note: check the box
  tick 4: look(drawer) -> a note: check the box
  tick 5: look(drawer) -> a note: check the box
  tick 6: look(drawer) -> a note: check the box
  tick 7: look(drawer) -> a note: check the box
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.03, seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(shelf) -> a note: check the pond
  tick 3: look(shelf) -> a note: check the pond
  tick 4: look(shelf) -> a note: check the pond
  tick 5: look(shelf) -> a note: check the pond
  tick 6: look(shelf) -> a note: check the pond
  tick 7: look(shelf) -> a note: check the pond
  tick 8: look(shelf) -> a note: check the pond
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.03, seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: open(cabinet) -> empty
  tick 2: open(cabinet) -> empty
  tick 3: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 3 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.03, seed 2042, chain chest->cabinet->drawer, target: green leaf
  tick 1: open(box) -> empty
  tick 2: look(chest) -> a note: check the cabinet
  tick 3: look(cabinet) -> a note: try the drawer
  tick 4: look(cabinet) -> a note: try the drawer
  tick 5: look(cabinet) -> a note: try the drawer
  tick 6: look(cabinet) -> a note: try the drawer
  tick 7: look(cabinet) -> a note: try the drawer
  tick 8: look(cabinet) -> a note: try the drawer
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.03, seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: open(box) -> empty
  tick 2: look(drawer) -> a note: check the basket
  tick 3: look(basket) -> a note: try the cabinet
  tick 4: look(shelf) -> nothing of note
  tick 5: look(shelf) -> nothing of note
  tick 6: look(shelf) -> nothing of note
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.03, seed 2042, chain jar->chest->basket, target: black thread
  tick 1: open(jar) -> empty
  tick 2: open(jar) -> empty
  tick 3: open(jar) -> empty
  tick 4: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 4 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.015, seed 2042, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: look(box) -> a note: check the jar
  tick 5: look(jar) -> a note: try the pond
  tick 6: look(jar) -> a note: try the pond
  tick 7: look(jar) -> a note: try the pond
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.015, seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(cabinet) -> a note: check the box
  tick 3: look(cabinet) -> a note: check the box
  tick 4: look(cabinet) -> a note: check the box
  tick 5: look(cabinet) -> a note: check the box
  tick 6: look(cabinet) -> a note: check the box
  tick 7: look(cabinet) -> a note: check the box
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.015, seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: look(drawer) -> a note: try the basket
  tick 4: look(drawer) -> a note: try the basket
  tick 5: look(drawer) -> a note: try the basket
  tick 6: look(drawer) -> a note: try the basket
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.015, seed 2042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(pond) -> a note: check the box
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: look(shelf) -> the shelf is closed; something is inside
  tick 5: look(shelf) -> the shelf is closed; something is inside
  tick 6: look(shelf) -> the shelf is closed; something is inside
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.015, seed 2042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(drawer) -> a note: check the box
  tick 3: look(drawer) -> a note: check the box
  tick 4: look(drawer) -> a note: check the box
  tick 5: look(drawer) -> a note: check the box
  tick 6: look(drawer) -> a note: check the box
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.015, seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(shelf) -> a note: check the pond
  tick 3: look(shelf) -> a note: check the pond
  tick 4: look(shelf) -> a note: check the pond
  tick 5: look(shelf) -> a note: check the pond
  tick 6: look(shelf) -> a note: check the pond
  tick 7: look(shelf) -> a note: check the pond
  tick 8: look(shelf) -> a note: check the pond
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.015, seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: look(drawer) -> a note: try the shelf
  tick 4: look(cabinet) -> a note: check the drawer
  tick 5: look(cabinet) -> a note: check the drawer
  tick 6: look(cabinet) -> a note: check the drawer
  tick 7: look(cabinet) -> a note: check the drawer
  tick 8: look(cabinet) -> a note: check the drawer
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.015, seed 2042, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: focus-packet [look], dose 0.015, seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: look(drawer) -> a note: check the basket
  tick 4: look(drawer) -> a note: check the basket
  tick 5: look(drawer) -> a note: check the basket
  tick 6: look(drawer) -> a note: check the basket
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [look], dose 0.015, seed 2042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: look(chest) -> a note: try the basket
  tick 4: look(chest) -> a note: try the basket
  tick 5: look(chest) -> a note: try the basket
  tick 6: look(chest) -> a note: try the basket
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.015, seed 2042, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: open(box) -> empty
  tick 5: look(shelf) -> nothing of note
  tick 6: look(shelf) -> nothing of note
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.015, seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: open(cabinet) -> empty
  tick 2: open(cabinet) -> empty
  tick 3: open(cabinet) -> empty
  tick 4: open(cabinet) -> empty
  tick 5: look(cabinet) -> a note: check the box
  tick 6: look(cabinet) -> a note: check the box
  tick 7: look(cabinet) -> a note: check the box
  tick 8: look(cabinet) -> a note: check the box
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.015, seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: open(box) -> empty
  tick 2: look(chest) -> a note: check the drawer
  tick 3: look(chest) -> a note: check the drawer
  tick 4: look(shelf) -> nothing of note
  tick 5: look(shelf) -> nothing of note
  tick 6: look(shelf) -> nothing of note
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.015, seed 2042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(pond) -> a note: check the box
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: look(shelf) -> the shelf is closed; something is inside
  tick 5: look(shelf) -> the shelf is closed; something is inside
  tick 6: look(shelf) -> the shelf is closed; something is inside
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.015, seed 2042, chain drawer->box->basket, target: red stone
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: open(box) -> empty
  tick 5: look(shelf) -> nothing of note
  tick 6: look(shelf) -> nothing of note
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.015, seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(shelf) -> a note: check the pond
  tick 3: look(shelf) -> a note: check the pond
  tick 4: look(shelf) -> a note: check the pond
  tick 5: look(shelf) -> a note: check the pond
  tick 6: look(shelf) -> a note: check the pond
  tick 7: look(shelf) -> a note: check the pond
  tick 8: look(shelf) -> a note: check the pond
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.015, seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: open(cabinet) -> empty
  tick 2: open(cabinet) -> empty
  tick 3: open(cabinet) -> empty
  tick 4: open(cabinet) -> empty
  tick 5: look(cabinet) -> a note: check the drawer
  tick 6: look(drawer) -> a note: try the shelf
  tick 7: look(drawer) -> a note: try the shelf
  tick 8: look(drawer) -> a note: try the shelf
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.015, seed 2042, chain chest->cabinet->drawer, target: green leaf
  tick 1: open(box) -> empty
  tick 2: look(chest) -> a note: check the cabinet
  tick 3: look(cabinet) -> a note: try the drawer
  tick 4: look(shelf) -> nothing of note
  tick 5: look(cabinet) -> a note: try the drawer
  tick 6: look(cabinet) -> a note: try the drawer
  tick 7: look(cabinet) -> a note: try the drawer
  tick 8: look(cabinet) -> a note: try the drawer
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.015, seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: open(box) -> empty
  tick 5: look(shelf) -> nothing of note
  tick 6: look(shelf) -> nothing of note
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: focus-packet [open], dose 0.015, seed 2042, chain jar->chest->basket, target: black thread
  tick 1: open(jar) -> empty
  tick 2: open(jar) -> empty
  tick 3: open(jar) -> empty
  tick 4: open(jar) -> empty
  tick 5: look(jar) -> a note: check the chest
  tick 6: look(chest) -> a note: try the basket
  tick 7: look(chest) -> a note: try the basket
  tick 8: look(chest) -> a note: try the basket
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

