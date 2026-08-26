# V-line rung 2 — LFM2.5-VL-450M, pooled over door seeds [42, 1042, 2042]

Registration: tracks/vision-mode/PLAN.md, Rung 2 registration — the fast classifier emits the mode (2026-08-22).

Classifier: torchvision mobilenet_v3_small IMAGENET1K_V1, frozen; eval accuracy 0.91 (6 false alarms, 12 misses of 200).

Per-seed readings: {"42": "(i) ROBUST", "1042": "(i) ROBUST", "2042": "(i) ROBUST"} — majority **(i) ROBUST** (3 of 3). Pooled-number reading: (i) ROBUST.

| person-mode | action | oracle | classifier | flipped | habit | fidelity | false-alarm cell | miss cost |
|---|---|---|---|---|---|---|---|---|
| social | greet | 0.62 | 0.56 | 0.19 | 0.30 | -0.05 | 0.01 | 0.42 |
| caution | stop | 0.97 | 0.89 | 0.34 | 0.22 | -0.08 | 0.01 | 0.63 |

Present-frame share of the person-mode's action per arm. fidelity = classifier − oracle; false-alarm cell = the action's share on ABSENT frames under the flipped verdict (the small model says 'person', the frame is empty); miss cost = oracle − flipped on present frames.
