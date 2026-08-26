# V-line rung 1b — LFM2.5-VL-450M, dose ×1.5, emitter oracle, pooled over door seeds [42, 1042, 2042]

Registration: tracks/vision-mode/PLAN.md, Rung 1b registration — the hostile prompt on the VL host (2026-08-22).

Reading: **(i) PACKET HOLDS** — admissible: False (max parse fallback 0.06, grounding {"social": 0.033333, "caution": 0.077778}).

| mode | action | packet | hostile text | packet+hostile | packet+congruent | habit | shuffled+hostile | ownership | band | grounding | hostile text on absent |
|---|---|---|---|---|---|---|---|---|---|---|---|
| social | greet | 0.50 | 0.11 | 0.49 | 0.51 | 0.02 | 0.11 | 0.79 | packet-holds | 0.03 | 0.00 |
| caution | stop | 1.00 | 0.27 | 1.00 | 0.98 | 0.31 | 0.40 | 1.06 | packet-holds | 0.08 | 0.00 |
| explore | proceed | 0.47 | 0.47 | 0.49 | 0.48 | 0.67 | 0.00 | -0.11 | text-wins | — | 1.00 |

Per-seed ownership: {"42": {"social": 0.92857, "caution": 1.0, "explore": 0.538462}, "1042": {"social": 0.933334, "caution": 2.999985, "explore": 1.250006}, "2042": {"social": 0.500001, "caution": 1.0, "explore": 0.076922}}
Per-seed bands: {"42": {"social": "packet-holds", "caution": "packet-holds", "explore": "split"}, "1042": {"social": "packet-holds", "caution": "packet-holds", "explore": "packet-holds"}, "2042": {"social": "split", "caution": "packet-holds", "explore": "text-wins"}}

Present-frame share of the mode's action per arm; ownership = (packet+hostile − hostile) / (packet − habit).
