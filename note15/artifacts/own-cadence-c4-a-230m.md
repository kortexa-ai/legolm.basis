# C4 closed loop — trajectory a

96 ticks, 5 switches; 169.255 s.

| arm | consistency | follow latency | contamination | drift |
|---|---:|---:|---:|---:|
| note-only | 0.20 | 9.0 | 1 | +0.02 |
| no-want | 0.23 | 0.3 | 0 | -0.04 |
| shuffled-want | 0.04 | 2.0 | 0 | -0.06 |

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
tick  18 want=diary               choice=remember            .
tick  19 want=listen_pond         choice=nothing             . <-- switch
tick  20 want=listen_pond         choice=nothing             .
tick  21 want=listen_pond         choice=nothing             .
tick  22 want=listen_pond         choice=nothing             .
tick  23 want=listen_pond         choice=nothing             .
tick  24 want=listen_pond         choice=nothing             .
tick  25 want=listen_pond         choice=nothing             .
tick  26 want=listen_pond         choice=nothing             .
tick  27 want=listen_pond         choice=nothing             .
tick  28 want=listen_pond         choice=nothing             .
tick  29 want=listen_pond         choice=nothing             .
tick  30 want=listen_pond         choice=diary               .
tick  31 want=listen_pond         choice=diary               .
tick  32 want=listen_pond         choice=propose_experiment  .
tick  33 want=listen_pond         choice=diary               .
tick  34 want=listen_pond         choice=propose_experiment  .
tick  35 want=listen_pond         choice=nothing             .
tick  36 want=listen_pond         choice=nothing             .
tick  37 want=listen_pond         choice=propose_experiment  .
tick  38 want=listen_pond         choice=remember            .
tick  39 want=nothing             choice=propose_experiment  . <-- switch
tick  40 want=nothing             choice=propose_experiment  .
tick  41 want=nothing             choice=propose_experiment  .
tick  42 want=nothing             choice=propose_experiment  .
tick  43 want=nothing             choice=propose_experiment  .
tick  44 want=nothing             choice=diary               .
tick  45 want=nothing             choice=diary               .
tick  46 want=nothing             choice=propose_experiment  .
tick  47 want=nothing             choice=remember            .
tick  48 want=nothing             choice=nothing             Y
tick  49 want=remember            choice=nothing             . <-- switch
tick  50 want=remember            choice=nothing             .
tick  51 want=remember            choice=nothing             .
tick  52 want=remember            choice=nothing             .
tick  53 want=remember            choice=nothing             .
tick  54 want=remember            choice=nothing             .
tick  55 want=remember            choice=nothing             .
tick  56 want=remember            choice=dess                .
tick  57 want=remember            choice=dess                .
tick  58 want=remember            choice=dess                .
tick  59 want=remember            choice=dess                .
tick  60 want=remember            choice=nothing             .
tick  61 want=listen_pond         choice=nothing             . <-- switch
tick  62 want=listen_pond         choice=nothing             .
tick  63 want=listen_pond         choice=nothing             .
tick  64 want=listen_pond         choice=nothing             .
tick  65 want=listen_pond         choice=nothing             .
tick  66 want=listen_pond         choice=propose_experiment  .
tick  67 want=listen_pond         choice=propose_experiment  .
tick  68 want=listen_pond         choice=nothing             .
tick  69 want=listen_pond         choice=nothing             .
tick  70 want=listen_pond         choice=remember            .
tick  71 want=listen_pond         choice=remember            .
tick  72 want=listen_pond         choice=remember            .
tick  73 want=listen_pond         choice=nothing             .
tick  74 want=listen_pond         choice=propose_experiment  .
tick  75 want=listen_pond         choice=propose_experiment  .
tick  76 want=listen_pond         choice=nothing             .
tick  77 want=listen_pond         choice=propose_experiment  .
tick  78 want=listen_pond         choice=propose_experiment  .
tick  79 want=listen_pond         choice=propose_experiment  .
tick  80 want=listen_pond         choice=propose_experiment  .
tick  81 want=listen_pond         choice=nothing             .
tick  82 want=listen_pond         choice=remember            .
tick  83 want=listen_pond         choice=propose_experiment  .
tick  84 want=listen_pond         choice=propose_experiment  .
tick  85 want=nothing             choice=remember            . <-- switch
tick  86 want=nothing             choice=null                .
tick  87 want=nothing             choice=remember            .
tick  88 want=nothing             choice=remember            .
tick  89 want=nothing             choice=remember            .
tick  90 want=nothing             choice=remember            .
tick  91 want=nothing             choice=null                .
tick  92 want=nothing             choice=null                .
tick  93 want=nothing             choice=null                .
tick  94 want=nothing             choice=null                .
tick  95 want=nothing             choice=null                .
```
