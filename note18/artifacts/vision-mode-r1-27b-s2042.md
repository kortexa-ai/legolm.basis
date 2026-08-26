# V-line rung 1 — Qwen3.8-27B, door seed 2042

Registration: tracks/vision-mode/PLAN.md, Rung 1 registration — mode packets on a vision-language host (2026-08-22).

Reading at this seed: **(i) LEAN**.

Present-frame share of the mode's action per arm (the lean is packet − habit; grounding is the mode's action share on ABSENT frames under the packet):

| mode | action | packet | shuffled | habit | text | lean | text lean | swap | grounding |
|---|---|---|---|---|---|---|---|---|---|
| social | greet | 0.97 | 0.00 | 0.00 | 0.90 | 0.97 | 0.90 | 0.97 | 0.00 |
| caution | stop | 1.00 | 0.00 | 0.00 | 0.63 | 1.00 | 0.63 | 1.00 | 0.13 |
| explore | proceed | 1.00 | 0.03 | 1.00 | 1.00 | 0.00 | 0.00 | 0.97 | — |

Gates: held-out phrasing token accuracy 1.00 (pass); zero-dose exact; base weights unchanged.
Layer plan: tower depth 64, source 51, inject [19, 29, 40] (prior, no scan). Dose 0.15, 192 steps.
Wall 1706.63 s on smarty (cuda, bfloat16).

Habit mix on present / absent frames: {"greet": 0.0, "stop": 0.0, "proceed": 1.0, "other": 0.0} / {"greet": 0.0, "stop": 0.0, "proceed": 1.0, "other": 0.0}.
