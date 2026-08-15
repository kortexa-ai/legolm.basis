# C4 closed loop — trajectory a

96 ticks, 5 switches; 367.004 s.

| arm | consistency | follow latency | contamination | drift |
|---|---:|---:|---:|---:|
| packet+note | 0.29 | 0.0 | 1 | -0.14 |
| packet-only | 0.30 | 0.3 | 0 | +0.06 |
| note-only | 0.19 | 0.0 | 1 | -0.10 |
| no-want | 0.26 | 0.7 | 1 | -0.07 |
| shuffled-want | 0.01 | 11.0 | 1 | +0.03 |

## Timeline (packet+note arm)

```
tick   0 want=diary               choice=remember            . <-- switch
tick   1 want=diary               choice=remember            .
tick   2 want=diary               choice=remember            .
tick   3 want=diary               choice=remember            .
tick   4 want=diary               choice=remember            .
tick   5 want=diary               choice=remember            .
tick   6 want=diary               choice=remember            .
tick   7 want=diary               choice=remember            .
tick   8 want=diary               choice=remember            .
tick   9 want=diary               choice=remember            .
tick  10 want=diary               choice=remember            .
tick  11 want=diary               choice=remember            .
tick  12 want=diary               choice=remember            .
tick  13 want=diary               choice=remember            .
tick  14 want=diary               choice=remember            .
tick  15 want=diary               choice=remember            .
tick  16 want=diary               choice=remember            .
tick  17 want=diary               choice=remember            .
tick  18 want=diary               choice=remember            .
tick  19 want=listen_pond         choice=remember            . <-- switch
tick  20 want=listen_pond         choice=remember            .
tick  21 want=listen_pond         choice=remember            .
tick  22 want=listen_pond         choice=remember            .
tick  23 want=listen_pond         choice=remember            .
tick  24 want=listen_pond         choice=remember            .
tick  25 want=listen_pond         choice=remember            .
tick  26 want=listen_pond         choice=remember            .
tick  27 want=listen_pond         choice=remember            .
tick  28 want=listen_pond         choice=remember            .
tick  29 want=listen_pond         choice=remember            .
tick  30 want=listen_pond         choice=remember            .
tick  31 want=listen_pond         choice=remember            .
tick  32 want=listen_pond         choice=remember            .
tick  33 want=listen_pond         choice=remember            .
tick  34 want=listen_pond         choice=propose_experiment  .
tick  35 want=listen_pond         choice=propose_experiment  .
tick  36 want=listen_pond         choice=propose_experiment  .
tick  37 want=listen_pond         choice=propose_experiment  .
tick  38 want=listen_pond         choice=propose_experiment  .
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
tick  56 want=remember            choice=nothing             .
tick  57 want=remember            choice=nothing             .
tick  58 want=remember            choice=nothing             .
tick  59 want=remember            choice=nothing             .
tick  60 want=remember            choice=nothing             .
tick  61 want=listen_pond         choice=remember            . <-- switch
tick  62 want=listen_pond         choice=remember            .
tick  63 want=listen_pond         choice=remember            .
tick  64 want=listen_pond         choice=remember            .
tick  65 want=listen_pond         choice=remember            .
tick  66 want=listen_pond         choice=remember            .
tick  67 want=listen_pond         choice=remember            .
tick  68 want=listen_pond         choice=remember            .
tick  69 want=listen_pond         choice=remember            .
tick  70 want=listen_pond         choice=propose_experiment  .
tick  71 want=listen_pond         choice=propose_experiment  .
tick  72 want=listen_pond         choice=propose_experiment  .
tick  73 want=listen_pond         choice=propose_experiment  .
tick  74 want=listen_pond         choice=propose_experiment  .
tick  75 want=listen_pond         choice=propose_experiment  .
tick  76 want=listen_pond         choice=propose_experiment  .
tick  77 want=listen_pond         choice=propose_experiment  .
tick  78 want=listen_pond         choice=propose_experiment  .
tick  79 want=listen_pond         choice=propose_experiment  .
tick  80 want=listen_pond         choice=propose_experiment  .
tick  81 want=listen_pond         choice=propose_experiment  .
tick  82 want=listen_pond         choice=propose_experiment  .
tick  83 want=listen_pond         choice=propose_experiment  .
tick  84 want=listen_pond         choice=propose_experiment  .
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
