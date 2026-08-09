# M0: joint-presence floors

Size 27B, prompt "Anything I should keep in mind right now?", 183.228 s, host `Qwen/Qwen3.6-27B`.

| pair | cell | joint | A | B |
|---|---|---:|---:|---:|
| `temporal+vitals` | solo-a | 0.000 | 0.200 | 0.000 |
| `temporal+vitals` | solo-b | 0.000 | 0.000 | 0.200 |
| `temporal+vitals` | merge | 0.000 | 0.000 | 0.000 |
| `temporal+vitals` | prompt-joint | 0.000 | 0.000 | 0.000 |
| `temporal+vitals` | router-oracle | 0.000 | 0.200 | 0.100 |
| `temporal+geo` | solo-a | 0.000 | 0.200 | 0.000 |
| `temporal+geo` | solo-b | 0.000 | 0.000 | 0.100 |
| `temporal+geo` | merge | 0.000 | 0.100 | 0.000 |
| `temporal+geo` | prompt-joint | 0.000 | 0.000 | 0.000 |
| `temporal+geo` | router-oracle | 0.000 | 0.200 | 0.100 |
| `vitals+imu` | solo-a | 0.000 | 0.167 | 0.000 |
| `vitals+imu` | solo-b | 0.000 | 0.000 | 0.000 |
| `vitals+imu` | merge | 0.000 | 0.167 | 0.083 |
| `vitals+imu` | prompt-joint | 0.000 | 0.000 | 0.000 |
| `vitals+imu` | router-oracle | 0.000 | 0.167 | 0.000 |

Floor to beat (max joint over cells): `temporal+vitals` 0.000, `temporal+geo` 0.000, `vitals+imu` 0.000
