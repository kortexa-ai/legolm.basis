# g6-27b-door-test-at-scale-27b

Host machine `smarty`, device `cuda`, dtype `bfloat16`, host `Qwen/Qwen3.8-27B` @ `1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0`, budget 8, 3117.618 s (phase A 1354.784 s, phase B 1740.52 s). git `b9ce53dc40654ab319f9d5a688abf70db7d7f720`. Registration: tracks/goal-pursuit/PLAN.md, G6-27B registration — the door test at scale (2026-08-20).

**Scope.** symbol-following door by door on a frozen 27B: the G1 goal want through the residual BUS against the same want through the latent PREFIX, with G6's crossed probe and door-conflict cell. ONE bridge seed (s42) — chains x installed items are the replication axis and n=1 in the seed direction is the standing limitation. Nothing here cites GS.

## Reading

Precondition (text lift >= 0.50): **True** (text lift +1.00).

**Primary reading: none-of-the-registered-readings.**

| reading | rule | holds |
|---|---|---|
| i_scale_invariant | prefix lift >= 0.70 of text's AND bus lift <= 0.35 of text's | False |
| ii_bus_carries_nouns | bus lift >= 0.70 of text's | False |
| iii_graded | bus lift strictly between 0.35 and 0.70 of text's | False |
| iv_prefix_fails | prefix lift < 0.50 of text's | False |

Conflict: recorded either way; no threshold. Split-door: composes / interferes recorded against the 230M's 2042 signature (format breakdown: submissions stop and invalid actions appear while each door works alone); no threshold.

Note: (i) and (ii) are mutually exclusive on the bus ratio; (iv) is about the prefix and can hold beside either, so all four are recorded and the primary follows the registration's order.

## Doors

Source: trained in this run. Source layer 51, inject layers [19, 29, 40], dose 0.15, bus 256/16 positions, injection `conditioned`. Placement source: the GF-27B doors' recorded contract, taken as the registered prior; NO rescan (registration: the prior stands); agrees with the registration's numbers: True.

| arm | checkpoint | sha256 | pin source | verified |
|---|---|---|---|---|
| goal | `checkpoints/experiments/g6-goal-bridge-27b-s42.pt` | `8248eaf6fbd444e51bb8b3a2ab316ffcd7fe4bc713b3c7053eca533a4631109f` | written by this run | False |
| constant | `checkpoints/experiments/g6-constant-bridge-27b-s42.pt` | `f708fb8498fe061dfb44efe3ba09a73186bccbb9aa1da29606a3c5d7ab92074e` | written by this run | False |

## Phase A — the doors at 27B

Coherence gate rule: degenerate iff fewer than 10 distinct tokens or a word 3-gram repeated more than 4 times. Start dose 0.15, surviving dose 0.15 after 0 halving(s) of at most 3. The gate bridge is UNTRAINED: only `fit_source_statistics` ran on the train taps. The prompt, verbatim:

```text
You are on a small errand. Pick exactly one action as JSON. Allowed tools: look, open, done. Places: shelf, box, drawer, pond, cabinet, basket, chest, jar. Respond with exactly one compact JSON object and no markdown fences. Valid examples: {"tool":"look","args":{"place":"shelf"}} or {"tool":"open","args":{"place":"box"}} or {"tool":"done","args":{"item":"amber key"}}. done submits the item you retrieved and ends the errand.

So far:
1. You are at the shelf.

What do you do next? One JSON action.
```

### Coherence attempt 1 — dose 0.15 — PASS

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

run_g1's recipe reproduced at 27B by gf27b_bridge's machinery: the GOAL bridge (conditioned on the goal-assignment exchange, 8-way aux head on the bus) first and the CONSTANT bridge second on ONE rng stream, seed 42. G1's coin flip on the constant arm's goal text is KEPT (GF-27B dropped it because GF's world is goal-free).

192 steps, batch 8, lr 0.003, AdamW wd 0.0, grad clip 1.0, dose 0.15, injection `conditioned` at [19, 29, 40], seed 42.

Wall projection at step 8: 3.38 s/step -> 0.361 h for both bridges against a 10.0 h budget; steps 192 -> 192 (cut: False).

| bridge | step | loss | token accuracy | grad norm |
|---|---:|---:|---:|---:|
| goal | 1 | 3.4540 | 0.7881 | 13.3055 |
| goal | 32 | 2.1888 | 1.0000 | 5.8141 |
| goal | 64 | 1.2685 | 1.0000 | 3.8710 |
| goal | 96 | 3.5863 | 1.0000 | 3.5630 |
| goal | 128 | 0.0024 | 1.0000 | 0.0035 |
| goal | 160 | 0.0118 | 1.0000 | 0.0104 |
| goal | 192 | 0.0012 | 1.0000 | 0.0230 |
| constant | 1 | 1.3001 | 0.7983 | 10.6134 |
| constant | 32 | 0.0042 | 1.0000 | 0.0060 |
| constant | 64 | 0.0000 | 1.0000 | 0.0002 |
| constant | 96 | 0.0080 | 0.9926 | 0.0050 |
| constant | 128 | 0.0001 | 1.0000 | 0.0003 |
| constant | 160 | 0.0035 | 1.0000 | 0.0059 |
| constant | 192 | 0.0021 | 1.0000 | 0.0063 |

Goal bridge wall 649.238 s, constant bridge wall 650.144 s.

### Phase A gates

| gate | result |
|---|---|
| held-out phrasing token accuracy | 0.9939 over 240 pairs (exact 0.8958, by position {'8': 0.9931, '9': 0.9946}) |
| aux on the held-out taps (16 points, 8-way) | 7/16 |
| zero-dose bit-exactness | PASS |
| base weights byte-identical | PASS (goal True, constant True, doors True, end True) |

## Phase B — plumbing gates (before any arm; failure stops the run)

| gate | what | identical | prefix tokens |
|---|---|---|---:|
| a_no_prefix_zero_dose | no-prefix, fraction 0.0, hooks armed vs plain generate | True | 0 |
| b_prefixed_zero_dose | WITH the chain-0 goal prefix, fraction 0.0, hooks armed vs the same prefixed generate with no hooks | True | 8 |
| c_prefix_length_constant_across_arms | the per-INSTALLED-ITEM prefix length is constant across the prefix arms, so the injection placement is identical across them | True | one prefix tensor is embedded per installed item and reused by prefix-only and split-door; the arms differ only in the bus payload |

Rule: any gate failure stops the run before arms (registration, gate clause); the decode contract is the arms' own (greedy, enable_thinking=False, MAX_NEW 128).

### Injection placement

Armed by: relay_experiment.relay_injection -> MultiResidualInjection, one ResidualInjection per inject layer, position=-1, once=False, mode 'conditioned'. Layout `inputs_embeds = [goal prefix (P) ; prompt (L)]`. The prefill hook fires once and injects **1** position at index `P + L - 1` — the LAST token of the rendered chat prompt (the generation-prompt tail); positions 0..P-1 (the entire goal prefix) and P..P+L-2 are NOT injected. Prefix positions injected: 0. each KV-cached step takes start=0 over its single new position, so every generated token is injected. Bank offsets: 0 on the last prefill position, then 1, 2, ... per generated token, clamped at delta_positions-1 = 15; __enter__ resets the counter, so every generate call starts at 0. Prefix text rule: g6_splitdoor.installed_goal_line(item), verbatim and with NO separator, embedded through model.get_input_embeddings() — G6's text on GF-3's path, as registered.

Prefix tokens by installed item: {'black thread': 8, 'blue feather': 8, 'gold bell': 8, 'red stone': 8, 'green leaf': 8, 'amber key': 8, 'jade coin': 8, 'white shell': 8}.

### Decode contract (the eval line's, imported)

`enable_thinking=False` (template accepted the keyword: True, it changes the rendered prompt: True), MAX_NEW 128 against the errand's 64, greedy. Think-strip: closed <think>...</think> blocks removed (DOTALL); then a dangling </think> with no opener drops everything up to and including it; then an unclosed <think> drops everything from it to the end of the decode. Parser: gp.parse_model_action, the 230M's, unchanged.

| decodes | episode ticks | closed block | dangling close | dangling open | changed | empty after strip | invalid-output fallbacks | state echoes |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2508 | 2508 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Plain cells — the installed item is the chain's own

| arm | seed | success | depth | ticks | submit | guess | invalid | repeat |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| text | 42 | 1.00 | 3.00 | 5.2 | 1.00 | 0.00 | 0 | 0 |
| bus-only | 42 | 0.50 | 3.00 | 5.2 | 1.00 | 0.00 | 0 | 0 |
| prefix-only | 42 | 1.00 | 3.00 | 5.0 | 1.00 | 0.00 | 0 | 0 |
| split-door | 42 | 0.90 | 2.90 | 5.8 | 0.90 | 0.00 | 0 | 0 |

## Crossed probe — symbol following, door by door

| arm | seed | follow-installed (in pair) | follow-target (installed elsewhere) | follow-reveal-first | installed-dependent chains | submit rate | decided |
|---|---|---:|---:|---:|---:|---:|---:|
| text | 42 | 1.00 | 1.00 | 0.50 | 10 | 0.30 | 22 |
| bus-only | 42 | 0.50 | 0.45 | 0.57 | 0 | 0.94 | 75 |
| prefix-only | 42 | 1.00 | 0.50 | 0.50 | 10 | 0.33 | 26 |
| split-door | 42 | 1.00 | 0.00 | 0.39 | 9 | 0.29 | 23 |

## The causal cell — P(submit = distractor)

Over rows whose submit is one of the chain's two revealed items: p(submit = distractor | installed == distractor) minus p(submit = distractor | installed out of the pair).

| arm | installed = distractor | installed elsewhere | lift | z | ratio vs text | rows (distractor / elsewhere) |
|---|---:|---:|---:|---:|---:|---|
| text | 1.00 | 0.00 | +1.00 | +3.46 | 1.00 | 10 / 2 |
| bus-only | 0.50 | 0.55 | -0.05 | -0.27 | -0.05 | 10 / 55 |
| prefix-only | 1.00 | 0.50 | +0.50 | +2.48 | 0.50 | 10 / 6 |
| split-door | 1.00 | 1.00 | +0.00 | -- | 0.00 | 10 / 4 |

## Door conflict — split-door, the two doors disagree

| seed | episodes | prefix wins | bus wins | other | no submit |
|---|---:|---:|---:|---:|---:|
| 42 | 20 | 19 | 0 | 1 | 1 |

### By direction

| seed | direction | episodes | prefix | bus | other |
|---|---|---:|---:|---:|---:|
| 42 | prefix_names_target | 10 | 9 | 0 | 1 |
| 42 | prefix_names_distractor | 10 | 10 | 0 | 0 |

**Split-door status: recorded: neither composition nor the 2042 breakdown.** 2042 format-breakdown signature: False (split submission rate 0.9, invalid actions 0; bus-only submission 1.0, prefix-only 1.0). Split lift +0.00 against the better single door +0.50.


### Response surface — text, seed 42 (rows: chain target/distractor; columns: installed item; cell: submitted item, `*` = followed the installed item)

| chain (t/d) | ak | jc | gb | rs | bf | gl | bt | ws |
|---|---|---|---|---|---|---|---|---|
| bt/gl | -- | -- | -- | -- | -- | gl* | bt* | -- |
| bf/gb | -- | -- | gb* | -- | bf* | -- | -- | -- |
| bt/bf | -- | -- | -- | -- | bf* | -- | bt* | -- |
| gb/bf | gb | jc* | gb* | -- | bf* | -- | -- | -- |
| rs/bf | -- | -- | -- | rs* | bf* | -- | -- | -- |
| gb/bf | -- | -- | gb* | -- | bf* | -- | -- | -- |
| gb/bt | -- | -- | gb* | -- | -- | -- | bt* | -- |
| gl/ak | ak* | jc* | -- | -- | -- | gl* | -- | -- |
| ak/bt | ak* | -- | ak | -- | -- | -- | bt* | -- |
| bt/gb | -- | -- | gb* | -- | -- | -- | bt* | -- |

### Response surface — bus-only, seed 42 (rows: chain target/distractor; columns: installed item; cell: submitted item, `*` = followed the installed item)

| chain (t/d) | ak | jc | gb | rs | bf | gl | bt | ws |
|---|---|---|---|---|---|---|---|---|
| bt/gl | -- | -- | -- | -- | -- | bt | bt* | bt |
| bf/gb | bf | bf | bf | bf | bf* | bf | bf | bf |
| bt/bf | bf | bf | bf | bf | bf* | bf | bf | bf |
| gb/bf | bf | bf | bf | bf | bf* | bf | bf | bf |
| rs/bf | rs | rs | rs | rs* | rs | rs | rs | rs |
| gb/bf | bf | bf | bf | bf | bf* | bf | bf | bf |
| gb/bt | gb | gb | gb* | gb | gb | gb | gb | gb |
| gl/ak | ak* | ak | ak | ak | ak | ak | ak | ak |
| ak/bt | ak* | ak | ak | ak | ak | ak | ak | ak |
| bt/gb | gb | gb | gb* | gb | gb | gb | gb | gb |

### Response surface — prefix-only, seed 42 (rows: chain target/distractor; columns: installed item; cell: submitted item, `*` = followed the installed item)

| chain (t/d) | ak | jc | gb | rs | bf | gl | bt | ws |
|---|---|---|---|---|---|---|---|---|
| bt/gl | -- | -- | -- | -- | -- | gl* | bt* | -- |
| bf/gb | -- | -- | gb* | -- | bf* | -- | -- | -- |
| bt/bf | -- | -- | -- | -- | bf* | -- | bt* | -- |
| gb/bf | -- | -- | gb* | -- | bf* | -- | -- | -- |
| rs/bf | -- | -- | -- | rs* | bf* | -- | -- | -- |
| gb/bf | -- | -- | gb* | -- | bf* | -- | -- | -- |
| gb/bt | -- | -- | gb* | -- | -- | -- | bt* | -- |
| gl/ak | ak* | ak | ak | ak | -- | gl* | -- | -- |
| ak/bt | ak* | ak | ak | ak | -- | -- | bt* | -- |
| bt/gb | -- | -- | gb* | -- | -- | -- | bt* | -- |

### Response surface — split-door, seed 42 (rows: chain target/distractor; columns: installed item; cell: submitted item, `*` = followed the installed item)

| chain (t/d) | ak | jc | gb | rs | bf | gl | bt | ws |
|---|---|---|---|---|---|---|---|---|
| bt/gl | -- | -- | -- | -- | -- | gl* | -- | -- |
| bf/gb | -- | -- | gb* | -- | bf* | -- | -- | -- |
| bt/bf | -- | -- | -- | -- | bf* | -- | bt* | -- |
| gb/bf | -- | -- | gb* | -- | bf* | -- | -- | -- |
| rs/bf | -- | -- | -- | rs* | bf* | -- | -- | -- |
| gb/bf | -- | -- | gb* | -- | bf* | -- | -- | -- |
| gb/bt | -- | -- | gb* | -- | -- | -- | bt* | -- |
| gl/ak | ak* | ak | ak | ak | -- | gl* | -- | ak |
| ak/bt | ak* | -- | -- | -- | -- | -- | bt* | -- |
| bt/gb | -- | -- | gb* | -- | -- | -- | bt* | -- |

## Transcripts — plain cells

```
Episode — arm: text, seed 42, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: look(pond) -> the pond is closed; something is inside
  tick 4: open(pond) -> you find: black thread and green leaf
  tick 5: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: text, seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: open(box) -> empty
  tick 3: look(box) -> a note: try the pond
  tick 4: look(pond) -> the pond is closed; something is inside
  tick 5: open(pond) -> you find: blue feather and gold bell
  tick 6: done(blue feather) -> you submit: blue feather
  PASS — depth 3/3, 6 of 8 ticks
```

```
Episode — arm: text, seed 42, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: look(basket) -> the basket is closed; something is inside
  tick 4: open(basket) -> you find: black thread and blue feather
  tick 5: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: text, seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: open(box) -> empty
  tick 3: look(box) -> a note: try the shelf
  tick 4: look(shelf) -> the shelf is closed; something is inside
  tick 5: open(shelf) -> you find: blue feather and gold bell
  tick 6: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 6 of 8 ticks
```

```
Episode — arm: text, seed 42, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: open(box) -> empty
  tick 3: look(box) -> a note: try the basket
  tick 4: open(basket) -> you find: red stone and blue feather
  tick 5: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: text, seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: open(cabinet) -> you find: blue feather and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: text, seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: open(shelf) -> you find: black thread and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: text, seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: look(drawer) -> the drawer is closed; something is inside
  tick 4: open(drawer) -> you find: green leaf and amber key
  tick 5: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: text, seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: open(cabinet) -> you find: amber key and black thread
  tick 5: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: text, seed 42, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: open(chest) -> empty
  tick 3: look(chest) -> a note: try the basket
  tick 4: open(basket) -> you find: black thread and gold bell
  tick 5: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: bus-only, seed 42, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: look(pond) -> the pond is closed; something is inside
  tick 4: open(pond) -> you find: black thread and green leaf
  tick 5: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: bus-only, seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: open(box) -> empty
  tick 3: look(box) -> a note: try the pond
  tick 4: look(pond) -> the pond is closed; something is inside
  tick 5: open(pond) -> you find: blue feather and gold bell
  tick 6: done(blue feather) -> you submit: blue feather
  PASS — depth 3/3, 6 of 8 ticks
```

```
Episode — arm: bus-only, seed 42, chain chest->drawer->basket, target: black thread
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
Episode — arm: bus-only, seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: open(box) -> empty
  tick 3: look(box) -> a note: try the shelf
  tick 4: look(shelf) -> the shelf is closed; something is inside
  tick 5: open(shelf) -> you find: blue feather and gold bell
  tick 6: done(blue feather) -> you submit: blue feather
  FAIL (wrong submit) — depth 3/3, 6 of 8 ticks
```

```
Episode — arm: bus-only, seed 42, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: open(box) -> empty
  tick 3: look(box) -> a note: try the basket
  tick 4: open(basket) -> you find: red stone and blue feather
  tick 5: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: bus-only, seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(blue feather) -> you submit: blue feather
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: bus-only, seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: open(shelf) -> you find: black thread and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: bus-only, seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: open(chest) -> empty
  tick 2: look(shelf) -> nothing of note
  tick 3: look(box) -> nothing of note
  tick 4: look(drawer) -> the drawer is closed; something is inside
  tick 5: open(drawer) -> you find: green leaf and amber key
  tick 6: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 3/3, 6 of 8 ticks
```

```
Episode — arm: bus-only, seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: open(cabinet) -> you find: amber key and black thread
  tick 5: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: bus-only, seed 42, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: open(chest) -> empty
  tick 3: look(chest) -> a note: try the basket
  tick 4: open(basket) -> you find: black thread and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: prefix-only, seed 42, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: look(pond) -> the pond is closed; something is inside
  tick 4: open(pond) -> you find: black thread and green leaf
  tick 5: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: prefix-only, seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: look(pond) -> the pond is closed; something is inside
  tick 4: open(pond) -> you find: blue feather and gold bell
  tick 5: done(blue feather) -> you submit: blue feather
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: prefix-only, seed 42, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: look(basket) -> the basket is closed; something is inside
  tick 4: open(basket) -> you find: black thread and blue feather
  tick 5: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: prefix-only, seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: open(box) -> empty
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: open(shelf) -> you find: blue feather and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: prefix-only, seed 42, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: look(basket) -> the basket is closed; something is inside
  tick 4: open(basket) -> you find: red stone and blue feather
  tick 5: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: prefix-only, seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: open(cabinet) -> you find: blue feather and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: prefix-only, seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: open(shelf) -> you find: black thread and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: prefix-only, seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: look(drawer) -> the drawer is closed; something is inside
  tick 4: open(drawer) -> you find: green leaf and amber key
  tick 5: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: prefix-only, seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: open(cabinet) -> you find: amber key and black thread
  tick 5: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: prefix-only, seed 42, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: open(chest) -> empty
  tick 3: look(chest) -> a note: try the basket
  tick 4: open(basket) -> you find: black thread and gold bell
  tick 5: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: split-door, seed 42, chain box->jar->pond, target: black thread
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
Episode — arm: split-door, seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: look(pond) -> the pond is closed; something is inside
  tick 4: open(pond) -> you find: blue feather and gold bell
  tick 5: done(blue feather) -> you submit: blue feather
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: split-door, seed 42, chain chest->drawer->basket, target: black thread
  tick 1: open(chest) -> empty
  tick 2: look(shelf) -> nothing of note
  tick 3: look(box) -> nothing of note
  tick 4: look(drawer) -> a note: try the basket
  tick 5: look(basket) -> the basket is closed; something is inside
  tick 6: open(basket) -> you find: black thread and blue feather
  tick 7: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 7 of 8 ticks
```

```
Episode — arm: split-door, seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: open(box) -> empty
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: open(shelf) -> you find: blue feather and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: split-door, seed 42, chain drawer->box->basket, target: red stone
  tick 1: open(drawer) -> empty
  tick 2: look(shelf) -> nothing of note
  tick 3: look(box) -> a note: try the basket
  tick 4: look(basket) -> the basket is closed; something is inside
  tick 5: open(basket) -> you find: red stone and blue feather
  tick 6: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 6 of 8 ticks
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
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: open(shelf) -> you find: black thread and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: split-door, seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: open(chest) -> empty
  tick 2: look(shelf) -> nothing of note
  tick 3: look(basket) -> nothing of note
  tick 4: look(pond) -> nothing of note
  tick 5: look(box) -> nothing of note
  tick 6: look(cabinet) -> a note: try the drawer
  tick 7: open(drawer) -> you find: green leaf and amber key
  tick 8: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 8 of 8 ticks
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
  tick 1: open(jar) -> empty
  tick 2: look(shelf) -> nothing of note
  tick 3: look(box) -> nothing of note
  tick 4: look(drawer) -> nothing of note
  tick 5: look(cabinet) -> nothing of note
  tick 6: look(basket) -> the basket is closed; something is inside
  tick 7: open(basket) -> you find: black thread and gold bell
  tick 8: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 8 of 8 ticks
```


## Transcripts — door conflict

```
Episode — arm: conflict:prefix=black thread|bus=green leaf, seed 42, chain box->jar->pond, target: black thread
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
Episode — arm: conflict:prefix=green leaf|bus=black thread, seed 42, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: look(shelf) -> nothing of note
  tick 3: look(basket) -> nothing of note
  tick 4: look(drawer) -> nothing of note
  tick 5: look(cabinet) -> nothing of note
  tick 6: look(pond) -> the pond is closed; something is inside
  tick 7: open(pond) -> you find: black thread and green leaf
  tick 8: done(green leaf) -> you submit: green leaf
  FAIL (wrong submit) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: conflict:prefix=blue feather|bus=gold bell, seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: look(pond) -> the pond is closed; something is inside
  tick 4: open(pond) -> you find: blue feather and gold bell
  tick 5: done(blue feather) -> you submit: blue feather
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: conflict:prefix=gold bell|bus=blue feather, seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: look(pond) -> the pond is closed; something is inside
  tick 4: open(pond) -> you find: blue feather and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: conflict:prefix=black thread|bus=blue feather, seed 42, chain chest->drawer->basket, target: black thread
  tick 1: open(chest) -> empty
  tick 2: look(shelf) -> nothing of note
  tick 3: look(box) -> nothing of note
  tick 4: look(drawer) -> a note: try the basket
  tick 5: look(basket) -> the basket is closed; something is inside
  tick 6: open(basket) -> you find: black thread and blue feather
  tick 7: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 7 of 8 ticks
```

```
Episode — arm: conflict:prefix=blue feather|bus=black thread, seed 42, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: look(basket) -> the basket is closed; something is inside
  tick 4: open(basket) -> you find: black thread and blue feather
  tick 5: done(blue feather) -> you submit: blue feather
  FAIL (wrong submit) — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: conflict:prefix=gold bell|bus=blue feather, seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: open(box) -> empty
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: open(shelf) -> you find: blue feather and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: conflict:prefix=blue feather|bus=gold bell, seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: open(box) -> empty
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: open(shelf) -> you find: blue feather and gold bell
  tick 5: done(blue feather) -> you submit: blue feather
  FAIL (wrong submit) — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: conflict:prefix=red stone|bus=blue feather, seed 42, chain drawer->box->basket, target: red stone
  tick 1: open(drawer) -> empty
  tick 2: look(shelf) -> nothing of note
  tick 3: look(box) -> a note: try the basket
  tick 4: look(basket) -> the basket is closed; something is inside
  tick 5: open(basket) -> you find: red stone and blue feather
  tick 6: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 6 of 8 ticks
```

```
Episode — arm: conflict:prefix=blue feather|bus=red stone, seed 42, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: open(box) -> empty
  tick 3: look(shelf) -> nothing of note
  tick 4: look(cabinet) -> nothing of note
  tick 5: look(basket) -> the basket is closed; something is inside
  tick 6: open(basket) -> you find: red stone and blue feather
  tick 7: done(blue feather) -> you submit: blue feather
  FAIL (wrong submit) — depth 3/3, 7 of 8 ticks
```

```
Episode — arm: conflict:prefix=gold bell|bus=blue feather, seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: conflict:prefix=blue feather|bus=gold bell, seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(blue feather) -> you submit: blue feather
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: conflict:prefix=gold bell|bus=black thread, seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: open(shelf) -> you find: black thread and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: conflict:prefix=black thread|bus=gold bell, seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: open(shelf) -> you find: black thread and gold bell
  tick 5: done(black thread) -> you submit: black thread
  FAIL (wrong submit) — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: conflict:prefix=green leaf|bus=amber key, seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: open(chest) -> empty
  tick 2: look(shelf) -> nothing of note
  tick 3: look(box) -> nothing of note
  tick 4: look(drawer) -> the drawer is closed; something is inside
  tick 5: open(drawer) -> you find: green leaf and amber key
  tick 6: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 6 of 8 ticks
```

```
Episode — arm: conflict:prefix=amber key|bus=green leaf, seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: open(chest) -> empty
  tick 2: look(shelf) -> nothing of note
  tick 3: look(box) -> nothing of note
  tick 4: look(drawer) -> the drawer is closed; something is inside
  tick 5: open(drawer) -> you find: green leaf and amber key
  tick 6: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 3/3, 6 of 8 ticks
```

```
Episode — arm: conflict:prefix=amber key|bus=black thread, seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: conflict:prefix=black thread|bus=amber key, seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: open(drawer) -> empty
  tick 2: look(shelf) -> nothing of note
  tick 3: look(box) -> nothing of note
  tick 4: look(cabinet) -> the cabinet is closed; something is inside
  tick 5: open(cabinet) -> you find: amber key and black thread
  tick 6: done(black thread) -> you submit: black thread
  FAIL (wrong submit) — depth 3/3, 6 of 8 ticks
```

```
Episode — arm: conflict:prefix=black thread|bus=gold bell, seed 42, chain jar->chest->basket, target: black thread
  tick 1: open(jar) -> empty
  tick 2: look(shelf) -> nothing of note
  tick 3: look(box) -> nothing of note
  tick 4: look(drawer) -> nothing of note
  tick 5: look(cabinet) -> nothing of note
  tick 6: look(basket) -> the basket is closed; something is inside
  tick 7: open(basket) -> you find: black thread and gold bell
  tick 8: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: conflict:prefix=gold bell|bus=black thread, seed 42, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: open(chest) -> empty
  tick 3: look(chest) -> a note: try the basket
  tick 4: open(basket) -> you find: black thread and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 5 of 8 ticks
```

