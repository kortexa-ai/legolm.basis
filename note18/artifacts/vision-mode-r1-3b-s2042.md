# V-line rung 1 — LFM2.5-VL-3B, door seed 2042

Registration: tracks/vision-mode/PLAN.md, Rung 1 registration — mode packets on a vision-language host (2026-08-22).

Reading at this seed: **(i) LEAN**.

Present-frame share of the mode's action per arm (the lean is packet − habit; grounding is the mode's action share on ABSENT frames under the packet):

| mode | action | packet | shuffled | habit | text | lean | text lean | swap | grounding |
|---|---|---|---|---|---|---|---|---|---|
| social | greet | 0.47 | 0.00 | 0.30 | 0.97 | 0.17 | 0.67 | 0.47 | 0.10 |
| caution | stop | 1.00 | 0.00 | 0.03 | 0.93 | 0.97 | 0.90 | 1.00 | 0.07 |
| explore | proceed | 1.00 | 0.03 | 0.67 | 1.00 | 0.33 | 0.33 | 0.97 | — |

Gates: held-out phrasing token accuracy 0.99 (pass); zero-dose exact; base weights unchanged.
Layer plan: tower depth 30, source 24, inject [9, 14, 19] (prior, no scan). Dose 0.15, 192 steps.
Wall 299.812 s on smarty (cuda, bfloat16).

Habit mix on present / absent frames: {"greet": 0.3, "stop": 0.033333, "proceed": 0.666667, "other": 0.0} / {"greet": 0.1, "stop": 0.0, "proceed": 0.9, "other": 0.0}.
