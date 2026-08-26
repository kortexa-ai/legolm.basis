# V-line rung 1 — LFM2.5-VL-450M, door seed 1042

Registration: tracks/vision-mode/PLAN.md, Rung 1 registration — mode packets on a vision-language host (2026-08-22).

Reading at this seed: **(i) LEAN**.

Present-frame share of the mode's action per arm (the lean is packet − habit; grounding is the mode's action share on ABSENT frames under the packet):

| mode | action | packet | shuffled | habit | text | lean | text lean | swap | grounding |
|---|---|---|---|---|---|---|---|---|---|
| social | greet | 0.87 | 0.00 | 0.20 | 0.97 | 0.67 | 0.77 | 0.87 | 0.00 |
| caution | stop | 1.00 | 0.00 | 0.60 | 1.00 | 0.40 | 0.40 | 1.00 | 0.00 |
| explore | proceed | 0.53 | 0.00 | 0.20 | 0.27 | 0.33 | 0.07 | 0.53 | — |

Gates: held-out phrasing token accuracy 0.99 (pass); zero-dose exact; base weights unchanged.
Layer plan: tower depth 16, source 13, inject [5, 7, 10] (prior, no scan). Dose 0.15, 192 steps.
Wall 72.29 s on smarty (cuda, bfloat16).

Habit mix on present / absent frames: {"greet": 0.2, "stop": 0.6, "proceed": 0.2, "other": 0.0} / {"greet": 0.0, "stop": 0.0, "proceed": 1.0, "other": 0.0}.
