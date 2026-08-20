# gf2b-packet-space-lean

Host machine `snappy`, device `mps`, budget 8, 2324.557 s. Registration: tracks/goal-pursuit/PLAN.md, GF-2b registration — the lean, constructed in the packet's own space (2026-08-16 afternoon).

The GF bridge pair, reproduced per seed by the registered recipe (training dose untouched at 0.15); the delivery fraction is FIXED at 0.15 in every cell and the axis is alpha, the weight on the FOCUS component. Two loci: `feature` mixes the taps on the bridge's input manifold and lets the focus bridge encode the mix; `payload` lets each bridge deliver its own packet and mixes the per-layer deltas elementwise at the injection site. The shuffled arm at a (locus, alpha) IS the other focus's cell in the same construction, so each cell is generated once and read by both arms.

What alpha moves, stated before the numbers are read: the injection normalizes whatever delta it is handed and rescales it by the position's own residual norm, so alpha turns the injected packet's DIRECTION and never its magnitude. The delivered dose is 0.15 at every alpha and at both loci — GF-2b dilutes what the packet says, not how loudly it says it, which is what makes this axis a different question from GF-2's fraction sweep.

Rows marked **cited: GF-2** are not rerun here: alpha 1.0 is GF-2's focus-packet cell at dose 0.15 and alpha 0.0 is GF-2's no-focus cell, both standing by greedy determinism per the registration. Source: `findings/goal-pursuit-gf2-230m.json` (git eacd5a19971e, device `mps`, generated 2026-08-16T19:17:06Z). At alpha 0.0 the focus and shuffled constructions coincide — the focus component has weight zero — so there is no focus-vs-shuffled contrast and the JS column is blank. The cited `pooled` rows are GF-2's own pooling over its three registered seeds, which is this run's seed set exactly when the registered seeds are run.

## The preregistered selector — per locus

### locus: feature

Rule: largest constructed alpha (feature locus) with pooled true-packet focused share <= 0.85 for BOTH focuses and pooled true-packet union done share >= 0.05.

**VERDICT: null — no constructed alpha satisfies both clauses.** No alpha in 0.75, 0.5, 0.25 keeps the focused share at or below 0.85 for both focuses while leaving the union done share at or above 0.05.

Recorded beside it, the strict-literal variant that reads BOTH clauses off the union mix: null.

| alpha | look share | open share | union done share | focused clause | done clause | selected |
|---|---:|---:|---:|---|---|---|
| 0.75 | 1.00 | 0.79 | 0.00 | fail | fail | no |
| 0.5 | 1.00 | 0.79 | 0.00 | fail | fail | no |
| 0.25 | 1.00 | 0.79 | 0.00 | fail | fail | no |

### locus: payload

Rule: largest constructed alpha (payload locus) with pooled true-packet focused share <= 0.85 for BOTH focuses and pooled true-packet union done share >= 0.05.

**VERDICT: alpha 0.25** — the largest constructed alpha that keeps the focused share at or below 0.85 for both focuses and the union done share at or above 0.05.

Recorded beside it, the strict-literal variant that reads BOTH clauses off the union mix: alpha 0.5.

| alpha | look share | open share | union done share | focused clause | done clause | selected |
|---|---:|---:|---:|---|---|---|
| 0.75 | 1.00 | 0.60 | 0.03 | fail | fail | no |
| 0.5 | 0.98 | 0.36 | 0.08 | fail | pass | no |
| 0.25 | 0.79 | 0.26 | 0.11 | pass | pass | **yes** |

## Headline — one table per locus, rows are alphas

Focused-tool share, signed JS against the SAME-(locus, alpha) shuffled arm (positive iff the focused tool's share rises under the true packet), first-tick focused rate, the done share and the repertoire count (tool categories above 0.05) — all under the true packet. The cited anchor rows bound the axis at both ends.

### locus: feature

| alpha | focus | seed | focused share | JS vs swapped (signed) | first-tick focused | done share | repertoire |
|---|---|---|---:|---:|---:|---:|---:|
| 1 (cited: GF-2) | look | 42 | 1.00 | +0.7039 | 1.00 | 0.00 | 1 |
| 1 (cited: GF-2) | look | 1042 | 1.00 | +1.0000 | 1.00 | 0.00 | 1 |
| 1 (cited: GF-2) | look | 2042 | 1.00 | +0.4821 | 1.00 | 0.00 | 1 |
| 1 (cited: GF-2) | look | pooled | 1.00 | +0.6875 | 1.00 | 0.00 | 1 |
| 0.75 | look | 42 | 1.00 | +0.7039 | 1.00 | 0.00 | 1 |
| 0.75 | look | 1042 | 1.00 | +1.0000 | 1.00 | 0.00 | 1 |
| 0.75 | look | 2042 | 1.00 | +0.4821 | 1.00 | 0.00 | 1 |
| 0.75 | look | pooled | 1.00 | +0.6875 | 1.00 | 0.00 | 1 |
| 0.5 | look | 42 | 1.00 | +0.7039 | 1.00 | 0.00 | 1 |
| 0.5 | look | 1042 | 1.00 | +1.0000 | 1.00 | 0.00 | 1 |
| 0.5 | look | 2042 | 1.00 | +0.4821 | 1.00 | 0.00 | 1 |
| 0.5 | look | pooled | 1.00 | +0.6875 | 1.00 | 0.00 | 1 |
| 0.25 | look | 42 | 1.00 | +0.7039 | 1.00 | 0.00 | 1 |
| 0.25 | look | 1042 | 1.00 | +1.0000 | 1.00 | 0.00 | 1 |
| 0.25 | look | 2042 | 1.00 | +0.4821 | 1.00 | 0.00 | 1 |
| 0.25 | look | pooled | 1.00 | +0.6875 | 1.00 | 0.00 | 1 |
| 0 (cited: GF-2) | look | 42 | 0.50 | -- | 1.00 | 0.25 | 3 |
| 0 (cited: GF-2) | look | 1042 | 0.50 | -- | 1.00 | 0.25 | 3 |
| 0 (cited: GF-2) | look | 2042 | 0.50 | -- | 1.00 | 0.25 | 3 |
| 0 (cited: GF-2) | look | pooled | 0.50 | -- | 1.00 | 0.25 | 3 |
| 1 (cited: GF-2) | open | 42 | 0.85 | +0.7039 | 1.00 | 0.01 | 2 |
| 1 (cited: GF-2) | open | 1042 | 1.00 | +1.0000 | 1.00 | 0.00 | 1 |
| 1 (cited: GF-2) | open | 2042 | 0.49 | +0.4821 | 0.60 | 0.01 | 3 |
| 1 (cited: GF-2) | open | pooled | 0.79 | +0.6875 | 0.87 | 0.01 | 3 |
| 0.75 | open | 42 | 0.85 | +0.7039 | 1.00 | 0.01 | 2 |
| 0.75 | open | 1042 | 1.00 | +1.0000 | 1.00 | 0.00 | 1 |
| 0.75 | open | 2042 | 0.49 | +0.4821 | 0.60 | 0.01 | 3 |
| 0.75 | open | pooled | 0.79 | +0.6875 | 0.87 | 0.01 | 3 |
| 0.5 | open | 42 | 0.85 | +0.7039 | 1.00 | 0.01 | 2 |
| 0.5 | open | 1042 | 1.00 | +1.0000 | 1.00 | 0.00 | 1 |
| 0.5 | open | 2042 | 0.49 | +0.4821 | 0.60 | 0.01 | 3 |
| 0.5 | open | pooled | 0.79 | +0.6875 | 0.87 | 0.01 | 3 |
| 0.25 | open | 42 | 0.85 | +0.7039 | 1.00 | 0.01 | 2 |
| 0.25 | open | 1042 | 1.00 | +1.0000 | 1.00 | 0.00 | 1 |
| 0.25 | open | 2042 | 0.49 | +0.4821 | 0.60 | 0.01 | 3 |
| 0.25 | open | pooled | 0.79 | +0.6875 | 0.87 | 0.01 | 3 |
| 0 (cited: GF-2) | open | 42 | 0.25 | -- | 0.00 | 0.25 | 3 |
| 0 (cited: GF-2) | open | 1042 | 0.25 | -- | 0.00 | 0.25 | 3 |
| 0 (cited: GF-2) | open | 2042 | 0.25 | -- | 0.00 | 0.25 | 3 |
| 0 (cited: GF-2) | open | pooled | 0.25 | -- | 0.00 | 0.25 | 3 |

### locus: payload

| alpha | focus | seed | focused share | JS vs swapped (signed) | first-tick focused | done share | repertoire |
|---|---|---|---:|---:|---:|---:|---:|
| 1 (cited: GF-2) | look | 42 | 1.00 | +0.7039 | 1.00 | 0.00 | 1 |
| 1 (cited: GF-2) | look | 1042 | 1.00 | +1.0000 | 1.00 | 0.00 | 1 |
| 1 (cited: GF-2) | look | 2042 | 1.00 | +0.4821 | 1.00 | 0.00 | 1 |
| 1 (cited: GF-2) | look | pooled | 1.00 | +0.6875 | 1.00 | 0.00 | 1 |
| 0.75 | look | 42 | 1.00 | +0.4803 | 1.00 | 0.00 | 1 |
| 0.75 | look | 1042 | 1.00 | +0.6433 | 1.00 | 0.00 | 1 |
| 0.75 | look | 2042 | 1.00 | +0.3113 | 1.00 | 0.00 | 1 |
| 0.75 | look | pooled | 1.00 | +0.4908 | 1.00 | 0.00 | 1 |
| 0.5 | look | 42 | 1.00 | +0.5136 | 1.00 | 0.00 | 1 |
| 0.5 | look | 1042 | 0.94 | +0.4073 | 1.00 | 0.00 | 2 |
| 0.5 | look | 2042 | 1.00 | +0.3569 | 1.00 | 0.00 | 1 |
| 0.5 | look | pooled | 0.98 | +0.4174 | 1.00 | 0.00 | 1 |
| 0.25 | look | 42 | 0.71 | +0.0963 | 1.00 | 0.03 | 2 |
| 0.25 | look | 1042 | 0.69 | +0.0560 | 1.00 | 0.06 | 3 |
| 0.25 | look | 2042 | 0.96 | +0.2840 | 1.00 | 0.00 | 1 |
| 0.25 | look | pooled | 0.79 | +0.1154 | 1.00 | 0.03 | 2 |
| 0 (cited: GF-2) | look | 42 | 0.50 | -- | 1.00 | 0.25 | 3 |
| 0 (cited: GF-2) | look | 1042 | 0.50 | -- | 1.00 | 0.25 | 3 |
| 0 (cited: GF-2) | look | 2042 | 0.50 | -- | 1.00 | 0.25 | 3 |
| 0 (cited: GF-2) | look | pooled | 0.50 | -- | 1.00 | 0.25 | 3 |
| 1 (cited: GF-2) | open | 42 | 0.85 | +0.7039 | 1.00 | 0.01 | 2 |
| 1 (cited: GF-2) | open | 1042 | 1.00 | +1.0000 | 1.00 | 0.00 | 1 |
| 1 (cited: GF-2) | open | 2042 | 0.49 | +0.4821 | 0.60 | 0.01 | 3 |
| 1 (cited: GF-2) | open | pooled | 0.79 | +0.6875 | 0.87 | 0.01 | 3 |
| 0.75 | open | 42 | 0.44 | +0.4803 | 1.00 | 0.25 | 3 |
| 0.75 | open | 1042 | 0.79 | +0.6433 | 1.00 | 0.00 | 2 |
| 0.75 | open | 2042 | 0.40 | +0.3113 | 0.50 | 0.10 | 3 |
| 0.75 | open | pooled | 0.60 | +0.4908 | 0.83 | 0.08 | 3 |
| 0.5 | open | 42 | 0.41 | +0.5136 | 0.50 | 0.31 | 3 |
| 0.5 | open | 1042 | 0.38 | +0.4073 | 0.50 | 0.21 | 3 |
| 0.5 | open | 2042 | 0.31 | +0.3569 | 0.00 | 0.25 | 3 |
| 0.5 | open | pooled | 0.36 | +0.4174 | 0.33 | 0.25 | 3 |
| 0.25 | open | 42 | 0.26 | -0.0963 | 0.00 | 0.26 | 3 |
| 0.25 | open | 1042 | 0.25 | -0.0560 | 0.00 | 0.25 | 3 |
| 0.25 | open | 2042 | 0.28 | +0.2840 | 0.00 | 0.28 | 3 |
| 0.25 | open | pooled | 0.26 | +0.1154 | 0.00 | 0.26 | 3 |
| 0 (cited: GF-2) | open | 42 | 0.25 | -- | 0.00 | 0.25 | 3 |
| 0 (cited: GF-2) | open | 1042 | 0.25 | -- | 0.00 | 0.25 | 3 |
| 0 (cited: GF-2) | open | 2042 | 0.25 | -- | 0.00 | 0.25 | 3 |
| 0 (cited: GF-2) | open | pooled | 0.25 | -- | 0.00 | 0.25 | 3 |

## Paired first tick — the constructed packet vs the same-(locus, alpha) shuffled construction, chain by chain

| locus | alpha | seed | focus | wins | losses | ties |
|---|---|---|---|---:|---:|---:|
| feature | 0.75 | 42 | look | 10 | 0 | 0 |
| feature | 0.75 | 1042 | look | 10 | 0 | 0 |
| feature | 0.75 | 2042 | look | 6 | 0 | 4 |
| feature | 0.75 | pooled | look | 26 | 0 | 4 |
| feature | 0.75 | 42 | open | 10 | 0 | 0 |
| feature | 0.75 | 1042 | open | 10 | 0 | 0 |
| feature | 0.75 | 2042 | open | 6 | 0 | 4 |
| feature | 0.75 | pooled | open | 26 | 0 | 4 |
| feature | 0.5 | 42 | look | 10 | 0 | 0 |
| feature | 0.5 | 1042 | look | 10 | 0 | 0 |
| feature | 0.5 | 2042 | look | 6 | 0 | 4 |
| feature | 0.5 | pooled | look | 26 | 0 | 4 |
| feature | 0.5 | 42 | open | 10 | 0 | 0 |
| feature | 0.5 | 1042 | open | 10 | 0 | 0 |
| feature | 0.5 | 2042 | open | 6 | 0 | 4 |
| feature | 0.5 | pooled | open | 26 | 0 | 4 |
| feature | 0.25 | 42 | look | 10 | 0 | 0 |
| feature | 0.25 | 1042 | look | 10 | 0 | 0 |
| feature | 0.25 | 2042 | look | 6 | 0 | 4 |
| feature | 0.25 | pooled | look | 26 | 0 | 4 |
| feature | 0.25 | 42 | open | 10 | 0 | 0 |
| feature | 0.25 | 1042 | open | 10 | 0 | 0 |
| feature | 0.25 | 2042 | open | 6 | 0 | 4 |
| feature | 0.25 | pooled | open | 26 | 0 | 4 |
| payload | 0.75 | 42 | look | 10 | 0 | 0 |
| payload | 0.75 | 1042 | look | 10 | 0 | 0 |
| payload | 0.75 | 2042 | look | 5 | 0 | 5 |
| payload | 0.75 | pooled | look | 25 | 0 | 5 |
| payload | 0.75 | 42 | open | 10 | 0 | 0 |
| payload | 0.75 | 1042 | open | 10 | 0 | 0 |
| payload | 0.75 | 2042 | open | 5 | 0 | 5 |
| payload | 0.75 | pooled | open | 25 | 0 | 5 |
| payload | 0.5 | 42 | look | 5 | 0 | 5 |
| payload | 0.5 | 1042 | look | 5 | 0 | 5 |
| payload | 0.5 | 2042 | look | 0 | 0 | 10 |
| payload | 0.5 | pooled | look | 10 | 0 | 20 |
| payload | 0.5 | 42 | open | 5 | 0 | 5 |
| payload | 0.5 | 1042 | open | 5 | 0 | 5 |
| payload | 0.5 | 2042 | open | 0 | 0 | 10 |
| payload | 0.5 | pooled | open | 10 | 0 | 20 |
| payload | 0.25 | 42 | look | 0 | 0 | 10 |
| payload | 0.25 | 1042 | look | 0 | 0 | 10 |
| payload | 0.25 | 2042 | look | 0 | 0 | 10 |
| payload | 0.25 | pooled | look | 0 | 0 | 30 |
| payload | 0.25 | 42 | open | 0 | 0 | 10 |
| payload | 0.25 | 1042 | open | 0 | 0 | 10 |
| payload | 0.25 | 2042 | open | 0 | 0 | 10 |
| payload | 0.25 | pooled | open | 0 | 0 | 30 |

## Tool mix — pooled shares over all decision points, constructed packet

| locus | alpha | focus | look | open | done | other |
|---|---|---|---:|---:|---:|---:|
| feature | 0.75 | look | 1.00 | 0.00 | 0.00 | 0.00 |
| feature | 0.75 | open | 0.14 | 0.79 | 0.01 | 0.06 |
| feature | 0.5 | look | 1.00 | 0.00 | 0.00 | 0.00 |
| feature | 0.5 | open | 0.14 | 0.79 | 0.01 | 0.06 |
| feature | 0.25 | look | 1.00 | 0.00 | 0.00 | 0.00 |
| feature | 0.25 | open | 0.14 | 0.79 | 0.01 | 0.06 |
| payload | 0.75 | look | 1.00 | 0.00 | 0.00 | 0.00 |
| payload | 0.75 | open | 0.30 | 0.60 | 0.08 | 0.02 |
| payload | 0.5 | look | 0.98 | 0.00 | 0.00 | 0.02 |
| payload | 0.5 | open | 0.38 | 0.36 | 0.25 | 0.00 |
| payload | 0.25 | look | 0.79 | 0.18 | 0.03 | 0.00 |
| payload | 0.25 | open | 0.47 | 0.26 | 0.26 | 0.00 |
| -- | 1 (cited: GF-2) | look | 1.00 | 0.00 | 0.00 | 0.00 |
| -- | 1 (cited: GF-2) | open | 0.14 | 0.79 | 0.01 | 0.06 |
| -- | 0 (cited: GF-2) | no-focus | 0.50 | 0.25 | 0.25 | 0.00 |

## Transcripts

Every generated episode of this run; the cited anchor cells live in GF-2's artifact and are not reproduced here.

```
Episode — arm: feature mix [look], alpha 0.75, seed 42, chain box->jar->pond, target: black thread
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
Episode — arm: feature mix [look], alpha 0.75, seed 42, chain cabinet->box->pond, target: blue feather
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
Episode — arm: feature mix [look], alpha 0.75, seed 42, chain chest->drawer->basket, target: black thread
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
Episode — arm: feature mix [look], alpha 0.75, seed 42, chain pond->box->shelf, target: gold bell
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
Episode — arm: feature mix [look], alpha 0.75, seed 42, chain drawer->box->basket, target: red stone
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
Episode — arm: feature mix [look], alpha 0.75, seed 42, chain shelf->pond->cabinet, target: gold bell
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
Episode — arm: feature mix [look], alpha 0.75, seed 42, chain cabinet->drawer->shelf, target: gold bell
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
Episode — arm: feature mix [look], alpha 0.75, seed 42, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: feature mix [look], alpha 0.75, seed 42, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: feature mix [look], alpha 0.75, seed 42, chain jar->chest->basket, target: black thread
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
Episode — arm: feature mix [open], alpha 0.75, seed 42, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 3 of 8 ticks
```

```
Episode — arm: feature mix [open], alpha 0.75, seed 42, chain cabinet->box->pond, target: blue feather
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
Episode — arm: feature mix [open], alpha 0.75, seed 42, chain chest->drawer->basket, target: black thread
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
Episode — arm: feature mix [open], alpha 0.75, seed 42, chain pond->box->shelf, target: gold bell
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
Episode — arm: feature mix [open], alpha 0.75, seed 42, chain drawer->box->basket, target: red stone
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
Episode — arm: feature mix [open], alpha 0.75, seed 42, chain shelf->pond->cabinet, target: gold bell
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
Episode — arm: feature mix [open], alpha 0.75, seed 42, chain cabinet->drawer->shelf, target: gold bell
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
Episode — arm: feature mix [open], alpha 0.75, seed 42, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: feature mix [open], alpha 0.75, seed 42, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: feature mix [open], alpha 0.75, seed 42, chain jar->chest->basket, target: black thread
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
Episode — arm: feature mix [look], alpha 0.5, seed 42, chain box->jar->pond, target: black thread
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
Episode — arm: feature mix [look], alpha 0.5, seed 42, chain cabinet->box->pond, target: blue feather
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
Episode — arm: feature mix [look], alpha 0.5, seed 42, chain chest->drawer->basket, target: black thread
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
Episode — arm: feature mix [look], alpha 0.5, seed 42, chain pond->box->shelf, target: gold bell
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
Episode — arm: feature mix [look], alpha 0.5, seed 42, chain drawer->box->basket, target: red stone
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
Episode — arm: feature mix [look], alpha 0.5, seed 42, chain shelf->pond->cabinet, target: gold bell
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
Episode — arm: feature mix [look], alpha 0.5, seed 42, chain cabinet->drawer->shelf, target: gold bell
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
Episode — arm: feature mix [look], alpha 0.5, seed 42, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: feature mix [look], alpha 0.5, seed 42, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: feature mix [look], alpha 0.5, seed 42, chain jar->chest->basket, target: black thread
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
Episode — arm: feature mix [open], alpha 0.5, seed 42, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 3 of 8 ticks
```

```
Episode — arm: feature mix [open], alpha 0.5, seed 42, chain cabinet->box->pond, target: blue feather
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
Episode — arm: feature mix [open], alpha 0.5, seed 42, chain chest->drawer->basket, target: black thread
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
Episode — arm: feature mix [open], alpha 0.5, seed 42, chain pond->box->shelf, target: gold bell
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
Episode — arm: feature mix [open], alpha 0.5, seed 42, chain drawer->box->basket, target: red stone
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
Episode — arm: feature mix [open], alpha 0.5, seed 42, chain shelf->pond->cabinet, target: gold bell
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
Episode — arm: feature mix [open], alpha 0.5, seed 42, chain cabinet->drawer->shelf, target: gold bell
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
Episode — arm: feature mix [open], alpha 0.5, seed 42, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: feature mix [open], alpha 0.5, seed 42, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: feature mix [open], alpha 0.5, seed 42, chain jar->chest->basket, target: black thread
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
Episode — arm: feature mix [look], alpha 0.25, seed 42, chain box->jar->pond, target: black thread
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
Episode — arm: feature mix [look], alpha 0.25, seed 42, chain cabinet->box->pond, target: blue feather
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
Episode — arm: feature mix [look], alpha 0.25, seed 42, chain chest->drawer->basket, target: black thread
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
Episode — arm: feature mix [look], alpha 0.25, seed 42, chain pond->box->shelf, target: gold bell
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
Episode — arm: feature mix [look], alpha 0.25, seed 42, chain drawer->box->basket, target: red stone
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
Episode — arm: feature mix [look], alpha 0.25, seed 42, chain shelf->pond->cabinet, target: gold bell
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
Episode — arm: feature mix [look], alpha 0.25, seed 42, chain cabinet->drawer->shelf, target: gold bell
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
Episode — arm: feature mix [look], alpha 0.25, seed 42, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: feature mix [look], alpha 0.25, seed 42, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: feature mix [look], alpha 0.25, seed 42, chain jar->chest->basket, target: black thread
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
Episode — arm: feature mix [open], alpha 0.25, seed 42, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 3 of 8 ticks
```

```
Episode — arm: feature mix [open], alpha 0.25, seed 42, chain cabinet->box->pond, target: blue feather
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
Episode — arm: feature mix [open], alpha 0.25, seed 42, chain chest->drawer->basket, target: black thread
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
Episode — arm: feature mix [open], alpha 0.25, seed 42, chain pond->box->shelf, target: gold bell
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
Episode — arm: feature mix [open], alpha 0.25, seed 42, chain drawer->box->basket, target: red stone
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
Episode — arm: feature mix [open], alpha 0.25, seed 42, chain shelf->pond->cabinet, target: gold bell
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
Episode — arm: feature mix [open], alpha 0.25, seed 42, chain cabinet->drawer->shelf, target: gold bell
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
Episode — arm: feature mix [open], alpha 0.25, seed 42, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: feature mix [open], alpha 0.25, seed 42, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: feature mix [open], alpha 0.25, seed 42, chain jar->chest->basket, target: black thread
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
Episode — arm: payload mix [look], alpha 0.75, seed 42, chain box->jar->pond, target: black thread
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
Episode — arm: payload mix [look], alpha 0.75, seed 42, chain cabinet->box->pond, target: blue feather
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
Episode — arm: payload mix [look], alpha 0.75, seed 42, chain chest->drawer->basket, target: black thread
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
Episode — arm: payload mix [look], alpha 0.75, seed 42, chain pond->box->shelf, target: gold bell
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
Episode — arm: payload mix [look], alpha 0.75, seed 42, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: look(basket) -> the basket is closed; something is inside
  tick 4: look(basket) -> the basket is closed; something is inside
  tick 5: look(basket) -> the basket is closed; something is inside
  tick 6: look(basket) -> the basket is closed; something is inside
  tick 7: look(basket) -> the basket is closed; something is inside
  tick 8: look(box) -> a note: try the basket
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.75, seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: look(cabinet) -> the cabinet is closed; something is inside
  tick 5: look(cabinet) -> the cabinet is closed; something is inside
  tick 6: look(pond) -> a note: try the cabinet
  tick 7: look(cabinet) -> the cabinet is closed; something is inside
  tick 8: look(cabinet) -> the cabinet is closed; something is inside
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.75, seed 42, chain cabinet->drawer->shelf, target: gold bell
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
Episode — arm: payload mix [look], alpha 0.75, seed 42, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: payload mix [look], alpha 0.75, seed 42, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: payload mix [look], alpha 0.75, seed 42, chain jar->chest->basket, target: black thread
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
Episode — arm: payload mix [open], alpha 0.75, seed 42, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.75, seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: open(cabinet) -> empty
  tick 2: done(cabinet) -> you submit: (nothing)
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.75, seed 42, chain chest->drawer->basket, target: black thread
  tick 1: open(chest) -> empty
  tick 2: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.75, seed 42, chain pond->box->shelf, target: gold bell
  tick 1: open(key) -> that is not a place here
  tick 2: look(pond) -> a note: check the box
  tick 3: open(box) -> empty
  tick 4: look(box) -> a note: try the shelf
  tick 5: look(shelf) -> the shelf is closed; something is inside
  tick 6: open(shelf) -> you find: blue feather and gold bell
  tick 7: look(feather) -> that is not a place here
  tick 8: look(feather) -> that is not a place here
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.75, seed 42, chain drawer->box->basket, target: red stone
  tick 1: open(drawer) -> empty
  tick 2: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.75, seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: open(shelf) -> empty
  tick 2: done(empty) -> you submit: (nothing)
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.75, seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: open(cabinet) -> empty
  tick 2: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.75, seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: open(key) -> that is not a place here
  tick 2: look(chest) -> a note: check the cabinet
  tick 3: open(cabinet) -> empty
  tick 4: look(cabinet) -> a note: try the drawer
  tick 5: look(drawer) -> the drawer is closed; something is inside
  tick 6: open(drawer) -> you find: green leaf and amber key
  tick 7: look(drawer) -> the drawer is closed; something is inside
  tick 8: look(drawer) -> the drawer is closed; something is inside
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.75, seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: open(drawer) -> empty
  tick 2: done(amber key) -> you submit: amber key
  PASS — depth 0/3, 2 of 8 ticks, guessed
```

```
Episode — arm: payload mix [open], alpha 0.75, seed 42, chain jar->chest->basket, target: black thread
  tick 1: open(jar) -> empty
  tick 2: done(empty) -> you submit: (nothing)
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.5, seed 42, chain box->jar->pond, target: black thread
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
Episode — arm: payload mix [look], alpha 0.5, seed 42, chain cabinet->box->pond, target: blue feather
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
Episode — arm: payload mix [look], alpha 0.5, seed 42, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: look(basket) -> the basket is closed; something is inside
  tick 4: look(basket) -> the basket is closed; something is inside
  tick 5: look(basket) -> the basket is closed; something is inside
  tick 6: look(basket) -> the basket is closed; something is inside
  tick 7: look(basket) -> the basket is closed; something is inside
  tick 8: look(drawer) -> a note: try the basket
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.5, seed 42, chain pond->box->shelf, target: gold bell
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
Episode — arm: payload mix [look], alpha 0.5, seed 42, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: look(basket) -> the basket is closed; something is inside
  tick 4: look(basket) -> the basket is closed; something is inside
  tick 5: look(basket) -> the basket is closed; something is inside
  tick 6: look(basket) -> the basket is closed; something is inside
  tick 7: look(basket) -> the basket is closed; something is inside
  tick 8: look(box) -> a note: try the basket
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.5, seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: look(cabinet) -> the cabinet is closed; something is inside
  tick 5: look(cabinet) -> the cabinet is closed; something is inside
  tick 6: look(cabinet) -> the cabinet is closed; something is inside
  tick 7: look(cabinet) -> the cabinet is closed; something is inside
  tick 8: look(cabinet) -> the cabinet is closed; something is inside
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.5, seed 42, chain cabinet->drawer->shelf, target: gold bell
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
Episode — arm: payload mix [look], alpha 0.5, seed 42, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: payload mix [look], alpha 0.5, seed 42, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: payload mix [look], alpha 0.5, seed 42, chain jar->chest->basket, target: black thread
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
Episode — arm: payload mix [open], alpha 0.5, seed 42, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.5, seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: open(box) -> empty
  tick 3: done(empty) -> you submit: empty
  FAIL (wrong submit) — depth 1/3, 3 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.5, seed 42, chain chest->drawer->basket, target: black thread
  tick 1: open(chest) -> empty
  tick 2: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.5, seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: open(box) -> empty
  tick 3: done(empty) -> you submit: empty
  FAIL (wrong submit) — depth 1/3, 3 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.5, seed 42, chain drawer->box->basket, target: red stone
  tick 1: open(drawer) -> empty
  tick 2: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.5, seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: open(pond) -> empty
  tick 3: look(pond) -> a note: try the cabinet
  tick 4: open(cabinet) -> you find: blue feather and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.5, seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: open(cabinet) -> empty
  tick 2: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.5, seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: open(cabinet) -> empty
  tick 3: look(cabinet) -> a note: try the drawer
  tick 4: open(drawer) -> you find: green leaf and amber key
  tick 5: look(drawer) -> the drawer is closed; something is inside
  tick 6: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 6 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.5, seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: open(drawer) -> empty
  tick 2: done(amber key) -> you submit: amber key
  PASS — depth 0/3, 2 of 8 ticks, guessed
```

```
Episode — arm: payload mix [open], alpha 0.5, seed 42, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: open(chest) -> empty
  tick 3: look(chest) -> a note: try the basket
  tick 4: open(basket) -> you find: black thread and gold bell
  tick 5: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 5 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.25, seed 42, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: look(green leaf) -> that is not a place here
  tick 5: look(green leaf) -> that is not a place here
  tick 6: open(green leaf) -> that is not a place here
  tick 7: look(green leaf) -> that is not a place here
  tick 8: look(green leaf) -> that is not a place here
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.25, seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(blue feather) -> you submit: blue feather
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.25, seed 42, chain chest->drawer->basket, target: black thread
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
Episode — arm: payload mix [look], alpha 0.25, seed 42, chain pond->box->shelf, target: gold bell
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
Episode — arm: payload mix [look], alpha 0.25, seed 42, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: look(basket) -> the basket is closed; something is inside
  tick 5: look(basket) -> the basket is closed; something is inside
  tick 6: open(basket) -> you find: red stone and blue feather
  tick 7: look(basket) -> the basket is closed; something is inside
  tick 8: look(basket) -> the basket is closed; something is inside
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.25, seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: look(cabinet) -> the cabinet is closed; something is inside
  tick 5: open(cabinet) -> you find: blue feather and gold bell
  tick 6: look(cabinet) -> the cabinet is closed; something is inside
  tick 7: look(cabinet) -> the cabinet is closed; something is inside
  tick 8: open(cabinet) -> you find: blue feather and gold bell
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.25, seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: look(drawer) -> a note: try the shelf
  tick 5: open(shelf) -> you find: black thread and gold bell
  tick 6: look(drawer) -> a note: try the shelf
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.25, seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.25, seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: look(cabinet) -> the cabinet is closed; something is inside
  tick 5: look(cabinet) -> the cabinet is closed; something is inside
  tick 6: open(cabinet) -> you find: amber key and black thread
  tick 7: look(cabinet) -> the cabinet is closed; something is inside
  tick 8: look(cabinet) -> the cabinet is closed; something is inside
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.25, seed 42, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: look(basket) -> the basket is closed; something is inside
  tick 5: look(basket) -> the basket is closed; something is inside
  tick 6: open(basket) -> you find: black thread and gold bell
  tick 7: look(thread) -> that is not a place here
  tick 8: look(thread) -> that is not a place here
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.25, seed 42, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: open(jar) -> empty
  tick 3: look(jar) -> a note: try the pond
  tick 4: done(pond) -> you submit: pond
  FAIL (wrong submit) — depth 2/3, 4 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.25, seed 42, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(blue feather) -> you submit: blue feather
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.25, seed 42, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.25, seed 42, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(blue feather) -> you submit: blue feather
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.25, seed 42, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: open(box) -> empty
  tick 3: done(empty) -> you submit: empty
  FAIL (wrong submit) — depth 1/3, 3 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.25, seed 42, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.25, seed 42, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: open(drawer) -> empty
  tick 3: done(empty) -> you submit: empty
  FAIL (wrong submit) — depth 1/3, 3 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.25, seed 42, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.25, seed 42, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: open(basket) -> empty
  tick 3: look(basket) -> a note: try the cabinet
  tick 4: done(cabinet) -> you submit: cabinet
  FAIL (wrong submit) — depth 2/3, 4 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.25, seed 42, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: feature mix [look], alpha 0.75, seed 1042, chain box->jar->pond, target: black thread
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
Episode — arm: feature mix [look], alpha 0.75, seed 1042, chain cabinet->box->pond, target: blue feather
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
Episode — arm: feature mix [look], alpha 0.75, seed 1042, chain chest->drawer->basket, target: black thread
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
Episode — arm: feature mix [look], alpha 0.75, seed 1042, chain pond->box->shelf, target: gold bell
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
Episode — arm: feature mix [look], alpha 0.75, seed 1042, chain drawer->box->basket, target: red stone
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
Episode — arm: feature mix [look], alpha 0.75, seed 1042, chain shelf->pond->cabinet, target: gold bell
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
Episode — arm: feature mix [look], alpha 0.75, seed 1042, chain cabinet->drawer->shelf, target: gold bell
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
Episode — arm: feature mix [look], alpha 0.75, seed 1042, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: feature mix [look], alpha 0.75, seed 1042, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: feature mix [look], alpha 0.75, seed 1042, chain jar->chest->basket, target: black thread
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
Episode — arm: feature mix [open], alpha 0.75, seed 1042, chain box->jar->pond, target: black thread
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
Episode — arm: feature mix [open], alpha 0.75, seed 1042, chain cabinet->box->pond, target: blue feather
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
Episode — arm: feature mix [open], alpha 0.75, seed 1042, chain chest->drawer->basket, target: black thread
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
Episode — arm: feature mix [open], alpha 0.75, seed 1042, chain pond->box->shelf, target: gold bell
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
Episode — arm: feature mix [open], alpha 0.75, seed 1042, chain drawer->box->basket, target: red stone
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
Episode — arm: feature mix [open], alpha 0.75, seed 1042, chain shelf->pond->cabinet, target: gold bell
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
Episode — arm: feature mix [open], alpha 0.75, seed 1042, chain cabinet->drawer->shelf, target: gold bell
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
Episode — arm: feature mix [open], alpha 0.75, seed 1042, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: feature mix [open], alpha 0.75, seed 1042, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: feature mix [open], alpha 0.75, seed 1042, chain jar->chest->basket, target: black thread
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
Episode — arm: feature mix [look], alpha 0.5, seed 1042, chain box->jar->pond, target: black thread
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
Episode — arm: feature mix [look], alpha 0.5, seed 1042, chain cabinet->box->pond, target: blue feather
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
Episode — arm: feature mix [look], alpha 0.5, seed 1042, chain chest->drawer->basket, target: black thread
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
Episode — arm: feature mix [look], alpha 0.5, seed 1042, chain pond->box->shelf, target: gold bell
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
Episode — arm: feature mix [look], alpha 0.5, seed 1042, chain drawer->box->basket, target: red stone
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
Episode — arm: feature mix [look], alpha 0.5, seed 1042, chain shelf->pond->cabinet, target: gold bell
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
Episode — arm: feature mix [look], alpha 0.5, seed 1042, chain cabinet->drawer->shelf, target: gold bell
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
Episode — arm: feature mix [look], alpha 0.5, seed 1042, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: feature mix [look], alpha 0.5, seed 1042, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: feature mix [look], alpha 0.5, seed 1042, chain jar->chest->basket, target: black thread
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
Episode — arm: feature mix [open], alpha 0.5, seed 1042, chain box->jar->pond, target: black thread
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
Episode — arm: feature mix [open], alpha 0.5, seed 1042, chain cabinet->box->pond, target: blue feather
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
Episode — arm: feature mix [open], alpha 0.5, seed 1042, chain chest->drawer->basket, target: black thread
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
Episode — arm: feature mix [open], alpha 0.5, seed 1042, chain pond->box->shelf, target: gold bell
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
Episode — arm: feature mix [open], alpha 0.5, seed 1042, chain drawer->box->basket, target: red stone
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
Episode — arm: feature mix [open], alpha 0.5, seed 1042, chain shelf->pond->cabinet, target: gold bell
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
Episode — arm: feature mix [open], alpha 0.5, seed 1042, chain cabinet->drawer->shelf, target: gold bell
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
Episode — arm: feature mix [open], alpha 0.5, seed 1042, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: feature mix [open], alpha 0.5, seed 1042, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: feature mix [open], alpha 0.5, seed 1042, chain jar->chest->basket, target: black thread
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
Episode — arm: feature mix [look], alpha 0.25, seed 1042, chain box->jar->pond, target: black thread
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
Episode — arm: feature mix [look], alpha 0.25, seed 1042, chain cabinet->box->pond, target: blue feather
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
Episode — arm: feature mix [look], alpha 0.25, seed 1042, chain chest->drawer->basket, target: black thread
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
Episode — arm: feature mix [look], alpha 0.25, seed 1042, chain pond->box->shelf, target: gold bell
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
Episode — arm: feature mix [look], alpha 0.25, seed 1042, chain drawer->box->basket, target: red stone
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
Episode — arm: feature mix [look], alpha 0.25, seed 1042, chain shelf->pond->cabinet, target: gold bell
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
Episode — arm: feature mix [look], alpha 0.25, seed 1042, chain cabinet->drawer->shelf, target: gold bell
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
Episode — arm: feature mix [look], alpha 0.25, seed 1042, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: feature mix [look], alpha 0.25, seed 1042, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: feature mix [look], alpha 0.25, seed 1042, chain jar->chest->basket, target: black thread
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
Episode — arm: feature mix [open], alpha 0.25, seed 1042, chain box->jar->pond, target: black thread
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
Episode — arm: feature mix [open], alpha 0.25, seed 1042, chain cabinet->box->pond, target: blue feather
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
Episode — arm: feature mix [open], alpha 0.25, seed 1042, chain chest->drawer->basket, target: black thread
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
Episode — arm: feature mix [open], alpha 0.25, seed 1042, chain pond->box->shelf, target: gold bell
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
Episode — arm: feature mix [open], alpha 0.25, seed 1042, chain drawer->box->basket, target: red stone
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
Episode — arm: feature mix [open], alpha 0.25, seed 1042, chain shelf->pond->cabinet, target: gold bell
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
Episode — arm: feature mix [open], alpha 0.25, seed 1042, chain cabinet->drawer->shelf, target: gold bell
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
Episode — arm: feature mix [open], alpha 0.25, seed 1042, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: feature mix [open], alpha 0.25, seed 1042, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: feature mix [open], alpha 0.25, seed 1042, chain jar->chest->basket, target: black thread
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
Episode — arm: payload mix [look], alpha 0.75, seed 1042, chain box->jar->pond, target: black thread
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
Episode — arm: payload mix [look], alpha 0.75, seed 1042, chain cabinet->box->pond, target: blue feather
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
Episode — arm: payload mix [look], alpha 0.75, seed 1042, chain chest->drawer->basket, target: black thread
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
Episode — arm: payload mix [look], alpha 0.75, seed 1042, chain pond->box->shelf, target: gold bell
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
Episode — arm: payload mix [look], alpha 0.75, seed 1042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: look(basket) -> the basket is closed; something is inside
  tick 4: look(basket) -> the basket is closed; something is inside
  tick 5: look(basket) -> the basket is closed; something is inside
  tick 6: look(basket) -> the basket is closed; something is inside
  tick 7: look(drawer) -> a note: check the box
  tick 8: look(box) -> a note: try the basket
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.75, seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: look(cabinet) -> the cabinet is closed; something is inside
  tick 5: look(cabinet) -> the cabinet is closed; something is inside
  tick 6: look(cabinet) -> the cabinet is closed; something is inside
  tick 7: look(cabinet) -> the cabinet is closed; something is inside
  tick 8: look(pond) -> a note: try the cabinet
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.75, seed 1042, chain cabinet->drawer->shelf, target: gold bell
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
Episode — arm: payload mix [look], alpha 0.75, seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: look(drawer) -> the drawer is closed; something is inside
  tick 4: look(drawer) -> the drawer is closed; something is inside
  tick 5: look(drawer) -> the drawer is closed; something is inside
  tick 6: look(drawer) -> the drawer is closed; something is inside
  tick 7: look(drawer) -> the drawer is closed; something is inside
  tick 8: look(cabinet) -> a note: try the drawer
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.75, seed 1042, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: payload mix [look], alpha 0.75, seed 1042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: look(basket) -> the basket is closed; something is inside
  tick 4: look(basket) -> the basket is closed; something is inside
  tick 5: look(basket) -> the basket is closed; something is inside
  tick 6: look(basket) -> the basket is closed; something is inside
  tick 7: look(basket) -> the basket is closed; something is inside
  tick 8: look(chest) -> a note: try the basket
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.75, seed 1042, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: open(box) -> empty
  tick 4: open(box) -> empty
  tick 5: close(empty) -> that did not work
  tick 6: close(empty) -> that did not work
  tick 7: close(empty) -> that did not work
  tick 8: open(box) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.75, seed 1042, chain cabinet->box->pond, target: blue feather
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
Episode — arm: payload mix [open], alpha 0.75, seed 1042, chain chest->drawer->basket, target: black thread
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
Episode — arm: payload mix [open], alpha 0.75, seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: open(door) -> that is not a place here
  tick 2: open(door) -> that is not a place here
  tick 3: look(pond) -> a note: check the box
  tick 4: open(box) -> empty
  tick 5: look(box) -> a note: try the shelf
  tick 6: open(shelf) -> you find: blue feather and gold bell
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: open(shelf) -> you find: blue feather and gold bell
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.75, seed 1042, chain drawer->box->basket, target: red stone
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
Episode — arm: payload mix [open], alpha 0.75, seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: open(box) -> empty
  tick 2: open(box) -> empty
  tick 3: look(box) -> nothing of note
  tick 4: open(box) -> empty
  tick 5: look(box) -> nothing of note
  tick 6: open(box) -> empty
  tick 7: look(note) -> that is not a place here
  tick 8: open(box) -> empty
  FAIL (budget) — depth 0/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.75, seed 1042, chain cabinet->drawer->shelf, target: gold bell
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
Episode — arm: payload mix [open], alpha 0.75, seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: open(kitchen) -> that is not a place here
  tick 2: open(kitchen) -> that is not a place here
  tick 3: look(chest) -> a note: check the cabinet
  tick 4: open(cabinet) -> empty
  tick 5: look(cabinet) -> a note: try the drawer
  tick 6: open(drawer) -> you find: green leaf and amber key
  tick 7: look(drawer) -> the drawer is closed; something is inside
  tick 8: open(drawer) -> you find: green leaf and amber key
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.75, seed 1042, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: payload mix [open], alpha 0.75, seed 1042, chain jar->chest->basket, target: black thread
  tick 1: open(jar) -> empty
  tick 2: open(jar) -> empty
  tick 3: look(jar) -> a note: check the chest
  tick 4: open(chest) -> empty
  tick 5: look(chest) -> a note: try the basket
  tick 6: open(basket) -> you find: black thread and gold bell
  tick 7: open(basket) -> you find: black thread and gold bell
  tick 8: look(basket) -> the basket is closed; something is inside
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.5, seed 1042, chain box->jar->pond, target: black thread
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
Episode — arm: payload mix [look], alpha 0.5, seed 1042, chain cabinet->box->pond, target: blue feather
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
Episode — arm: payload mix [look], alpha 0.5, seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: look(basket) -> the basket is closed; something is inside
  tick 4: look(basket) -> the basket is closed; something is inside
  tick 5: look(basket) -> the basket is closed; something is inside
  tick 6: look(basket) -> the basket is closed; something is inside
  tick 7: look(basket) -> the basket is closed; something is inside
  tick 8: look(drawer) -> a note: try the basket
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.5, seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: look(shelf) -> the shelf is closed; something is inside
  tick 4: look(shelf) -> the shelf is closed; something is inside
  tick 5: look(shelf) -> the shelf is closed; something is inside
  tick 6: look(shelf) -> the shelf is closed; something is inside
  tick 7: remember() -> that did not work
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.5, seed 1042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: look(basket) -> the basket is closed; something is inside
  tick 4: look(basket) -> the basket is closed; something is inside
  tick 5: look(basket) -> the basket is closed; something is inside
  tick 6: look(basket) -> the basket is closed; something is inside
  tick 7: look(basket) -> the basket is closed; something is inside
  tick 8: look(box) -> a note: try the basket
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.5, seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: look(cabinet) -> the cabinet is closed; something is inside
  tick 5: look(cabinet) -> the cabinet is closed; something is inside
  tick 6: look(cabinet) -> the cabinet is closed; something is inside
  tick 7: remember() -> that did not work
  tick 8: look(cabinet) -> the cabinet is closed; something is inside
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.5, seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: look(drawer) -> a note: try the shelf
  tick 4: look(drawer) -> a note: try the shelf
  tick 5: look(drawer) -> a note: try the shelf
  tick 6: look(drawer) -> a note: try the shelf
  tick 7: remember() -> that did not work
  tick 8: remember() -> that did not work
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.5, seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: look(drawer) -> the drawer is closed; something is inside
  tick 4: look(drawer) -> the drawer is closed; something is inside
  tick 5: look(drawer) -> the drawer is closed; something is inside
  tick 6: look(drawer) -> the drawer is closed; something is inside
  tick 7: remember() -> that did not work
  tick 8: look(drawer) -> the drawer is closed; something is inside
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.5, seed 1042, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: payload mix [look], alpha 0.5, seed 1042, chain jar->chest->basket, target: black thread
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
Episode — arm: payload mix [open], alpha 0.5, seed 1042, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.5, seed 1042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: open(box) -> empty
  tick 3: look(box) -> a note: try the pond
  tick 4: open(pond) -> you find: blue feather and gold bell
  tick 5: look(pond) -> the pond is closed; something is inside
  tick 6: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 6 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.5, seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: open(chest) -> empty
  tick 2: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.5, seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: open(box) -> empty
  tick 3: look(box) -> a note: try the shelf
  tick 4: open(shelf) -> you find: blue feather and gold bell
  tick 5: look(shelf) -> the shelf is closed; something is inside
  tick 6: look(shelf) -> the shelf is closed; something is inside
  tick 7: open(shelf) -> you find: blue feather and gold bell
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.5, seed 1042, chain drawer->box->basket, target: red stone
  tick 1: open(drawer) -> empty
  tick 2: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.5, seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: open(pond) -> empty
  tick 3: look(pond) -> a note: try the cabinet
  tick 4: open(cabinet) -> you find: blue feather and gold bell
  tick 5: look(cabinet) -> the cabinet is closed; something is inside
  tick 6: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 6 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.5, seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: open(cabinet) -> empty
  tick 2: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.5, seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: open(cabinet) -> empty
  tick 3: look(cabinet) -> a note: try the drawer
  tick 4: look(drawer) -> the drawer is closed; something is inside
  tick 5: open(drawer) -> you find: green leaf and amber key
  tick 6: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 6 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.5, seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: open(drawer) -> empty
  tick 2: done(amber key) -> you submit: amber key
  PASS — depth 0/3, 2 of 8 ticks, guessed
```

```
Episode — arm: payload mix [open], alpha 0.5, seed 1042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: open(chest) -> empty
  tick 3: look(chest) -> a note: try the basket
  tick 4: look(basket) -> the basket is closed; something is inside
  tick 5: open(basket) -> you find: black thread and gold bell
  tick 6: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 6 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.25, seed 1042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: look(green leaf) -> that is not a place here
  tick 5: look(green leaf) -> that is not a place here
  tick 6: open(green leaf) -> that is not a place here
  tick 7: look(green leaf) -> that is not a place here
  tick 8: look(green leaf) -> that is not a place here
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.25, seed 1042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(blue feather) -> you submit: blue feather
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.25, seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: look(drawer) -> a note: try the basket
  tick 5: look(basket) -> the basket is closed; something is inside
  tick 6: open(basket) -> you find: black thread and blue feather
  tick 7: look(basket) -> the basket is closed; something is inside
  tick 8: look(basket) -> the basket is closed; something is inside
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.25, seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: look(fencelight) -> that is not a place here
  tick 5: look(fencelight) -> that is not a place here
  tick 6: open(fencelight) -> that is not a place here
  tick 7: look(fencelight) -> that is not a place here
  tick 8: look(fencelight) -> that is not a place here
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.25, seed 1042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: look(basket) -> the basket is closed; something is inside
  tick 5: look(basket) -> the basket is closed; something is inside
  tick 6: open(basket) -> you find: red stone and blue feather
  tick 7: look(stone) -> that is not a place here
  tick 8: look(stone) -> that is not a place here
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.25, seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: look(cabinet) -> the cabinet is closed; something is inside
  tick 5: look(cabinet) -> the cabinet is closed; something is inside
  tick 6: open(cabinet) -> you find: blue feather and gold bell
  tick 7: done(blue feather and gold bell) -> you submit: blue feather and gold bell
  FAIL (wrong submit) — depth 3/3, 7 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.25, seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: look(drawer) -> a note: try the shelf
  tick 5: look(shelf) -> the shelf is closed; something is inside
  tick 6: open(shelf) -> you find: black thread and gold bell
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.25, seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.25, seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: look(cabinet) -> the cabinet is closed; something is inside
  tick 5: look(cabinet) -> the cabinet is closed; something is inside
  tick 6: open(cabinet) -> you find: amber key and black thread
  tick 7: look(cabinet) -> the cabinet is closed; something is inside
  tick 8: look(cabinet) -> the cabinet is closed; something is inside
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.25, seed 1042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.25, seed 1042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: open(pond) -> you find: black thread and green leaf
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.25, seed 1042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.25, seed 1042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.25, seed 1042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.25, seed 1042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: open(basket) -> you find: red stone and blue feather
  tick 4: done(red stone) -> you submit: red stone
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.25, seed 1042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.25, seed 1042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the shelf
  tick 3: open(shelf) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.25, seed 1042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.25, seed 1042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: look(basket) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: amber key and black thread
  tick 4: done(amber key) -> you submit: amber key
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.25, seed 1042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: feature mix [look], alpha 0.75, seed 2042, chain box->jar->pond, target: black thread
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
Episode — arm: feature mix [look], alpha 0.75, seed 2042, chain cabinet->box->pond, target: blue feather
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
Episode — arm: feature mix [look], alpha 0.75, seed 2042, chain chest->drawer->basket, target: black thread
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
Episode — arm: feature mix [look], alpha 0.75, seed 2042, chain pond->box->shelf, target: gold bell
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
Episode — arm: feature mix [look], alpha 0.75, seed 2042, chain drawer->box->basket, target: red stone
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
Episode — arm: feature mix [look], alpha 0.75, seed 2042, chain shelf->pond->cabinet, target: gold bell
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
Episode — arm: feature mix [look], alpha 0.75, seed 2042, chain cabinet->drawer->shelf, target: gold bell
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
Episode — arm: feature mix [look], alpha 0.75, seed 2042, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: feature mix [look], alpha 0.75, seed 2042, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: feature mix [look], alpha 0.75, seed 2042, chain jar->chest->basket, target: black thread
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
Episode — arm: feature mix [open], alpha 0.75, seed 2042, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: done(empty) -> you submit: (nothing)
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: feature mix [open], alpha 0.75, seed 2042, chain cabinet->box->pond, target: blue feather
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
Episode — arm: feature mix [open], alpha 0.75, seed 2042, chain chest->drawer->basket, target: black thread
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
Episode — arm: feature mix [open], alpha 0.75, seed 2042, chain pond->box->shelf, target: gold bell
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
Episode — arm: feature mix [open], alpha 0.75, seed 2042, chain drawer->box->basket, target: red stone
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
Episode — arm: feature mix [open], alpha 0.75, seed 2042, chain shelf->pond->cabinet, target: gold bell
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
Episode — arm: feature mix [open], alpha 0.75, seed 2042, chain cabinet->drawer->shelf, target: gold bell
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
Episode — arm: feature mix [open], alpha 0.75, seed 2042, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: feature mix [open], alpha 0.75, seed 2042, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: feature mix [open], alpha 0.75, seed 2042, chain jar->chest->basket, target: black thread
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
Episode — arm: feature mix [look], alpha 0.5, seed 2042, chain box->jar->pond, target: black thread
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
Episode — arm: feature mix [look], alpha 0.5, seed 2042, chain cabinet->box->pond, target: blue feather
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
Episode — arm: feature mix [look], alpha 0.5, seed 2042, chain chest->drawer->basket, target: black thread
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
Episode — arm: feature mix [look], alpha 0.5, seed 2042, chain pond->box->shelf, target: gold bell
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
Episode — arm: feature mix [look], alpha 0.5, seed 2042, chain drawer->box->basket, target: red stone
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
Episode — arm: feature mix [look], alpha 0.5, seed 2042, chain shelf->pond->cabinet, target: gold bell
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
Episode — arm: feature mix [look], alpha 0.5, seed 2042, chain cabinet->drawer->shelf, target: gold bell
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
Episode — arm: feature mix [look], alpha 0.5, seed 2042, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: feature mix [look], alpha 0.5, seed 2042, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: feature mix [look], alpha 0.5, seed 2042, chain jar->chest->basket, target: black thread
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
Episode — arm: feature mix [open], alpha 0.5, seed 2042, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: done(empty) -> you submit: (nothing)
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: feature mix [open], alpha 0.5, seed 2042, chain cabinet->box->pond, target: blue feather
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
Episode — arm: feature mix [open], alpha 0.5, seed 2042, chain chest->drawer->basket, target: black thread
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
Episode — arm: feature mix [open], alpha 0.5, seed 2042, chain pond->box->shelf, target: gold bell
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
Episode — arm: feature mix [open], alpha 0.5, seed 2042, chain drawer->box->basket, target: red stone
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
Episode — arm: feature mix [open], alpha 0.5, seed 2042, chain shelf->pond->cabinet, target: gold bell
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
Episode — arm: feature mix [open], alpha 0.5, seed 2042, chain cabinet->drawer->shelf, target: gold bell
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
Episode — arm: feature mix [open], alpha 0.5, seed 2042, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: feature mix [open], alpha 0.5, seed 2042, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: feature mix [open], alpha 0.5, seed 2042, chain jar->chest->basket, target: black thread
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
Episode — arm: feature mix [look], alpha 0.25, seed 2042, chain box->jar->pond, target: black thread
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
Episode — arm: feature mix [look], alpha 0.25, seed 2042, chain cabinet->box->pond, target: blue feather
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
Episode — arm: feature mix [look], alpha 0.25, seed 2042, chain chest->drawer->basket, target: black thread
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
Episode — arm: feature mix [look], alpha 0.25, seed 2042, chain pond->box->shelf, target: gold bell
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
Episode — arm: feature mix [look], alpha 0.25, seed 2042, chain drawer->box->basket, target: red stone
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
Episode — arm: feature mix [look], alpha 0.25, seed 2042, chain shelf->pond->cabinet, target: gold bell
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
Episode — arm: feature mix [look], alpha 0.25, seed 2042, chain cabinet->drawer->shelf, target: gold bell
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
Episode — arm: feature mix [look], alpha 0.25, seed 2042, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: feature mix [look], alpha 0.25, seed 2042, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: feature mix [look], alpha 0.25, seed 2042, chain jar->chest->basket, target: black thread
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
Episode — arm: feature mix [open], alpha 0.25, seed 2042, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: done(empty) -> you submit: (nothing)
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: feature mix [open], alpha 0.25, seed 2042, chain cabinet->box->pond, target: blue feather
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
Episode — arm: feature mix [open], alpha 0.25, seed 2042, chain chest->drawer->basket, target: black thread
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
Episode — arm: feature mix [open], alpha 0.25, seed 2042, chain pond->box->shelf, target: gold bell
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
Episode — arm: feature mix [open], alpha 0.25, seed 2042, chain drawer->box->basket, target: red stone
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
Episode — arm: feature mix [open], alpha 0.25, seed 2042, chain shelf->pond->cabinet, target: gold bell
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
Episode — arm: feature mix [open], alpha 0.25, seed 2042, chain cabinet->drawer->shelf, target: gold bell
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
Episode — arm: feature mix [open], alpha 0.25, seed 2042, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: feature mix [open], alpha 0.25, seed 2042, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: feature mix [open], alpha 0.25, seed 2042, chain jar->chest->basket, target: black thread
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
Episode — arm: payload mix [look], alpha 0.75, seed 2042, chain box->jar->pond, target: black thread
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
Episode — arm: payload mix [look], alpha 0.75, seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: look(pond) -> the pond is closed; something is inside
  tick 4: look(pond) -> the pond is closed; something is inside
  tick 5: look(pond) -> the pond is closed; something is inside
  tick 6: look(pond) -> the pond is closed; something is inside
  tick 7: look(pond) -> the pond is closed; something is inside
  tick 8: look(box) -> a note: try the pond
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.75, seed 2042, chain chest->drawer->basket, target: black thread
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
Episode — arm: payload mix [look], alpha 0.75, seed 2042, chain pond->box->shelf, target: gold bell
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
Episode — arm: payload mix [look], alpha 0.75, seed 2042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: look(basket) -> the basket is closed; something is inside
  tick 4: look(box) -> a note: try the basket
  tick 5: look(basket) -> the basket is closed; something is inside
  tick 6: look(box) -> a note: try the basket
  tick 7: look(box) -> a note: try the basket
  tick 8: look(box) -> a note: try the basket
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.75, seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: look(pond) -> a note: try the cabinet
  tick 5: look(cabinet) -> the cabinet is closed; something is inside
  tick 6: look(cabinet) -> the cabinet is closed; something is inside
  tick 7: look(shelf) -> a note: check the pond
  tick 8: look(pond) -> a note: try the cabinet
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.75, seed 2042, chain cabinet->drawer->shelf, target: gold bell
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
Episode — arm: payload mix [look], alpha 0.75, seed 2042, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: payload mix [look], alpha 0.75, seed 2042, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: payload mix [look], alpha 0.75, seed 2042, chain jar->chest->basket, target: black thread
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
Episode — arm: payload mix [open], alpha 0.75, seed 2042, chain box->jar->pond, target: black thread
  tick 1: open(box) -> empty
  tick 2: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.75, seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: open(box) -> empty
  tick 3: look(box) -> a note: try the pond
  tick 4: open(pond) -> you find: blue feather and gold bell
  tick 5: look(pond) -> the pond is closed; something is inside
  tick 6: open(pond) -> you find: blue feather and gold bell
  tick 7: look(pond) -> the pond is closed; something is inside
  tick 8: look(pond) -> the pond is closed; something is inside
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.75, seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: open(chest) -> empty
  tick 2: done(empty) -> you submit: (nothing)
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.75, seed 2042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: open(box) -> empty
  tick 3: look(box) -> a note: try the shelf
  tick 4: open(shelf) -> you find: blue feather and gold bell
  tick 5: look(shelf) -> the shelf is closed; something is inside
  tick 6: open(shelf) -> you find: blue feather and gold bell
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.75, seed 2042, chain drawer->box->basket, target: red stone
  tick 1: open(drawer) -> empty
  tick 2: done(drawer) -> you submit: (nothing)
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.75, seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: open(pond) -> empty
  tick 3: look(pond) -> a note: try the cabinet
  tick 4: open(cabinet) -> you find: blue feather and gold bell
  tick 5: look(cabinet) -> the cabinet is closed; something is inside
  tick 6: look(cabinet) -> the cabinet is closed; something is inside
  tick 7: open(cabinet) -> you find: blue feather and gold bell
  tick 8: look(cabinet) -> the cabinet is closed; something is inside
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.75, seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: open(cabinet) -> empty
  tick 2: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.75, seed 2042, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: payload mix [open], alpha 0.75, seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: open(drawer) -> empty
  tick 2: done(drawer) -> you submit: (nothing)
  FAIL (wrong submit) — depth 0/3, 2 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.75, seed 2042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: open(chest) -> empty
  tick 3: look(chest) -> a note: try the basket
  tick 4: look(basket) -> the basket is closed; something is inside
  tick 5: open(basket) -> you find: black thread and gold bell
  tick 6: look(gold bell) -> that is not a place here
  tick 7: look(gold bell) -> that is not a place here
  tick 8: open(gold bell) -> that is not a place here
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.5, seed 2042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: look(jar) -> a note: try the pond
  tick 3: look(pond) -> the pond is closed; something is inside
  tick 4: look(pond) -> the pond is closed; something is inside
  tick 5: look(pond) -> the pond is closed; something is inside
  tick 6: look(pond) -> the pond is closed; something is inside
  tick 7: look(pond) -> the pond is closed; something is inside
  tick 8: look(jar) -> a note: try the pond
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.5, seed 2042, chain cabinet->box->pond, target: blue feather
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
Episode — arm: payload mix [look], alpha 0.5, seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: look(drawer) -> a note: try the basket
  tick 4: look(drawer) -> a note: try the basket
  tick 5: look(basket) -> the basket is closed; something is inside
  tick 6: look(basket) -> the basket is closed; something is inside
  tick 7: look(basket) -> the basket is closed; something is inside
  tick 8: look(drawer) -> a note: try the basket
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.5, seed 2042, chain pond->box->shelf, target: gold bell
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
Episode — arm: payload mix [look], alpha 0.5, seed 2042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: look(basket) -> the basket is closed; something is inside
  tick 4: look(basket) -> the basket is closed; something is inside
  tick 5: look(basket) -> the basket is closed; something is inside
  tick 6: look(basket) -> the basket is closed; something is inside
  tick 7: look(basket) -> the basket is closed; something is inside
  tick 8: look(box) -> a note: try the basket
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.5, seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: look(cabinet) -> the cabinet is closed; something is inside
  tick 5: look(cabinet) -> the cabinet is closed; something is inside
  tick 6: look(cabinet) -> the cabinet is closed; something is inside
  tick 7: look(cabinet) -> the cabinet is closed; something is inside
  tick 8: look(pond) -> a note: try the cabinet
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.5, seed 2042, chain cabinet->drawer->shelf, target: gold bell
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
Episode — arm: payload mix [look], alpha 0.5, seed 2042, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: payload mix [look], alpha 0.5, seed 2042, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: payload mix [look], alpha 0.5, seed 2042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: look(basket) -> the basket is closed; something is inside
  tick 4: look(basket) -> the basket is closed; something is inside
  tick 5: look(basket) -> the basket is closed; something is inside
  tick 6: look(basket) -> the basket is closed; something is inside
  tick 7: look(basket) -> the basket is closed; something is inside
  tick 8: look(chest) -> a note: try the basket
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.5, seed 2042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: open(jar) -> empty
  tick 3: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 1/3, 3 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.5, seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: open(box) -> empty
  tick 3: done(empty) -> you submit: empty
  FAIL (wrong submit) — depth 1/3, 3 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.5, seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: open(drawer) -> empty
  tick 3: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 1/3, 3 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.5, seed 2042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: open(box) -> empty
  tick 3: done(empty) -> you submit: empty
  FAIL (wrong submit) — depth 1/3, 3 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.5, seed 2042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: open(box) -> empty
  tick 3: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 1/3, 3 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.5, seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: open(pond) -> empty
  tick 3: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 1/3, 3 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.5, seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: open(drawer) -> empty
  tick 3: done(empty) -> you submit: empty
  FAIL (wrong submit) — depth 1/3, 3 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.5, seed 2042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(drawer) -> you submit: (nothing)
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.5, seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: open(basket) -> empty
  tick 3: done(amber key) -> you submit: amber key
  PASS — depth 1/3, 3 of 8 ticks, guessed
```

```
Episode — arm: payload mix [open], alpha 0.5, seed 2042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: look(bright light) -> that is not a place here
  tick 5: look(bright light) -> that is not a place here
  tick 6: open(bright light) -> that is not a place here
  tick 7: look(bright light) -> that is not a place here
  tick 8: look(bright light) -> that is not a place here
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.25, seed 2042, chain box->jar->pond, target: black thread
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
Episode — arm: payload mix [look], alpha 0.25, seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: look(pond) -> the pond is closed; something is inside
  tick 5: look(pond) -> the pond is closed; something is inside
  tick 6: look(pond) -> the pond is closed; something is inside
  tick 7: open(pond) -> you find: blue feather and gold bell
  tick 8: look(pond) -> the pond is closed; something is inside
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.25, seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: look(basket) -> the basket is closed; something is inside
  tick 4: look(basket) -> the basket is closed; something is inside
  tick 5: look(basket) -> the basket is closed; something is inside
  tick 6: look(basket) -> the basket is closed; something is inside
  tick 7: look(basket) -> the basket is closed; something is inside
  tick 8: look(drawer) -> a note: try the basket
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.25, seed 2042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: look(shelf) -> the shelf is closed; something is inside
  tick 5: look(shelf) -> the shelf is closed; something is inside
  tick 6: look(shelf) -> the shelf is closed; something is inside
  tick 7: look(shelf) -> the shelf is closed; something is inside
  tick 8: look(shelf) -> the shelf is closed; something is inside
  FAIL (budget) — depth 3/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.25, seed 2042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: look(box) -> a note: try the basket
  tick 3: look(basket) -> the basket is closed; something is inside
  tick 4: look(basket) -> the basket is closed; something is inside
  tick 5: look(basket) -> the basket is closed; something is inside
  tick 6: look(basket) -> the basket is closed; something is inside
  tick 7: look(basket) -> the basket is closed; something is inside
  tick 8: look(box) -> a note: try the basket
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.25, seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: look(cabinet) -> the cabinet is closed; something is inside
  tick 4: look(cabinet) -> the cabinet is closed; something is inside
  tick 5: look(cabinet) -> the cabinet is closed; something is inside
  tick 6: look(cabinet) -> the cabinet is closed; something is inside
  tick 7: look(cabinet) -> the cabinet is closed; something is inside
  tick 8: look(pond) -> a note: try the cabinet
  FAIL (budget) — depth 2/3, 8 of 8 ticks
```

```
Episode — arm: payload mix [look], alpha 0.25, seed 2042, chain cabinet->drawer->shelf, target: gold bell
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
Episode — arm: payload mix [look], alpha 0.25, seed 2042, chain chest->cabinet->drawer, target: green leaf
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
Episode — arm: payload mix [look], alpha 0.25, seed 2042, chain drawer->basket->cabinet, target: amber key
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
Episode — arm: payload mix [look], alpha 0.25, seed 2042, chain jar->chest->basket, target: black thread
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
Episode — arm: payload mix [open], alpha 0.25, seed 2042, chain box->jar->pond, target: black thread
  tick 1: look(box) -> a note: check the jar
  tick 2: open(jar) -> empty
  tick 3: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 1/3, 3 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.25, seed 2042, chain cabinet->box->pond, target: blue feather
  tick 1: look(cabinet) -> a note: check the box
  tick 2: look(box) -> a note: try the pond
  tick 3: open(pond) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.25, seed 2042, chain chest->drawer->basket, target: black thread
  tick 1: look(chest) -> a note: check the drawer
  tick 2: look(drawer) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and blue feather
  tick 4: done(black thread) -> you submit: black thread
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.25, seed 2042, chain pond->box->shelf, target: gold bell
  tick 1: look(pond) -> a note: check the box
  tick 2: look(box) -> a note: try the shelf
  tick 3: open(shelf) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.25, seed 2042, chain drawer->box->basket, target: red stone
  tick 1: look(drawer) -> a note: check the box
  tick 2: open(box) -> empty
  tick 3: done(amber key) -> you submit: amber key
  FAIL (wrong submit) — depth 1/3, 3 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.25, seed 2042, chain shelf->pond->cabinet, target: gold bell
  tick 1: look(shelf) -> a note: check the pond
  tick 2: look(pond) -> a note: try the cabinet
  tick 3: open(cabinet) -> you find: blue feather and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.25, seed 2042, chain cabinet->drawer->shelf, target: gold bell
  tick 1: look(cabinet) -> a note: check the drawer
  tick 2: open(drawer) -> empty
  tick 3: done(empty) -> you submit: empty
  FAIL (wrong submit) — depth 1/3, 3 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.25, seed 2042, chain chest->cabinet->drawer, target: green leaf
  tick 1: look(chest) -> a note: check the cabinet
  tick 2: look(cabinet) -> a note: try the drawer
  tick 3: open(drawer) -> you find: green leaf and amber key
  tick 4: done(green leaf) -> you submit: green leaf
  PASS — depth 3/3, 4 of 8 ticks
```

```
Episode — arm: payload mix [open], alpha 0.25, seed 2042, chain drawer->basket->cabinet, target: amber key
  tick 1: look(drawer) -> a note: check the basket
  tick 2: open(basket) -> empty
  tick 3: done(amber key) -> you submit: amber key
  PASS — depth 1/3, 3 of 8 ticks, guessed
```

```
Episode — arm: payload mix [open], alpha 0.25, seed 2042, chain jar->chest->basket, target: black thread
  tick 1: look(jar) -> a note: check the chest
  tick 2: look(chest) -> a note: try the basket
  tick 3: open(basket) -> you find: black thread and gold bell
  tick 4: done(gold bell) -> you submit: gold bell
  FAIL (wrong submit) — depth 3/3, 4 of 8 ticks
```

