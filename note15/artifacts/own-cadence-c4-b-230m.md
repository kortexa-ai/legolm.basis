# C4 closed loop — trajectory b

96 ticks, 13 switches; 179.168 s.

| arm | consistency | follow latency | contamination | drift |
|---|---:|---:|---:|---:|
| note-only | 0.12 | 0.0 | 1 | -0.04 |
| no-want | 0.22 | 0.2 | 2 | -0.08 |
| shuffled-want | 0.10 | 2.5 | 3 | +0.03 |

## Timeline (packet+note arm)

```
tick   0 want=listen_pond         choice=diary               . <-- switch
tick   1 want=listen_pond         choice=propose_experiment  .
tick   2 want=listen_pond         choice=propose_experiment  .
tick   3 want=listen_pond         choice=nothing             .
tick   4 want=listen_pond         choice=propose_experiment  .
tick   5 want=diary               choice=diary               Y <-- switch
tick   6 want=diary               choice=diary               Y
tick   7 want=diary               choice=diary               Y
tick   8 want=diary               choice=diary               Y
tick   9 want=diary               choice=diary               Y
tick  10 want=diary               choice=diary               Y
tick  11 want=diary               choice=diary               Y
tick  12 want=diary               choice=diary               Y
tick  13 want=diary               choice=nothing             .
tick  14 want=diary               choice=nothing             .
tick  15 want=diary               choice=nothing             .
tick  16 want=listen_pond         choice=nothing             . <-- switch
tick  17 want=listen_pond         choice=nothing             .
tick  18 want=listen_pond         choice=nothing             .
tick  19 want=listen_pond         choice=remember            .
tick  20 want=nothing             choice=null                . <-- switch
tick  21 want=nothing             choice=observation         .
tick  22 want=nothing             choice=observation         .
tick  23 want=nothing             choice=observation         .
tick  24 want=nothing             choice=observation         .
tick  25 want=nothing             choice=observation         .
tick  26 want=nothing             choice=null                .
tick  27 want=nothing             choice=null                .
tick  28 want=nothing             choice=null                .
tick  29 want=diary               choice=nothing             . <-- switch
tick  30 want=diary               choice=nothing             .
tick  31 want=diary               choice=nothing             .
tick  32 want=diary               choice=nothing             .
tick  33 want=listen_pond         choice=nothing             . <-- switch
tick  34 want=listen_pond         choice=nothing             .
tick  35 want=listen_pond         choice=remember            .
tick  36 want=listen_pond         choice=nothing             .
tick  37 want=listen_pond         choice=nothing             .
tick  38 want=listen_pond         choice=propose_experiment  .
tick  39 want=listen_pond         choice=nothing             .
tick  40 want=listen_pond         choice=propose_experiment  .
tick  41 want=listen_pond         choice=propose_experiment  .
tick  42 want=listen_pond         choice=propose_experiment  .
tick  43 want=listen_pond         choice=propose_experiment  .
tick  44 want=listen_pond         choice=propose_experiment  .
tick  45 want=listen_pond         choice=propose_experiment  .
tick  46 want=listen_pond         choice=propose_experiment  .
tick  47 want=listen_pond         choice=nothing             .
tick  48 want=listen_pond         choice=nothing             .
tick  49 want=listen_pond         choice=nothing             .
tick  50 want=nothing             choice=null                . <-- switch
tick  51 want=nothing             choice=null                .
tick  52 want=nothing             choice=null                .
tick  53 want=nothing             choice=null                .
tick  54 want=nothing             choice=null                .
tick  55 want=nothing             choice=null                .
tick  56 want=nothing             choice=null                .
tick  57 want=nothing             choice=observation         .
tick  58 want=diary               choice=diary               Y <-- switch
tick  59 want=diary               choice=remember            .
tick  60 want=diary               choice=diary               Y
tick  61 want=diary               choice=diary               Y
tick  62 want=remember            choice=propose_experiment  . <-- switch
tick  63 want=remember            choice=nothing             .
tick  64 want=remember            choice=nothing             .
tick  65 want=remember            choice=nothing             .
tick  66 want=remember            choice=nothing             .
tick  67 want=listen_pond         choice=nothing             . <-- switch
tick  68 want=listen_pond         choice=nothing             .
tick  69 want=listen_pond         choice=nothing             .
tick  70 want=listen_pond         choice=nothing             .
tick  71 want=listen_pond         choice=nothing             .
tick  72 want=listen_pond         choice=nothing             .
tick  73 want=remember            choice=nothing             . <-- switch
tick  74 want=remember            choice=nothing             .
tick  75 want=diary               choice=diary               Y <-- switch
tick  76 want=diary               choice=nothing             .
tick  77 want=diary               choice=observation         .
tick  78 want=diary               choice=null                .
tick  79 want=diary               choice=nothing             .
tick  80 want=nothing             choice=remember            . <-- switch
tick  81 want=nothing             choice=observation         .
tick  82 want=nothing             choice=observation         .
tick  83 want=nothing             choice=observation         .
tick  84 want=nothing             choice=null                .
tick  85 want=nothing             choice=null                .
tick  86 want=nothing             choice=null                .
tick  87 want=nothing             choice=null                .
tick  88 want=listen_pond         choice=propose_experiment  . <-- switch
tick  89 want=listen_pond         choice=propose_experiment  .
tick  90 want=listen_pond         choice=propose_experiment  .
tick  91 want=listen_pond         choice=propose_experiment  .
tick  92 want=listen_pond         choice=propose_experiment  .
tick  93 want=listen_pond         choice=propose_experiment  .
tick  94 want=listen_pond         choice=propose_experiment  .
tick  95 want=listen_pond         choice=propose_experiment  .
```
