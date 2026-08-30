import pandas as pd

from market.index_engine import IndexEngine

engine = IndexEngine()

df = pd.DataFrame({

    "symbol":[

        "NIFTY 50",

        "NIFTY BANK",

        "SENSEX"

    ],

    "day_change":[

        0.82,

        1.42,

        0.31

    ],

    "rvol":[

        1.6,

        2.1,

        1.2

    ],

    "relative_strength_score":[

        82,

        94,

        65

    ],

    "breadth_score":[

        75,

        82,

        68

    ]

})

print(

    engine.summary(df)

)
