# V-line rung 1b — LFM2.5-VL-450M, dose ×1, emitter oracle, pooled over door seeds [42, 1042, 2042]

Registration: tracks/vision-mode/PLAN.md, Rung 1b registration — the hostile prompt on the VL host (2026-08-22).

Reading: **(i) PACKET HOLDS** — admissible: True (max parse fallback 0.00, grounding {"social": 0.011111, "caution": 0.033333}).

| mode | action | packet | hostile text | packet+hostile | packet+congruent | habit | shuffled+hostile | ownership | band | grounding | hostile text on absent |
|---|---|---|---|---|---|---|---|---|---|---|---|
| social | greet | 0.63 | 0.29 | 0.56 | 0.74 | 0.30 | 0.16 | 0.80 | packet-holds | 0.01 | 0.00 |
| caution | stop | 1.00 | 0.18 | 0.99 | 1.00 | 0.22 | 0.31 | 1.04 | packet-holds | 0.03 | 0.01 |
| explore | proceed | 0.52 | 0.02 | 0.33 | 0.53 | 0.48 | 0.00 | — | — | — | 0.62 |

Per-seed ownership: {"42": {"social": 1.250006, "caution": 0.965518, "explore": null}, "1042": {"social": 0.499999, "caution": 1.333333, "explore": 0.900001}, "2042": {"social": 1.5, "caution": 1.0, "explore": -2.799996}}
Per-seed bands: {"42": {"social": "packet-holds", "caution": "packet-holds", "explore": null}, "1042": {"social": "split", "caution": "packet-holds", "explore": "packet-holds"}, "2042": {"social": "packet-holds", "caution": "packet-holds", "explore": "text-wins"}}

Present-frame share of the mode's action per arm; ownership = (packet+hostile − hostile) / (packet − habit).
