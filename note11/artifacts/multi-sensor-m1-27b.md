# M1: the joint bridge

Size 27B, 14394.005 s, floors from `multi-sensor-m0-27b.json`.

| pair | seed | passed | joint@1.0 | best (beta) | A | B | fit | S2c-signature |
|---|---|---|---:|---:|---:|---:|---:|---|
| `temporal+geo` | 1042 | False | 0.800 | 0.800 (1.00) | 1.000 | 0.800 | 0.95 | False |
| `temporal+geo` | 2042 | True | 0.800 | 0.800 (1.00) | 1.000 | 0.800 | 0.96 | False |
| `temporal+geo` | 42 | False | 0.900 | 0.900 (1.00) | 1.000 | 0.900 | 0.99 | False |
| `temporal+vitals` | 1042 | True | 1.000 | 1.000 (1.00) | 1.000 | 1.000 | 0.96 | False |
| `temporal+vitals` | 2042 | True | 1.000 | 1.000 (1.00) | 1.000 | 1.000 | 0.96 | False |
| `temporal+vitals` | 42 | True | 1.000 | 1.000 (1.00) | 1.000 | 1.000 | 0.94 | False |
| `vitals+imu` | 1042 | True | 0.917 | 0.917 (1.00) | 1.000 | 0.917 | 0.96 | False |
| `vitals+imu` | 2042 | True | 1.000 | 1.000 (1.00) | 1.000 | 1.000 | 0.98 | False |
| `vitals+imu` | 42 | True | 1.000 | 1.000 (1.00) | 1.000 | 1.000 | 0.98 | False |
