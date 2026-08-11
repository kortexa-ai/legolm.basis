# C3b canary: the C1 signature under the serve wrapper

true 0.60 vs no-packet 0.20 vs shuffled 0.00 — PASS

| goal | arm | choice | consistent |
|---|---|---|---|
| listen_pond | no-packet | propose_experiment | False |
| listen_pond | true | remember | False |
| listen_pond | shuffled | propose_experiment | False |
| propose_experiment | no-packet | propose_experiment | True |
| propose_experiment | true | propose_experiment | True |
| propose_experiment | shuffled | remember | False |
| diary | no-packet | propose_experiment | False |
| diary | true | remember | False |
| diary | shuffled | remember | False |
| remember | no-packet | propose_experiment | False |
| remember | true | remember | True |
| remember | shuffled | nothing | False |
| nothing | no-packet | propose_experiment | False |
| nothing | true | nothing | True |
| nothing | shuffled | remember | False |
