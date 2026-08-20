# gf3r-two-door-composition-230m

Host machine `smarty`, device `cuda`, dtype `bfloat16`, budget 8, 187.352 s. Registration: tracks/goal-pursuit/PLAN.md, GF-3r registration — the replication arm at 230M: does the two-door composition need scale, or just a lean? (2026-08-20 morning).

**Scope.** the split-door composition at 230M on bridges trained in process per seed: the chain's goal line through G6's latent prefix and the focus packet through the bus, in one generate call, under GF-2b's payload-space lean (alpha 0.25) and under the unmixed grip (alpha 1); 3 bridge seed(s) x 10 eval chains. Nothing here cites GS.

## The two doors

G6's prefix-only door verbatim: g6_splitdoor.installed_goal_line(chain['item']) embedded through model.get_input_embeddings() (g5_referent.embed_ids) and prepended to the GOAL-FREE prompt's embeddings; gp.run_episode is called with goal_text=None in every arm and the decider asserts it. nothing trains against prefix-formatted inputs; both bridges were trained on token-id prompts. GF-3 at 27B prefixed gp.goal_line(chain) + '\n\n'; G6 prefixed the bare goal line, and the registration pins G6's mechanism, so GF-3r carries no trailing blank line.

Bus: the focus + constant bridge pair trained per seed by GF's recipe (192 steps, batch 8, lr 0.003, train dose 0.15), delivered at the fixed dose 0.15 into layers [4, 6, 8] from the tap at layer 12; the mix is GF-2b's `payload` locus at alpha 0.25 (lean) and 1 (grip).

Armed block: `self-LFM230M-r4-dream4.pt` — gp.load_armed_host — the 230M production stack: frozen host, rank-4 attn LoRA, the dream4 self-block injected at the constant state (GF's and GF-2b's own code path).

Memory gate: required 20.0 GiB free, applied: True.

## Payload identities (checked before any arm decodes)

alpha 1.0 must reproduce the unmixed focus packet exactly and alpha 0.0 must reproduce the constant bridge's plain delivery exactly; the lean packet must differ from BOTH the constant packet and the grip packet. All four are checked at every held-out phrasing of both focuses, and a failure stops the run.

| seed | check | must be | exact | max abs difference |
|---|---|---|---|---:|
| 42 | grip_alpha1_equals_unmixed_look_8 | identical | True | 0 |
| 42 | constant_equals_alpha0_mix_look_8 | identical | True | 0 |
| 42 | grip_alpha1_equals_unmixed_look_9 | identical | True | 0 |
| 42 | constant_equals_alpha0_mix_look_9 | identical | True | 0 |
| 42 | grip_alpha1_equals_unmixed_open_8 | identical | True | 0 |
| 42 | constant_equals_alpha0_mix_open_8 | identical | True | 0 |
| 42 | grip_alpha1_equals_unmixed_open_9 | identical | True | 0 |
| 42 | constant_equals_alpha0_mix_open_9 | identical | True | 0 |
| 42 | lean_differs_from_constant_look_8 | different | False | 6.24 |
| 42 | lean_differs_from_grip_look_8 | different | False | 18.7 |
| 42 | lean_differs_from_constant_look_9 | different | False | 5.91 |
| 42 | lean_differs_from_grip_look_9 | different | False | 17.7 |
| 42 | lean_differs_from_constant_open_8 | different | False | 4.82 |
| 42 | lean_differs_from_grip_open_8 | different | False | 14.5 |
| 42 | lean_differs_from_constant_open_9 | different | False | 2.12 |
| 42 | lean_differs_from_grip_open_9 | different | False | 6.36 |
| 1042 | grip_alpha1_equals_unmixed_look_8 | identical | True | 0 |
| 1042 | constant_equals_alpha0_mix_look_8 | identical | True | 0 |
| 1042 | grip_alpha1_equals_unmixed_look_9 | identical | True | 0 |
| 1042 | constant_equals_alpha0_mix_look_9 | identical | True | 0 |
| 1042 | grip_alpha1_equals_unmixed_open_8 | identical | True | 0 |
| 1042 | constant_equals_alpha0_mix_open_8 | identical | True | 0 |
| 1042 | grip_alpha1_equals_unmixed_open_9 | identical | True | 0 |
| 1042 | constant_equals_alpha0_mix_open_9 | identical | True | 0 |
| 1042 | lean_differs_from_constant_look_8 | different | False | 9.43 |
| 1042 | lean_differs_from_grip_look_8 | different | False | 28.3 |
| 1042 | lean_differs_from_constant_look_9 | different | False | 6.58 |
| 1042 | lean_differs_from_grip_look_9 | different | False | 19.7 |
| 1042 | lean_differs_from_constant_open_8 | different | False | 5.63 |
| 1042 | lean_differs_from_grip_open_8 | different | False | 16.9 |
| 1042 | lean_differs_from_constant_open_9 | different | False | 4.06 |
| 1042 | lean_differs_from_grip_open_9 | different | False | 12.2 |
| 2042 | grip_alpha1_equals_unmixed_look_8 | identical | True | 0 |
| 2042 | constant_equals_alpha0_mix_look_8 | identical | True | 0 |
| 2042 | grip_alpha1_equals_unmixed_look_9 | identical | True | 0 |
| 2042 | constant_equals_alpha0_mix_look_9 | identical | True | 0 |
| 2042 | grip_alpha1_equals_unmixed_open_8 | identical | True | 0 |
| 2042 | constant_equals_alpha0_mix_open_8 | identical | True | 0 |
| 2042 | grip_alpha1_equals_unmixed_open_9 | identical | True | 0 |
| 2042 | constant_equals_alpha0_mix_open_9 | identical | True | 0 |
| 2042 | lean_differs_from_constant_look_8 | different | False | 6.26 |
| 2042 | lean_differs_from_grip_look_8 | different | False | 18.8 |
| 2042 | lean_differs_from_constant_look_9 | different | False | 4.68 |
| 2042 | lean_differs_from_grip_look_9 | different | False | 14 |
| 2042 | lean_differs_from_constant_open_8 | different | False | 8.23 |
| 2042 | lean_differs_from_grip_open_8 | different | False | 24.7 |
| 2042 | lean_differs_from_constant_open_9 | different | False | 5.29 |
| 2042 | lean_differs_from_grip_open_9 | different | False | 15.9 |

## Plumbing gates (run before each seed's arms; failure stops the run)

| seed | gate | what | identical | prefix tokens |
|---|---|---|---|---:|
| 42 | a_no_prefix_zero_dose | no-prefix, fraction 0.0, hooks armed vs plain generate | True | 0 |
| 42 | b_prefixed_zero_dose | WITH the chain-0 goal prefix, fraction 0.0, hooks armed vs the same prefixed generate with no hooks | True | 9 |
| 1042 | a_no_prefix_zero_dose | no-prefix, fraction 0.0, hooks armed vs plain generate | True | 0 |
| 1042 | b_prefixed_zero_dose | WITH the chain-0 goal prefix, fraction 0.0, hooks armed vs the same prefixed generate with no hooks | True | 9 |
| 2042 | a_no_prefix_zero_dose | no-prefix, fraction 0.0, hooks armed vs plain generate | True | 0 |
| 2042 | b_prefixed_zero_dose | WITH the chain-0 goal prefix, fraction 0.0, hooks armed vs the same prefixed generate with no hooks | True | 9 |
| all | c_prefix_length_constant_across_arms | the per-chain prefix length is constant across arms, so the injection placement is identical across arms | True | one prefix tensor is embedded per chain and reused by all five arms at every seed; the arms differ only in the bus payload |

Rule: any gate failure stops the run before arms (registration, gate clause); the decode contract is the arms' own (greedy, no think-strip, MAX_NEW 64).

Base weights unchanged at every seed: True.

## Injection placement (registered gate (c))

Armed by: relay_experiment.relay_injection -> MultiResidualInjection, one ResidualInjection per inject layer, position=-1, once=False, mode 'conditioned', layers [4, 6, 8]. Read from: mom_bridge.ResidualInjection._hook (mode 'conditioned'): the zero-dose early return, the start index and bank offsets under 'positional'/'conditioned', and __enter__'s reset of next_offset.

Layout `inputs_embeds = [goal prefix (P) ; prompt (L)]`. The prefill hook fires once and injects **1** position at index `P + L - 1` — the LAST token of the rendered chat prompt (the generation-prompt tail); positions 0..P-1 (the entire goal prefix) and P..P+L-2 are NOT injected. Prefix positions injected: 0. each KV-cached step takes start=0 over its single new position, so every generated token is injected.

Bank offsets: 0 on the last prefill position, then 1, 2, ... per generated token, clamped at delta_positions-1 = 15; __enter__ resets the counter, so every generate call starts at 0. Effect of the prefix length: P shifts the ABSOLUTE index of the injection point by exactly P and changes nothing else: not the relative placement (always the last prefill position), not the bank-offset schedule, not the count of injected positions. Zero dose: at fraction 0.0 the hook returns the layer output before it reads the residual — the property gates (a) and (b) test.

Identical across arms: the five arms differ only in the payload; the prefix is one cached tensor per chain, reused by every arm, so P is a property of the chain alone and the placement is identical across arms by construction.

Where the mix lands: the payload arms hand the hook a MixedConditionedPayload, which evaluates BOTH bound receivers on the same state and offsets and returns alpha*focus + (1-alpha)*constant BEFORE the injection normalizes the delta to a direction and rescales it by the position's own residual norm — so alpha turns what the packet SAYS, never how loudly, and the delivered dose is 0.15 at every alpha.

## Headline — success, finish tick, tool mix

`prefix-only` is the composition baseline: the goal prefix with the CONSTANT (drive) packet. The mix columns are pooled shares over all decision points; the first-tick columns are shares over the cell's episodes.

| arm | packet | alpha | seed | success | successes | mean finish tick | invalid | look | open | done | other |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| prefix-only | constant (drive) | 0 | 42 | 0.70 | 7 | 4.00 | 0 | 0.50 | 0.25 | 0.25 | 0.00 |
| prefix-only | constant (drive) | 0 | 1042 | 0.80 | 8 | 4.25 | 4 | 0.48 | 0.19 | 0.24 | 0.10 |
| prefix-only | constant (drive) | 0 | 2042 | 0.40 | 4 | 4.00 | 0 | 0.50 | 0.25 | 0.25 | 0.00 |
| prefix-only | constant (drive) | 0 | pooled | 0.63 | 19 | 4.11 | 4 | 0.49 | 0.23 | 0.25 | 0.03 |
| prefix-look-lean | look | 0.25 | 42 | 0.40 | 4 | 5.25 | 0 | 0.61 | 0.24 | 0.15 | 0.00 |
| prefix-look-lean | look | 0.25 | 1042 | 0.10 | 1 | 4.00 | 19 | 0.56 | 0.14 | 0.04 | 0.26 |
| prefix-look-lean | look | 0.25 | 2042 | 0.50 | 5 | 4.00 | 3 | 0.50 | 0.23 | 0.20 | 0.07 |
| prefix-look-lean | look | 0.25 | pooled | 0.33 | 10 | 4.50 | 22 | 0.56 | 0.19 | 0.12 | 0.13 |
| prefix-open-lean | open | 0.25 | 42 | 0.70 | 7 | 4.00 | 0 | 0.50 | 0.25 | 0.25 | 0.00 |
| prefix-open-lean | open | 0.25 | 1042 | 0.20 | 2 | 5.00 | 9 | 0.40 | 0.23 | 0.19 | 0.19 |
| prefix-open-lean | open | 0.25 | 2042 | 0.30 | 3 | 4.00 | 0 | 0.49 | 0.26 | 0.26 | 0.00 |
| prefix-open-lean | open | 0.25 | pooled | 0.40 | 12 | 4.17 | 9 | 0.46 | 0.24 | 0.23 | 0.07 |
| prefix-look-grip | look | 1 | 42 | 0.00 | 0 | -- | 0 | 1.00 | 0.00 | 0.00 | 0.00 |
| prefix-look-grip | look | 1 | 1042 | 0.00 | 0 | -- | 11 | 0.86 | 0.00 | 0.00 | 0.14 |
| prefix-look-grip | look | 1 | 2042 | 0.00 | 0 | -- | 0 | 1.00 | 0.00 | 0.00 | 0.00 |
| prefix-look-grip | look | 1 | pooled | 0.00 | 0 | -- | 11 | 0.95 | 0.00 | 0.00 | 0.05 |
| prefix-open-grip | open | 1 | 42 | 0.00 | 0 | -- | 31 | 0.00 | 0.96 | 0.01 | 0.03 |
| prefix-open-grip | open | 1 | 1042 | 0.00 | 0 | -- | 24 | 0.00 | 0.97 | 0.00 | 0.03 |
| prefix-open-grip | open | 1 | 2042 | 0.10 | 1 | 3.00 | 9 | 0.17 | 0.60 | 0.23 | 0.00 |
| prefix-open-grip | open | 1 | pooled | 0.03 | 1 | 3.00 | 64 | 0.03 | 0.90 | 0.05 | 0.02 |

### First tick (pooled over seeds)

| arm | look | open | done | other |
|---|---:|---:|---:|---:|
| prefix-only | 1.00 | 0.00 | 0.00 | 0.00 |
| prefix-look-lean | 1.00 | 0.00 | 0.00 | 0.00 |
| prefix-open-lean | 1.00 | 0.00 | 0.00 | 0.00 |
| prefix-look-grip | 1.00 | 0.00 | 0.00 | 0.00 |
| prefix-open-grip | 0.00 | 1.00 | 0.00 | 0.00 |

## Paired per chain against prefix-only

Success: helps = the packet arm succeeded where prefix-only failed, hurts = the reverse. The ticks-to-success delta is signed (packet arm minus prefix-only) and NULL whenever either arm failed the chain.

| arm | seed | helps | hurts | same | both succeeded | mean ticks delta |
|---|---|---:|---:|---:|---:|---:|
| prefix-look-lean | 42 | 0 | 3 | 7 | 4 | 1.25 |
| prefix-look-lean | 1042 | 0 | 7 | 3 | 1 | 0.00 |
| prefix-look-lean | 2042 | 2 | 1 | 7 | 3 | 0.00 |
| prefix-look-lean | pooled | 2 | 11 | 17 | 8 | 0.62 |
| prefix-open-lean | 42 | 0 | 0 | 10 | 7 | 0.00 |
| prefix-open-lean | 1042 | 0 | 6 | 4 | 2 | 1.00 |
| prefix-open-lean | 2042 | 0 | 1 | 9 | 3 | 0.00 |
| prefix-open-lean | pooled | 0 | 7 | 23 | 12 | 0.17 |
| prefix-look-grip | 42 | 0 | 7 | 3 | 0 | -- |
| prefix-look-grip | 1042 | 0 | 8 | 2 | 0 | -- |
| prefix-look-grip | 2042 | 0 | 4 | 6 | 0 | -- |
| prefix-look-grip | pooled | 0 | 19 | 11 | 0 | -- |
| prefix-open-grip | 42 | 0 | 7 | 3 | 0 | -- |
| prefix-open-grip | 1042 | 0 | 8 | 2 | 0 | -- |
| prefix-open-grip | 2042 | 1 | 4 | 5 | 0 | -- |
| prefix-open-grip | pooled | 1 | 19 | 10 | 0 | -- |

### prefix-look-lean vs prefix-only, chain by chain (pooled)

| chain | target | packet | baseline | outcome | packet ticks | baseline ticks | delta | packet submit | baseline submit |
|---|---|---|---|---|---:|---:|---:|---|---|
| box-jar-pond-black_thread | black thread | False | False | same | 4 | 4 | -- | green leaf | green leaf |
| cabinet-box-pond-blue_feather | blue feather | False | False | same | 4 | 4 | -- | gold bell | gold bell |
| chest-drawer-basket-black_thread | black thread | False | True | hurts | 8 | 4 | -- | None | black thread |
| pond-box-shelf-gold_bell | gold bell | False | True | hurts | 8 | 4 | -- | None | gold bell |
| drawer-box-basket-red_stone | red stone | True | True | same | 8 | 4 | +4 | red stone | red stone |
| shelf-pond-cabinet-gold_bell | gold bell | True | True | same | 5 | 4 | +1 | gold bell | gold bell |
| cabinet-drawer-shelf-gold_bell | gold bell | True | True | same | 4 | 4 | +0 | gold bell | gold bell |
| chest-cabinet-drawer-green_leaf | green leaf | False | True | hurts | 4 | 4 | -- | amber key | green leaf |
| drawer-basket-cabinet-amber_key | amber key | True | True | same | 4 | 4 | +0 | amber key | amber key |
| jar-chest-basket-black_thread | black thread | False | False | same | 5 | 4 | -- | gold bell | gold bell |
| box-jar-pond-black_thread | black thread | False | True | hurts | 7 | 5 | -- | inside | black thread |
| cabinet-box-pond-blue_feather | blue feather | False | False | same | 5 | 4 | -- | gold bell | amber key |
| chest-drawer-basket-black_thread | black thread | False | True | hurts | 8 | 4 | -- | None | black thread |
| pond-box-shelf-gold_bell | gold bell | False | True | hurts | 8 | 5 | -- | None | gold bell |
| drawer-box-basket-red_stone | red stone | False | True | hurts | 8 | 4 | -- | None | red stone |
| shelf-pond-cabinet-gold_bell | gold bell | False | True | hurts | 8 | 4 | -- | None | gold bell |
| cabinet-drawer-shelf-gold_bell | gold bell | False | True | hurts | 8 | 4 | -- | None | gold bell |
| chest-cabinet-drawer-green_leaf | green leaf | False | True | hurts | 8 | 4 | -- | None | green leaf |
| drawer-basket-cabinet-amber_key | amber key | True | True | same | 4 | 4 | +0 | amber key | amber key |
| jar-chest-basket-black_thread | black thread | False | False | same | 8 | 4 | -- | None | amber key |
| box-jar-pond-black_thread | black thread | False | False | same | 4 | 4 | -- | green leaf | green leaf |
| cabinet-box-pond-blue_feather | blue feather | False | False | same | 4 | 4 | -- | gold bell | gold bell |
| chest-drawer-basket-black_thread | black thread | True | False | helps | 4 | 4 | -- | black thread | blue feather |
| pond-box-shelf-gold_bell | gold bell | False | True | hurts | 8 | 4 | -- | None | gold bell |
| drawer-box-basket-red_stone | red stone | True | True | same | 4 | 4 | +0 | red stone | red stone |
| shelf-pond-cabinet-gold_bell | gold bell | True | True | same | 4 | 4 | +0 | gold bell | gold bell |
| cabinet-drawer-shelf-gold_bell | gold bell | True | True | same | 4 | 4 | +0 | gold bell | gold bell |
| chest-cabinet-drawer-green_leaf | green leaf | True | False | helps | 4 | 4 | -- | green leaf | amber key |
| drawer-basket-cabinet-amber_key | amber key | False | False | same | 4 | 4 | -- | black thread | black thread |
| jar-chest-basket-black_thread | black thread | False | False | same | 4 | 4 | -- | gold bell | gold bell |

### prefix-open-lean vs prefix-only, chain by chain (pooled)

| chain | target | packet | baseline | outcome | packet ticks | baseline ticks | delta | packet submit | baseline submit |
|---|---|---|---|---|---:|---:|---:|---|---|
| box-jar-pond-black_thread | black thread | False | False | same | 4 | 4 | -- | green leaf | green leaf |
| cabinet-box-pond-blue_feather | blue feather | False | False | same | 4 | 4 | -- | gold bell | gold bell |
| chest-drawer-basket-black_thread | black thread | True | True | same | 4 | 4 | +0 | black thread | black thread |
| pond-box-shelf-gold_bell | gold bell | True | True | same | 4 | 4 | +0 | gold bell | gold bell |
| drawer-box-basket-red_stone | red stone | True | True | same | 4 | 4 | +0 | red stone | red stone |
| shelf-pond-cabinet-gold_bell | gold bell | True | True | same | 4 | 4 | +0 | gold bell | gold bell |
| cabinet-drawer-shelf-gold_bell | gold bell | True | True | same | 4 | 4 | +0 | gold bell | gold bell |
| chest-cabinet-drawer-green_leaf | green leaf | True | True | same | 4 | 4 | +0 | green leaf | green leaf |
| drawer-basket-cabinet-amber_key | amber key | True | True | same | 4 | 4 | +0 | amber key | amber key |
| jar-chest-basket-black_thread | black thread | False | False | same | 4 | 4 | -- | gold bell | gold bell |
| box-jar-pond-black_thread | black thread | False | True | hurts | 6 | 5 | -- | pond | black thread |
| cabinet-box-pond-blue_feather | blue feather | False | False | same | 3 | 4 | -- | amber key | amber key |
| chest-drawer-basket-black_thread | black thread | False | True | hurts | 3 | 4 | -- | amber key | black thread |
| pond-box-shelf-gold_bell | gold bell | False | True | hurts | 8 | 5 | -- | None | gold bell |
| drawer-box-basket-red_stone | red stone | False | True | hurts | 5 | 4 | -- | amber key | red stone |
| shelf-pond-cabinet-gold_bell | gold bell | True | True | same | 5 | 4 | +1 | gold bell | gold bell |
| cabinet-drawer-shelf-gold_bell | gold bell | False | True | hurts | 4 | 4 | -- | empty | gold bell |
| chest-cabinet-drawer-green_leaf | green leaf | True | True | same | 5 | 4 | +1 | green leaf | green leaf |
| drawer-basket-cabinet-amber_key | amber key | False | True | hurts | 4 | 4 | -- | cabinet | amber key |
| jar-chest-basket-black_thread | black thread | False | False | same | 5 | 4 | -- | gold bell | amber key |
| box-jar-pond-black_thread | black thread | False | False | same | 4 | 4 | -- | green leaf | green leaf |
| cabinet-box-pond-blue_feather | blue feather | False | False | same | 4 | 4 | -- | gold bell | gold bell |
| chest-drawer-basket-black_thread | black thread | False | False | same | 4 | 4 | -- | blue feather | blue feather |
| pond-box-shelf-gold_bell | gold bell | False | True | hurts | 3 | 4 | -- | amber key | gold bell |
| drawer-box-basket-red_stone | red stone | True | True | same | 4 | 4 | +0 | red stone | red stone |
| shelf-pond-cabinet-gold_bell | gold bell | True | True | same | 4 | 4 | +0 | gold bell | gold bell |
| cabinet-drawer-shelf-gold_bell | gold bell | True | True | same | 4 | 4 | +0 | gold bell | gold bell |
| chest-cabinet-drawer-green_leaf | green leaf | False | False | same | 4 | 4 | -- | amber key | amber key |
| drawer-basket-cabinet-amber_key | amber key | False | False | same | 4 | 4 | -- | black thread | black thread |
| jar-chest-basket-black_thread | black thread | False | False | same | 4 | 4 | -- | gold bell | gold bell |

### prefix-look-grip vs prefix-only, chain by chain (pooled)

| chain | target | packet | baseline | outcome | packet ticks | baseline ticks | delta | packet submit | baseline submit |
|---|---|---|---|---|---:|---:|---:|---|---|
| box-jar-pond-black_thread | black thread | False | False | same | 8 | 4 | -- | None | green leaf |
| cabinet-box-pond-blue_feather | blue feather | False | False | same | 8 | 4 | -- | None | gold bell |
| chest-drawer-basket-black_thread | black thread | False | True | hurts | 8 | 4 | -- | None | black thread |
| pond-box-shelf-gold_bell | gold bell | False | True | hurts | 8 | 4 | -- | None | gold bell |
| drawer-box-basket-red_stone | red stone | False | True | hurts | 8 | 4 | -- | None | red stone |
| shelf-pond-cabinet-gold_bell | gold bell | False | True | hurts | 8 | 4 | -- | None | gold bell |
| cabinet-drawer-shelf-gold_bell | gold bell | False | True | hurts | 8 | 4 | -- | None | gold bell |
| chest-cabinet-drawer-green_leaf | green leaf | False | True | hurts | 8 | 4 | -- | None | green leaf |
| drawer-basket-cabinet-amber_key | amber key | False | True | hurts | 8 | 4 | -- | None | amber key |
| jar-chest-basket-black_thread | black thread | False | False | same | 8 | 4 | -- | None | gold bell |
| box-jar-pond-black_thread | black thread | False | True | hurts | 8 | 5 | -- | None | black thread |
| cabinet-box-pond-blue_feather | blue feather | False | False | same | 8 | 4 | -- | None | amber key |
| chest-drawer-basket-black_thread | black thread | False | True | hurts | 8 | 4 | -- | None | black thread |
| pond-box-shelf-gold_bell | gold bell | False | True | hurts | 8 | 5 | -- | None | gold bell |
| drawer-box-basket-red_stone | red stone | False | True | hurts | 8 | 4 | -- | None | red stone |
| shelf-pond-cabinet-gold_bell | gold bell | False | True | hurts | 8 | 4 | -- | None | gold bell |
| cabinet-drawer-shelf-gold_bell | gold bell | False | True | hurts | 8 | 4 | -- | None | gold bell |
| chest-cabinet-drawer-green_leaf | green leaf | False | True | hurts | 8 | 4 | -- | None | green leaf |
| drawer-basket-cabinet-amber_key | amber key | False | True | hurts | 8 | 4 | -- | None | amber key |
| jar-chest-basket-black_thread | black thread | False | False | same | 8 | 4 | -- | None | amber key |
| box-jar-pond-black_thread | black thread | False | False | same | 8 | 4 | -- | None | green leaf |
| cabinet-box-pond-blue_feather | blue feather | False | False | same | 8 | 4 | -- | None | gold bell |
| chest-drawer-basket-black_thread | black thread | False | False | same | 8 | 4 | -- | None | blue feather |
| pond-box-shelf-gold_bell | gold bell | False | True | hurts | 8 | 4 | -- | None | gold bell |
| drawer-box-basket-red_stone | red stone | False | True | hurts | 8 | 4 | -- | None | red stone |
| shelf-pond-cabinet-gold_bell | gold bell | False | True | hurts | 8 | 4 | -- | None | gold bell |
| cabinet-drawer-shelf-gold_bell | gold bell | False | True | hurts | 8 | 4 | -- | None | gold bell |
| chest-cabinet-drawer-green_leaf | green leaf | False | False | same | 8 | 4 | -- | None | amber key |
| drawer-basket-cabinet-amber_key | amber key | False | False | same | 8 | 4 | -- | None | black thread |
| jar-chest-basket-black_thread | black thread | False | False | same | 8 | 4 | -- | None | gold bell |

### prefix-open-grip vs prefix-only, chain by chain (pooled)

| chain | target | packet | baseline | outcome | packet ticks | baseline ticks | delta | packet submit | baseline submit |
|---|---|---|---|---|---:|---:|---:|---|---|
| box-jar-pond-black_thread | black thread | False | False | same | 8 | 4 | -- | None | green leaf |
| cabinet-box-pond-blue_feather | blue feather | False | False | same | 8 | 4 | -- | None | gold bell |
| chest-drawer-basket-black_thread | black thread | False | True | hurts | 8 | 4 | -- | None | black thread |
| pond-box-shelf-gold_bell | gold bell | False | True | hurts | 8 | 4 | -- | None | gold bell |
| drawer-box-basket-red_stone | red stone | False | True | hurts | 8 | 4 | -- | None | red stone |
| shelf-pond-cabinet-gold_bell | gold bell | False | True | hurts | 8 | 4 | -- | None | gold bell |
| cabinet-drawer-shelf-gold_bell | gold bell | False | True | hurts | 8 | 4 | -- | None | gold bell |
| chest-cabinet-drawer-green_leaf | green leaf | False | True | hurts | 8 | 4 | -- | None | green leaf |
| drawer-basket-cabinet-amber_key | amber key | False | True | hurts | 8 | 4 | -- | None | amber key |
| jar-chest-basket-black_thread | black thread | False | False | same | 8 | 4 | -- |  | gold bell |
| box-jar-pond-black_thread | black thread | False | True | hurts | 8 | 5 | -- | None | black thread |
| cabinet-box-pond-blue_feather | blue feather | False | False | same | 8 | 4 | -- | None | amber key |
| chest-drawer-basket-black_thread | black thread | False | True | hurts | 8 | 4 | -- | None | black thread |
| pond-box-shelf-gold_bell | gold bell | False | True | hurts | 8 | 5 | -- | None | gold bell |
| drawer-box-basket-red_stone | red stone | False | True | hurts | 8 | 4 | -- | None | red stone |
| shelf-pond-cabinet-gold_bell | gold bell | False | True | hurts | 8 | 4 | -- | None | gold bell |
| cabinet-drawer-shelf-gold_bell | gold bell | False | True | hurts | 8 | 4 | -- | None | gold bell |
| chest-cabinet-drawer-green_leaf | green leaf | False | True | hurts | 8 | 4 | -- | None | green leaf |
| drawer-basket-cabinet-amber_key | amber key | False | True | hurts | 8 | 4 | -- | None | amber key |
| jar-chest-basket-black_thread | black thread | False | False | same | 8 | 4 | -- | None | amber key |
| box-jar-pond-black_thread | black thread | False | False | same | 2 | 4 | -- | amber key | green leaf |
| cabinet-box-pond-blue_feather | blue feather | False | False | same | 3 | 4 | -- | amber key | gold bell |
| chest-drawer-basket-black_thread | black thread | False | False | same | 2 | 4 | -- | amber key | blue feather |
| pond-box-shelf-gold_bell | gold bell | False | True | hurts | 2 | 4 | -- | amber key | gold bell |
| drawer-box-basket-red_stone | red stone | False | True | hurts | 8 | 4 | -- | None | red stone |
| shelf-pond-cabinet-gold_bell | gold bell | False | True | hurts | 2 | 4 | -- | amber key | gold bell |
| cabinet-drawer-shelf-gold_bell | gold bell | False | True | hurts | 3 | 4 | -- | amber key | gold bell |
| chest-cabinet-drawer-green_leaf | green leaf | False | False | same | 2 | 4 | -- | amber key | amber key |
| drawer-basket-cabinet-amber_key | amber key | True | False | helps | 3 | 4 | -- | amber key | black thread |
| jar-chest-basket-black_thread | black thread | False | False | same | 8 | 4 | -- | None | gold bell |

## Reading (v) — channel breakdown, per seed

Rule: a packet arm's invalid actions DOMINATE a seed when invalid_actions >= 0.5 x that arm's decision points in that seed (decision points = the total number of ticks the arm's episodes took in that seed); the seed is flagged CHANNEL BREAKDOWN if any packet arm dominates.

| seed | arm | invalid actions | decision points | invalid share | dominates |
|---|---|---:|---:|---:|---|
| 42 | prefix-look-lean | 0 | 54 | 0.00 | False |
| 42 | prefix-open-lean | 0 | 40 | 0.00 | False |
| 42 | prefix-look-grip | 0 | 80 | 0.00 | False |
| 42 | prefix-open-grip | 31 | 80 | 0.39 | False |
| 1042 | prefix-look-lean | 19 | 72 | 0.26 | False |
| 1042 | prefix-open-lean | 9 | 48 | 0.19 | False |
| 1042 | prefix-look-grip | 11 | 80 | 0.14 | False |
| 1042 | prefix-open-grip | 24 | 80 | 0.30 | False |
| 2042 | prefix-look-lean | 3 | 44 | 0.07 | False |
| 2042 | prefix-open-lean | 0 | 39 | 0.00 | False |
| 2042 | prefix-look-grip | 0 | 80 | 0.00 | False |
| 2042 | prefix-open-grip | 9 | 35 | 0.26 | False |

## Decision rules and the reading

These thresholds are the harness's operationalization of the registered prose readings. They are printed here, not hidden.

- `order`: (iv) precondition first, on the ALL-SEED pooled prefix-only success; then (v) breakdown, flagged per seed; then (i)/(ii)/(iii) on the pooled episodes of the DECIDING (non-breakdown) seeds, with breakdown seeds reported beside them
- `precondition_min_pooled_prefix_only_success`: 0.8
- `composes`: pooled success_rate(arm) >= success_rate(prefix-only) - 0.1 AND the mix moves toward the focus: tool_mix[focus](arm) - tool_mix[focus](prefix-only) >= 0.15 OR first_tick_mix[focus](arm) - first_tick_mix[focus](prefix-only) >= 0.15 (review amendment before the run: share alone is blind when the focus is already the habitual tool -- GF-3's 27B LOOK arm moved first tick 0.8->1.0 at share 0.63->0.64)
- `overrides`: pooled success_rate(arm) <= success_rate(prefix-only) - 0.3 OR tool_mix['done'](arm) < 0.05
- `breakdown`: a packet arm's invalid actions DOMINATE a seed when invalid_actions >= 0.5 x that arm's decision points in that seed (decision points = the total number of ticks the arm's episodes took in that seed); the seed is flagged CHANNEL BREAKDOWN if any packet arm dominates
- `reading_ladder`: (i) both lean arms compose AND at least one grip arm overrides; (ii) both lean arms compose AND no grip arm overrides; (iii) neither lean arm composes; a split (exactly one lean arm composes) is reported as 'mixed' rather than forced into one of the three, because the registration's (i)-(iii) all speak of the lean arms in the plural. A FAILED PRECONDITION takes precedence over the ladder — the registration calls (iv) the finding — and the ladder's own outcome is recorded beside it as `ladder_key`, never dropped

| clause | value |
|---|---|
| (iv) pooled prefix-only success (all seeds) | 0.63 (threshold 0.80, fails: True) |
| (v) breakdown seeds | none |
| deciding seeds | 42, 1042, 2042 |

| arm | success | baseline | focused share | rise | done | composes | overrides |
|---|---:|---:|---:|---:|---:|---|---|
| prefix-look-lean | 0.33 | 0.63 | 0.56 | +0.07 | 0.12 | False | True |
| prefix-open-lean | 0.40 | 0.63 | 0.24 | +0.01 | 0.23 | False | False |
| prefix-look-grip | 0.00 | 0.63 | 0.95 | +0.46 | 0.00 | False | True |
| prefix-open-grip | 0.03 | 0.63 | 0.90 | +0.67 | 0.05 | False | True |

**READING: iv-precondition-fail** — PRECONDITION FAIL — pooled prefix-only success 0.63 is below 0.80; the prefix door's dependence on the drive bridge is the finding, and the ladder below reads iii-neither-composes underneath it.

Ladder underneath: `iii-neither-composes` — NEITHER COMPOSES — the two-door composition needs host scale; the 27B positive is scale-dependent and paper 17's bound tightens.

## Transcripts

Every episode, in the order it ran. The goal never appears in any prompt: it is resident in the latent prefix.

```
Episode — arm: prefix-only [constant, alpha 0], seed 42, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(green leaf) -> you submit: green leaf
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only [constant, alpha 0], seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only [constant, alpha 0], seed 42, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only [constant, alpha 0], seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only [constant, alpha 0], seed 42, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only [constant, alpha 0], seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only [constant, alpha 0], seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only [constant, alpha 0], seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only [constant, alpha 0], seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only [constant, alpha 0], seed 42, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only [constant, alpha 0], seed 1042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: remember() -> that did not work
  tick 4: open(pond) -> you find: black thread and green leaf
  tick 5: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: prefix-only [constant, alpha 0], seed 1042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: remember() -> that did not work
  tick 4: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 2/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only [constant, alpha 0], seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only [constant, alpha 0], seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: remember() -> that did not work
  tick 4: open(shelf) -> you find: blue feather and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: prefix-only [constant, alpha 0], seed 1042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only [constant, alpha 0], seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only [constant, alpha 0], seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only [constant, alpha 0], seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only [constant, alpha 0], seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only [constant, alpha 0], seed 1042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: remember() -> that did not work
  tick 4: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 2/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only [constant, alpha 0], seed 2042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(green leaf) -> you submit: green leaf
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only [constant, alpha 0], seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only [constant, alpha 0], seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(blue feather) -> you submit: blue feather
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only [constant, alpha 0], seed 2042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only [constant, alpha 0], seed 2042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only [constant, alpha 0], seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only [constant, alpha 0], seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only [constant, alpha 0], seed 2042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only [constant, alpha 0], seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(black thread) -> you submit: black thread
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-only [constant, alpha 0], seed 2042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-look-lean [look, alpha 0.25], seed 42, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(green leaf) -> you submit: green leaf
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-look-lean [look, alpha 0.25], seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-look-lean [look, alpha 0.25], seed 42, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: look(basket) -> the basket is closed; something is inside
  tick 5: look(basket) -> the basket is closed; something is inside
  tick 6: open(basket) -> you find: black thread and blue feather
  tick 7: look(basket) -> the basket is closed; something is inside
  tick 8: look(basket) -> the basket is closed; something is inside
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: prefix-look-lean [look, alpha 0.25], seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: look(shelf) -> the shelf is closed; something is inside
  tick 5: look(shelf) -> the shelf is closed; something is inside
  tick 6: open(shelf) -> you find: blue feather and gold bell
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: prefix-look-lean [look, alpha 0.25], seed 42, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: look(basket) -> the basket is closed; something is inside
  tick 5: look(basket) -> the basket is closed; something is inside
  tick 6: open(basket) -> you find: red stone and blue feather
  tick 7: look(basket) -> the basket is closed; something is inside
  tick 8: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: prefix-look-lean [look, alpha 0.25], seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: look(cabinet) -> the cabinet is closed; something is inside
  tick 5: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: prefix-look-lean [look, alpha 0.25], seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-look-lean [look, alpha 0.25], seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-look-lean [look, alpha 0.25], seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-look-lean [look, alpha 0.25], seed 42, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: look(basket) -> the basket is closed; something is inside
  tick 5: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: prefix-look-lean [look, alpha 0.25], seed 1042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: remember() -> that did not work
  tick 3: look(jar) -> a note: try the pond
  tick 4: remember() -> that did not work
  tick 5: look(pond) -> the pond is closed; something is inside
  tick 6: look(pond) -> the pond is closed; something is inside
  tick 7: done(inside) -> you submit: inside
  FAIL (wrong submit) — depth 2/3, 7 of 8 ticks
```

```
Episode — arm: prefix-look-lean [look, alpha 0.25], seed 1042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: remember() -> that did not work
  tick 4: open(pond) -> you find: blue feather and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: prefix-look-lean [look, alpha 0.25], seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: remember() -> that did not work
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: look(drawer) -> a note: try the basket
  tick 6: look(basket) -> the basket is closed; something is inside
  tick 7: remember() -> that did not work
  tick 8: look(basket) -> the basket is closed; something is inside
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: prefix-look-lean [look, alpha 0.25], seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: remember() -> that did not work
  tick 3: look(box) -> a note: try the shelf
  tick 4: remember() -> that did not work
  tick 5: look(shelf) -> the shelf is closed; something is inside
  tick 6: open(shelf) -> you find: blue feather and gold bell
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: prefix-look-lean [look, alpha 0.25], seed 1042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: remember() -> that did not work
  tick 4: open(basket) -> you find: red stone and blue feather
  tick 5: look(basket) -> the basket is closed; something is inside
  tick 6: look(basket) -> the basket is closed; something is inside
  tick 7: open(basket) -> you find: red stone and blue feather
  tick 8: look(basket) -> the basket is closed; something is inside
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: prefix-look-lean [look, alpha 0.25], seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: remember() -> that did not work
  tick 3: look(pond) -> a note: try the cabinet
  tick 4: open(cabinet) -> you find: blue feather and gold bell
  tick 5: look(cabinet) -> the cabinet is closed; something is inside
  tick 6: look(cabinet) -> the cabinet is closed; something is inside
  tick 7: open(cabinet) -> you find: blue feather and gold bell
  tick 8: look(cabinet) -> the cabinet is closed; something is inside
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: prefix-look-lean [look, alpha 0.25], seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: remember() -> that did not work
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: look(drawer) -> a note: try the shelf
  tick 6: look(shelf) -> the shelf is closed; something is inside
  tick 7: open(shelf) -> you find: black thread and gold bell
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: prefix-look-lean [look, alpha 0.25], seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: remember() -> that did not work
  tick 3: remember() -> that did not work
  tick 4: remember() -> that did not work
  tick 5: look(cabinet) -> a note: try the drawer
  tick 6: look(drawer) -> the drawer is closed; something is inside
  tick 7: open(drawer) -> you find: green leaf and amber key
  tick 8: look(drawer) -> the drawer is closed; something is inside
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: prefix-look-lean [look, alpha 0.25], seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-look-lean [look, alpha 0.25], seed 1042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: remember() -> that did not work
  tick 3: look(chest) -> a note: try the basket
  tick 4: open(basket) -> you find: black thread and gold bell
  tick 5: look(basket) -> the basket is closed; something is inside
  tick 6: remember() -> that did not work
  tick 7: look(basket) -> the basket is closed; something is inside
  tick 8: look(basket) -> the basket is closed; something is inside
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: prefix-look-lean [look, alpha 0.25], seed 2042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(green leaf) -> you submit: green leaf
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-look-lean [look, alpha 0.25], seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-look-lean [look, alpha 0.25], seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-look-lean [look, alpha 0.25], seed 2042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: remember() -> that did not work
  tick 5: look(shelf) -> the shelf is closed; something is inside
  tick 6: remember() -> that did not work
  tick 7: remember() -> that did not work
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: prefix-look-lean [look, alpha 0.25], seed 2042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-look-lean [look, alpha 0.25], seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-look-lean [look, alpha 0.25], seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-look-lean [look, alpha 0.25], seed 2042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-look-lean [look, alpha 0.25], seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(black thread) -> you submit: black thread
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-look-lean [look, alpha 0.25], seed 2042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-open-lean [open, alpha 0.25], seed 42, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(green leaf) -> you submit: green leaf
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-open-lean [open, alpha 0.25], seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-open-lean [open, alpha 0.25], seed 42, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-open-lean [open, alpha 0.25], seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-open-lean [open, alpha 0.25], seed 42, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-open-lean [open, alpha 0.25], seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-open-lean [open, alpha 0.25], seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-open-lean [open, alpha 0.25], seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-open-lean [open, alpha 0.25], seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-open-lean [open, alpha 0.25], seed 42, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-open-lean [open, alpha 0.25], seed 1042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: remember() -> that did not work
  tick 3: open(jar) -> empty
  tick 4: remember() -> that did not work
  tick 5: look(jar) -> a note: try the pond
  tick 6: done(pond) -> you submit: pond
  FAIL (wrong submit) — depth 2/3, 6 of 8 ticks
```

```
Episode — arm: prefix-open-lean [open, alpha 0.25], seed 1042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: open(box) -> empty
  tick 3: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 1/3, 3 of 8 ticks
```

```
Episode — arm: prefix-open-lean [open, alpha 0.25], seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: open(drawer) -> empty
  tick 3: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 1/3, 3 of 8 ticks
```

```
Episode — arm: prefix-open-lean [open, alpha 0.25], seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: remember() -> that did not work
  tick 3: look(box) -> a note: try the shelf
  tick 4: remember() -> that did not work
  tick 5: open(shelf) -> you find: blue feather and gold bell
  tick 6: look(shelf) -> the shelf is closed; something is inside
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: open(shelf) -> you find: blue feather and gold bell
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: prefix-open-lean [open, alpha 0.25], seed 1042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: open(box) -> empty
  tick 3: look(box) -> a note: try the basket
  tick 4: remember() -> that did not work
  tick 5: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 2/3, 5 of 8 ticks
```

```
Episode — arm: prefix-open-lean [open, alpha 0.25], seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: remember() -> that did not work
  tick 3: look(pond) -> a note: try the cabinet
  tick 4: open(cabinet) -> you find: blue feather and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: prefix-open-lean [open, alpha 0.25], seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: remember() -> that did not work
  tick 3: open(drawer) -> empty
  tick 4: done(empty) -> you submit: empty
  FAIL (wrong submit) — depth 1/3, 4 of 8 ticks
```

```
Episode — arm: prefix-open-lean [open, alpha 0.25], seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: remember() -> that did not work
  tick 4: open(drawer) -> you find: green leaf and amber key
  tick 5: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: prefix-open-lean [open, alpha 0.25], seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: open(basket) -> empty
  tick 3: look(basket) -> a note: try the cabinet
  tick 4: done(cabinet) -> you submit: cabinet
  FAIL (wrong submit) — depth 2/3, 4 of 8 ticks
```

```
Episode — arm: prefix-open-lean [open, alpha 0.25], seed 1042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: remember() -> that did not work
  tick 3: look(chest) -> a note: try the basket
  tick 4: open(basket) -> you find: black thread and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: prefix-open-lean [open, alpha 0.25], seed 2042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(green leaf) -> you submit: green leaf
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-open-lean [open, alpha 0.25], seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-open-lean [open, alpha 0.25], seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(blue feather) -> you submit: blue feather
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-open-lean [open, alpha 0.25], seed 2042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: open(box) -> empty
  tick 3: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 1/3, 3 of 8 ticks
```

```
Episode — arm: prefix-open-lean [open, alpha 0.25], seed 2042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-open-lean [open, alpha 0.25], seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-open-lean [open, alpha 0.25], seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-open-lean [open, alpha 0.25], seed 2042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-open-lean [open, alpha 0.25], seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(black thread) -> you submit: black thread
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-open-lean [open, alpha 0.25], seed 2042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-look-grip [look, alpha 1], seed 42, chain box->jar->pond, target: black thread
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
Episode — arm: prefix-look-grip [look, alpha 1], seed 42, chain cabinet->box->pond, target: blue feather
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
Episode — arm: prefix-look-grip [look, alpha 1], seed 42, chain chest->drawer->basket, target: black thread
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
Episode — arm: prefix-look-grip [look, alpha 1], seed 42, chain pond->box->shelf, target: gold bell
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
Episode — arm: prefix-look-grip [look, alpha 1], seed 42, chain drawer->box->basket, target: red stone
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
Episode — arm: prefix-look-grip [look, alpha 1], seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: look(cabinet) -> the cabinet is closed; something is inside
  tick 5: look(cabinet) -> the cabinet is closed; something is inside
  tick 6: look(pond) -> a note: try the cabinet
  tick 7: look(cabinet) -> the cabinet is closed; something is inside
  tick 8: look(shelf) -> a note: check the pond
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: prefix-look-grip [look, alpha 1], seed 42, chain cabinet->drawer->shelf, target: gold bell
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
Episode — arm: prefix-look-grip [look, alpha 1], seed 42, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: prefix-look-grip [look, alpha 1], seed 42, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: prefix-look-grip [look, alpha 1], seed 42, chain jar->chest->basket, target: black thread
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
Episode — arm: prefix-look-grip [look, alpha 1], seed 1042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: look(pond) -> the pond is closed; something is inside
  tick 4: look(jar) -> a note: try the pond
  tick 5: look(pond) -> the pond is closed; something is inside
  tick 6: look(jar) -> a note: try the pond
  tick 7: look(pond) -> the pond is closed; something is inside
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: prefix-look-grip [look, alpha 1], seed 1042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: look(pond) -> the pond is closed; something is inside
  tick 4: look(pond) -> the pond is closed; something is inside
  tick 5: look(pond) -> the pond is closed; something is inside
  tick 6: look(pond) -> the pond is closed; something is inside
  tick 7: look(pond) -> the pond is closed; something is inside
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: prefix-look-grip [look, alpha 1], seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: look(drawer) -> a note: try the basket
  tick 4: look(drawer) -> a note: try the basket
  tick 5: look(drawer) -> a note: try the basket
  tick 6: look(drawer) -> a note: try the basket
  tick 7: look(chest) -> a note: check the drawer
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: prefix-look-grip [look, alpha 1], seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: look(shelf) -> the shelf is closed; something is inside
  tick 5: look(shelf) -> the shelf is closed; something is inside
  tick 6: look(shelf) -> the shelf is closed; something is inside
  tick 7: remember() -> that did not work
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: prefix-look-grip [look, alpha 1], seed 1042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: look(box) -> a note: try the basket
  tick 4: look(box) -> a note: try the basket
  tick 5: look(box) -> a note: try the basket
  tick 6: look(box) -> a note: try the basket
  tick 7: look(drawer) -> a note: check the box
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: prefix-look-grip [look, alpha 1], seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: look(cabinet) -> the cabinet is closed; something is inside
  tick 5: look(pond) -> a note: try the cabinet
  tick 6: look(cabinet) -> the cabinet is closed; something is inside
  tick 7: look(shelf) -> a note: check the pond
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: prefix-look-grip [look, alpha 1], seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: look(drawer) -> a note: try the shelf
  tick 4: look(drawer) -> a note: try the shelf
  tick 5: look(drawer) -> a note: try the shelf
  tick 6: remember() -> that did not work
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: prefix-look-grip [look, alpha 1], seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: look(drawer) -> the drawer is closed; something is inside
  tick 4: look(drawer) -> the drawer is closed; something is inside
  tick 5: look(drawer) -> the drawer is closed; something is inside
  tick 6: look(cabinet) -> a note: try the drawer
  tick 7: look(drawer) -> the drawer is closed; something is inside
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: prefix-look-grip [look, alpha 1], seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: look(cabinet) -> the cabinet is closed; something is inside
  tick 5: look(cabinet) -> the cabinet is closed; something is inside
  tick 6: look(basket) -> a note: try the cabinet
  tick 7: remember() -> that did not work
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: prefix-look-grip [look, alpha 1], seed 1042, chain jar->chest->basket, target: black thread
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
Episode — arm: prefix-look-grip [look, alpha 1], seed 2042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: look(pond) -> the pond is closed; something is inside
  tick 4: look(pond) -> the pond is closed; something is inside
  tick 5: look(pond) -> the pond is closed; something is inside
  tick 6: look(pond) -> the pond is closed; something is inside
  tick 7: look(pond) -> the pond is closed; something is inside
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: prefix-look-grip [look, alpha 1], seed 2042, chain cabinet->box->pond, target: blue feather
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
Episode — arm: prefix-look-grip [look, alpha 1], seed 2042, chain chest->drawer->basket, target: black thread
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
Episode — arm: prefix-look-grip [look, alpha 1], seed 2042, chain pond->box->shelf, target: gold bell
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
Episode — arm: prefix-look-grip [look, alpha 1], seed 2042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: look(basket) -> the basket is closed; something is inside
  tick 4: look(basket) -> the basket is closed; something is inside
  tick 5: look(basket) -> the basket is closed; something is inside
  tick 6: look(box) -> a note: try the basket
  tick 7: look(box) -> a note: try the basket
  tick 8: look(box) -> a note: try the basket
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: prefix-look-grip [look, alpha 1], seed 2042, chain shelf->pond->cabinet, target: gold bell
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
Episode — arm: prefix-look-grip [look, alpha 1], seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: look(drawer) -> a note: try the shelf
  tick 4: look(drawer) -> a note: try the shelf
  tick 5: look(drawer) -> a note: try the shelf
  tick 6: look(drawer) -> a note: try the shelf
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: prefix-look-grip [look, alpha 1], seed 2042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: look(drawer) -> the drawer is closed; something is inside
  tick 4: look(drawer) -> the drawer is closed; something is inside
  tick 5: look(drawer) -> the drawer is closed; something is inside
  tick 6: look(drawer) -> the drawer is closed; something is inside
  tick 7: look(cabinet) -> a note: try the drawer
  tick 8: look(drawer) -> the drawer is closed; something is inside
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: prefix-look-grip [look, alpha 1], seed 2042, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: prefix-look-grip [look, alpha 1], seed 2042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: look(basket) -> the basket is closed; something is inside
  tick 4: look(basket) -> the basket is closed; something is inside
  tick 5: look(basket) -> the basket is closed; something is inside
  tick 6: look(chest) -> a note: try the basket
  tick 7: look(basket) -> the basket is closed; something is inside
  tick 8: look(chest) -> a note: try the basket
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: prefix-open-grip [open, alpha 1], seed 42, chain box->jar->pond, target: black thread
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
Episode — arm: prefix-open-grip [open, alpha 1], seed 42, chain cabinet->box->pond, target: blue feather
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
Episode — arm: prefix-open-grip [open, alpha 1], seed 42, chain chest->drawer->basket, target: black thread
  tick 1: open(kitchen) -> that is not a place here
  tick 2: open(kitchen) -> that is not a place here
  tick 3: open(kitchen) -> that is not a place here
  tick 4: open(kitchen) -> that is not a place here
  tick 5: open(kitchen) -> that is not a place here
  tick 6: open(kitchen) -> that is not a place here
  tick 7: remember() -> that did not work
  tick 8: open(kitchen) -> that is not a place here
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: prefix-open-grip [open, alpha 1], seed 42, chain pond->box->shelf, target: gold bell
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
Episode — arm: prefix-open-grip [open, alpha 1], seed 42, chain drawer->box->basket, target: red stone
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
Episode — arm: prefix-open-grip [open, alpha 1], seed 42, chain shelf->pond->cabinet, target: gold bell
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
Episode — arm: prefix-open-grip [open, alpha 1], seed 42, chain cabinet->drawer->shelf, target: gold bell
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
Episode — arm: prefix-open-grip [open, alpha 1], seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: open(kitchen) -> that is not a place here
  tick 2: open(kitchen) -> that is not a place here
  tick 3: open(kitchen) -> that is not a place here
  tick 4: open(kitchen) -> that is not a place here
  tick 5: open(kitchen) -> that is not a place here
  tick 6: open(kitchen) -> that is not a place here
  tick 7: remember() -> that did not work
  tick 8: open(kitchen) -> that is not a place here
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: prefix-open-grip [open, alpha 1], seed 42, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: prefix-open-grip [open, alpha 1], seed 42, chain jar->chest->basket, target: black thread
  tick 1: open(kitchen) -> that is not a place here
  tick 2: open(kitchen) -> that is not a place here
  tick 3: open(kitchen) -> that is not a place here
  tick 4: open(kitchen) -> that is not a place here
  tick 5: open(kitchen) -> that is not a place here
  tick 6: open(kitchen) -> that is not a place here
  tick 7: open(kitchen) -> that is not a place here
  tick 8: done(kitchen) -> you submit: (nothing)
  FAIL (wrong submit) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: prefix-open-grip [open, alpha 1], seed 1042, chain box->jar->pond, target: black thread
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
Episode — arm: prefix-open-grip [open, alpha 1], seed 1042, chain cabinet->box->pond, target: blue feather
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
Episode — arm: prefix-open-grip [open, alpha 1], seed 1042, chain chest->drawer->basket, target: black thread
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
Episode — arm: prefix-open-grip [open, alpha 1], seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: open(kit) -> that is not a place here
  tick 2: open(kit) -> that is not a place here
  tick 3: open(kit) -> that is not a place here
  tick 4: open(kit) -> that is not a place here
  tick 5: open(kit) -> that is not a place here
  tick 6: open(kit) -> that is not a place here
  tick 7: open(kit) -> that is not a place here
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: prefix-open-grip [open, alpha 1], seed 1042, chain drawer->box->basket, target: red stone
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
Episode — arm: prefix-open-grip [open, alpha 1], seed 1042, chain shelf->pond->cabinet, target: gold bell
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
Episode — arm: prefix-open-grip [open, alpha 1], seed 1042, chain cabinet->drawer->shelf, target: gold bell
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
Episode — arm: prefix-open-grip [open, alpha 1], seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: open(kitchen) -> that is not a place here
  tick 2: open(kitchen) -> that is not a place here
  tick 3: open(kitchen) -> that is not a place here
  tick 4: open(kitchen) -> that is not a place here
  tick 5: open(kitchen) -> that is not a place here
  tick 6: open(kitchen) -> that is not a place here
  tick 7: open(kitchen) -> that is not a place here
  tick 8: open() -> that is not a place here
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: prefix-open-grip [open, alpha 1], seed 1042, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: prefix-open-grip [open, alpha 1], seed 1042, chain jar->chest->basket, target: black thread
  tick 1: open(kitchen) -> that is not a place here
  tick 2: open(kitchen) -> that is not a place here
  tick 3: open(kitchen) -> that is not a place here
  tick 4: open(kitchen) -> that is not a place here
  tick 5: open(kitchen) -> that is not a place here
  tick 6: open(kitchen) -> that is not a place here
  tick 7: open(kitchen) -> that is not a place here
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: prefix-open-grip [open, alpha 1], seed 2042, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: prefix-open-grip [open, alpha 1], seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: open(cabinet) -> empty
  tick 2: open(cabinet) -> empty
  tick 3: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 3 of 8 ticks
```

```
Episode — arm: prefix-open-grip [open, alpha 1], seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: open(chest) -> empty
  tick 2: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: prefix-open-grip [open, alpha 1], seed 2042, chain pond->box->shelf, target: gold bell
  tick 1: open(box) -> empty
  tick 2: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: prefix-open-grip [open, alpha 1], seed 2042, chain drawer->box->basket, target: red stone
  tick 1: open(door) -> that is not a place here
  tick 2: open(door) -> that is not a place here
  tick 3: look(shelf) -> nothing of note
  tick 4: open(door) -> that is not a place here
  tick 5: look(shelf) -> nothing of note
  tick 6: open(shelf) -> empty
  tick 7: look(empty) -> that is not a place here
  tick 8: open(empty) -> that is not a place here
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: prefix-open-grip [open, alpha 1], seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: open(box) -> empty
  tick 2: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: prefix-open-grip [open, alpha 1], seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: open(cabinet) -> empty
  tick 2: open(cabinet) -> empty
  tick 3: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 3 of 8 ticks
```

```
Episode — arm: prefix-open-grip [open, alpha 1], seed 2042, chain chest->cabinet->drawer, target: green leaf
  tick 1: open(box) -> empty
  tick 2: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: prefix-open-grip [open, alpha 1], seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: open(door) -> that is not a place here
  tick 2: open(door) -> that is not a place here
  tick 3: done(amber key) -> you submit: amber key
  PASS — depth 0/3, 3 of 8 ticks, guessed
```

```
Episode — arm: prefix-open-grip [open, alpha 1], seed 2042, chain jar->chest->basket, target: black thread
  tick 1: open(door) -> that is not a place here
  tick 2: open(door) -> that is not a place here
  tick 3: look(jar) -> a note: check the chest
  tick 4: open(chest) -> empty
  tick 5: look(chest) -> a note: try the basket
  tick 6: open(basket) -> you find: black thread and gold bell
  tick 7: look(basket) -> the basket is closed; something is inside
  tick 8: open(basket) -> you find: black thread and gold bell
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

