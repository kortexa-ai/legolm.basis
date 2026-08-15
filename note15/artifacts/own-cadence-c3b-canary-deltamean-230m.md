# C3b canary: the C1 signature under the serve wrapper

true 0.20 vs no-packet 0.20 vs shuffled 0.20 — FAIL

| goal | arm | choice | consistent |
|---|---|---|---|
| listen_pond | no-packet | listen_pond | True |
| listen_pond | true | remember | False |
| listen_pond | shuffled | remember | False |
| propose_experiment | no-packet | listen_pond | False |
| propose_experiment | true | remember | False |
| propose_experiment | shuffled | remember | False |
| diary | no-packet | listen_pond | False |
| diary | true | remember | False |
| diary | shuffled | remember | False |
| remember | no-packet | listen_pond | False |
| remember | true | remember | True |
| remember | shuffled | remember | True |
| nothing | no-packet | listen_pond | False |
| nothing | true | remember | False |
| nothing | shuffled | remember | False |
