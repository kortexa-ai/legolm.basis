# g2-truncated-context

Host `LiquidAI/LFM2.5-230M`, budget 8, 1627.52 s.

| arm | seed | success | depth | ticks | submit | guess | invalid | repeat |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| last-obs-text | 42 | 1.00 | 3.00 | 4.0 | 1.00 | 0.00 | 0 | 0 |
| last-obs-text | 1042 | 1.00 | 3.00 | 4.0 | 1.00 | 0.00 | 0 | 0 |
| last-obs-text | 2042 | 1.00 | 3.00 | 4.0 | 1.00 | 0.00 | 0 | 0 |
| progress-packet | 42 | 1.00 | 0.00 | 2.0 | 1.00 | 1.00 | 0 | 0 |
| progress-packet | 1042 | 1.00 | 0.00 | 2.0 | 1.00 | 1.00 | 0 | 0 |
| progress-packet | 2042 | 1.00 | 0.00 | 2.0 | 1.00 | 1.00 | 0 | 0 |
| all-latent | 42 | 0.60 | 2.90 | 4.0 | 0.90 | 0.00 | 0 | 5 |
| all-latent | 1042 | 0.50 | 2.60 | 4.0 | 0.70 | 0.00 | 0 | 17 |
| all-latent | 2042 | 0.60 | 3.00 | 4.0 | 1.00 | 0.00 | 0 | 0 |

## Transcripts

```
Episode — arm: last-obs-text, seed 42, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: last-obs-text, seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(blue feather) -> you submit: blue feather
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: last-obs-text, seed 42, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: last-obs-text, seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: last-obs-text, seed 42, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: last-obs-text, seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: last-obs-text, seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: last-obs-text, seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: last-obs-text, seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: last-obs-text, seed 42, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: last-obs-text, seed 1042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: last-obs-text, seed 1042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(blue feather) -> you submit: blue feather
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: last-obs-text, seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: last-obs-text, seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: last-obs-text, seed 1042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: last-obs-text, seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: last-obs-text, seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: last-obs-text, seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: last-obs-text, seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: last-obs-text, seed 1042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: last-obs-text, seed 2042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: last-obs-text, seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(blue feather) -> you submit: blue feather
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: last-obs-text, seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: last-obs-text, seed 2042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: last-obs-text, seed 2042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: last-obs-text, seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: last-obs-text, seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: last-obs-text, seed 2042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: last-obs-text, seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: last-obs-text, seed 2042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: progress-packet, seed 42, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: done(black thread) -> you submit: black thread
  PASS — depth 0/3, 2 of 8 ticks, guessed
```

```
Episode — arm: progress-packet, seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: open(cabinet) -> empty
  tick 2: done(blue feather) -> you submit: blue feather
  PASS — depth 0/3, 2 of 8 ticks, guessed
```

```
Episode — arm: progress-packet, seed 42, chain chest->drawer->basket, target: black thread
  tick 1: open(box) -> empty
  tick 2: done(black thread) -> you submit: black thread
  PASS — depth 0/3, 2 of 8 ticks, guessed
```

```
Episode — arm: progress-packet, seed 42, chain pond->box->shelf, target: gold bell
  tick 1: open(box) -> empty
  tick 2: done(gold bell) -> you submit: gold bell
  PASS — depth 0/3, 2 of 8 ticks, guessed
```

```
Episode — arm: progress-packet, seed 42, chain drawer->box->basket, target: red stone
  tick 1: open(box) -> empty
  tick 2: done(red stone) -> you submit: red stone
  PASS — depth 0/3, 2 of 8 ticks, guessed
```

```
Episode — arm: progress-packet, seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: open(box) -> empty
  tick 2: done(gold bell) -> you submit: gold bell
  PASS — depth 0/3, 2 of 8 ticks, guessed
```

```
Episode — arm: progress-packet, seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: open(cabinet) -> empty
  tick 2: done(gold bell) -> you submit: gold bell
  PASS — depth 0/3, 2 of 8 ticks, guessed
```

```
Episode — arm: progress-packet, seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: open(box) -> empty
  tick 2: done(green leaf) -> you submit: green leaf
  PASS — depth 0/3, 2 of 8 ticks, guessed
```

```
Episode — arm: progress-packet, seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: open(box) -> empty
  tick 2: done(amber key) -> you submit: amber key
  PASS — depth 0/3, 2 of 8 ticks, guessed
```

```
Episode — arm: progress-packet, seed 42, chain jar->chest->basket, target: black thread
  tick 1: open(jar) -> empty
  tick 2: done(black thread) -> you submit: black thread
  PASS — depth 0/3, 2 of 8 ticks, guessed
```

```
Episode — arm: progress-packet, seed 1042, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: done(black thread) -> you submit: black thread
  PASS — depth 0/3, 2 of 8 ticks, guessed
```

```
Episode — arm: progress-packet, seed 1042, chain cabinet->box->pond, target: blue feather
  tick 1: open(cabinet) -> empty
  tick 2: done(blue feather) -> you submit: blue feather
  PASS — depth 0/3, 2 of 8 ticks, guessed
```

```
Episode — arm: progress-packet, seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: open(box) -> empty
  tick 2: done(black thread) -> you submit: black thread
  PASS — depth 0/3, 2 of 8 ticks, guessed
```

```
Episode — arm: progress-packet, seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: open(box) -> empty
  tick 2: done(gold bell) -> you submit: gold bell
  PASS — depth 0/3, 2 of 8 ticks, guessed
```

```
Episode — arm: progress-packet, seed 1042, chain drawer->box->basket, target: red stone
  tick 1: open(box) -> empty
  tick 2: done(red stone) -> you submit: red stone
  PASS — depth 0/3, 2 of 8 ticks, guessed
```

```
Episode — arm: progress-packet, seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: open(box) -> empty
  tick 2: done(gold bell) -> you submit: gold bell
  PASS — depth 0/3, 2 of 8 ticks, guessed
```

```
Episode — arm: progress-packet, seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: open(cabinet) -> empty
  tick 2: done(gold bell) -> you submit: gold bell
  PASS — depth 0/3, 2 of 8 ticks, guessed
```

```
Episode — arm: progress-packet, seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: open(box) -> empty
  tick 2: done(green leaf) -> you submit: green leaf
  PASS — depth 0/3, 2 of 8 ticks, guessed
```

```
Episode — arm: progress-packet, seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: open(box) -> empty
  tick 2: done(amber key) -> you submit: amber key
  PASS — depth 0/3, 2 of 8 ticks, guessed
```

```
Episode — arm: progress-packet, seed 1042, chain jar->chest->basket, target: black thread
  tick 1: open(jar) -> empty
  tick 2: done(black thread) -> you submit: black thread
  PASS — depth 0/3, 2 of 8 ticks, guessed
```

```
Episode — arm: progress-packet, seed 2042, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: done(black thread) -> you submit: black thread
  PASS — depth 0/3, 2 of 8 ticks, guessed
```

```
Episode — arm: progress-packet, seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: open(cabinet) -> empty
  tick 2: done(blue feather) -> you submit: blue feather
  PASS — depth 0/3, 2 of 8 ticks, guessed
```

```
Episode — arm: progress-packet, seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: open(box) -> empty
  tick 2: done(black thread) -> you submit: black thread
  PASS — depth 0/3, 2 of 8 ticks, guessed
```

```
Episode — arm: progress-packet, seed 2042, chain pond->box->shelf, target: gold bell
  tick 1: open(box) -> empty
  tick 2: done(gold bell) -> you submit: gold bell
  PASS — depth 0/3, 2 of 8 ticks, guessed
```

```
Episode — arm: progress-packet, seed 2042, chain drawer->box->basket, target: red stone
  tick 1: open(box) -> empty
  tick 2: done(red stone) -> you submit: red stone
  PASS — depth 0/3, 2 of 8 ticks, guessed
```

```
Episode — arm: progress-packet, seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: open(box) -> empty
  tick 2: done(gold bell) -> you submit: gold bell
  PASS — depth 0/3, 2 of 8 ticks, guessed
```

```
Episode — arm: progress-packet, seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: open(cabinet) -> empty
  tick 2: done(gold bell) -> you submit: gold bell
  PASS — depth 0/3, 2 of 8 ticks, guessed
```

```
Episode — arm: progress-packet, seed 2042, chain chest->cabinet->drawer, target: green leaf
  tick 1: open(box) -> empty
  tick 2: done(green leaf) -> you submit: green leaf
  PASS — depth 0/3, 2 of 8 ticks, guessed
```

```
Episode — arm: progress-packet, seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: open(box) -> empty
  tick 2: done(amber key) -> you submit: amber key
  PASS — depth 0/3, 2 of 8 ticks, guessed
```

```
Episode — arm: progress-packet, seed 2042, chain jar->chest->basket, target: black thread
  tick 1: open(jar) -> empty
  tick 2: done(black thread) -> you submit: black thread
  PASS — depth 0/3, 2 of 8 ticks, guessed
```

```
Episode — arm: all-latent, seed 42, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: all-latent, seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: all-latent, seed 42, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: all-latent, seed 42, chain pond->box->shelf, target: gold bell
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
Episode — arm: all-latent, seed 42, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: all-latent, seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: all-latent, seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(black thread) -> you submit: black thread
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: all-latent, seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: all-latent, seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(black thread) -> you submit: black thread
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: all-latent, seed 42, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: all-latent, seed 1042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: all-latent, seed 1042, chain cabinet->box->pond, target: blue feather
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
Episode — arm: all-latent, seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: all-latent, seed 1042, chain pond->box->shelf, target: gold bell
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
Episode — arm: all-latent, seed 1042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: all-latent, seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: all-latent, seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: look(shelf) -> the shelf is closed; something is inside
  tick 5: look(shelf) -> the shelf is closed; something is inside
  tick 6: look(shelf) -> the shelf is closed; something is inside
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: all-latent, seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: all-latent, seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(black thread) -> you submit: black thread
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: all-latent, seed 1042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: all-latent, seed 2042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(green leaf) -> you submit: green leaf
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: all-latent, seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: all-latent, seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: all-latent, seed 2042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: all-latent, seed 2042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: all-latent, seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: all-latent, seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: all-latent, seed 2042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: all-latent, seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(black thread) -> you submit: black thread
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: all-latent, seed 2042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```
