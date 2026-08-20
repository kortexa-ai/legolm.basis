# g6-split-door-want

Host machine `smarty`, device `cuda`, budget 8, 597.116 s. Registration: tracks/goal-pursuit/PLAN.md, 2026-08-15 G6.

## Plain cells — the installed item is the chain's own

| arm | seed | success | depth | ticks | submit | guess | invalid | repeat |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| text | 42 | 1.00 | 3.00 | 4.0 | 1.00 | 0.00 | 0 | 0 |
| text | 1042 | 1.00 | 3.00 | 4.0 | 1.00 | 0.00 | 0 | 0 |
| text | 2042 | 1.00 | 2.80 | 4.0 | 1.00 | 0.10 | 0 | 1 |
| bus-only | 42 | 0.70 | 3.00 | 4.0 | 1.00 | 0.00 | 0 | 0 |
| bus-only | 1042 | 0.70 | 3.00 | 4.0 | 1.00 | 0.00 | 0 | 0 |
| bus-only | 2042 | 0.70 | 2.80 | 4.0 | 1.00 | 0.00 | 0 | 1 |
| prefix-only | 42 | 1.00 | 3.00 | 4.0 | 1.00 | 0.00 | 0 | 0 |
| prefix-only | 1042 | 1.00 | 3.00 | 4.0 | 1.00 | 0.00 | 0 | 0 |
| prefix-only | 2042 | 1.00 | 3.00 | 4.0 | 1.00 | 0.00 | 0 | 0 |
| split-door | 42 | 0.80 | 3.00 | 4.5 | 1.00 | 0.00 | 4 | 0 |
| split-door | 1042 | 0.90 | 3.00 | 4.0 | 1.00 | 0.00 | 0 | 0 |
| split-door | 2042 | 0.00 | 1.00 | None | 0.00 | 0.00 | 70 | 13 |

## Crossed probe — symbol following, door by door

| arm | seed | follow-installed (in pair) | follow-target (installed elsewhere) | follow-reveal-first | installed-dependent chains | submit rate | decided |
|---|---|---:|---:|---:|---:|---:|---:|
| text | 42 | 1.00 | 0.63 | 0.68 | 10 | 1.00 | 80 |
| text | 1042 | 1.00 | 0.62 | 0.36 | 10 | 1.00 | 80 |
| text | 2042 | 1.00 | 0.71 | 0.51 | 10 | 1.00 | 71 |
| bus-only | 42 | 0.60 | 0.62 | 0.39 | 3 | 1.00 | 80 |
| bus-only | 1042 | 0.50 | 0.68 | 0.39 | 2 | 1.00 | 80 |
| bus-only | 2042 | 0.61 | 0.79 | 0.46 | 3 | 1.00 | 71 |
| prefix-only | 42 | 0.89 | 0.69 | 0.76 | 7 | 1.00 | 78 |
| prefix-only | 1042 | 0.90 | 0.70 | 0.47 | 8 | 1.00 | 80 |
| prefix-only | 2042 | 0.89 | 0.80 | 0.54 | 7 | 1.00 | 79 |
| split-door | 42 | 0.63 | 0.60 | 0.32 | 3 | 0.95 | 74 |
| split-door | 1042 | 0.75 | 0.72 | 0.45 | 5 | 1.00 | 80 |
| split-door | 2042 | -- | -- | -- | 0 | 0.00 | 0 |

## Door conflict — split-door, the two doors disagree

| seed | prefix wins | bus wins | other |
|---|---:|---:|---:|
| 42 | 9 | 10 | 1 |
| 1042 | 11 | 9 | 0 |
| 2042 | 0 | 0 | 20 |

### Response surface — text, seed 42 (rows: chain target/distractor; columns: installed item; cell: submitted item, `*` = followed the installed item)

| chain (t/d) | ak | jc | gb | rs | bf | gl | bt | ws |
|---|---|---|---|---|---|---|---|---|
| bt/gl | bt | bt | bt | bt | bt | gl* | bt* | bt |
| bf/gb | gb | gb | gb* | gb | bf* | bf | gb | bf |
| bt/bf | bt | bt | bt | bt | bf* | bt | bt* | bt |
| gb/bf | gb | gb | gb* | gb | bf* | gb | gb | bf |
| rs/bf | rs | rs | rs | rs* | bf* | rs | rs | rs |
| gb/bf | bf | gb | gb* | bf | bf* | bf | bf | bf |
| gb/bt | bt | bt | gb* | bt | bt | bt | bt* | bt |
| gl/ak | ak* | gl | gl | gl | gl | gl* | gl | gl |
| ak/bt | ak* | bt | bt | bt | bt | bt | bt* | bt |
| bt/gb | bt | bt | gb* | bt | bt | bt | bt* | bt |

### Response surface — text, seed 1042 (rows: chain target/distractor; columns: installed item; cell: submitted item, `*` = followed the installed item)

| chain (t/d) | ak | jc | gb | rs | bf | gl | bt | ws |
|---|---|---|---|---|---|---|---|---|
| bt/gl | bt | bt | bt | bt | bt | gl* | bt* | bt |
| bf/gb | gb | gb | gb* | gb | bf* | gb | gb | gb |
| bt/bf | bt | bt | bt | bt | bf* | bt | bt* | bt |
| gb/bf | gb | gb | gb* | gb | bf* | gb | gb | gb |
| rs/bf | rs | rs | rs | rs* | bf* | rs | rs | rs |
| gb/bf | gb | gb | gb* | gb | bf* | gb | gb | gb |
| gb/bt | gb | gb | gb* | gb | gb | gb | bt* | gb |
| gl/ak | ak* | ak | ak | gl | ak | gl* | ak | ak |
| ak/bt | ak* | bt | bt | bt | bt | bt | bt* | bt |
| bt/gb | gb | gb | gb* | gb | gb | gb | bt* | gb |

### Response surface — text, seed 2042 (rows: chain target/distractor; columns: installed item; cell: submitted item, `*` = followed the installed item)

| chain (t/d) | ak | jc | gb | rs | bf | gl | bt | ws |
|---|---|---|---|---|---|---|---|---|
| bt/gl | bt | bt | bt | bt | bt | gl* | bt* | bt |
| bf/gb | gb | jc* | gb* | rs* | bf* | gl* | gb | gb |
| bt/bf | bt | bt | bt | bt | bf* | bt | bt* | bt |
| gb/bf | gb | jc* | gb* | gb | bf* | gl* | bt* | ws* |
| rs/bf | rs | jc* | gb* | rs* | bf* | rs | rs | rs |
| gb/bf | gb | gb | gb* | gb | bf* | gb | gb | gb |
| gb/bt | gb | gb | gb* | gb | bt | gb | bt* | bt |
| gl/ak | ak* | gl | gl | gl | gl | gl* | gl | gl |
| ak/bt | ak* | ak | bt | bt | bt | bt | bt* | bt |
| bt/gb | gb | gb | gb* | gb | gb | gb | bt* | bt |

### Response surface — bus-only, seed 42 (rows: chain target/distractor; columns: installed item; cell: submitted item, `*` = followed the installed item)

| chain (t/d) | ak | jc | gb | rs | bf | gl | bt | ws |
|---|---|---|---|---|---|---|---|---|
| bt/gl | gl | gl | gl | gl | gl | gl* | gl | gl |
| bf/gb | gb | gb | gb* | gb | gb | gb | gb | gb |
| bt/bf | bt | bt | bt | bt | bt | bt | bt* | bt |
| gb/bf | gb | gb | gb* | gb | gb | gb | gb | gb |
| rs/bf | rs | rs | rs | rs* | rs | rs | rs | rs |
| gb/bf | gb | gb | gb* | gb | gb | gb | gb | gb |
| gb/bt | bt | gb | gb* | gb | bt | gb | bt* | gb |
| gl/ak | gl | gl | gl | gl | gl | gl* | gl | gl |
| ak/bt | bt | ak | bt | bt | bt | bt | bt* | bt |
| bt/gb | bt | gb | gb* | gb | bt | gb | bt* | gb |

### Response surface — bus-only, seed 1042 (rows: chain target/distractor; columns: installed item; cell: submitted item, `*` = followed the installed item)

| chain (t/d) | ak | jc | gb | rs | bf | gl | bt | ws |
|---|---|---|---|---|---|---|---|---|
| bt/gl | bt | gl | gl | gl | gl | gl* | gl | gl |
| bf/gb | gb | gb | gb* | gb | gb | gb | gb | gb |
| bt/bf | bt | bt | bt | bt | bt | bt | bt* | bt |
| gb/bf | gb | gb | gb* | gb | gb | gb | gb | gb |
| rs/bf | rs | rs | rs | rs* | rs | rs | rs | rs |
| gb/bf | gb | gb | gb* | gb | gb | gb | gb | gb |
| gb/bt | gb | gb | gb* | gb | gb | gb | gb | gb |
| gl/ak | gl | gl | gl | gl | gl | gl* | gl | gl |
| ak/bt | ak* | ak | ak | ak | ak | bt | ak | bt |
| bt/gb | gb | gb | gb* | gb | gb | gb | gb | gb |

### Response surface — bus-only, seed 2042 (rows: chain target/distractor; columns: installed item; cell: submitted item, `*` = followed the installed item)

| chain (t/d) | ak | jc | gb | rs | bf | gl | bt | ws |
|---|---|---|---|---|---|---|---|---|
| bt/gl | bt | bt | bt | bt | bt | bt | bt* | bt |
| bf/gb | ak* | ak | em | ak | em | em | em | em |
| bt/bf | bt | bt | bt | bt | bt | bt | bt* | bt |
| gb/bf | gb | gb | gb* | gb | gb | gb | gb | gb |
| rs/bf | rs | rs | rs | rs* | rs | rs | rs | rs |
| gb/bf | gb | gb | gb* | gb | bf* | gb | gb | gb |
| gb/bt | ak* | gb | gb* | gb | gb | gb | gb | gb |
| gl/ak | ak* | ak | gl | gl | gl | gl* | gl | gl |
| ak/bt | bt | bt | bt | bt | bt | bt | bt* | bt |
| bt/gb | gb | gb | gb* | gb | bt | gb | gb | bt |

### Response surface — prefix-only, seed 42 (rows: chain target/distractor; columns: installed item; cell: submitted item, `*` = followed the installed item)

| chain (t/d) | ak | jc | gb | rs | bf | gl | bt | ws |
|---|---|---|---|---|---|---|---|---|
| bt/gl | bt | bt | bt | bt | bt | gl* | bt* | bt |
| bf/gb | bf | bf | gb* | bf | bf* | bf | bf | bf |
| bt/bf | bt | bt | bt | bt | bt | bt | bt* | bt |
| gb/bf | ak* | gb | gb* | gb | ak | gb | gb | gb |
| rs/bf | rs | rs | rs | rs* | rs | rs | rs | rs |
| gb/bf | bf | bf | gb* | bf | bf* | bf | bf | bf |
| gb/bt | bt | bt | gb* | bt | bt | bt | bt* | bt |
| gl/ak | ak* | ak | ak | ak | ak | gl* | ak | ak |
| ak/bt | ak* | ak | ak | ak | ak | ak | bt* | ak |
| bt/gb | bt | bt | gb* | bt | bt | bt | bt* | bt |

### Response surface — prefix-only, seed 1042 (rows: chain target/distractor; columns: installed item; cell: submitted item, `*` = followed the installed item)

| chain (t/d) | ak | jc | gb | rs | bf | gl | bt | ws |
|---|---|---|---|---|---|---|---|---|
| bt/gl | bt | bt | bt | bt | bt | gl* | bt* | bt |
| bf/gb | gb | gb | gb* | gb | bf* | gb | gb | gb |
| bt/bf | bt | bt | bt | bt | bt | bt | bt* | bt |
| gb/bf | gb | gb | gb* | gb | bf* | gb | gb | gb |
| rs/bf | rs | rs | rs | rs* | rs | rs | rs | rs |
| gb/bf | gb | gb | gb* | gb | bf* | gb | gb | gb |
| gb/bt | bt | gb | gb* | gb | gb | gb | bt* | gb |
| gl/ak | ak* | ak | ak | ak | ak | gl* | ak | ak |
| ak/bt | ak* | ak | ak | ak | ak | ak | bt* | ak |
| bt/gb | bt | gb | gb* | gb | gb | gb | bt* | gb |

### Response surface — prefix-only, seed 2042 (rows: chain target/distractor; columns: installed item; cell: submitted item, `*` = followed the installed item)

| chain (t/d) | ak | jc | gb | rs | bf | gl | bt | ws |
|---|---|---|---|---|---|---|---|---|
| bt/gl | bt | bt | bt | bt | bt | gl* | bt* | bt |
| bf/gb | gb | gb | gb* | gb | bf* | gb | gb | gb |
| bt/bf | bt | bt | bt | bt | bt | bt | bt* | bt |
| gb/bf | gb | gb | gb* | gb | ak | gb | gb | gb |
| rs/bf | rs | rs | rs | rs* | rs | rs | rs | rs |
| gb/bf | gb | gb | gb* | gb | bf* | gb | gb | gb |
| gb/bt | bt | gb | gb* | gb | gb | gb | bt* | gb |
| gl/ak | ak* | gl | gl | gl | gl | gl* | gl | gl |
| ak/bt | ak* | ak | ak | ak | ak | ak | bt* | ak |
| bt/gb | bt | gb | gb* | gb | gb | gb | bt* | gb |

### Response surface — split-door, seed 42 (rows: chain target/distractor; columns: installed item; cell: submitted item, `*` = followed the installed item)

| chain (t/d) | ak | jc | gb | rs | bf | gl | bt | ws |
|---|---|---|---|---|---|---|---|---|
| bt/gl | gl | gl | gl | gl | gl | gl* | gl | gl |
| bf/gb | ak* | gb | gb* | gb | gb | gb | gb | gb |
| bt/bf | -- | bt | bt | bt | bt | bt | bt* | bt |
| gb/bf | gb | gb | gb* | gb | gb | gb | gb | gb |
| rs/bf | rs | rs | rs | rs* | rs | rs | rs | rs |
| gb/bf | ca | gb | gb* | gb | gb | gb | gb | gb |
| gb/bt | -- | gb | gb* | gb | gb | gb | gb | gb |
| gl/ak | -- | ak | ak | gl | gl | gl* | gl | gl |
| ak/bt | ak* | ak | bt | bt | bt | bt | bt* | bt |
| bt/gb | bt | gb | gb* | gb | -- | gb | bt* | gb |

### Response surface — split-door, seed 1042 (rows: chain target/distractor; columns: installed item; cell: submitted item, `*` = followed the installed item)

| chain (t/d) | ak | jc | gb | rs | bf | gl | bt | ws |
|---|---|---|---|---|---|---|---|---|
| bt/gl | bt | gl | gl | gl | gl | gl* | bt* | gl |
| bf/gb | gb | gb | gb* | gb | bf* | gb | gb | gb |
| bt/bf | bt | bt | bt | bt | bt | bt | bt* | bt |
| gb/bf | gb | gb | gb* | gb | bf* | gb | gb | gb |
| rs/bf | rs | rs | rs | rs* | rs | rs | rs | rs |
| gb/bf | gb | gb | gb* | gb | bf* | gb | gb | gb |
| gb/bt | gb | gb | gb* | gb | gb | gb | gb | gb |
| gl/ak | ak* | gl | gl | gl | gl | gl* | gl | gl |
| ak/bt | ak* | ak | ak | ak | ak | ak | ak | ak |
| bt/gb | gb | gb | gb* | gb | gb | gb | gb | gb |

### Response surface — split-door, seed 2042 (rows: chain target/distractor; columns: installed item; cell: submitted item, `*` = followed the installed item)

| chain (t/d) | ak | jc | gb | rs | bf | gl | bt | ws |
|---|---|---|---|---|---|---|---|---|
| bt/gl | -- | -- | -- | -- | -- | -- | -- | -- |
| bf/gb | -- | -- | -- | -- | -- | -- | -- | -- |
| bt/bf | -- | -- | -- | -- | -- | -- | -- | -- |
| gb/bf | -- | -- | -- | -- | -- | -- | -- | -- |
| rs/bf | -- | -- | -- | -- | -- | -- | -- | -- |
| gb/bf | -- | -- | -- | -- | -- | -- | -- | -- |
| gb/bt | -- | -- | -- | -- | -- | -- | -- | -- |
| gl/ak | -- | -- | -- | -- | -- | -- | -- | -- |
| ak/bt | -- | -- | -- | -- | -- | -- | -- | -- |
| bt/gb | -- | -- | -- | -- | -- | -- | -- | -- |

## Transcripts — plain cells

```
Episode — arm: text, seed 42, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: text, seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(blue feather) -> you submit: blue feather
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: text, seed 42, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: text, seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: text, seed 42, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: text, seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: text, seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: text, seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: text, seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: text, seed 42, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: text, seed 1042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: text, seed 1042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(blue feather) -> you submit: blue feather
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: text, seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: text, seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: text, seed 1042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: text, seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: text, seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: text, seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: text, seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: text, seed 1042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: text, seed 2042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: text, seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(cabinet) -> a note: check the box
  tick 3: open(box) -> empty
  tick 4: done(blue feather) -> you submit: blue feather
  PASS — depth 1/3, 4 of 8 ticks, guessed
```

```
Episode — arm: text, seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: text, seed 2042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: text, seed 2042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: text, seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: text, seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: text, seed 2042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: text, seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: text, seed 2042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: bus-only, seed 42, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(green leaf) -> you submit: green leaf
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: bus-only, seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: bus-only, seed 42, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: bus-only, seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: bus-only, seed 42, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: bus-only, seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: bus-only, seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: bus-only, seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: bus-only, seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(black thread) -> you submit: black thread
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: bus-only, seed 42, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: bus-only, seed 1042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(green leaf) -> you submit: green leaf
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: bus-only, seed 1042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: bus-only, seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: bus-only, seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: bus-only, seed 1042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: bus-only, seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: bus-only, seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: bus-only, seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: bus-only, seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: bus-only, seed 1042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: bus-only, seed 2042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: bus-only, seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(cabinet) -> a note: check the box
  tick 3: open(box) -> empty
  tick 4: done(empty) -> you submit: empty
  FAIL (wrong submit) — depth 1/3, 4 of 8 ticks
```

```
Episode — arm: bus-only, seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: bus-only, seed 2042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: bus-only, seed 2042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: bus-only, seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: bus-only, seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: bus-only, seed 2042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: bus-only, seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(black thread) -> you submit: black thread
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: bus-only, seed 2042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only, seed 42, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only, seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(blue feather) -> you submit: blue feather
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only, seed 42, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only, seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only, seed 42, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only, seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only, seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only, seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only, seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only, seed 42, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only, seed 1042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only, seed 1042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(blue feather) -> you submit: blue feather
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only, seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only, seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only, seed 1042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only, seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only, seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only, seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only, seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only, seed 1042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only, seed 2042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only, seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(blue feather) -> you submit: blue feather
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only, seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only, seed 2042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only, seed 2042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only, seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only, seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only, seed 2042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only, seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only, seed 2042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: split-door, seed 42, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: remember() -> that did not work
  tick 3: look(jar) -> a note: try the pond
  tick 4: open(pond) -> you find: black thread and green leaf
  tick 5: done(green leaf) -> you submit: green leaf
  FAIL (wrong submit) — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: split-door, seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: split-door, seed 42, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: remember() -> that did not work
  tick 3: look(drawer) -> a note: try the basket
  tick 4: open(basket) -> you find: black thread and blue feather
  tick 5: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: split-door, seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: split-door, seed 42, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: split-door, seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: split-door, seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: split-door, seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: split-door, seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: split-door, seed 42, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: remember() -> that did not work
  tick 3: look(chest) -> a note: try the basket
  tick 4: remember() -> that did not work
  tick 5: look(basket) -> the basket is closed; something is inside
  tick 6: open(basket) -> you find: black thread and gold bell
  tick 7: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 7 of 8 ticks
```

```
Episode — arm: split-door, seed 1042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: split-door, seed 1042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(blue feather) -> you submit: blue feather
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: split-door, seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: split-door, seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: split-door, seed 1042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: split-door, seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: split-door, seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: split-door, seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: split-door, seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: split-door, seed 1042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: split-door, seed 2042, chain box->jar->pond, target: black thread
  tick 1: remember() -> that did not work
  tick 2: look(box) -> a note: check the jar
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  tick 6: look(jar) -> a note: try the pond
  tick 7: remember() -> that did not work
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: split-door, seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: remember() -> that did not work
  tick 2: look(cabinet) -> a note: check the box
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  tick 6: remember() -> that did not work
  tick 7: remember() -> that did not work
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: split-door, seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: remember() -> that did not work
  tick 2: remember() -> that did not work
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  tick 6: remember() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: split-door, seed 2042, chain pond->box->shelf, target: gold bell
  tick 1: remember() -> that did not work
  tick 2: look(pond) -> a note: check the box
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  tick 6: look(box) -> a note: try the shelf
  tick 7: remember() -> that did not work
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: split-door, seed 2042, chain drawer->box->basket, target: red stone
  tick 1: remember() -> that did not work
  tick 2: remember() -> that did not work
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  tick 6: remember() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: nothing() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: split-door, seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: remember() -> that did not work
  tick 2: look(shelf) -> a note: check the pond
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  tick 6: look(pond) -> a note: try the cabinet
  tick 7: remember() -> that did not work
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: split-door, seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: remember() -> that did not work
  tick 2: look(cabinet) -> a note: check the drawer
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  tick 6: remember() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: split-door, seed 2042, chain chest->cabinet->drawer, target: green leaf
  tick 1: remember() -> that did not work
  tick 2: look(chest) -> a note: check the cabinet
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  tick 6: look(cabinet) -> a note: try the drawer
  tick 7: remember() -> that did not work
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: split-door, seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: remember() -> that did not work
  tick 2: remember() -> that did not work
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  tick 6: remember() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: split-door, seed 2042, chain jar->chest->basket, target: black thread
  tick 1: remember() -> that did not work
  tick 2: remember() -> that did not work
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  tick 6: remember() -> that did not work
  tick 7: remember() -> that did not work
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```


## Transcripts — door conflict

```
Episode — arm: conflict:prefix=black thread|bus=green leaf, seed 42, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: remember() -> that did not work
  tick 3: look(jar) -> a note: try the pond
  tick 4: open(pond) -> you find: black thread and green leaf
  tick 5: done(green leaf) -> you submit: green leaf
  FAIL (wrong submit) — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: conflict:prefix=green leaf|bus=black thread, seed 42, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: remember() -> that did not work
  tick 3: look(jar) -> a note: try the pond
  tick 4: remember() -> that did not work
  tick 5: look(pond) -> the pond is closed; something is inside
  tick 6: open(pond) -> you find: black thread and green leaf
  tick 7: done(green leaf) -> you submit: green leaf
  FAIL (wrong submit) — depth 3/3, 7 of 8 ticks
```

```
Episode — arm: conflict:prefix=blue feather|bus=gold bell, seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: conflict:prefix=gold bell|bus=blue feather, seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: conflict:prefix=black thread|bus=blue feather, seed 42, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: remember() -> that did not work
  tick 3: look(drawer) -> a note: try the basket
  tick 4: open(basket) -> you find: black thread and blue feather
  tick 5: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: conflict:prefix=blue feather|bus=black thread, seed 42, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: conflict:prefix=gold bell|bus=blue feather, seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: conflict:prefix=blue feather|bus=gold bell, seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: conflict:prefix=red stone|bus=blue feather, seed 42, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: conflict:prefix=blue feather|bus=red stone, seed 42, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: conflict:prefix=gold bell|bus=blue feather, seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: remember() -> that did not work
  tick 3: remember() -> that did not work
  tick 4: look(pond) -> a note: try the cabinet
  tick 5: open(cabinet) -> you find: blue feather and gold bell
  tick 6: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 6 of 8 ticks
```

```
Episode — arm: conflict:prefix=blue feather|bus=gold bell, seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: conflict:prefix=gold bell|bus=black thread, seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: remember() -> that did not work
  tick 3: look(drawer) -> a note: try the shelf
  tick 4: remember() -> that did not work
  tick 5: look(shelf) -> the shelf is closed; something is inside
  tick 6: open(shelf) -> you find: black thread and gold bell
  tick 7: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 7 of 8 ticks
```

```
Episode — arm: conflict:prefix=black thread|bus=gold bell, seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: remember() -> that did not work
  tick 3: look(drawer) -> a note: try the shelf
  tick 4: open(shelf) -> you find: black thread and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: conflict:prefix=green leaf|bus=amber key, seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: remember() -> that did not work
  tick 2: look(chest) -> a note: check the cabinet
  tick 3: open(cabinet) -> empty
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  tick 6: look(cabinet) -> a note: try the drawer
  tick 7: remember() -> that did not work
  tick 8: look(drawer) -> the drawer is closed; something is inside
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: conflict:prefix=amber key|bus=green leaf, seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: conflict:prefix=amber key|bus=black thread, seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(black thread) -> you submit: black thread
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: conflict:prefix=black thread|bus=amber key, seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: remember() -> that did not work
  tick 3: look(basket) -> a note: try the cabinet
  tick 4: remember() -> that did not work
  tick 5: look(cabinet) -> the cabinet is closed; something is inside
  tick 6: open(cabinet) -> you find: amber key and black thread
  tick 7: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 7 of 8 ticks
```

```
Episode — arm: conflict:prefix=black thread|bus=gold bell, seed 42, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: remember() -> that did not work
  tick 3: look(chest) -> a note: try the basket
  tick 4: open(basket) -> you find: black thread and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: conflict:prefix=gold bell|bus=black thread, seed 42, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: remember() -> that did not work
  tick 3: remember() -> that did not work
  tick 4: look(chest) -> a note: try the basket
  tick 5: look(basket) -> the basket is closed; something is inside
  tick 6: open(basket) -> you find: black thread and gold bell
  tick 7: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 7 of 8 ticks
```

```
Episode — arm: conflict:prefix=black thread|bus=green leaf, seed 1042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(green leaf) -> you submit: green leaf
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: conflict:prefix=green leaf|bus=black thread, seed 1042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(green leaf) -> you submit: green leaf
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: conflict:prefix=blue feather|bus=gold bell, seed 1042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: conflict:prefix=gold bell|bus=blue feather, seed 1042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: conflict:prefix=black thread|bus=blue feather, seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: conflict:prefix=blue feather|bus=black thread, seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: conflict:prefix=gold bell|bus=blue feather, seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: conflict:prefix=blue feather|bus=gold bell, seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: conflict:prefix=red stone|bus=blue feather, seed 1042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: conflict:prefix=blue feather|bus=red stone, seed 1042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: conflict:prefix=gold bell|bus=blue feather, seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: conflict:prefix=blue feather|bus=gold bell, seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: conflict:prefix=gold bell|bus=black thread, seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: conflict:prefix=black thread|bus=gold bell, seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: conflict:prefix=green leaf|bus=amber key, seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: conflict:prefix=amber key|bus=green leaf, seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: conflict:prefix=amber key|bus=black thread, seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: conflict:prefix=black thread|bus=amber key, seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: conflict:prefix=black thread|bus=gold bell, seed 1042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: conflict:prefix=gold bell|bus=black thread, seed 1042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: conflict:prefix=black thread|bus=green leaf, seed 2042, chain box->jar->pond, target: black thread
  tick 1: remember() -> that did not work
  tick 2: look(box) -> a note: check the jar
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  tick 6: look(jar) -> a note: try the pond
  tick 7: remember() -> that did not work
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: conflict:prefix=green leaf|bus=black thread, seed 2042, chain box->jar->pond, target: black thread
  tick 1: remember() -> that did not work
  tick 2: look(box) -> a note: check the jar
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  tick 6: look(jar) -> a note: try the pond
  tick 7: remember() -> that did not work
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: conflict:prefix=blue feather|bus=gold bell, seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: remember() -> that did not work
  tick 2: look(cabinet) -> a note: check the box
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  tick 6: remember() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: conflict:prefix=gold bell|bus=blue feather, seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: remember() -> that did not work
  tick 2: look(cabinet) -> a note: check the box
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  tick 6: look(box) -> a note: try the pond
  tick 7: remember() -> that did not work
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: conflict:prefix=black thread|bus=blue feather, seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: remember() -> that did not work
  tick 2: remember() -> that did not work
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  tick 6: remember() -> that did not work
  tick 7: look(chest) -> a note: check the drawer
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: conflict:prefix=blue feather|bus=black thread, seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: remember() -> that did not work
  tick 2: remember() -> that did not work
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  tick 6: remember() -> that did not work
  tick 7: look(chest) -> a note: check the drawer
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: conflict:prefix=gold bell|bus=blue feather, seed 2042, chain pond->box->shelf, target: gold bell
  tick 1: remember() -> that did not work
  tick 2: look(pond) -> a note: check the box
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  tick 6: look(box) -> a note: try the shelf
  tick 7: remember() -> that did not work
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: conflict:prefix=blue feather|bus=gold bell, seed 2042, chain pond->box->shelf, target: gold bell
  tick 1: remember() -> that did not work
  tick 2: look(pond) -> a note: check the box
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  tick 6: look(box) -> a note: try the shelf
  tick 7: remember() -> that did not work
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: conflict:prefix=red stone|bus=blue feather, seed 2042, chain drawer->box->basket, target: red stone
  tick 1: remember() -> that did not work
  tick 2: remember() -> that did not work
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  tick 6: remember() -> that did not work
  tick 7: look(drawer) -> a note: check the box
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: conflict:prefix=blue feather|bus=red stone, seed 2042, chain drawer->box->basket, target: red stone
  tick 1: remember() -> that did not work
  tick 2: remember() -> that did not work
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  tick 6: remember() -> that did not work
  tick 7: look(drawer) -> a note: check the box
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: conflict:prefix=gold bell|bus=blue feather, seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: remember() -> that did not work
  tick 2: remember() -> that did not work
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  tick 6: remember() -> that did not work
  tick 7: remember() -> that did not work
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: conflict:prefix=blue feather|bus=gold bell, seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: remember() -> that did not work
  tick 2: look(shelf) -> a note: check the pond
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  tick 6: look(pond) -> a note: try the cabinet
  tick 7: remember() -> that did not work
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: conflict:prefix=gold bell|bus=black thread, seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: remember() -> that did not work
  tick 2: look(cabinet) -> a note: check the drawer
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  tick 6: look(drawer) -> a note: try the shelf
  tick 7: remember() -> that did not work
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: conflict:prefix=black thread|bus=gold bell, seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: remember() -> that did not work
  tick 2: remember() -> that did not work
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  tick 6: remember() -> that did not work
  tick 7: look(cabinet) -> a note: check the drawer
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: conflict:prefix=green leaf|bus=amber key, seed 2042, chain chest->cabinet->drawer, target: green leaf
  tick 1: remember() -> that did not work
  tick 2: remember() -> that did not work
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  tick 6: remember() -> that did not work
  tick 7: remember() -> that did not work
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: conflict:prefix=amber key|bus=green leaf, seed 2042, chain chest->cabinet->drawer, target: green leaf
  tick 1: remember() -> that did not work
  tick 2: look(chest) -> a note: check the cabinet
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  tick 6: nothing() -> that did not work
  tick 7: nothing() -> that did not work
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: conflict:prefix=amber key|bus=black thread, seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: remember() -> that did not work
  tick 2: look(drawer) -> a note: check the basket
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  tick 6: remember() -> that did not work
  tick 7: remember() -> that did not work
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: conflict:prefix=black thread|bus=amber key, seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: remember() -> that did not work
  tick 2: remember() -> that did not work
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  tick 6: remember() -> that did not work
  tick 7: remember() -> that did not work
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: conflict:prefix=black thread|bus=gold bell, seed 2042, chain jar->chest->basket, target: black thread
  tick 1: remember() -> that did not work
  tick 2: remember() -> that did not work
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  tick 6: remember() -> that did not work
  tick 7: remember() -> that did not work
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: conflict:prefix=gold bell|bus=black thread, seed 2042, chain jar->chest->basket, target: black thread
  tick 1: remember() -> that did not work
  tick 2: look(jar) -> a note: check the chest
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  tick 6: look(chest) -> a note: try the basket
  tick 7: remember() -> that did not work
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

