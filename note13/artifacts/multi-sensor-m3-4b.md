# M3: depth-partition control

Size 4B, pair `temporal+vitals`, 4116.167 s. Halves: `temporal` on [3, 7, 11, 15], `vitals` on [19, 23, 27, 31]. M0 floor 0.000, M1 joint 0.90/1.00/1.00.

| seed | valid | solo-a A | solo-b B | merge joint | merge A | merge B | shuffled | fit a/b |
|---|---|---:|---:|---:|---:|---:|---:|---|
| 1042 | True | 1.000 | 1.000 | 0.000 | 0.400 | 0.100 | 0.000 | 0.89/0.96 |
| 2042 | True | 1.000 | 1.000 | 0.000 | 0.100 | 0.700 | 0.000 | 0.90/0.96 |
| 42 | True | 1.000 | 1.000 | 0.000 | 0.200 | 0.300 | 0.000 | 0.86/0.95 |

Reading: merge at floor at every valid seed — papers 7/9's prediction holds; M1's win is the single writer, not parameter non-collision
