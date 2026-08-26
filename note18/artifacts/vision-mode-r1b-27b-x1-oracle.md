# V-line rung 1b — Qwen3.8-27B, dose ×1, emitter oracle, pooled over door seeds [42, 1042, 2042]

Registration: tracks/vision-mode/PLAN.md, Rung 1b registration — the hostile prompt on the VL host (2026-08-22).

Reading: **(i) PACKET HOLDS** — admissible: True (max parse fallback 0.00, grounding {"social": 0.0, "caution": 0.044444}).

| mode | action | packet | hostile text | packet+hostile | packet+congruent | habit | shuffled+hostile | ownership | band | grounding | hostile text on absent |
|---|---|---|---|---|---|---|---|---|---|---|---|
| social | greet | 0.98 | 0.22 | 0.77 | 1.00 | 0.33 | 0.00 | 0.84 | packet-holds | 0.00 | 0.00 |
| caution | stop | 1.00 | 0.11 | 0.89 | 0.98 | 0.13 | 0.00 | 0.90 | packet-holds | 0.04 | 0.00 |
| explore | proceed | 1.00 | 0.29 | 0.98 | 1.00 | 0.53 | 0.02 | 1.48 | packet-holds | — | 1.00 |

Per-seed ownership: {"42": {"social": 1.461539, "caution": 1.173913, "explore": 1.083332}, "1042": {"social": 1.249999, "caution": 0.920001, "explore": 0.833333}, "2042": {"social": 0.344827, "caution": 0.666667, "explore": null}}
Per-seed bands: {"42": {"social": "packet-holds", "caution": "packet-holds", "explore": "packet-holds"}, "1042": {"social": "packet-holds", "caution": "packet-holds", "explore": "packet-holds"}, "2042": {"social": "split", "caution": "split", "explore": null}}

Present-frame share of the mode's action per arm; ownership = (packet+hostile − hostile) / (packet − habit).
