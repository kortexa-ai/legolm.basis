# g3-serving-shape

Host `LiquidAI/LFM2.5-230M`, budget 8, 52.137 s.

| arm | seed | success | depth | ticks | submit | guess | invalid | repeat |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| oracle | decode | 1.00 | 3.00 | 4.0 | 1.00 | 0.00 | 0 | 0 |
| goal-text | decode | 0.00 | 0.00 | None | 0.00 | 0.00 | 3 | 67 |
| bare-serve-no-goal | decode | 0.00 | 0.00 | None | 0.00 | 0.00 | 0 | 70 |
| policy+goal-text | decode | 0.40 | 0.10 | 1.0 | 1.00 | 0.40 | 0 | 1 |
| policy-no-goal | decode | 0.10 | 0.00 | 1.0 | 1.00 | 0.10 | 0 | 0 |

## Transcripts

```
Episode — arm: oracle, seed decode, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: oracle, seed decode, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(blue feather) -> you submit: blue feather
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: oracle, seed decode, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: oracle, seed decode, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: oracle, seed decode, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: oracle, seed decode, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: oracle, seed decode, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: oracle, seed decode, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: oracle, seed decode, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: oracle, seed decode, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: goal-text, seed decode, chain box->jar->pond, target: black thread
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
Episode — arm: goal-text, seed decode, chain cabinet->box->pond, target: blue feather
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
Episode — arm: goal-text, seed decode, chain chest->drawer->basket, target: black thread
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: open(box) -> empty
  tick 5: open(box) -> empty
  tick 6: open(box) -> empty
  tick 7: open(box) -> empty
  tick 8: open(amber key) -> that is not a place here
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: goal-text, seed decode, chain pond->box->shelf, target: gold bell
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
Episode — arm: goal-text, seed decode, chain drawer->box->basket, target: red stone
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
Episode — arm: goal-text, seed decode, chain shelf->pond->cabinet, target: gold bell
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
Episode — arm: goal-text, seed decode, chain cabinet->drawer->shelf, target: gold bell
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
Episode — arm: goal-text, seed decode, chain chest->cabinet->drawer, target: green leaf
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: open(box) -> empty
  tick 5: open(box) -> empty
  tick 6: open(box) -> empty
  tick 7: open(box) -> empty
  tick 8: open(amber key) -> that is not a place here
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: goal-text, seed decode, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: goal-text, seed decode, chain jar->chest->basket, target: black thread
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: open(box) -> empty
  tick 5: open(box) -> empty
  tick 6: open(box) -> empty
  tick 7: open(box) -> empty
  tick 8: open(amber key) -> that is not a place here
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: bare-serve-no-goal, seed decode, chain box->jar->pond, target: black thread
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
Episode — arm: bare-serve-no-goal, seed decode, chain cabinet->box->pond, target: blue feather
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
Episode — arm: bare-serve-no-goal, seed decode, chain chest->drawer->basket, target: black thread
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
Episode — arm: bare-serve-no-goal, seed decode, chain pond->box->shelf, target: gold bell
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
Episode — arm: bare-serve-no-goal, seed decode, chain drawer->box->basket, target: red stone
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
Episode — arm: bare-serve-no-goal, seed decode, chain shelf->pond->cabinet, target: gold bell
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
Episode — arm: bare-serve-no-goal, seed decode, chain cabinet->drawer->shelf, target: gold bell
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
Episode — arm: bare-serve-no-goal, seed decode, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: bare-serve-no-goal, seed decode, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: bare-serve-no-goal, seed decode, chain jar->chest->basket, target: black thread
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
Episode — arm: policy+goal-text, seed decode, chain box->jar->pond, target: black thread
  tick 1: done(black thread) -> you submit: black thread
  PASS — depth 0/3, 1 of 8 ticks, guessed
```

```
Episode — arm: policy+goal-text, seed decode, chain cabinet->box->pond, target: blue feather
  tick 1: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 1 of 8 ticks
```

```
Episode — arm: policy+goal-text, seed decode, chain chest->drawer->basket, target: black thread
  tick 1: done(black thread) -> you submit: black thread
  PASS — depth 0/3, 1 of 8 ticks, guessed
```

```
Episode — arm: policy+goal-text, seed decode, chain pond->box->shelf, target: gold bell
  tick 1: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 1 of 8 ticks
```

```
Episode — arm: policy+goal-text, seed decode, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(drawer) -> a note: check the box
  tick 3: open(box) -> empty
  tick 4: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 1/3, 4 of 8 ticks
```

```
Episode — arm: policy+goal-text, seed decode, chain shelf->pond->cabinet, target: gold bell
  tick 1: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 1 of 8 ticks
```

```
Episode — arm: policy+goal-text, seed decode, chain cabinet->drawer->shelf, target: gold bell
  tick 1: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 1 of 8 ticks
```

```
Episode — arm: policy+goal-text, seed decode, chain chest->cabinet->drawer, target: green leaf
  tick 1: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 1 of 8 ticks
```

```
Episode — arm: policy+goal-text, seed decode, chain drawer->basket->cabinet, target: amber key
  tick 1: done(amber key) -> you submit: amber key
  PASS — depth 0/3, 1 of 8 ticks, guessed
```

```
Episode — arm: policy+goal-text, seed decode, chain jar->chest->basket, target: black thread
  tick 1: done(black thread) -> you submit: black thread
  PASS — depth 0/3, 1 of 8 ticks, guessed
```

```
Episode — arm: policy-no-goal, seed decode, chain box->jar->pond, target: black thread
  tick 1: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 1 of 8 ticks
```

```
Episode — arm: policy-no-goal, seed decode, chain cabinet->box->pond, target: blue feather
  tick 1: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 1 of 8 ticks
```

```
Episode — arm: policy-no-goal, seed decode, chain chest->drawer->basket, target: black thread
  tick 1: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 1 of 8 ticks
```

```
Episode — arm: policy-no-goal, seed decode, chain pond->box->shelf, target: gold bell
  tick 1: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 1 of 8 ticks
```

```
Episode — arm: policy-no-goal, seed decode, chain drawer->box->basket, target: red stone
  tick 1: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 1 of 8 ticks
```

```
Episode — arm: policy-no-goal, seed decode, chain shelf->pond->cabinet, target: gold bell
  tick 1: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 1 of 8 ticks
```

```
Episode — arm: policy-no-goal, seed decode, chain cabinet->drawer->shelf, target: gold bell
  tick 1: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 1 of 8 ticks
```

```
Episode — arm: policy-no-goal, seed decode, chain chest->cabinet->drawer, target: green leaf
  tick 1: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 1 of 8 ticks
```

```
Episode — arm: policy-no-goal, seed decode, chain drawer->basket->cabinet, target: amber key
  tick 1: done(amber key) -> you submit: amber key
  PASS — depth 0/3, 1 of 8 ticks, guessed
```

```
Episode — arm: policy-no-goal, seed decode, chain jar->chest->basket, target: black thread
  tick 1: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 1 of 8 ticks
```
