# V-line rung 2y — LFM2.5-VL-450M, pooled over door seeds [42, 1042, 2042]

Registration: tracks/vision-mode/PLAN.md, Rung 2y registration — a person detector in the classifier's seat (2026-08-23).

Classifier: ultralytics yolo26n, COCO-pretrained detector, frozen; eval accuracy 0.96 (2 false alarms, 5 misses of 200).

Per-seed readings: {"42": "(i) ROBUST", "1042": "(i) ROBUST", "2042": "(i) ROBUST"} — majority **(i) ROBUST** (3 of 3). Pooled-number reading: (i) ROBUST.

| person-mode | action | oracle | classifier | flipped | habit | fidelity | false-alarm cell | miss cost |
|---|---|---|---|---|---|---|---|---|
| social | greet | 0.62 | 0.59 | 0.17 | 0.30 | -0.03 | 0.02 | 0.45 |
| caution | stop | 0.97 | 0.93 | 0.30 | 0.22 | -0.04 | 0.01 | 0.67 |

Present-frame share of the person-mode's action per arm. fidelity = classifier − oracle; false-alarm cell = the action's share on ABSENT frames under the flipped verdict (the small model says 'person', the frame is empty); miss cost = oracle − flipped on present frames.
