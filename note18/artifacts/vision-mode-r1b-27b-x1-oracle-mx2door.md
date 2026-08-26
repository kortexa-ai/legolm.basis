# V-line rung 1b — Qwen3.8-27B, dose ×1, emitter oracle, pooled over door seeds [42, 1042, 2042]

Registration: tracks/vision-mode/PLAN.md, Rung 1b registration — the hostile prompt on the VL host (2026-08-22).

Reading: **(i) PACKET HOLDS** — admissible: True (max parse fallback 0.00, grounding {"social": 0.011111, "caution": 0.022222}).

| mode | action | packet | hostile text | packet+hostile | packet+congruent | habit | shuffled+hostile | ownership | band | grounding | hostile text on absent |
|---|---|---|---|---|---|---|---|---|---|---|---|
| social | greet | 0.94 | 0.41 | 0.87 | 0.96 | 0.40 | 0.00 | 0.84 | packet-holds | 0.01 | 0.00 |
| caution | stop | 0.82 | 0.23 | 0.82 | 0.80 | 0.40 | 0.00 | 1.39 | packet-holds | 0.02 | 0.01 |
| explore | proceed | 1.00 | 0.12 | 1.00 | 1.00 | 0.20 | 0.20 | 1.10 | packet-holds | — | 1.00 |

Per-seed ownership: {"42": {"social": 1.166666, "caution": null, "explore": 1.349999}, "1042": {"social": 0.733334, "caution": 1.999998, "explore": 0.966667}, "2042": {"social": 0.199998, "caution": 1.173913, "explore": 1.045455}}
Per-seed bands: {"42": {"social": "packet-holds", "caution": null, "explore": "packet-holds"}, "1042": {"social": "packet-holds", "caution": "packet-holds", "explore": "packet-holds"}, "2042": {"social": "text-wins", "caution": "packet-holds", "explore": "packet-holds"}}

Present-frame share of the mode's action per arm; ownership = (packet+hostile − hostile) / (packet − habit).
