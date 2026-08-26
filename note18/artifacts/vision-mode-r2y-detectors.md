# V-line rung 2y-size — the detector size axis

Registration: tracks/vision-mode/PLAN.md, Rung 2y-size registration — the detector size axis, for the last five misses (2026-08-23).

Reading on the 200: **DETECTOR FLOOR**; chosen for rung 2y by calibration misses: **yolo26m**.

| detector | params | eval acc | eval FA | eval misses | calib acc | calib FA | calib misses | ms/frame (calib) |
|---|---|---|---|---|---|---|---|---|
| yolo26n | 2.4M | 0.965 | 2 | 5 | 0.986 | 25 | 25 | 3.5 |
| yolo26s | 9.5M | 0.995 | 1 | 0 | 0.990 | 22 | 12 | 3.6 |
| yolo26m | 20.4M | 0.990 | 2 | 0 | 0.991 | 22 | 10 | 4.4 |

The nano's error frames on the 200, verdict / best qualifying confidence / largest box fraction per size:

| image | label | yolo26n | yolo26s | yolo26m |
|---|---|---|---|---|
| 223747 | present | absent / 0.00 / 0.000 | present / 0.53 / 0.891 | present / 0.47 / 0.955 |
| 261706 | absent | present / 0.41 / 0.340 | absent / 0.00 / 0.000 | present / 0.47 / 0.344 |
| 402765 | present | absent / 0.00 / 0.000 | present / 0.90 / 0.971 | present / 0.72 / 0.962 |
| 480275 | present | absent / 0.00 / 0.000 | present / 0.34 / 0.106 | present / 0.30 / 0.172 |
| 509699 | absent | present / 0.52 / 0.103 | present / 0.87 / 0.113 | present / 0.89 / 0.103 |
| 523807 | present | absent / 0.00 / 0.000 | present / 0.56 / 0.198 | present / 0.77 / 0.191 |
| 554266 | present | absent / 0.00 / 0.028 | present / 0.55 / 0.212 | present / 0.44 / 0.207 |
