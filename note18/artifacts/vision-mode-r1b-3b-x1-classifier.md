# V-line rung 1b — LFM2.5-VL-3B, dose ×1, emitter classifier, pooled over door seeds [42, 1042, 2042]

Registration: tracks/vision-mode/PLAN.md, Rung 1b registration — the hostile prompt on the VL host (2026-08-22).

Reading: **(i) PACKET HOLDS** — admissible: True (max parse fallback 0.00, grounding {"social": 0.022222, "caution": 0.0}).

| mode | action | packet | hostile text | packet+hostile | packet+congruent | habit | shuffled+hostile | ownership | band | grounding | hostile text on absent |
|---|---|---|---|---|---|---|---|---|---|---|---|
| social | greet | 0.46 | 0.03 | 0.28 | 0.47 | 0.47 | 0.00 | — | — | 0.02 | 0.00 |
| caution | stop | 0.71 | 0.00 | 0.40 | 0.90 | 0.09 | 0.00 | 0.64 | split | 0.00 | 0.00 |
| explore | proceed | 1.00 | 0.06 | 0.92 | 1.00 | 0.44 | 0.10 | 1.56 | packet-holds | — | 0.33 |

Per-seed ownership: {"42": {"social": 4.66667, "caution": 0.0, "explore": 1.933334}, "1042": {"social": -0.375001, "caution": 0.52, "explore": 1.040001}, "2042": {"social": 1.250006, "caution": 0.851852, "explore": 2.300003}}
Per-seed bands: {"42": {"social": "packet-holds", "caution": "text-wins", "explore": "packet-holds"}, "1042": {"social": "text-wins", "caution": "split", "explore": "packet-holds"}, "2042": {"social": "packet-holds", "caution": "packet-holds", "explore": "packet-holds"}}

Present-frame share of the mode's action per arm; ownership = (packet+hostile − hostile) / (packet − habit).
