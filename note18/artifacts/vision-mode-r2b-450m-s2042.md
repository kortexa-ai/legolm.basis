# V-line rung 2b — LFM2.5-VL-450M, door seed 2042

Registration: tracks/vision-mode/PLAN.md, Rung 2b registration — boxes on the bus (2026-08-23).

Detector: ultralytics yolo26n, COCO-pretrained detector, frozen; eval accuracy 0.96 (2 false alarms, 5 misses of 200).

Reading at this seed: **(iii) ONE BIT**. Projection gate 0.98 (passed); weight norm 0.27.

| person-mode | action | boxes | switch | lying | habit | gain | lie cell | silence cost | boxes on empty |
|---|---|---|---|---|---|---|---|---|---|
| social | greet | 0.48 | 0.45 | 0.48 | 0.30 | 0.03 | 0.01 | 0.00 | 0.01 |
| caution | stop | 0.97 | 0.93 | 0.97 | 0.02 | 0.04 | 0.01 | 0.00 | 0.01 |

Present-frame share of the person-mode's action per arm. gain = boxes − switch; lie cell = the action's share on ABSENT frames when a person frame's boxes ride the bus; silence cost = boxes − lying on present frames (zeros on the bus); boxes on empty = the BOXES arm's action share on absent frames.
