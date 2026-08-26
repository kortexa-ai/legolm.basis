# V-line rung 2b — LFM2.5-VL-3B, pooled over door seeds [42, 1042, 2042]

Registration: tracks/vision-mode/PLAN.md, Rung 2b registration — boxes on the bus (2026-08-23).

Detector: ultralytics yolo26n, COCO-pretrained detector, frozen; eval accuracy 0.96 (2 false alarms, 5 misses of 200).

Per-seed readings: {"42": "(iv) MIXED", "1042": "(iii) ONE BIT", "2042": "(iii) ONE BIT"} — majority **(iii) ONE BIT** (2 of 3). Pooled-number reading: (iv) MIXED.
Per-seed gates: {"42": 0.9896, "1042": 0.987, "2042": 0.9922}.

| person-mode | action | boxes | switch | lying | habit | gain | lie cell | silence cost | boxes on empty |
|---|---|---|---|---|---|---|---|---|---|
| social | greet | 0.45 | 0.44 | 0.46 | 0.53 | 0.01 | 0.02 | -0.00 | 0.02 |
| caution | stop | 0.93 | 0.70 | 0.76 | 0.07 | 0.22 | 0.04 | 0.17 | 0.05 |

Present-frame share of the person-mode's action per arm. gain = boxes − switch; lie cell = the action's share on ABSENT frames when a person frame's boxes ride the bus; silence cost = boxes − lying on present frames (zeros on the bus); boxes on empty = the BOXES arm's action share on absent frames.
