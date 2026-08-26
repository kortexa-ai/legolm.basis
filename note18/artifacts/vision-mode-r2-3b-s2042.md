# V-line rung 2 — LFM2.5-VL-3B, door seed 2042

Registration: tracks/vision-mode/PLAN.md, Rung 2 registration — the fast classifier emits the mode (2026-08-22).

Classifier: torchvision mobilenet_v3_small IMAGENET1K_V1, frozen; eval accuracy 0.91 (6 false alarms, 12 misses of 200).

Reading at this seed: **(iv) MIXED**.

| person-mode | action | oracle | classifier | flipped | habit | fidelity | false-alarm cell | miss cost |
|---|---|---|---|---|---|---|---|---|
| social | greet | 0.43 | 0.39 | 0.04 | 0.41 | -0.04 | 0.02 | 0.39 |
| caution | stop | 0.99 | 0.87 | 0.12 | 0.01 | -0.12 | 0.07 | 0.87 |

Present-frame share of the person-mode's action per arm. fidelity = classifier − oracle; false-alarm cell = the action's share on ABSENT frames under the flipped verdict (the small model says 'person', the frame is empty); miss cost = oracle − flipped on present frames.
