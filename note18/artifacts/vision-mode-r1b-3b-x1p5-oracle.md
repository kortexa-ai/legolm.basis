# V-line rung 1b — LFM2.5-VL-3B, dose ×1.5, emitter oracle, pooled over door seeds [42, 1042, 2042]

Registration: tracks/vision-mode/PLAN.md, Rung 1b registration — the hostile prompt on the VL host (2026-08-22).

Reading: **(i) PACKET HOLDS** — admissible: True (max parse fallback 0.04, grounding {"social": 0.133333, "caution": 0.177778}).

| mode | action | packet | hostile text | packet+hostile | packet+congruent | habit | shuffled+hostile | ownership | band | grounding | hostile text on absent |
|---|---|---|---|---|---|---|---|---|---|---|---|
| social | greet | 0.48 | 0.64 | 0.50 | 0.49 | 0.99 | 0.00 | 0.28 | text-wins | 0.13 | 0.01 |
| caution | stop | 0.89 | 0.01 | 0.74 | 1.00 | 0.01 | 0.00 | 0.84 | packet-holds | 0.18 | 0.00 |
| explore | proceed | 1.00 | 0.01 | 1.00 | 1.00 | 0.00 | 0.00 | 0.99 | packet-holds | — | 0.23 |

Per-seed ownership: {"42": {"social": 0.499999, "caution": 0.380953, "explore": 1.0}, "1042": {"social": 0.866666, "caution": 0.933334, "explore": 1.0}, "2042": {"social": -0.411764, "caution": 1.071429, "explore": 0.966667}}
Per-seed bands: {"42": {"social": "split", "caution": "split", "explore": "packet-holds"}, "1042": {"social": "packet-holds", "caution": "packet-holds", "explore": "packet-holds"}, "2042": {"social": "text-wins", "caution": "packet-holds", "explore": "packet-holds"}}

Present-frame share of the mode's action per arm; ownership = (packet+hostile − hostile) / (packet − habit).
