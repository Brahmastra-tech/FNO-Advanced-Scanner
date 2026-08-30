import pandas as pd

from analytics.market_breadth import MarketBreadth

df = pd.DataFrame({

    "symbol":[

        "SBIN",

        "RELIANCE",

        "TCS",

        "INFY",

        "HDFCBANK"

    ],

    "day_change_pct":[

        1.4,

        0.8,

        -0.5,

        0.3,

        -0.2

    ]

})

engine = MarketBreadth()

breadth = engine.calculate(df)

print(breadth)

print(engine.market_status(breadth))
