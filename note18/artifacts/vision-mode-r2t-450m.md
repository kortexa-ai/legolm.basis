# V-line rung 2t — LFM2.5-VL-450M, pooled over door seeds [42, 1042, 2042]

Registration: tracks/vision-mode/PLAN.md, Rung 2t registration — the drowsy captain (2026-08-23).

60 episodes × 16 steps, 227 cuts; lookout yolo26s.

Per-seed readings: {"42": "(i) FREE LUNCH", "1042": "(iv) MIXED", "2042": "(i) FREE LUNCH"} — majority **(i) FREE LUNCH** (2 of 3). Pooled-number reading: (i) FREE LUNCH.

| person-mode | gate | agreement | wake fraction | saved | oracle correct | cut lag | false wakes |
|---|---|---|---|---|---|---|---|
| social | always | 1.00 | 1.00 | 0.00 | 0.79 | 0.00 | 2199 |
| social | never | 0.65 | 0.06 | 0.94 | 0.51 | 0.00 | 0 |
| social | verdict | 0.97 | 0.16 | 0.84 | 0.79 | 0.98 | 30 |
| social | box | 0.99 | 0.28 | 0.72 | 0.79 | 0.30 | 225 |
| social | pixel | 1.00 | 0.95 | 0.05 | 0.79 | 0.00 | 2046 |
| social | cut_oracle | 0.99 | 0.24 | 0.76 | 0.80 | 0.00 | 0 |
| caution | always | 1.00 | 1.00 | 0.00 | 0.98 | 0.00 | 2199 |
| caution | never | 0.67 | 0.06 | 0.94 | 0.66 | 0.00 | 0 |
| caution | verdict | 0.99 | 0.16 | 0.84 | 0.97 | 0.98 | 30 |
| caution | box | 1.00 | 0.28 | 0.72 | 0.98 | 0.30 | 225 |
| caution | pixel | 1.00 | 0.95 | 0.05 | 0.98 | 0.00 | 2046 |
| caution | cut_oracle | 0.99 | 0.24 | 0.76 | 0.98 | 0.00 | 0 |

agreement = share of steps whose latched action equals ALWAYS's; saved = 1 − wake fraction; cut lag = mean steps from a true cut to the next wake; the CUT-ORACLE row is the ceiling (its disagreement with ALWAYS is the big model's own jitter-instability).
