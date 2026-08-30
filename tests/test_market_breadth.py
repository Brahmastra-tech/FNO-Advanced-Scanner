import pandas as pd

from market.market_breadth import MarketBreadth

engine = MarketBreadth()

df = pd.DataFrame({

    "symbol":[

        "SBIN",

        "RELIANCE",

        "ICICI",

        "BEL"

    ],

    "day_change":[

        1.2,

        -0.6,

        0.4,

        2.1

    ]

})

print(

    engine.analyze(df)

)
