# M0: joint-presence floors

Size 4B, prompt "Anything I should keep in mind right now?", 60.096 s, host `Qwen/Qwen3.5-4B`.

| pair | cell | joint | A | B |
|---|---|---:|---:|---:|
| `temporal+vitals` | solo-a | 0.000 | 0.800 | 0.000 |
| `temporal+vitals` | solo-b | 0.000 | 0.000 | 0.300 |
| `temporal+vitals` | merge | 0.000 | 0.400 | 0.000 |
| `temporal+vitals` | prompt-joint | 0.000 | 0.000 | 0.000 |
| `temporal+vitals` | router-oracle | 0.000 | 0.800 | 0.100 |
| `temporal+geo` | solo-a | 0.000 | 0.800 | 0.000 |
| `temporal+geo` | solo-b | 0.000 | 0.000 | 0.300 |
| `temporal+geo` | merge | 0.000 | 0.500 | 0.100 |
| `temporal+geo` | prompt-joint | 0.000 | 0.000 | 0.000 |
| `temporal+geo` | router-oracle | 0.000 | 0.800 | 0.100 |
| `vitals+imu` | solo-a | 0.000 | 0.333 | 0.000 |
| `vitals+imu` | solo-b | 0.000 | 0.000 | 0.667 |
| `vitals+imu` | merge | 0.167 | 0.167 | 0.917 |
| `vitals+imu` | prompt-joint | 0.000 | 0.000 | 0.000 |
| `vitals+imu` | router-oracle | 0.000 | 0.333 | 0.500 |

Floor to beat (max joint over cells): `temporal+vitals` 0.000, `temporal+geo` 0.000, `vitals+imu` 0.167
