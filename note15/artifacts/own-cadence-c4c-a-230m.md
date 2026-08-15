# C4 closed loop — trajectory a

96 ticks, 5 switches; 294.615 s.

| arm | consistency | follow latency | contamination | drift |
|---|---:|---:|---:|---:|
| packet+note | 1.00 | 0.0 | 0 | +0.00 |
| packet-only | 0.80 | 0.0 | 0 | +0.00 |
| note-only | 0.46 | 0.0 | 2 | +0.00 |
| no-want | 0.46 | 0.0 | 2 | +0.00 |
| shuffled-want | 0.00 | None | 4 | +0.00 |

## Timeline (packet+note arm)

```
tick   0 want=diary               choice=diary               Y <-- switch
tick   1 want=diary               choice=diary               Y
tick   2 want=diary               choice=diary               Y
tick   3 want=diary               choice=diary               Y
tick   4 want=diary               choice=diary               Y
tick   5 want=diary               choice=diary               Y
tick   6 want=diary               choice=diary               Y
tick   7 want=diary               choice=diary               Y
tick   8 want=diary               choice=diary               Y
tick   9 want=diary               choice=diary               Y
tick  10 want=diary               choice=diary               Y
tick  11 want=diary               choice=diary               Y
tick  12 want=diary               choice=diary               Y
tick  13 want=diary               choice=diary               Y
tick  14 want=diary               choice=diary               Y
tick  15 want=diary               choice=diary               Y
tick  16 want=diary               choice=diary               Y
tick  17 want=diary               choice=diary               Y
tick  18 want=diary               choice=diary               Y
tick  19 want=listen_pond         choice=listen_pond         Y <-- switch
tick  20 want=listen_pond         choice=listen_pond         Y
tick  21 want=listen_pond         choice=listen_pond         Y
tick  22 want=listen_pond         choice=listen_pond         Y
tick  23 want=listen_pond         choice=listen_pond         Y
tick  24 want=listen_pond         choice=listen_pond         Y
tick  25 want=listen_pond         choice=listen_pond         Y
tick  26 want=listen_pond         choice=listen_pond         Y
tick  27 want=listen_pond         choice=listen_pond         Y
tick  28 want=listen_pond         choice=listen_pond         Y
tick  29 want=listen_pond         choice=listen_pond         Y
tick  30 want=listen_pond         choice=listen_pond         Y
tick  31 want=listen_pond         choice=listen_pond         Y
tick  32 want=listen_pond         choice=listen_pond         Y
tick  33 want=listen_pond         choice=listen_pond         Y
tick  34 want=listen_pond         choice=listen_pond         Y
tick  35 want=listen_pond         choice=listen_pond         Y
tick  36 want=listen_pond         choice=listen_pond         Y
tick  37 want=listen_pond         choice=listen_pond         Y
tick  38 want=listen_pond         choice=listen_pond         Y
tick  39 want=nothing             choice=nothing             Y <-- switch
tick  40 want=nothing             choice=nothing             Y
tick  41 want=nothing             choice=nothing             Y
tick  42 want=nothing             choice=nothing             Y
tick  43 want=nothing             choice=nothing             Y
tick  44 want=nothing             choice=nothing             Y
tick  45 want=nothing             choice=nothing             Y
tick  46 want=nothing             choice=nothing             Y
tick  47 want=nothing             choice=nothing             Y
tick  48 want=nothing             choice=nothing             Y
tick  49 want=remember            choice=remember            Y <-- switch
tick  50 want=remember            choice=remember            Y
tick  51 want=remember            choice=remember            Y
tick  52 want=remember            choice=remember            Y
tick  53 want=remember            choice=remember            Y
tick  54 want=remember            choice=remember            Y
tick  55 want=remember            choice=remember            Y
tick  56 want=remember            choice=remember            Y
tick  57 want=remember            choice=remember            Y
tick  58 want=remember            choice=remember            Y
tick  59 want=remember            choice=remember            Y
tick  60 want=remember            choice=remember            Y
tick  61 want=listen_pond         choice=listen_pond         Y <-- switch
tick  62 want=listen_pond         choice=listen_pond         Y
tick  63 want=listen_pond         choice=listen_pond         Y
tick  64 want=listen_pond         choice=listen_pond         Y
tick  65 want=listen_pond         choice=listen_pond         Y
tick  66 want=listen_pond         choice=listen_pond         Y
tick  67 want=listen_pond         choice=listen_pond         Y
tick  68 want=listen_pond         choice=listen_pond         Y
tick  69 want=listen_pond         choice=listen_pond         Y
tick  70 want=listen_pond         choice=listen_pond         Y
tick  71 want=listen_pond         choice=listen_pond         Y
tick  72 want=listen_pond         choice=listen_pond         Y
tick  73 want=listen_pond         choice=listen_pond         Y
tick  74 want=listen_pond         choice=listen_pond         Y
tick  75 want=listen_pond         choice=listen_pond         Y
tick  76 want=listen_pond         choice=listen_pond         Y
tick  77 want=listen_pond         choice=listen_pond         Y
tick  78 want=listen_pond         choice=listen_pond         Y
tick  79 want=listen_pond         choice=listen_pond         Y
tick  80 want=listen_pond         choice=listen_pond         Y
tick  81 want=listen_pond         choice=listen_pond         Y
tick  82 want=listen_pond         choice=listen_pond         Y
tick  83 want=listen_pond         choice=listen_pond         Y
tick  84 want=listen_pond         choice=listen_pond         Y
tick  85 want=nothing             choice=nothing             Y <-- switch
tick  86 want=nothing             choice=nothing             Y
tick  87 want=nothing             choice=nothing             Y
tick  88 want=nothing             choice=nothing             Y
tick  89 want=nothing             choice=nothing             Y
tick  90 want=nothing             choice=nothing             Y
tick  91 want=nothing             choice=nothing             Y
tick  92 want=nothing             choice=nothing             Y
tick  93 want=nothing             choice=nothing             Y
tick  94 want=nothing             choice=nothing             Y
tick  95 want=nothing             choice=nothing             Y
```
