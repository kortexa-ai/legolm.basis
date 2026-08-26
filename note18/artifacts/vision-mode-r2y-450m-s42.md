# V-line rung 2y — LFM2.5-VL-450M, door seed 42

Registration: tracks/vision-mode/PLAN.md, Rung 2y registration — a person detector in the classifier's seat (2026-08-23).

Classifier: ultralytics yolo26n, COCO-pretrained detector, frozen; eval accuracy 0.96 (2 false alarms, 5 misses of 200).

Reading at this seed: **(i) ROBUST**.

| person-mode | action | oracle | classifier | flipped | habit | fidelity | false-alarm cell | miss cost |
|---|---|---|---|---|---|---|---|---|
| social | greet | 0.55 | 0.52 | 0.03 | 0.39 | -0.03 | 0.06 | 0.52 |
| caution | stop | 0.99 | 0.95 | 0.36 | 0.07 | -0.04 | 0.04 | 0.63 |

Present-frame share of the person-mode's action per arm. fidelity = classifier − oracle; false-alarm cell = the action's share on ABSENT frames under the flipped verdict (the small model says 'person', the frame is empty); miss cost = oracle − flipped on present frames.
