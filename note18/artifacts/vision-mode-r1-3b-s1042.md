# V-line rung 1 — LFM2.5-VL-3B, door seed 1042

Registration: tracks/vision-mode/PLAN.md, Rung 1 registration — mode packets on a vision-language host (2026-08-22).

Reading at this seed: **(i) LEAN**.

Present-frame share of the mode's action per arm (the lean is packet − habit; grounding is the mode's action share on ABSENT frames under the packet):

| mode | action | packet | shuffled | habit | text | lean | text lean | swap | grounding |
|---|---|---|---|---|---|---|---|---|---|
| social | greet | 0.50 | 0.00 | 0.73 | 0.83 | -0.23 | 0.10 | 0.50 | 0.03 |
| caution | stop | 1.00 | 0.00 | 0.10 | 0.87 | 0.90 | 0.77 | 1.00 | 0.00 |
| explore | proceed | 1.00 | 0.07 | 0.17 | 0.90 | 0.83 | 0.73 | 0.93 | — |

Gates: held-out phrasing token accuracy 0.99 (pass); zero-dose exact; base weights unchanged.
Layer plan: tower depth 30, source 24, inject [9, 14, 19] (prior, no scan). Dose 0.15, 192 steps.
Wall 298.918 s on smarty (cuda, bfloat16).

Habit mix on present / absent frames: {"greet": 0.733333, "stop": 0.1, "proceed": 0.166667, "other": 0.0} / {"greet": 0.033333, "stop": 0.0, "proceed": 0.966667, "other": 0.0}.
