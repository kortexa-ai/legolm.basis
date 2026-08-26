# V-line rung 2t — LFM2.5-VL-450M, door seed 42

Registration: tracks/vision-mode/PLAN.md, Rung 2t registration — the drowsy captain (2026-08-23).

60 episodes × 16 steps, 227 cuts; lookout yolo26s.

Reading at this seed (the VERDICT gate): **(i) FREE LUNCH**.

| person-mode | gate | agreement | wake fraction | saved | oracle correct | cut lag | false wakes |
|---|---|---|---|---|---|---|---|
| social | always | 1.00 | 1.00 | 0.00 | 0.76 | 0.00 | 733 |
| social | never | 0.65 | 0.06 | 0.94 | 0.49 | 0.00 | 0 |
| social | verdict | 0.98 | 0.16 | 0.84 | 0.76 | 0.98 | 10 |
| social | box | 0.99 | 0.28 | 0.72 | 0.75 | 0.30 | 75 |
| social | pixel | 1.00 | 0.95 | 0.05 | 0.76 | 0.00 | 682 |
| social | cut_oracle | 0.98 | 0.24 | 0.76 | 0.75 | 0.00 | 0 |
| caution | always | 1.00 | 1.00 | 0.00 | 0.99 | 0.00 | 733 |
| caution | never | 0.67 | 0.06 | 0.94 | 0.68 | 0.00 | 0 |
| caution | verdict | 1.00 | 0.16 | 0.84 | 0.99 | 0.98 | 10 |
| caution | box | 1.00 | 0.28 | 0.72 | 0.99 | 0.30 | 75 |
| caution | pixel | 1.00 | 0.95 | 0.05 | 0.99 | 0.00 | 682 |
| caution | cut_oracle | 0.99 | 0.24 | 0.76 | 0.99 | 0.00 | 0 |

agreement = share of steps whose latched action equals ALWAYS's; saved = 1 − wake fraction; cut lag = mean steps from a true cut to the next wake; the CUT-ORACLE row is the ceiling (its disagreement with ALWAYS is the big model's own jitter-instability).
