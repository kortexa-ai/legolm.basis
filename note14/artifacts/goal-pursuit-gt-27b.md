# gt-temporal-pressure-27b

Host `Qwen/Qwen3.6-27B`, budget 5, 5512.379 s.

| arm | seed | success | depth | ticks | submit | guess | invalid | repeat |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| none | 42 | 1.00 | 3.00 | 4.0 | 1.00 | 0.00 | 0 | 0 |
| none | 1042 | 1.00 | 3.00 | 4.0 | 1.00 | 0.00 | 0 | 0 |
| none | 2042 | 1.00 | 3.00 | 4.0 | 1.00 | 0.00 | 0 | 0 |
| countdown | 42 | 1.00 | 3.00 | 4.0 | 1.00 | 0.00 | 0 | 0 |
| countdown | 1042 | 1.00 | 3.00 | 4.0 | 1.00 | 0.00 | 0 | 0 |
| countdown | 2042 | 1.00 | 3.00 | 4.0 | 1.00 | 0.00 | 0 | 0 |
| temporal | 42 | 0.00 | 2.20 | None | 0.00 | 0.00 | 27 | 0 |
| temporal | 1042 | 1.00 | 3.00 | 5.0 | 1.00 | 0.00 | 10 | 0 |
| temporal | 2042 | 0.00 | 1.00 | None | 0.00 | 0.00 | 40 | 0 |

## Transcripts

```
Episode — arm: none, seed 42, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: none, seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(blue feather) -> you submit: blue feather
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: none, seed 42, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: none, seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: none, seed 42, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: none, seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: none, seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: none, seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: none, seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: none, seed 42, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: none, seed 1042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: none, seed 1042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(blue feather) -> you submit: blue feather
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: none, seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: none, seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: none, seed 1042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: none, seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: none, seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: none, seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: none, seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: none, seed 1042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: none, seed 2042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: none, seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(blue feather) -> you submit: blue feather
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: none, seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: none, seed 2042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: none, seed 2042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: none, seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: none, seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: none, seed 2042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: none, seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: none, seed 2042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: countdown, seed 42, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: countdown, seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(blue feather) -> you submit: blue feather
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: countdown, seed 42, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: countdown, seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: countdown, seed 42, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: countdown, seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: countdown, seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: countdown, seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: countdown, seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: countdown, seed 42, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: countdown, seed 1042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: countdown, seed 1042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(blue feather) -> you submit: blue feather
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: countdown, seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: countdown, seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: countdown, seed 1042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: countdown, seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: countdown, seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: countdown, seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: countdown, seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: countdown, seed 1042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: countdown, seed 2042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: countdown, seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(blue feather) -> you submit: blue feather
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: countdown, seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: countdown, seed 2042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: countdown, seed 2042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: countdown, seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: countdown, seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: countdown, seed 2042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: countdown, seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: countdown, seed 2042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 5 ticks
```

```
Episode — arm: temporal, seed 42, chain box->jar->pond, target: black thread
  tick 1: remember() -> that did not work
  tick 2: look(box) -> a note: check the jar
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  FAIL (budget) — depth 1/3, 5 of 5 ticks
```

```
Episode — arm: temporal, seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: open(pond) -> you find: blue feather and gold bell
  FAIL (budget) — depth 3/3, 5 of 5 ticks
```

```
Episode — arm: temporal, seed 42, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: remember() -> that did not work
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: look(drawer) -> a note: try the basket
  FAIL (budget) — depth 2/3, 5 of 5 ticks
```

```
Episode — arm: temporal, seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  FAIL (budget) — depth 2/3, 5 of 5 ticks
```

```
Episode — arm: temporal, seed 42, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: open(basket) -> you find: red stone and blue feather
  FAIL (budget) — depth 3/3, 5 of 5 ticks
```

```
Episode — arm: temporal, seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  FAIL (budget) — depth 2/3, 5 of 5 ticks
```

```
Episode — arm: temporal, seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: open(shelf) -> you find: black thread and gold bell
  FAIL (budget) — depth 3/3, 5 of 5 ticks
```

```
Episode — arm: temporal, seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: open(drawer) -> you find: green leaf and amber key
  FAIL (budget) — depth 3/3, 5 of 5 ticks
```

```
Episode — arm: temporal, seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: remember() -> that did not work
  FAIL (budget) — depth 2/3, 5 of 5 ticks
```

```
Episode — arm: temporal, seed 42, chain jar->chest->basket, target: black thread
  tick 1: remember() -> that did not work
  tick 2: look(jar) -> a note: check the chest
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: open(chest) -> empty
  FAIL (budget) — depth 1/3, 5 of 5 ticks
```

```
Episode — arm: temporal, seed 1042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: remember() -> that did not work
  tick 5: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 5 of 5 ticks
```

```
Episode — arm: temporal, seed 1042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: remember() -> that did not work
  tick 5: done(blue feather) -> you submit: blue feather
  PASS — depth 3/3, 5 of 5 ticks
```

```
Episode — arm: temporal, seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: remember() -> that did not work
  tick 5: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 5 of 5 ticks
```

```
Episode — arm: temporal, seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: remember() -> that did not work
  tick 5: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 5 of 5 ticks
```

```
Episode — arm: temporal, seed 1042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: remember() -> that did not work
  tick 5: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 5 of 5 ticks
```

```
Episode — arm: temporal, seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: remember() -> that did not work
  tick 5: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 5 of 5 ticks
```

```
Episode — arm: temporal, seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: remember() -> that did not work
  tick 5: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 5 of 5 ticks
```

```
Episode — arm: temporal, seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: remember() -> that did not work
  tick 5: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 5 of 5 ticks
```

```
Episode — arm: temporal, seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: remember() -> that did not work
  tick 5: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 5 of 5 ticks
```

```
Episode — arm: temporal, seed 1042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: remember() -> that did not work
  tick 5: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 5 of 5 ticks
```

```
Episode — arm: temporal, seed 2042, chain box->jar->pond, target: black thread
  tick 1: remember() -> that did not work
  tick 2: remember() -> that did not work
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: look(box) -> a note: check the jar
  FAIL (budget) — depth 1/3, 5 of 5 ticks
```

```
Episode — arm: temporal, seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: remember() -> that did not work
  tick 2: remember() -> that did not work
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: look(cabinet) -> a note: check the box
  FAIL (budget) — depth 1/3, 5 of 5 ticks
```

```
Episode — arm: temporal, seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: remember() -> that did not work
  tick 2: remember() -> that did not work
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: look(chest) -> a note: check the drawer
  FAIL (budget) — depth 1/3, 5 of 5 ticks
```

```
Episode — arm: temporal, seed 2042, chain pond->box->shelf, target: gold bell
  tick 1: remember() -> that did not work
  tick 2: remember() -> that did not work
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: look(pond) -> a note: check the box
  FAIL (budget) — depth 1/3, 5 of 5 ticks
```

```
Episode — arm: temporal, seed 2042, chain drawer->box->basket, target: red stone
  tick 1: remember() -> that did not work
  tick 2: remember() -> that did not work
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: look(drawer) -> a note: check the box
  FAIL (budget) — depth 1/3, 5 of 5 ticks
```

```
Episode — arm: temporal, seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: remember() -> that did not work
  tick 2: remember() -> that did not work
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: look(shelf) -> a note: check the pond
  FAIL (budget) — depth 1/3, 5 of 5 ticks
```

```
Episode — arm: temporal, seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: remember() -> that did not work
  tick 2: remember() -> that did not work
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: look(cabinet) -> a note: check the drawer
  FAIL (budget) — depth 1/3, 5 of 5 ticks
```

```
Episode — arm: temporal, seed 2042, chain chest->cabinet->drawer, target: green leaf
  tick 1: remember() -> that did not work
  tick 2: remember() -> that did not work
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: look(chest) -> a note: check the cabinet
  FAIL (budget) — depth 1/3, 5 of 5 ticks
```

```
Episode — arm: temporal, seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: remember() -> that did not work
  tick 2: remember() -> that did not work
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: look(drawer) -> a note: check the basket
  FAIL (budget) — depth 1/3, 5 of 5 ticks
```

```
Episode — arm: temporal, seed 2042, chain jar->chest->basket, target: black thread
  tick 1: remember() -> that did not work
  tick 2: remember() -> that did not work
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: look(jar) -> a note: check the chest
  FAIL (budget) — depth 1/3, 5 of 5 ticks
```
