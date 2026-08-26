# V-line rung 1 — LFM2.5-VL-3B, door seed 42

Registration: tracks/vision-mode/PLAN.md, Rung 1 registration — mode packets on a vision-language host (2026-08-22).

Reading at this seed: **(v) MIXED**.

Present-frame share of the mode's action per arm (the lean is packet − habit; grounding is the mode's action share on ABSENT frames under the packet):

| mode | action | packet | shuffled | habit | text | lean | text lean | swap | grounding |
|---|---|---|---|---|---|---|---|---|---|
| social | greet | 0.50 | 0.00 | 0.37 | 0.97 | 0.13 | 0.60 | 0.50 | 0.00 |
| caution | stop | 0.27 | 0.00 | 0.13 | 0.93 | 0.13 | 0.80 | 0.27 | 0.00 |
| explore | proceed | 1.00 | 0.50 | 0.50 | 1.00 | 0.50 | 0.50 | 0.50 | — |

Gates: held-out phrasing token accuracy 0.97 (pass); zero-dose exact; base weights unchanged.
Layer plan: tower depth 30, source 24, inject [9, 14, 19] (prior, no scan). Dose 0.15, 192 steps.
Wall 304.241 s on smarty (cuda, bfloat16).

Habit mix on present / absent frames: {"greet": 0.366667, "stop": 0.133333, "proceed": 0.5, "other": 0.0} / {"greet": 0.033333, "stop": 0.0, "proceed": 0.966667, "other": 0.0}.
