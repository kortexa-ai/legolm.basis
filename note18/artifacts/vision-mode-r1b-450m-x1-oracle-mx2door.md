# V-line rung 1b — LFM2.5-VL-450M, dose ×1, emitter oracle, pooled over door seeds [42, 1042, 2042]

Registration: tracks/vision-mode/PLAN.md, Rung 1b registration — the hostile prompt on the VL host (2026-08-22).

Reading: **(iv) ASYMMETRY: social=packet-holds, caution=packet-holds, explore=text-wins** — admissible: True (max parse fallback 0.00, grounding {"social": 0.0, "caution": 0.022222}).

| mode | action | packet | hostile text | packet+hostile | packet+congruent | habit | shuffled+hostile | ownership | band | grounding | hostile text on absent |
|---|---|---|---|---|---|---|---|---|---|---|---|
| social | greet | 0.50 | 0.31 | 0.50 | 0.50 | 0.29 | 0.32 | 0.89 | packet-holds | 0.00 | 0.00 |
| caution | stop | 0.82 | 0.20 | 0.83 | 0.83 | 0.39 | 0.50 | 1.46 | packet-holds | 0.02 | 0.00 |
| explore | proceed | 0.19 | 0.00 | 0.18 | 0.18 | 0.32 | 0.00 | -1.33 | text-wins | — | 0.83 |

Per-seed ownership: {"42": {"social": 0.933334, "caution": -4.99997, "explore": -0.090908}, "1042": {"social": 1.199998, "caution": 1.125, "explore": -0.0}, "2042": {"social": 1.0, "caution": 1.17647, "explore": 3.750009}}
Per-seed bands: {"42": {"social": "packet-holds", "caution": "text-wins", "explore": "text-wins"}, "1042": {"social": "packet-holds", "caution": "packet-holds", "explore": "text-wins"}, "2042": {"social": "packet-holds", "caution": "packet-holds", "explore": "packet-holds"}}

Present-frame share of the mode's action per arm; ownership = (packet+hostile − hostile) / (packet − habit).
