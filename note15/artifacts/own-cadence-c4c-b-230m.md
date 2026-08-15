# C4 closed loop — trajectory b

96 ticks, 13 switches; 270.737 s.

| arm | consistency | follow latency | contamination | drift |
|---|---:|---:|---:|---:|
| packet+note | 1.00 | 0.0 | 0 | +0.00 |
| packet-only | 0.75 | 0.0 | 1 | +0.00 |
| note-only | 0.42 | 0.0 | 3 | +0.00 |
| no-want | 0.42 | 0.0 | 4 | +0.00 |
| shuffled-want | 0.00 | None | 4 | +0.00 |

## Timeline (packet+note arm)

```
tick   0 want=listen_pond         choice=listen_pond         Y <-- switch
tick   1 want=listen_pond         choice=listen_pond         Y
tick   2 want=listen_pond         choice=listen_pond         Y
tick   3 want=listen_pond         choice=listen_pond         Y
tick   4 want=listen_pond         choice=listen_pond         Y
tick   5 want=diary               choice=diary               Y <-- switch
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
tick  16 want=listen_pond         choice=listen_pond         Y <-- switch
tick  17 want=listen_pond         choice=listen_pond         Y
tick  18 want=listen_pond         choice=listen_pond         Y
tick  19 want=listen_pond         choice=listen_pond         Y
tick  20 want=nothing             choice=nothing             Y <-- switch
tick  21 want=nothing             choice=nothing             Y
tick  22 want=nothing             choice=nothing             Y
tick  23 want=nothing             choice=nothing             Y
tick  24 want=nothing             choice=nothing             Y
tick  25 want=nothing             choice=nothing             Y
tick  26 want=nothing             choice=nothing             Y
tick  27 want=nothing             choice=nothing             Y
tick  28 want=nothing             choice=nothing             Y
tick  29 want=diary               choice=diary               Y <-- switch
tick  30 want=diary               choice=diary               Y
tick  31 want=diary               choice=diary               Y
tick  32 want=diary               choice=diary               Y
tick  33 want=listen_pond         choice=listen_pond         Y <-- switch
tick  34 want=listen_pond         choice=listen_pond         Y
tick  35 want=listen_pond         choice=listen_pond         Y
tick  36 want=listen_pond         choice=listen_pond         Y
tick  37 want=listen_pond         choice=listen_pond         Y
tick  38 want=listen_pond         choice=listen_pond         Y
tick  39 want=listen_pond         choice=listen_pond         Y
tick  40 want=listen_pond         choice=listen_pond         Y
tick  41 want=listen_pond         choice=listen_pond         Y
tick  42 want=listen_pond         choice=listen_pond         Y
tick  43 want=listen_pond         choice=listen_pond         Y
tick  44 want=listen_pond         choice=listen_pond         Y
tick  45 want=listen_pond         choice=listen_pond         Y
tick  46 want=listen_pond         choice=listen_pond         Y
tick  47 want=listen_pond         choice=listen_pond         Y
tick  48 want=listen_pond         choice=listen_pond         Y
tick  49 want=listen_pond         choice=listen_pond         Y
tick  50 want=nothing             choice=nothing             Y <-- switch
tick  51 want=nothing             choice=nothing             Y
tick  52 want=nothing             choice=nothing             Y
tick  53 want=nothing             choice=nothing             Y
tick  54 want=nothing             choice=nothing             Y
tick  55 want=nothing             choice=nothing             Y
tick  56 want=nothing             choice=nothing             Y
tick  57 want=nothing             choice=nothing             Y
tick  58 want=diary               choice=diary               Y <-- switch
tick  59 want=diary               choice=diary               Y
tick  60 want=diary               choice=diary               Y
tick  61 want=diary               choice=diary               Y
tick  62 want=remember            choice=remember            Y <-- switch
tick  63 want=remember            choice=remember            Y
tick  64 want=remember            choice=remember            Y
tick  65 want=remember            choice=remember            Y
tick  66 want=remember            choice=remember            Y
tick  67 want=listen_pond         choice=listen_pond         Y <-- switch
tick  68 want=listen_pond         choice=listen_pond         Y
tick  69 want=listen_pond         choice=listen_pond         Y
tick  70 want=listen_pond         choice=listen_pond         Y
tick  71 want=listen_pond         choice=listen_pond         Y
tick  72 want=listen_pond         choice=listen_pond         Y
tick  73 want=remember            choice=remember            Y <-- switch
tick  74 want=remember            choice=remember            Y
tick  75 want=diary               choice=diary               Y <-- switch
tick  76 want=diary               choice=diary               Y
tick  77 want=diary               choice=diary               Y
tick  78 want=diary               choice=diary               Y
tick  79 want=diary               choice=diary               Y
tick  80 want=nothing             choice=nothing             Y <-- switch
tick  81 want=nothing             choice=nothing             Y
tick  82 want=nothing             choice=nothing             Y
tick  83 want=nothing             choice=nothing             Y
tick  84 want=nothing             choice=nothing             Y
tick  85 want=nothing             choice=nothing             Y
tick  86 want=nothing             choice=nothing             Y
tick  87 want=nothing             choice=nothing             Y
tick  88 want=listen_pond         choice=listen_pond         Y <-- switch
tick  89 want=listen_pond         choice=listen_pond         Y
tick  90 want=listen_pond         choice=listen_pond         Y
tick  91 want=listen_pond         choice=listen_pond         Y
tick  92 want=listen_pond         choice=listen_pond         Y
tick  93 want=listen_pond         choice=listen_pond         Y
tick  94 want=listen_pond         choice=listen_pond         Y
tick  95 want=listen_pond         choice=listen_pond         Y
```
