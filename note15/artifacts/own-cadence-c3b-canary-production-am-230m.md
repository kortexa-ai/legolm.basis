# C3b canary: the C1 signature under the serve wrapper

true 0.80 vs no-packet 0.20 vs shuffled 0.00 — PASS

| goal | arm | choice | consistent |
|---|---|---|---|
| listen_pond | no-packet | listen_pond | True |
| listen_pond | true | listen_pond | True |
| listen_pond | shuffled | propose_experiment | False |
| propose_experiment | no-packet | listen_pond | False |
| propose_experiment | true | propose_experiment | True |
| propose_experiment | shuffled | remember | False |
| diary | no-packet | listen_pond | False |
| diary | true | remember | False |
| diary | shuffled | remember | False |
| remember | no-packet | listen_pond | False |
| remember | true | remember | True |
| remember | shuffled | nothing | False |
| nothing | no-packet | listen_pond | False |
| nothing | true | nothing | True |
| nothing | shuffled | listen_pond | False |
