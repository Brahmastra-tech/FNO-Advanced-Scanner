import pandas as pd

from analytics.breakout_engine import BreakoutEngine

df = pd.DataFrame({

    "symbol":[

        "SBIN",

        "RELIANCE"

    ],

    "high":[

        805,

        2930

    ],

    "low":[

        798,

        2890

    ],

    "close":[

        804.7,

        2910

    ],

    "compression_score":[

        92,

        65

    ],

    "structure_score":[

        95,

        60

    ],

    "smart_money_score":[

        82,

        45

    ]

})

engine = BreakoutEngine()

result = engine.calculate(df)

print(

    result[

        [

            "symbol",

            "breakout_score",

            "breakout_ready"

        ]

    ]

)
