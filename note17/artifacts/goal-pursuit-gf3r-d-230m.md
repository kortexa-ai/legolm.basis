# gf3r-d-drive-probe

Host machine `smarty`, device `cuda`, dtype `bfloat16`, budget 8, 321.853 s. Registration: tracks/goal-pursuit/PLAN.md, ## Overnight registrations -> ### GF-3r-d registration — which property of the drive bridge the prefix door needs (230M, smarty CUDA, stops nothing) (2026-08-20 night, before anything runs; Franci's plan).

**Scope.** the DRIVE PROBE at 230M on five bridges trained in process per seed across THREE rng streams (G1's goal+constant pair by G6's recipe, the goal bridge discarded; GF's focus+constant pair on a freshly re-seeded stream by GF's recipe, the focus bridge discarded; and a goal-exchange constant trained FIRST on a third freshly re-seeded stream): the chain's goal line through G6's latent prefix, and on the bus either NO packet at all (the hooks are not armed) or exactly ONE unmixed constant packet at dose 0.15; 3 bridge seed(s) x 10 eval chains x 4 arms. What is measured is WHICH property of the drive bridge the zero-shot prefix door needs — the exchange, the stream position, or none. No focus packet, no mix, no lean and no grip exist under this drive. Nothing here cites GS.

## The two doors

G6's prefix-only door verbatim: g6_splitdoor.installed_goal_line(chain['item']) embedded through model.get_input_embeddings() (g5_referent.embed_ids) and prepended to the GOAL-FREE prompt's embeddings; gp.run_episode is called with goal_text=None in every arm and the decider asserts it. nothing trains against prefix-formatted inputs; both bridges were trained on token-id prompts. GF-3 at 27B prefixed gp.goal_line(chain) + '\n\n'; G6 prefixed the bare goal line, and the registration pins G6's mechanism, so GF-3r carries no trailing blank line.

Bus: THREE constant bridges trained per seed on three rng streams (192 steps, batch 8, lr 0.003, train dose 0.15), each delivered UNMIXED at the fixed dose 0.15 into layers [4, 6, 8] from the tap at layer 12; the fourth arm arms no hook at all. There is no focus packet, no mix, no lean and no grip under this drive.

Armed block: `self-LFM230M-r4-dream4.pt` — gp.load_armed_host — the 230M production stack: frozen host, rank-4 attn LoRA, the dream4 self-block injected at the constant state (GF's and GF-2b's own code path).

Memory gate: required 20.0 GiB free, applied: True.

## The three constants — pairwise distinctness (checked before any arm decodes)

the THREE constant packets — G1's, GF's and the goal-first one — must be PAIRWISE distinct: each pair is evaluated on one synthetic residual state and the max |delta| must be strictly above 0, or two arms would be one arm under two names. There is no mix under this drive, so there is no alpha identity to check, and a failure stops the run.

| seed | check | must be | exact | max abs difference |
|---|---|---|---|---:|
| 42 | g1_constant_differs_from_gf_constant | different | False | 13.6 |
| 42 | goalfirst_constant_differs_from_g1_constant | different | False | 16.2 |
| 42 | goalfirst_constant_differs_from_gf_constant | different | False | 10.3 |
| 1042 | g1_constant_differs_from_gf_constant | different | False | 7.56 |
| 1042 | goalfirst_constant_differs_from_g1_constant | different | False | 13.3 |
| 1042 | goalfirst_constant_differs_from_gf_constant | different | False | 10.9 |
| 2042 | g1_constant_differs_from_gf_constant | different | False | 11 |
| 2042 | goalfirst_constant_differs_from_g1_constant | different | False | 16.9 |
| 2042 | goalfirst_constant_differs_from_gf_constant | different | False | 13.2 |

## Plumbing gates (run before each seed's arms; failure stops the run)

| seed | gate | what | identical | prefix tokens |
|---|---|---|---|---:|
| 42 | a_no_prefix_zero_dose | no-prefix, fraction 0.0, hooks armed vs plain generate | True | 0 |
| 42 | b_prefixed_zero_dose | WITH the chain-0 goal prefix, fraction 0.0, hooks armed vs the same prefixed generate with no hooks | True | 9 |
| 42 | b_prefixed_zero_dose_gf | WITH the chain-0 goal prefix, fraction 0.0, hooks armed on the gf CONSTANT packet vs the same prefixed generate with no hooks | True | 9 |
| 42 | b_prefixed_zero_dose_goalfirst | WITH the chain-0 goal prefix, fraction 0.0, hooks armed on the goalfirst CONSTANT packet vs the same prefixed generate with no hooks | True | 9 |
| 42 | b_matches_nopacket_arm_chain0 | gate (b)'s prefixed zero-dose HOOKS-ARMED decode vs arm prefix-nopacket's chain-0 tick-1 decode (no hooks armed at all) — the same prompt, the same prefix, the same generate path | True | 9 |
| 1042 | a_no_prefix_zero_dose | no-prefix, fraction 0.0, hooks armed vs plain generate | True | 0 |
| 1042 | b_prefixed_zero_dose | WITH the chain-0 goal prefix, fraction 0.0, hooks armed vs the same prefixed generate with no hooks | True | 9 |
| 1042 | b_prefixed_zero_dose_gf | WITH the chain-0 goal prefix, fraction 0.0, hooks armed on the gf CONSTANT packet vs the same prefixed generate with no hooks | True | 9 |
| 1042 | b_prefixed_zero_dose_goalfirst | WITH the chain-0 goal prefix, fraction 0.0, hooks armed on the goalfirst CONSTANT packet vs the same prefixed generate with no hooks | True | 9 |
| 1042 | b_matches_nopacket_arm_chain0 | gate (b)'s prefixed zero-dose HOOKS-ARMED decode vs arm prefix-nopacket's chain-0 tick-1 decode (no hooks armed at all) — the same prompt, the same prefix, the same generate path | True | 9 |
| 2042 | a_no_prefix_zero_dose | no-prefix, fraction 0.0, hooks armed vs plain generate | True | 0 |
| 2042 | b_prefixed_zero_dose | WITH the chain-0 goal prefix, fraction 0.0, hooks armed vs the same prefixed generate with no hooks | True | 9 |
| 2042 | b_prefixed_zero_dose_gf | WITH the chain-0 goal prefix, fraction 0.0, hooks armed on the gf CONSTANT packet vs the same prefixed generate with no hooks | True | 9 |
| 2042 | b_prefixed_zero_dose_goalfirst | WITH the chain-0 goal prefix, fraction 0.0, hooks armed on the goalfirst CONSTANT packet vs the same prefixed generate with no hooks | True | 9 |
| 2042 | b_matches_nopacket_arm_chain0 | gate (b)'s prefixed zero-dose HOOKS-ARMED decode vs arm prefix-nopacket's chain-0 tick-1 decode (no hooks armed at all) — the same prompt, the same prefix, the same generate path | True | 9 |
| all | c_prefix_length_constant_across_arms | the per-chain prefix length is constant across arms, so the injection placement is identical across arms | True | one prefix tensor is embedded per chain and reused by all four arms at every seed; the arms differ only in the bus payload |

Rule: any gate failure stops the run before arms (registration, gate clause); the decode contract is the arms' own (greedy, no think-strip, MAX_NEW 64).

Base weights unchanged at every seed: True.

## Injection placement (registered gate (c))

Armed by: relay_experiment.relay_injection -> MultiResidualInjection, one ResidualInjection per inject layer, position=-1, once=False, mode 'conditioned', layers [4, 6, 8]. Read from: mom_bridge.ResidualInjection._hook (mode 'conditioned'): the zero-dose early return, the start index and bank offsets under 'positional'/'conditioned', and __enter__'s reset of next_offset.

Layout `inputs_embeds = [goal prefix (P) ; prompt (L)]`. The prefill hook fires once and injects **1** position at index `P + L - 1` — the LAST token of the rendered chat prompt (the generation-prompt tail); positions 0..P-1 (the entire goal prefix) and P..P+L-2 are NOT injected. Prefix positions injected: 0. each KV-cached step takes start=0 over its single new position, so every generated token is injected.

Bank offsets: 0 on the last prefill position, then 1, 2, ... per generated token, clamped at delta_positions-1 = 15; __enter__ resets the counter, so every generate call starts at 0. Effect of the prefix length: P shifts the ABSOLUTE index of the injection point by exactly P and changes nothing else: not the relative placement (always the last prefill position), not the bank-offset schedule, not the count of injected positions. Zero dose: at fraction 0.0 the hook returns the layer output before it reads the residual — the property gates (a) and (b) test.

Identical across arms: the four arms differ only in the payload; the prefix is one cached tensor per chain, reused by every arm, so P is a property of the chain alone and the placement is identical across arms by construction.

Where the mix lands: no mix: GF-3r-d's arms carry an UNMIXED constant packet or no packet at all, so the hook is handed the constant bridge's own delivered payload at the trained dose 0.15 in the three packet arms and no hook is armed at all in prefix-nopacket.

## Headline — success, finish tick, tool mix

`prefix-nopacket` is the decisive cell AND the paired baseline: the latent prefix with no packet at all — the hooks are not armed. The other three arms each deliver ONE unmixed constant packet at dose 0.15. The mix columns are pooled shares over all decision points; the first-tick columns are shares over the cell's episodes.

| arm | packet | alpha | seed | success | successes | mean finish tick | invalid | look | open | done | other |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| prefix-nopacket | none — no hook armed | 0 | 42 | 0.00 | 0 | -- | 0 | 1.00 | 0.00 | 0.00 | 0.00 |
| prefix-nopacket | none — no hook armed | 0 | 1042 | 0.00 | 0 | -- | 0 | 1.00 | 0.00 | 0.00 | 0.00 |
| prefix-nopacket | none — no hook armed | 0 | 2042 | 0.00 | 0 | -- | 0 | 1.00 | 0.00 | 0.00 | 0.00 |
| prefix-nopacket | none — no hook armed | 0 | pooled | 0.00 | 0 | -- | 0 | 1.00 | 0.00 | 0.00 | 0.00 |
| prefix-g1const | G1 constant (goal exchange, 2nd on its stream) | 0 | 42 | 1.00 | 10 | 4.00 | 0 | 0.50 | 0.25 | 0.25 | 0.00 |
| prefix-g1const | G1 constant (goal exchange, 2nd on its stream) | 0 | 1042 | 1.00 | 10 | 4.00 | 0 | 0.50 | 0.25 | 0.25 | 0.00 |
| prefix-g1const | G1 constant (goal exchange, 2nd on its stream) | 0 | 2042 | 1.00 | 10 | 4.00 | 0 | 0.50 | 0.25 | 0.25 | 0.00 |
| prefix-g1const | G1 constant (goal exchange, 2nd on its stream) | 0 | pooled | 1.00 | 30 | 4.00 | 0 | 0.50 | 0.25 | 0.25 | 0.00 |
| prefix-gfconst | GF constant (focus exchange, 2nd on its stream) | 0 | 42 | 0.70 | 7 | 4.00 | 0 | 0.50 | 0.25 | 0.25 | 0.00 |
| prefix-gfconst | GF constant (focus exchange, 2nd on its stream) | 0 | 1042 | 0.80 | 8 | 4.25 | 4 | 0.48 | 0.19 | 0.24 | 0.10 |
| prefix-gfconst | GF constant (focus exchange, 2nd on its stream) | 0 | 2042 | 0.40 | 4 | 4.00 | 0 | 0.50 | 0.25 | 0.25 | 0.00 |
| prefix-gfconst | GF constant (focus exchange, 2nd on its stream) | 0 | pooled | 0.63 | 19 | 4.11 | 4 | 0.49 | 0.23 | 0.25 | 0.03 |
| prefix-goalfirst | goal-first constant (goal exchange, 1st on its stream) | 0 | 42 | 0.60 | 6 | 4.00 | 0 | 0.50 | 0.25 | 0.25 | 0.00 |
| prefix-goalfirst | goal-first constant (goal exchange, 1st on its stream) | 0 | 1042 | 1.00 | 10 | 4.00 | 0 | 0.50 | 0.25 | 0.25 | 0.00 |
| prefix-goalfirst | goal-first constant (goal exchange, 1st on its stream) | 0 | 2042 | 1.00 | 10 | 4.00 | 0 | 0.50 | 0.25 | 0.25 | 0.00 |
| prefix-goalfirst | goal-first constant (goal exchange, 1st on its stream) | 0 | pooled | 0.87 | 26 | 4.00 | 0 | 0.50 | 0.25 | 0.25 | 0.00 |

### First tick (pooled over seeds)

| arm | look | open | done | other |
|---|---:|---:|---:|---:|
| prefix-nopacket | 1.00 | 0.00 | 0.00 | 0.00 |
| prefix-g1const | 1.00 | 0.00 | 0.00 | 0.00 |
| prefix-gfconst | 1.00 | 0.00 | 0.00 | 0.00 |
| prefix-goalfirst | 1.00 | 0.00 | 0.00 | 0.00 |

## Paired per chain against prefix-nopacket

Success: helps = the packet arm succeeded where prefix-nopacket failed, hurts = the reverse. The ticks-to-success delta is signed (packet arm minus prefix-nopacket) and NULL whenever either arm failed the chain.

| arm | seed | helps | hurts | same | both succeeded | mean ticks delta |
|---|---|---:|---:|---:|---:|---:|
| prefix-g1const | 42 | 10 | 0 | 0 | 0 | -- |
| prefix-g1const | 1042 | 10 | 0 | 0 | 0 | -- |
| prefix-g1const | 2042 | 10 | 0 | 0 | 0 | -- |
| prefix-g1const | pooled | 30 | 0 | 0 | 0 | -- |
| prefix-gfconst | 42 | 7 | 0 | 3 | 0 | -- |
| prefix-gfconst | 1042 | 8 | 0 | 2 | 0 | -- |
| prefix-gfconst | 2042 | 4 | 0 | 6 | 0 | -- |
| prefix-gfconst | pooled | 19 | 0 | 11 | 0 | -- |
| prefix-goalfirst | 42 | 6 | 0 | 4 | 0 | -- |
| prefix-goalfirst | 1042 | 10 | 0 | 0 | 0 | -- |
| prefix-goalfirst | 2042 | 10 | 0 | 0 | 0 | -- |
| prefix-goalfirst | pooled | 26 | 0 | 4 | 0 | -- |

### prefix-g1const vs prefix-nopacket, chain by chain (pooled)

| chain | target | packet | baseline | outcome | packet ticks | baseline ticks | delta | packet submit | baseline submit |
|---|---|---|---|---|---:|---:|---:|---|---|
| box-jar-pond-black_thread | black thread | True | False | helps | 4 | 8 | -- | black thread | None |
| cabinet-box-pond-blue_feather | blue feather | True | False | helps | 4 | 8 | -- | blue feather | None |
| chest-drawer-basket-black_thread | black thread | True | False | helps | 4 | 8 | -- | black thread | None |
| pond-box-shelf-gold_bell | gold bell | True | False | helps | 4 | 8 | -- | gold bell | None |
| drawer-box-basket-red_stone | red stone | True | False | helps | 4 | 8 | -- | red stone | None |
| shelf-pond-cabinet-gold_bell | gold bell | True | False | helps | 4 | 8 | -- | gold bell | None |
| cabinet-drawer-shelf-gold_bell | gold bell | True | False | helps | 4 | 8 | -- | gold bell | None |
| chest-cabinet-drawer-green_leaf | green leaf | True | False | helps | 4 | 8 | -- | green leaf | None |
| drawer-basket-cabinet-amber_key | amber key | True | False | helps | 4 | 8 | -- | amber key | None |
| jar-chest-basket-black_thread | black thread | True | False | helps | 4 | 8 | -- | black thread | None |
| box-jar-pond-black_thread | black thread | True | False | helps | 4 | 8 | -- | black thread | None |
| cabinet-box-pond-blue_feather | blue feather | True | False | helps | 4 | 8 | -- | blue feather | None |
| chest-drawer-basket-black_thread | black thread | True | False | helps | 4 | 8 | -- | black thread | None |
| pond-box-shelf-gold_bell | gold bell | True | False | helps | 4 | 8 | -- | gold bell | None |
| drawer-box-basket-red_stone | red stone | True | False | helps | 4 | 8 | -- | red stone | None |
| shelf-pond-cabinet-gold_bell | gold bell | True | False | helps | 4 | 8 | -- | gold bell | None |
| cabinet-drawer-shelf-gold_bell | gold bell | True | False | helps | 4 | 8 | -- | gold bell | None |
| chest-cabinet-drawer-green_leaf | green leaf | True | False | helps | 4 | 8 | -- | green leaf | None |
| drawer-basket-cabinet-amber_key | amber key | True | False | helps | 4 | 8 | -- | amber key | None |
| jar-chest-basket-black_thread | black thread | True | False | helps | 4 | 8 | -- | black thread | None |
| box-jar-pond-black_thread | black thread | True | False | helps | 4 | 8 | -- | black thread | None |
| cabinet-box-pond-blue_feather | blue feather | True | False | helps | 4 | 8 | -- | blue feather | None |
| chest-drawer-basket-black_thread | black thread | True | False | helps | 4 | 8 | -- | black thread | None |
| pond-box-shelf-gold_bell | gold bell | True | False | helps | 4 | 8 | -- | gold bell | None |
| drawer-box-basket-red_stone | red stone | True | False | helps | 4 | 8 | -- | red stone | None |
| shelf-pond-cabinet-gold_bell | gold bell | True | False | helps | 4 | 8 | -- | gold bell | None |
| cabinet-drawer-shelf-gold_bell | gold bell | True | False | helps | 4 | 8 | -- | gold bell | None |
| chest-cabinet-drawer-green_leaf | green leaf | True | False | helps | 4 | 8 | -- | green leaf | None |
| drawer-basket-cabinet-amber_key | amber key | True | False | helps | 4 | 8 | -- | amber key | None |
| jar-chest-basket-black_thread | black thread | True | False | helps | 4 | 8 | -- | black thread | None |

### prefix-gfconst vs prefix-nopacket, chain by chain (pooled)

| chain | target | packet | baseline | outcome | packet ticks | baseline ticks | delta | packet submit | baseline submit |
|---|---|---|---|---|---:|---:|---:|---|---|
| box-jar-pond-black_thread | black thread | False | False | same | 4 | 8 | -- | green leaf | None |
| cabinet-box-pond-blue_feather | blue feather | False | False | same | 4 | 8 | -- | gold bell | None |
| chest-drawer-basket-black_thread | black thread | True | False | helps | 4 | 8 | -- | black thread | None |
| pond-box-shelf-gold_bell | gold bell | True | False | helps | 4 | 8 | -- | gold bell | None |
| drawer-box-basket-red_stone | red stone | True | False | helps | 4 | 8 | -- | red stone | None |
| shelf-pond-cabinet-gold_bell | gold bell | True | False | helps | 4 | 8 | -- | gold bell | None |
| cabinet-drawer-shelf-gold_bell | gold bell | True | False | helps | 4 | 8 | -- | gold bell | None |
| chest-cabinet-drawer-green_leaf | green leaf | True | False | helps | 4 | 8 | -- | green leaf | None |
| drawer-basket-cabinet-amber_key | amber key | True | False | helps | 4 | 8 | -- | amber key | None |
| jar-chest-basket-black_thread | black thread | False | False | same | 4 | 8 | -- | gold bell | None |
| box-jar-pond-black_thread | black thread | True | False | helps | 5 | 8 | -- | black thread | None |
| cabinet-box-pond-blue_feather | blue feather | False | False | same | 4 | 8 | -- | amber key | None |
| chest-drawer-basket-black_thread | black thread | True | False | helps | 4 | 8 | -- | black thread | None |
| pond-box-shelf-gold_bell | gold bell | True | False | helps | 5 | 8 | -- | gold bell | None |
| drawer-box-basket-red_stone | red stone | True | False | helps | 4 | 8 | -- | red stone | None |
| shelf-pond-cabinet-gold_bell | gold bell | True | False | helps | 4 | 8 | -- | gold bell | None |
| cabinet-drawer-shelf-gold_bell | gold bell | True | False | helps | 4 | 8 | -- | gold bell | None |
| chest-cabinet-drawer-green_leaf | green leaf | True | False | helps | 4 | 8 | -- | green leaf | None |
| drawer-basket-cabinet-amber_key | amber key | True | False | helps | 4 | 8 | -- | amber key | None |
| jar-chest-basket-black_thread | black thread | False | False | same | 4 | 8 | -- | amber key | None |
| box-jar-pond-black_thread | black thread | False | False | same | 4 | 8 | -- | green leaf | None |
| cabinet-box-pond-blue_feather | blue feather | False | False | same | 4 | 8 | -- | gold bell | None |
| chest-drawer-basket-black_thread | black thread | False | False | same | 4 | 8 | -- | blue feather | None |
| pond-box-shelf-gold_bell | gold bell | True | False | helps | 4 | 8 | -- | gold bell | None |
| drawer-box-basket-red_stone | red stone | True | False | helps | 4 | 8 | -- | red stone | None |
| shelf-pond-cabinet-gold_bell | gold bell | True | False | helps | 4 | 8 | -- | gold bell | None |
| cabinet-drawer-shelf-gold_bell | gold bell | True | False | helps | 4 | 8 | -- | gold bell | None |
| chest-cabinet-drawer-green_leaf | green leaf | False | False | same | 4 | 8 | -- | amber key | None |
| drawer-basket-cabinet-amber_key | amber key | False | False | same | 4 | 8 | -- | black thread | None |
| jar-chest-basket-black_thread | black thread | False | False | same | 4 | 8 | -- | gold bell | None |

### prefix-goalfirst vs prefix-nopacket, chain by chain (pooled)

| chain | target | packet | baseline | outcome | packet ticks | baseline ticks | delta | packet submit | baseline submit |
|---|---|---|---|---|---:|---:|---:|---|---|
| box-jar-pond-black_thread | black thread | True | False | helps | 4 | 8 | -- | black thread | None |
| cabinet-box-pond-blue_feather | blue feather | False | False | same | 4 | 8 | -- | amber key | None |
| chest-drawer-basket-black_thread | black thread | True | False | helps | 4 | 8 | -- | black thread | None |
| pond-box-shelf-gold_bell | gold bell | False | False | same | 4 | 8 | -- | amber key | None |
| drawer-box-basket-red_stone | red stone | False | False | same | 4 | 8 | -- | amber key | None |
| shelf-pond-cabinet-gold_bell | gold bell | True | False | helps | 4 | 8 | -- | gold bell | None |
| cabinet-drawer-shelf-gold_bell | gold bell | True | False | helps | 4 | 8 | -- | gold bell | None |
| chest-cabinet-drawer-green_leaf | green leaf | False | False | same | 4 | 8 | -- | amber key | None |
| drawer-basket-cabinet-amber_key | amber key | True | False | helps | 4 | 8 | -- | amber key | None |
| jar-chest-basket-black_thread | black thread | True | False | helps | 4 | 8 | -- | black thread | None |
| box-jar-pond-black_thread | black thread | True | False | helps | 4 | 8 | -- | black thread | None |
| cabinet-box-pond-blue_feather | blue feather | True | False | helps | 4 | 8 | -- | blue feather | None |
| chest-drawer-basket-black_thread | black thread | True | False | helps | 4 | 8 | -- | black thread | None |
| pond-box-shelf-gold_bell | gold bell | True | False | helps | 4 | 8 | -- | gold bell | None |
| drawer-box-basket-red_stone | red stone | True | False | helps | 4 | 8 | -- | red stone | None |
| shelf-pond-cabinet-gold_bell | gold bell | True | False | helps | 4 | 8 | -- | gold bell | None |
| cabinet-drawer-shelf-gold_bell | gold bell | True | False | helps | 4 | 8 | -- | gold bell | None |
| chest-cabinet-drawer-green_leaf | green leaf | True | False | helps | 4 | 8 | -- | green leaf | None |
| drawer-basket-cabinet-amber_key | amber key | True | False | helps | 4 | 8 | -- | amber key | None |
| jar-chest-basket-black_thread | black thread | True | False | helps | 4 | 8 | -- | black thread | None |
| box-jar-pond-black_thread | black thread | True | False | helps | 4 | 8 | -- | black thread | None |
| cabinet-box-pond-blue_feather | blue feather | True | False | helps | 4 | 8 | -- | blue feather | None |
| chest-drawer-basket-black_thread | black thread | True | False | helps | 4 | 8 | -- | black thread | None |
| pond-box-shelf-gold_bell | gold bell | True | False | helps | 4 | 8 | -- | gold bell | None |
| drawer-box-basket-red_stone | red stone | True | False | helps | 4 | 8 | -- | red stone | None |
| shelf-pond-cabinet-gold_bell | gold bell | True | False | helps | 4 | 8 | -- | gold bell | None |
| cabinet-drawer-shelf-gold_bell | gold bell | True | False | helps | 4 | 8 | -- | gold bell | None |
| chest-cabinet-drawer-green_leaf | green leaf | True | False | helps | 4 | 8 | -- | green leaf | None |
| drawer-basket-cabinet-amber_key | amber key | True | False | helps | 4 | 8 | -- | amber key | None |
| jar-chest-basket-black_thread | black thread | True | False | helps | 4 | 8 | -- | black thread | None |

## Bridges — five per seed, three rng streams

FIVE bridges per seed on THREE rng streams. Stream 1 is G1's: g6_splitdoor.run_g6's block verbatim, goal bridge first (trained only to place the rng, then discarded) and constant bridge second — GF-3r-g1's own G1 constant. The seeding is re-run and stream 2 is GF's: gf2b_mix's block, focus bridge first (discarded — no focus packet is delivered under this drive) and constant bridge second — GF-3r-g1's own GF constant. The seeding is re-run once more and stream 3 carries the NEW object: G1's constant recipe, same exchange and same examples, trained FIRST on its stream with no goal bridge in front of it. Exchange held, position changed.

| seed | bridge | rng stream | role | steps | final loss | final token accuracy |
|---|---|---|---|---:|---:|---:|
| 42 | g1_goal | stream 1 (G1's): random.Random(42) draw 1, torch.manual_seed(42) draw 1 | trained only to place the rng; DISCARDED | 7 | 0.0015 | 1.0000 |
| 42 | g1_constant | stream 1 (G1's): second bridge on the same random.Random object | the packet under arm prefix-g1const (GF-3r-g1's 1.00 reference) | 7 | 0.0011 | 1.0000 |
| 42 | focus | stream 2 (GF's): random.Random(42) re-seeded, torch.manual_seed(42) re-run | trained only to place the rng; DISCARDED (this drive carries no focus packet anywhere) | 7 | 0.0002 | 1.0000 |
| 42 | constant | stream 2 (GF's): second bridge on the same random.Random object | the packet under arm prefix-gfconst (GF-3r-g1's 0.63 reference) | 7 | 0.0008 | 1.0000 |
| 42 | goalfirst | stream 3 (NEW): random.Random(42) re-seeded, torch.manual_seed(42) re-run — FIRST bridge on the stream, no goal bridge in front of it | the packet under arm prefix-goalfirst: the GOAL exchange held, the stream position changed | 7 | 0.0007 | 1.0000 |
| 1042 | g1_goal | stream 1 (G1's): random.Random(1042) draw 1, torch.manual_seed(1042) draw 1 | trained only to place the rng; DISCARDED | 7 | 0.0007 | 1.0000 |
| 1042 | g1_constant | stream 1 (G1's): second bridge on the same random.Random object | the packet under arm prefix-g1const (GF-3r-g1's 1.00 reference) | 7 | 0.0010 | 1.0000 |
| 1042 | focus | stream 2 (GF's): random.Random(1042) re-seeded, torch.manual_seed(1042) re-run | trained only to place the rng; DISCARDED (this drive carries no focus packet anywhere) | 7 | 0.0002 | 1.0000 |
| 1042 | constant | stream 2 (GF's): second bridge on the same random.Random object | the packet under arm prefix-gfconst (GF-3r-g1's 0.63 reference) | 7 | 0.0036 | 1.0000 |
| 1042 | goalfirst | stream 3 (NEW): random.Random(1042) re-seeded, torch.manual_seed(1042) re-run — FIRST bridge on the stream, no goal bridge in front of it | the packet under arm prefix-goalfirst: the GOAL exchange held, the stream position changed | 7 | 0.0131 | 0.9934 |
| 2042 | g1_goal | stream 1 (G1's): random.Random(2042) draw 1, torch.manual_seed(2042) draw 1 | trained only to place the rng; DISCARDED | 7 | 0.0013 | 1.0000 |
| 2042 | g1_constant | stream 1 (G1's): second bridge on the same random.Random object | the packet under arm prefix-g1const (GF-3r-g1's 1.00 reference) | 7 | 0.0008 | 1.0000 |
| 2042 | focus | stream 2 (GF's): random.Random(2042) re-seeded, torch.manual_seed(2042) re-run | trained only to place the rng; DISCARDED (this drive carries no focus packet anywhere) | 7 | 0.0003 | 1.0000 |
| 2042 | constant | stream 2 (GF's): second bridge on the same random.Random object | the packet under arm prefix-gfconst (GF-3r-g1's 0.63 reference) | 7 | 0.0006 | 1.0000 |
| 2042 | goalfirst | stream 3 (NEW): random.Random(2042) re-seeded, torch.manual_seed(2042) re-run — FIRST bridge on the stream, no goal bridge in front of it | the packet under arm prefix-goalfirst: the GOAL exchange held, the stream position changed | 7 | 0.0132 | 0.9934 |

Recipes: g6_splitdoor.run_g6's train_bridge, verbatim (G1's recipe): gp.assignment_features, gp.ITEMS x 8 phrasings, the constant arm's goal-line coin flip included; gf2b_mix.run_gf2b's train_bridge, verbatim (GF's recipe): gf_focus.focus_features, the goal-FREE world, no coin flip; g6_splitdoor.run_g6's train_bridge, verbatim (G1's recipe): gp.assignment_features, gp.ITEMS x 8 phrasings, the constant arm's goal-line coin flip included — but trained FIRST on its stream.


## Invalid actions per packet arm, per seed (recorded only)

Rule: a packet arm's invalid actions DOMINATE a seed when invalid_actions >= 0.5 x that arm's decision points in that seed (decision points = the total number of ticks the arm's episodes took in that seed); recorded per seed, and under this drive it is RECORDED ONLY — GF-3r-d's readings are taken on all seeds.

| seed | arm | invalid actions | decision points | invalid share | dominates |
|---|---|---:|---:|---:|---|
| 42 | prefix-g1const | 0 | 40 | 0.00 | False |
| 42 | prefix-gfconst | 0 | 40 | 0.00 | False |
| 42 | prefix-goalfirst | 0 | 40 | 0.00 | False |
| 1042 | prefix-g1const | 0 | 40 | 0.00 | False |
| 1042 | prefix-gfconst | 4 | 42 | 0.10 | False |
| 1042 | prefix-goalfirst | 0 | 40 | 0.00 | False |
| 2042 | prefix-g1const | 0 | 40 | 0.00 | False |
| 2042 | prefix-gfconst | 0 | 40 | 0.00 | False |
| 2042 | prefix-goalfirst | 0 | 40 | 0.00 | False |

## Decision rules and the reading

These thresholds are the harness's operationalization of the registered prose readings. They are printed here, not hidden.

- `order`: (i) first, on the ALL-SEED pooled prefix-nopacket success — the registration calls arm 1 the decisive cell; then (ii), then (iii), then (iv) MIXED as the residue. The reference checks on prefix-g1const and prefix-gfconst are ALWAYS reported and never gate the reading
- `arms`: prefix-nopacket is the latent prefix with NO packet (the hooks are not armed at all); prefix-g1const, prefix-gfconst and prefix-goalfirst each carry ONE unmixed constant packet at the trained delivery dose 0.15
- `i_drive_not_needed`: pooled success_rate(prefix-nopacket) >= 0.90 — the prefix door stands alone and GF's constant actively hurts; Miso-scale resident-want designs drop the drive packet or validate it
- `ii_exchange`: pooled success_rate(prefix-nopacket) < 0.80 AND pooled success_rate(prefix-goalfirst) >= 0.90 — the door needs a drive and ANY goal-exchange drive will do
- `iii_position`: pooled success_rate(prefix-goalfirst) <= 0.70 — the drive must have been trained BEHIND a goal bridge; the pair, not the bridge, is the object
- `iv_mixed`: none of the above: prefix-goalfirst lands between the two references, recorded with the number
- `reference_checks`: GF-3r-g1 measured prefix-only over G1's constant at 1.00 pooled and over GF's at 0.63 pooled on exactly these bridges; this run reproduces a reference when its pooled rate is within 0.10 of that number. A failed reference check does not change the reading — it is reported beside it, because a run that does not reproduce them is measuring something else
- `breakdown`: a packet arm's invalid actions DOMINATE a seed when invalid_actions >= 0.5 x that arm's decision points in that seed (decision points = the total number of ticks the arm's episodes took in that seed); recorded per seed, and under this drive it is RECORDED ONLY — GF-3r-d's readings are taken on all seeds

| arm | packet | pooled success | successes | vs prefix-nopacket | done | invalid |
|---|---|---:|---:|---:|---:|---:|
| prefix-nopacket | none — no hook armed | 0.00 | 0/30 | +0.00 | 0.00 | 0 |
| prefix-g1const | G1 constant (goal exchange, 2nd on its stream) | 1.00 | 30/30 | +1.00 | 0.25 | 0 |
| prefix-gfconst | GF constant (focus exchange, 2nd on its stream) | 0.63 | 19/30 | +0.63 | 0.25 | 4 |
| prefix-goalfirst | goal-first constant (goal exchange, 1st on its stream) | 0.87 | 26/30 | +0.87 | 0.25 | 0 |

### Reference checks — does this run reproduce GF-3r-g1? (reported, never gating)

| arm | pooled success | GF-3r-g1 pooled | delta | tolerance | reproduces |
|---|---:|---:|---:|---:|---|
| prefix-g1const | 1.00 | 1.00 | +0.00 | 0.10 | True |
| prefix-gfconst | 0.63 | 0.63 | +0.00 | 0.10 | True |

| clause | value |
|---|---|
| (i) decisive cell — pooled prefix-nopacket success | 0.00 (bar 0.90) |
| pooled prefix-goalfirst success | 0.87 |
| both reference checks reproduce | True |
| seeds with a dominating invalid-action count | none |

**READING: iv-mixed** — MIXED — pooled prefix-nopacket 0.00 and prefix-goalfirst 0.87 satisfy none of (i), (ii) or (iii); the goal-first constant lands between the two references and the numbers are the finding.

## Transcripts

Every episode, in the order it ran. The goal never appears in any prompt: it is resident in the latent prefix.

```
Episode — arm: prefix-nopacket [none — no hook armed], seed 42, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(box) -> a note: check the jar
  tick 3: look(shelf) -> nothing of note
  tick 4: look(shelf) -> nothing of note
  tick 5: look(shelf) -> nothing of note
  tick 6: look(shelf) -> nothing of note
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: prefix-nopacket [none — no hook armed], seed 42, chain cabinet->box->pond, target: blue feather
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
Episode — arm: prefix-nopacket [none — no hook armed], seed 42, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: look(drawer) -> a note: try the basket
  tick 4: look(drawer) -> a note: try the basket
  tick 5: look(shelf) -> nothing of note
  tick 6: look(shelf) -> nothing of note
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: prefix-nopacket [none — no hook armed], seed 42, chain pond->box->shelf, target: gold bell
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
Episode — arm: prefix-nopacket [none — no hook armed], seed 42, chain drawer->box->basket, target: red stone
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
Episode — arm: prefix-nopacket [none — no hook armed], seed 42, chain shelf->pond->cabinet, target: gold bell
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
Episode — arm: prefix-nopacket [none — no hook armed], seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(cabinet) -> a note: check the drawer
  tick 3: look(cabinet) -> a note: check the drawer
  tick 4: look(cabinet) -> a note: check the drawer
  tick 5: look(cabinet) -> a note: check the drawer
  tick 6: look(cabinet) -> a note: check the drawer
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: prefix-nopacket [none — no hook armed], seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: look(cabinet) -> a note: try the drawer
  tick 4: look(cabinet) -> a note: try the drawer
  tick 5: look(cabinet) -> a note: try the drawer
  tick 6: look(cabinet) -> a note: try the drawer
  tick 7: look(cabinet) -> a note: try the drawer
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: prefix-nopacket [none — no hook armed], seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: look(drawer) -> a note: check the basket
  tick 4: look(shelf) -> nothing of note
  tick 5: look(shelf) -> nothing of note
  tick 6: look(shelf) -> nothing of note
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: prefix-nopacket [none — no hook armed], seed 42, chain jar->chest->basket, target: black thread
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
Episode — arm: prefix-nopacket [none — no hook armed], seed 1042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(box) -> a note: check the jar
  tick 3: look(shelf) -> nothing of note
  tick 4: look(shelf) -> nothing of note
  tick 5: look(shelf) -> nothing of note
  tick 6: look(shelf) -> nothing of note
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: prefix-nopacket [none — no hook armed], seed 1042, chain cabinet->box->pond, target: blue feather
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
Episode — arm: prefix-nopacket [none — no hook armed], seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: look(drawer) -> a note: try the basket
  tick 4: look(drawer) -> a note: try the basket
  tick 5: look(shelf) -> nothing of note
  tick 6: look(shelf) -> nothing of note
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: prefix-nopacket [none — no hook armed], seed 1042, chain pond->box->shelf, target: gold bell
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
Episode — arm: prefix-nopacket [none — no hook armed], seed 1042, chain drawer->box->basket, target: red stone
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
Episode — arm: prefix-nopacket [none — no hook armed], seed 1042, chain shelf->pond->cabinet, target: gold bell
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
Episode — arm: prefix-nopacket [none — no hook armed], seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(cabinet) -> a note: check the drawer
  tick 3: look(cabinet) -> a note: check the drawer
  tick 4: look(cabinet) -> a note: check the drawer
  tick 5: look(cabinet) -> a note: check the drawer
  tick 6: look(cabinet) -> a note: check the drawer
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: prefix-nopacket [none — no hook armed], seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: look(cabinet) -> a note: try the drawer
  tick 4: look(cabinet) -> a note: try the drawer
  tick 5: look(cabinet) -> a note: try the drawer
  tick 6: look(cabinet) -> a note: try the drawer
  tick 7: look(cabinet) -> a note: try the drawer
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: prefix-nopacket [none — no hook armed], seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: look(drawer) -> a note: check the basket
  tick 4: look(shelf) -> nothing of note
  tick 5: look(shelf) -> nothing of note
  tick 6: look(shelf) -> nothing of note
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: prefix-nopacket [none — no hook armed], seed 1042, chain jar->chest->basket, target: black thread
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
Episode — arm: prefix-nopacket [none — no hook armed], seed 2042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(box) -> a note: check the jar
  tick 3: look(shelf) -> nothing of note
  tick 4: look(shelf) -> nothing of note
  tick 5: look(shelf) -> nothing of note
  tick 6: look(shelf) -> nothing of note
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: prefix-nopacket [none — no hook armed], seed 2042, chain cabinet->box->pond, target: blue feather
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
Episode — arm: prefix-nopacket [none — no hook armed], seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: look(drawer) -> a note: try the basket
  tick 4: look(drawer) -> a note: try the basket
  tick 5: look(shelf) -> nothing of note
  tick 6: look(shelf) -> nothing of note
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: prefix-nopacket [none — no hook armed], seed 2042, chain pond->box->shelf, target: gold bell
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
Episode — arm: prefix-nopacket [none — no hook armed], seed 2042, chain drawer->box->basket, target: red stone
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
Episode — arm: prefix-nopacket [none — no hook armed], seed 2042, chain shelf->pond->cabinet, target: gold bell
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
Episode — arm: prefix-nopacket [none — no hook armed], seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(cabinet) -> a note: check the drawer
  tick 3: look(cabinet) -> a note: check the drawer
  tick 4: look(cabinet) -> a note: check the drawer
  tick 5: look(cabinet) -> a note: check the drawer
  tick 6: look(cabinet) -> a note: check the drawer
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 1/3, 8 of 8 ticks
```

```
Episode — arm: prefix-nopacket [none — no hook armed], seed 2042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: look(cabinet) -> a note: try the drawer
  tick 4: look(cabinet) -> a note: try the drawer
  tick 5: look(cabinet) -> a note: try the drawer
  tick 6: look(cabinet) -> a note: try the drawer
  tick 7: look(cabinet) -> a note: try the drawer
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: prefix-nopacket [none — no hook armed], seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: look(drawer) -> a note: check the basket
  tick 4: look(shelf) -> nothing of note
  tick 5: look(shelf) -> nothing of note
  tick 6: look(shelf) -> nothing of note
  tick 7: look(shelf) -> nothing of note
  tick 8: look(shelf) -> nothing of note
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: prefix-nopacket [none — no hook armed], seed 2042, chain jar->chest->basket, target: black thread
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
Episode — arm: prefix-g1const [G1 constant (goal exchange, 2nd on its stream)], seed 42, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-g1const [G1 constant (goal exchange, 2nd on its stream)], seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(blue feather) -> you submit: blue feather
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-g1const [G1 constant (goal exchange, 2nd on its stream)], seed 42, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-g1const [G1 constant (goal exchange, 2nd on its stream)], seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-g1const [G1 constant (goal exchange, 2nd on its stream)], seed 42, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-g1const [G1 constant (goal exchange, 2nd on its stream)], seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-g1const [G1 constant (goal exchange, 2nd on its stream)], seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-g1const [G1 constant (goal exchange, 2nd on its stream)], seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-g1const [G1 constant (goal exchange, 2nd on its stream)], seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-g1const [G1 constant (goal exchange, 2nd on its stream)], seed 42, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-g1const [G1 constant (goal exchange, 2nd on its stream)], seed 1042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-g1const [G1 constant (goal exchange, 2nd on its stream)], seed 1042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(blue feather) -> you submit: blue feather
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-g1const [G1 constant (goal exchange, 2nd on its stream)], seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-g1const [G1 constant (goal exchange, 2nd on its stream)], seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-g1const [G1 constant (goal exchange, 2nd on its stream)], seed 1042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-g1const [G1 constant (goal exchange, 2nd on its stream)], seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-g1const [G1 constant (goal exchange, 2nd on its stream)], seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-g1const [G1 constant (goal exchange, 2nd on its stream)], seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-g1const [G1 constant (goal exchange, 2nd on its stream)], seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-g1const [G1 constant (goal exchange, 2nd on its stream)], seed 1042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-g1const [G1 constant (goal exchange, 2nd on its stream)], seed 2042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-g1const [G1 constant (goal exchange, 2nd on its stream)], seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(blue feather) -> you submit: blue feather
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-g1const [G1 constant (goal exchange, 2nd on its stream)], seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-g1const [G1 constant (goal exchange, 2nd on its stream)], seed 2042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-g1const [G1 constant (goal exchange, 2nd on its stream)], seed 2042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-g1const [G1 constant (goal exchange, 2nd on its stream)], seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-g1const [G1 constant (goal exchange, 2nd on its stream)], seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-g1const [G1 constant (goal exchange, 2nd on its stream)], seed 2042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-g1const [G1 constant (goal exchange, 2nd on its stream)], seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-g1const [G1 constant (goal exchange, 2nd on its stream)], seed 2042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-gfconst [GF constant (focus exchange, 2nd on its stream)], seed 42, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(green leaf) -> you submit: green leaf
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-gfconst [GF constant (focus exchange, 2nd on its stream)], seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-gfconst [GF constant (focus exchange, 2nd on its stream)], seed 42, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-gfconst [GF constant (focus exchange, 2nd on its stream)], seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-gfconst [GF constant (focus exchange, 2nd on its stream)], seed 42, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-gfconst [GF constant (focus exchange, 2nd on its stream)], seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-gfconst [GF constant (focus exchange, 2nd on its stream)], seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-gfconst [GF constant (focus exchange, 2nd on its stream)], seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-gfconst [GF constant (focus exchange, 2nd on its stream)], seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-gfconst [GF constant (focus exchange, 2nd on its stream)], seed 42, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-gfconst [GF constant (focus exchange, 2nd on its stream)], seed 1042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: remember() -> that did not work
  tick 4: open(pond) -> you find: black thread and green leaf
  tick 5: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: prefix-gfconst [GF constant (focus exchange, 2nd on its stream)], seed 1042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: remember() -> that did not work
  tick 4: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 2/3, 4 of 8 ticks
```

```
Episode — arm: prefix-gfconst [GF constant (focus exchange, 2nd on its stream)], seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-gfconst [GF constant (focus exchange, 2nd on its stream)], seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: remember() -> that did not work
  tick 4: open(shelf) -> you find: blue feather and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: prefix-gfconst [GF constant (focus exchange, 2nd on its stream)], seed 1042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-gfconst [GF constant (focus exchange, 2nd on its stream)], seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-gfconst [GF constant (focus exchange, 2nd on its stream)], seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-gfconst [GF constant (focus exchange, 2nd on its stream)], seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-gfconst [GF constant (focus exchange, 2nd on its stream)], seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-gfconst [GF constant (focus exchange, 2nd on its stream)], seed 1042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: remember() -> that did not work
  tick 4: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 2/3, 4 of 8 ticks
```

```
Episode — arm: prefix-gfconst [GF constant (focus exchange, 2nd on its stream)], seed 2042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(green leaf) -> you submit: green leaf
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-gfconst [GF constant (focus exchange, 2nd on its stream)], seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-gfconst [GF constant (focus exchange, 2nd on its stream)], seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(blue feather) -> you submit: blue feather
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-gfconst [GF constant (focus exchange, 2nd on its stream)], seed 2042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-gfconst [GF constant (focus exchange, 2nd on its stream)], seed 2042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-gfconst [GF constant (focus exchange, 2nd on its stream)], seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-gfconst [GF constant (focus exchange, 2nd on its stream)], seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-gfconst [GF constant (focus exchange, 2nd on its stream)], seed 2042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-gfconst [GF constant (focus exchange, 2nd on its stream)], seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(black thread) -> you submit: black thread
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-gfconst [GF constant (focus exchange, 2nd on its stream)], seed 2042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-goalfirst [goal-first constant (goal exchange, 1st on its stream)], seed 42, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-goalfirst [goal-first constant (goal exchange, 1st on its stream)], seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-goalfirst [goal-first constant (goal exchange, 1st on its stream)], seed 42, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-goalfirst [goal-first constant (goal exchange, 1st on its stream)], seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-goalfirst [goal-first constant (goal exchange, 1st on its stream)], seed 42, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-goalfirst [goal-first constant (goal exchange, 1st on its stream)], seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-goalfirst [goal-first constant (goal exchange, 1st on its stream)], seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-goalfirst [goal-first constant (goal exchange, 1st on its stream)], seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-goalfirst [goal-first constant (goal exchange, 1st on its stream)], seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-goalfirst [goal-first constant (goal exchange, 1st on its stream)], seed 42, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-goalfirst [goal-first constant (goal exchange, 1st on its stream)], seed 1042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-goalfirst [goal-first constant (goal exchange, 1st on its stream)], seed 1042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(blue feather) -> you submit: blue feather
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-goalfirst [goal-first constant (goal exchange, 1st on its stream)], seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-goalfirst [goal-first constant (goal exchange, 1st on its stream)], seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-goalfirst [goal-first constant (goal exchange, 1st on its stream)], seed 1042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-goalfirst [goal-first constant (goal exchange, 1st on its stream)], seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-goalfirst [goal-first constant (goal exchange, 1st on its stream)], seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-goalfirst [goal-first constant (goal exchange, 1st on its stream)], seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-goalfirst [goal-first constant (goal exchange, 1st on its stream)], seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-goalfirst [goal-first constant (goal exchange, 1st on its stream)], seed 1042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-goalfirst [goal-first constant (goal exchange, 1st on its stream)], seed 2042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-goalfirst [goal-first constant (goal exchange, 1st on its stream)], seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(blue feather) -> you submit: blue feather
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-goalfirst [goal-first constant (goal exchange, 1st on its stream)], seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-goalfirst [goal-first constant (goal exchange, 1st on its stream)], seed 2042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-goalfirst [goal-first constant (goal exchange, 1st on its stream)], seed 2042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-goalfirst [goal-first constant (goal exchange, 1st on its stream)], seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-goalfirst [goal-first constant (goal exchange, 1st on its stream)], seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-goalfirst [goal-first constant (goal exchange, 1st on its stream)], seed 2042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-goalfirst [goal-first constant (goal exchange, 1st on its stream)], seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: prefix-goalfirst [goal-first constant (goal exchange, 1st on its stream)], seed 2042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

