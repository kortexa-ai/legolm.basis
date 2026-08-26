# V-line rung 1b — Qwen3.8-27B, dose ×1.5, emitter oracle, pooled over door seeds [42, 1042, 2042]

Registration: tracks/vision-mode/PLAN.md, Rung 1b registration — the hostile prompt on the VL host (2026-08-22).

Reading: **(i) PACKET HOLDS** — admissible: True (max parse fallback 0.00, grounding {"social": 0.0, "caution": 0.033333}).

| mode | action | packet | hostile text | packet+hostile | packet+congruent | habit | shuffled+hostile | ownership | band | grounding | hostile text on absent |
|---|---|---|---|---|---|---|---|---|---|---|---|
| social | greet | 0.99 | 0.33 | 0.89 | 1.00 | 0.38 | 0.00 | 0.91 | packet-holds | 0.00 | 0.00 |
| caution | stop | 1.00 | 0.02 | 0.91 | 0.97 | 0.04 | 0.00 | 0.93 | packet-holds | 0.03 | 0.00 |
| explore | proceed | 1.00 | 0.62 | 1.00 | 1.00 | 0.58 | 0.03 | 0.89 | packet-holds | — | 1.00 |

Per-seed ownership: {"42": {"social": 1.599999, "caution": 1.076922, "explore": 0.931034}, "1042": {"social": 1.049999, "caution": 1.0, "explore": 0.333333}, "2042": {"social": 0.7, "caution": 0.733333, "explore": null}}
Per-seed bands: {"42": {"social": "packet-holds", "caution": "packet-holds", "explore": "packet-holds"}, "1042": {"social": "packet-holds", "caution": "packet-holds", "explore": "split"}, "2042": {"social": "packet-holds", "caution": "packet-holds", "explore": null}}

Present-frame share of the mode's action per arm; ownership = (packet+hostile − hostile) / (packet − habit).
