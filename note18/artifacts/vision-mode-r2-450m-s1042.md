# V-line rung 2 — LFM2.5-VL-450M, door seed 1042

Registration: tracks/vision-mode/PLAN.md, Rung 2 registration — the fast classifier emits the mode (2026-08-22).

Classifier: torchvision mobilenet_v3_small IMAGENET1K_V1, frozen; eval accuracy 0.91 (6 false alarms, 12 misses of 200).

Reading at this seed: **(i) ROBUST**.

| person-mode | action | oracle | classifier | flipped | habit | fidelity | false-alarm cell | miss cost |
|---|---|---|---|---|---|---|---|---|
| social | greet | 0.82 | 0.79 | 0.45 | 0.20 | -0.03 | 0.00 | 0.37 |
| caution | stop | 0.94 | 0.85 | 0.10 | 0.58 | -0.09 | 0.00 | 0.84 |

Present-frame share of the person-mode's action per arm. fidelity = classifier − oracle; false-alarm cell = the action's share on ABSENT frames under the flipped verdict (the small model says 'person', the frame is empty); miss cost = oracle − flipped on present frames.
