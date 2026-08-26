# V-line rung 2y — Qwen3.8-27B, door seed 1042

Registration: tracks/vision-mode/PLAN.md, Rung 2y registration — a person detector in the classifier's seat (2026-08-23).

Classifier: ultralytics yolo26n, COCO-pretrained detector, frozen; eval accuracy 0.96 (2 false alarms, 5 misses of 200).

Reading at this seed: **(i) ROBUST**.

| person-mode | action | oracle | classifier | flipped | habit | fidelity | false-alarm cell | miss cost |
|---|---|---|---|---|---|---|---|---|
| social | greet | 0.97 | 0.94 | 0.03 | 0.40 | -0.03 | 0.00 | 0.94 |
| caution | stop | 0.96 | 0.92 | 0.04 | 0.12 | -0.04 | 0.05 | 0.92 |

Present-frame share of the person-mode's action per arm. fidelity = classifier − oracle; false-alarm cell = the action's share on ABSENT frames under the flipped verdict (the small model says 'person', the frame is empty); miss cost = oracle − flipped on present frames.
