# V-line rung 2b — LFM2.5-VL-450M, door seed 42

Registration: tracks/vision-mode/PLAN.md, Rung 2b registration — boxes on the bus (2026-08-23).

Detector: ultralytics yolo26n, COCO-pretrained detector, frozen; eval accuracy 0.96 (2 false alarms, 5 misses of 200).

Reading at this seed: **(iv) MIXED**. Projection gate 0.97 (passed); weight norm 1.54.

| person-mode | action | boxes | switch | lying | habit | gain | lie cell | silence cost | boxes on empty |
|---|---|---|---|---|---|---|---|---|---|
| social | greet | 0.61 | 0.52 | 0.50 | 0.39 | 0.09 | 0.12 | 0.11 | 0.04 |
| caution | stop | 0.84 | 0.95 | 0.99 | 0.07 | -0.11 | 0.07 | -0.15 | 0.05 |

Present-frame share of the person-mode's action per arm. gain = boxes − switch; lie cell = the action's share on ABSENT frames when a person frame's boxes ride the bus; silence cost = boxes − lying on present frames (zeros on the bus); boxes on empty = the BOXES arm's action share on absent frames.
