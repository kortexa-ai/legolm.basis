# gf3-wants-with-style-27b

Host machine `smarty`, device `cuda`, dtype `bfloat16`, budget 8, 134.592 s. Registration: tracks/goal-pursuit/PLAN.md, GF-3 parameter registration — wants with style, at 27B native (2026-08-16 evening).

**Scope.** the split-door composition at 27B on the s42 doors: the goal line through the latent prefix and the focus packet through the bus, in one generate call; one bridge seed, ten eval chains as the replication axis.

## Doors

| arm | checkpoint | sha256 (as loaded) | pin verified |
|---|---|---|---|
| focus | `checkpoints/experiments/gf-focus-bridge-27b-s42.pt` | `ca951c55f3ee92b464ced526d084437fdb1be198faa2c78fe1ea9089a9eedb02` | True |
| constant | `checkpoints/experiments/gf-constant-bridge-27b-s42.pt` | `63538c124011388c714c780c927a5d6ba3c74b5c5535f7a7ad28dedd3a6a99ae` | True |

Source layer 51, inject layers [19, 29, 40], dose 0.15, bus 256/16 positions, injection `conditioned` — read from the s42 checkpoint pair's own headers; agrees with the registration's recorded numbers: True.

Pins from `findings/goal-pursuit-gf-27b-bridge.json`; verified before any decode: True. Loader: gf27b_eval.load_door / door_contract / check_host_against_doors, imported verbatim — sha256 pins, header contract, and the source-statistics assertion. Source statistics: loaded with the state dict (LatentBridge registers source_center/source_scale as persistent buffers); never refit here.

## The prefix door

G5a's/G6's latent prefix: gp.goal_line(chain) + '\n\n' embedded through model.get_input_embeddings() and prepended to the GOAL-FREE prompt's embeddings; gp.run_episode is called with goal_text=None in every arm and the decider asserts it. nothing trains against prefix-formatted inputs; the doors were trained on token-id prompts.

## Injection placement (registered gate (c))

Armed by: relay_experiment.relay_injection -> MultiResidualInjection, one ResidualInjection per inject layer, position=-1, once=False, mode 'conditioned'. Read from: mom_bridge.ResidualInjection._hook (mode 'conditioned'), lines 459-460 (zero-dose early return), 470-484 (start index and bank offsets) and 547-550 (__enter__ resets next_offset).

Layout `inputs_embeds = [goal prefix (P) ; prompt (L)]`. The prefill hook fires once and injects **1** position at index `P + L - 1` — the LAST token of the rendered chat prompt (the generation-prompt tail); positions 0..P-1 (the entire goal prefix) and P..P+L-2 are NOT injected. Prefix positions injected: 0. each KV-cached step takes start=0 over its single new position, so every generated token is injected.

Bank offsets: 0 on the last prefill position, then 1, 2, ... per generated token, clamped at delta_positions-1 = 15; __enter__ resets the counter, so every generate call starts at 0. Effect of the prefix length: P shifts the ABSOLUTE index of the injection point by exactly P and changes nothing else: not the relative placement (always the last prefill position), not the bank-offset schedule, not the count of injected positions. Zero dose: at fraction 0.0 the hook returns the layer output before it reads the residual (mom_bridge.py:459-460) — the property gates (a) and (b) test.

Identical across arms: the three arms differ only in the payload; the prefix is one cached tensor per chain, reused by every arm, so P is a property of the chain alone and the placement is identical across arms by construction.

## Plumbing gates (run before any arm; failure stops the run)

| gate | what | identical | prefix tokens |
|---|---|---|---:|
| a_no_prefix_zero_dose | no-prefix, fraction 0.0, hooks armed vs plain generate | True | 0 |
| b_prefixed_zero_dose | WITH the chain-0 goal prefix, fraction 0.0, hooks armed vs the same prefixed generate with no hooks | True | 9 |
| c_prefix_length_constant_across_arms | the per-chain prefix length is constant across arms, so the injection placement is identical across arms | True | one prefix tensor is embedded per chain and reused by all three arms; the arms differ only in the bus payload |

Rule: any gate failure stops the run before arms (registration, gate clause); the decode contract is the arms' own (greedy, enable_thinking=False, MAX_NEW 128).

## Decode adaptations (the eval's, imported)

`enable_thinking=False` (template accepted the keyword: True, it changes the rendered prompt: True), MAX_NEW 128 against the errand's 64, greedy. Think-strip: closed <think>...</think> blocks removed (DOTALL); then a dangling </think> with no opener drops everything up to and including it; then an unclosed <think> drops everything from it to the end of the decode. Parser: gp.parse_model_action, the 230M's, unchanged. Generation return: with inputs_embeds and no input_ids, HF returns ONLY the generated ids, so generate_prefixed_with_packet slices nothing off the front.

| think-strip | decodes | closed block | dangling close | dangling open | changed | empty after strip |
|---|---:|---:|---:|---:|---:|---:|
| all arms | 173 | 0 | 0 | 0 | 0 | 0 |

## Headline — success, finish tick, tool mix

`prefix-only` is the composition baseline: the goal prefix with the CONSTANT (drive) packet. The mix columns are pooled shares over all decision points; the first-tick columns are shares over the arm's ten episodes.

| arm | packet | success | successes | mean finish tick | look | open | done | other |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| prefix-only | constant (drive) | 0.90 | 9 | 5.11 | 0.63 | 0.20 | 0.17 | 0.00 |
| prefix-look | look | 1.00 | 10 | 5.60 | 0.64 | 0.18 | 0.18 | 0.00 |
| prefix-open | open | 0.80 | 8 | 5.88 | 0.17 | 0.70 | 0.13 | 0.00 |

### First tick

| arm | look | open | done | other |
|---|---:|---:|---:|---:|
| prefix-only | 0.80 | 0.20 | 0.00 | 0.00 |
| prefix-look | 1.00 | 0.00 | 0.00 | 0.00 |
| prefix-open | 0.20 | 0.80 | 0.00 | 0.00 |

## Paired per chain against prefix-only

Success: helps = the packet arm succeeded where prefix-only failed, hurts = the reverse. The ticks-to-success delta is signed (packet arm minus prefix-only) and NULL whenever either arm failed the chain.

| arm | helps | hurts | same | both succeeded | mean ticks delta |
|---|---:|---:|---:|---:|---:|
| prefix-look | 1 | 0 | 9 | 9 | 0.44 |
| prefix-open | 0 | 1 | 9 | 8 | 0.75 |

### prefix-look vs prefix-only, chain by chain

| chain | target | packet | baseline | outcome | packet ticks | baseline ticks | delta | packet submit | baseline submit |
|---|---|---|---|---|---:|---:|---:|---|---|
| box-jar-pond-black_thread | black thread | True | False | helps | 6 | 8 | -- | black thread | None |
| cabinet-box-pond-blue_feather | blue feather | True | True | same | 6 | 5 | +1 | blue feather | blue feather |
| chest-drawer-basket-black_thread | black thread | True | True | same | 6 | 5 | +1 | black thread | black thread |
| pond-box-shelf-gold_bell | gold bell | True | True | same | 5 | 5 | +0 | gold bell | gold bell |
| drawer-box-basket-red_stone | red stone | True | True | same | 6 | 5 | +1 | red stone | red stone |
| shelf-pond-cabinet-gold_bell | gold bell | True | True | same | 5 | 5 | +0 | gold bell | gold bell |
| cabinet-drawer-shelf-gold_bell | gold bell | True | True | same | 6 | 5 | +1 | gold bell | gold bell |
| chest-cabinet-drawer-green_leaf | green leaf | True | True | same | 5 | 6 | -1 | green leaf | green leaf |
| drawer-basket-cabinet-amber_key | amber key | True | True | same | 5 | 5 | +0 | amber key | amber key |
| jar-chest-basket-black_thread | black thread | True | True | same | 6 | 5 | +1 | black thread | black thread |

### prefix-open vs prefix-only, chain by chain

| chain | target | packet | baseline | outcome | packet ticks | baseline ticks | delta | packet submit | baseline submit |
|---|---|---|---|---|---:|---:|---:|---|---|
| box-jar-pond-black_thread | black thread | False | False | same | 8 | 8 | -- | None | None |
| cabinet-box-pond-blue_feather | blue feather | False | True | hurts | 8 | 5 | -- | None | blue feather |
| chest-drawer-basket-black_thread | black thread | True | True | same | 7 | 5 | +2 | black thread | black thread |
| pond-box-shelf-gold_bell | gold bell | True | True | same | 5 | 5 | +0 | gold bell | gold bell |
| drawer-box-basket-red_stone | red stone | True | True | same | 7 | 5 | +2 | red stone | red stone |
| shelf-pond-cabinet-gold_bell | gold bell | True | True | same | 6 | 5 | +1 | gold bell | gold bell |
| cabinet-drawer-shelf-gold_bell | gold bell | True | True | same | 4 | 5 | -1 | gold bell | gold bell |
| chest-cabinet-drawer-green_leaf | green leaf | True | True | same | 5 | 6 | -1 | green leaf | green leaf |
| drawer-basket-cabinet-amber_key | amber key | True | True | same | 5 | 5 | +0 | amber key | amber key |
| jar-chest-basket-black_thread | black thread | True | True | same | 8 | 5 | +3 | black thread | black thread |

## Transcripts

Every episode, in the order it ran. The goal never appears in any prompt: it is resident in the latent prefix.

```
Episode — arm: prefix-only [constant], seed 42, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: look(shelf) -> nothing of note
  tick 3: look(drawer) -> nothing of note
  tick 4: look(basket) -> nothing of note
  tick 5: look(cabinet) -> nothing of note
  tick 6: look(chest) -> nothing of note
  tick 7: look(jar) -> a note: try the pond
  tick 8: look(pond) -> the pond is closed; something is inside
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: prefix-only [constant], seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: look(pond) -> the pond is closed; something is inside
  tick 4: open(pond) -> you find: blue feather and gold bell
  tick 5: done(blue feather) -> you submit: blue feather
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: prefix-only [constant], seed 42, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: look(basket) -> the basket is closed; something is inside
  tick 4: open(basket) -> you find: black thread and blue feather
  tick 5: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: prefix-only [constant], seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: open(shelf) -> you find: blue feather and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: prefix-only [constant], seed 42, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: look(basket) -> the basket is closed; something is inside
  tick 4: open(basket) -> you find: red stone and blue feather
  tick 5: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: prefix-only [constant], seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: open(cabinet) -> you find: blue feather and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: prefix-only [constant], seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: open(shelf) -> you find: black thread and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: prefix-only [constant], seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: open(chest) -> empty
  tick 2: look(shelf) -> nothing of note
  tick 3: look(box) -> nothing of note
  tick 4: look(drawer) -> the drawer is closed; something is inside
  tick 5: open(drawer) -> you find: green leaf and amber key
  tick 6: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 6 of 8 ticks
```

```
Episode — arm: prefix-only [constant], seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: open(cabinet) -> you find: amber key and black thread
  tick 5: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: prefix-only [constant], seed 42, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: look(basket) -> the basket is closed; something is inside
  tick 4: open(basket) -> you find: black thread and gold bell
  tick 5: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: prefix-look [look], seed 42, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: look(pond) -> the pond is closed; something is inside
  tick 4: look(pond) -> the pond is closed; something is inside
  tick 5: open(pond) -> you find: black thread and green leaf
  tick 6: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 6 of 8 ticks
```

```
Episode — arm: prefix-look [look], seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: look(pond) -> the pond is closed; something is inside
  tick 4: look(pond) -> the pond is closed; something is inside
  tick 5: open(pond) -> you find: blue feather and gold bell
  tick 6: done(blue feather) -> you submit: blue feather
  PASS — depth 3/3, 6 of 8 ticks
```

```
Episode — arm: prefix-look [look], seed 42, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: look(basket) -> the basket is closed; something is inside
  tick 4: look(basket) -> the basket is closed; something is inside
  tick 5: open(basket) -> you find: black thread and blue feather
  tick 6: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 6 of 8 ticks
```

```
Episode — arm: prefix-look [look], seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: open(shelf) -> you find: blue feather and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: prefix-look [look], seed 42, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: look(basket) -> the basket is closed; something is inside
  tick 4: look(basket) -> the basket is closed; something is inside
  tick 5: open(basket) -> you find: red stone and blue feather
  tick 6: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 6 of 8 ticks
```

```
Episode — arm: prefix-look [look], seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: open(cabinet) -> you find: blue feather and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: prefix-look [look], seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: look(shelf) -> the shelf is closed; something is inside
  tick 5: open(shelf) -> you find: black thread and gold bell
  tick 6: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 6 of 8 ticks
```

```
Episode — arm: prefix-look [look], seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: look(drawer) -> the drawer is closed; something is inside
  tick 4: open(drawer) -> you find: green leaf and amber key
  tick 5: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: prefix-look [look], seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: open(cabinet) -> you find: amber key and black thread
  tick 5: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: prefix-look [look], seed 42, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: look(basket) -> the basket is closed; something is inside
  tick 4: look(basket) -> the basket is closed; something is inside
  tick 5: open(basket) -> you find: black thread and gold bell
  tick 6: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 6 of 8 ticks
```

```
Episode — arm: prefix-open [open], seed 42, chain box->jar->pond, target: black thread
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
Episode — arm: prefix-open [open], seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: open(cabinet) -> empty
  tick 2: look(shelf) -> nothing of note
  tick 3: open(box) -> empty
  tick 4: open(drawer) -> empty
  tick 5: open(chest) -> empty
  tick 6: open(basket) -> empty
  tick 7: open(jar) -> empty
  tick 8: open(pond) -> you find: blue feather and gold bell
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: prefix-open [open], seed 42, chain chest->drawer->basket, target: black thread
  tick 1: open(chest) -> empty
  tick 2: look(shelf) -> nothing of note
  tick 3: open(box) -> empty
  tick 4: open(drawer) -> empty
  tick 5: open(cabinet) -> empty
  tick 6: open(basket) -> you find: black thread and blue feather
  tick 7: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 7 of 8 ticks
```

```
Episode — arm: prefix-open [open], seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: open(box) -> empty
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: open(shelf) -> you find: blue feather and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: prefix-open [open], seed 42, chain drawer->box->basket, target: red stone
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
Episode — arm: prefix-open [open], seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: open(pond) -> empty
  tick 3: open(box) -> empty
  tick 4: open(drawer) -> empty
  tick 5: open(cabinet) -> you find: blue feather and gold bell
  tick 6: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 6 of 8 ticks
```

```
Episode — arm: prefix-open [open], seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: open(cabinet) -> empty
  tick 2: look(shelf) -> the shelf is closed; something is inside
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-open [open], seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: open(chest) -> empty
  tick 2: look(shelf) -> nothing of note
  tick 3: open(box) -> empty
  tick 4: open(drawer) -> you find: green leaf and amber key
  tick 5: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: prefix-open [open], seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: open(drawer) -> empty
  tick 2: look(shelf) -> nothing of note
  tick 3: open(box) -> empty
  tick 4: open(cabinet) -> you find: amber key and black thread
  tick 5: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: prefix-open [open], seed 42, chain jar->chest->basket, target: black thread
  tick 1: open(jar) -> empty
  tick 2: look(shelf) -> nothing of note
  tick 3: open(box) -> empty
  tick 4: open(drawer) -> empty
  tick 5: open(cabinet) -> empty
  tick 6: open(chest) -> empty
  tick 7: open(basket) -> you find: black thread and gold bell
  tick 8: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 8 of 8 ticks
```

