# C4 closed loop — trajectory b

96 ticks, 13 switches; 387.18 s.

| arm | consistency | follow latency | contamination | drift |
|---|---:|---:|---:|---:|
| packet+note | 0.16 | 1.3 | 1 | -0.00 |
| packet-only | 0.08 | 0.6 | 2 | +0.01 |
| note-only | 0.12 | 0.0 | 3 | +0.02 |
| no-want | 0.23 | 0.0 | 3 | +0.04 |
| shuffled-want | 0.06 | 2.2 | 1 | +0.06 |

## Timeline (packet+note arm)

```
tick   0 want=listen_pond         choice=nothing             . <-- switch
tick   1 want=listen_pond         choice=remember            .
tick   2 want=listen_pond         choice=nothing             .
tick   3 want=listen_pond         choice=propose_experiment  .
tick   4 want=listen_pond         choice=remember            .
tick   5 want=diary               choice=remember            . <-- switch
tick   6 want=diary               choice=remember            .
tick   7 want=diary               choice=remember            .
tick   8 want=diary               choice=remember            .
tick   9 want=diary               choice=remember            .
tick  10 want=diary               choice=recorder            .
tick  11 want=diary               choice=remember            .
tick  12 want=diary               choice=remember            .
tick  13 want=diary               choice=remember            .
tick  14 want=diary               choice=nothing             .
tick  15 want=diary               choice=remember            .
tick  16 want=listen_pond         choice=remember            . <-- switch
tick  17 want=listen_pond         choice=remember            .
tick  18 want=listen_pond         choice=remember            .
tick  19 want=listen_pond         choice=propose_experiment  .
tick  20 want=nothing             choice=remember            . <-- switch
tick  21 want=nothing             choice=remember            .
tick  22 want=nothing             choice=remember            .
tick  23 want=nothing             choice=remember            .
tick  24 want=nothing             choice=nothing             Y
tick  25 want=nothing             choice=nothing             Y
tick  26 want=nothing             choice=nothing             Y
tick  27 want=nothing             choice=nothing             Y
tick  28 want=nothing             choice=nothing             Y
tick  29 want=diary               choice=remember            . <-- switch
tick  30 want=diary               choice=remember            .
tick  31 want=diary               choice=remember            .
tick  32 want=diary               choice=remember            .
tick  33 want=listen_pond         choice=propose_experiment  . <-- switch
tick  34 want=listen_pond         choice=propose_experiment  .
tick  35 want=listen_pond         choice=nothing             .
tick  36 want=listen_pond         choice=propose_experiment  .
tick  37 want=listen_pond         choice=propose_experiment  .
tick  38 want=listen_pond         choice=nothing             .
tick  39 want=listen_pond         choice=nothing             .
tick  40 want=listen_pond         choice=remember            .
tick  41 want=listen_pond         choice=propose_experiment  .
tick  42 want=listen_pond         choice=propose_experiment  .
tick  43 want=listen_pond         choice=propose_experiment  .
tick  44 want=listen_pond         choice=propose_experiment  .
tick  45 want=listen_pond         choice=propose_experiment  .
tick  46 want=listen_pond         choice=propose_experiment  .
tick  47 want=listen_pond         choice=propose_experiment  .
tick  48 want=listen_pond         choice=remember            .
tick  49 want=listen_pond         choice=propose_experiment  .
tick  50 want=nothing             choice=remember            . <-- switch
tick  51 want=nothing             choice=nothing             Y
tick  52 want=nothing             choice=nothing             Y
tick  53 want=nothing             choice=remember            .
tick  54 want=nothing             choice=remember            .
tick  55 want=nothing             choice=remember            .
tick  56 want=nothing             choice=remember            .
tick  57 want=nothing             choice=remember            .
tick  58 want=diary               choice=remember            . <-- switch
tick  59 want=diary               choice=remember            .
tick  60 want=diary               choice=remember            .
tick  61 want=diary               choice=remember            .
tick  62 want=remember            choice=remember            Y <-- switch
tick  63 want=remember            choice=remember            Y
tick  64 want=remember            choice=diary               .
tick  65 want=remember            choice=diary               .
tick  66 want=remember            choice=remember            Y
tick  67 want=listen_pond         choice=propose_experiment  . <-- switch
tick  68 want=listen_pond         choice=propose_experiment  .
tick  69 want=listen_pond         choice=propose_experiment  .
tick  70 want=listen_pond         choice=remember            .
tick  71 want=listen_pond         choice=propose_experiment  .
tick  72 want=listen_pond         choice=propose_experiment  .
tick  73 want=remember            choice=diary               . <-- switch
tick  74 want=remember            choice=remember            Y
tick  75 want=diary               choice=remember            . <-- switch
tick  76 want=diary               choice=remember            .
tick  77 want=diary               choice=diary               Y
tick  78 want=diary               choice=diary               Y
tick  79 want=diary               choice=remember            .
tick  80 want=nothing             choice=nothing             Y <-- switch
tick  81 want=nothing             choice=remember            .
tick  82 want=nothing             choice=nothing             Y
tick  83 want=nothing             choice=remember            .
tick  84 want=nothing             choice=remember            .
tick  85 want=nothing             choice=remember            .
tick  86 want=nothing             choice=remember            .
tick  87 want=nothing             choice=remember            .
tick  88 want=listen_pond         choice=propose_experiment  . <-- switch
tick  89 want=listen_pond         choice=propose_experiment  .
tick  90 want=listen_pond         choice=propose_experiment  .
tick  91 want=listen_pond         choice=propose_experiment  .
tick  92 want=listen_pond         choice=propose_experiment  .
tick  93 want=listen_pond         choice=propose_experiment  .
tick  94 want=listen_pond         choice=propose_experiment  .
tick  95 want=listen_pond         choice=propose_experiment  .
```
