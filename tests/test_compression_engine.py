import pandas as pd

from analytics.compression_engine import CompressionEngine

df = pd.DataFrame({

    "symbol":[

        "SBIN",

        "RELIANCE",

        "TCS"

    ],

    "open":[

        800,

        2900,

        3400

    ],

    "high":[

        804,

        2925,

        3408

    ],

    "low":[

        798,

        2895,

        3398

    ],

    "close":[

        802,

        2910,

        3402

    ]

})

engine = CompressionEngine()

result = engine.calculate(df)

print(

    result[

        [

            "symbol",

            "range_pct",

            "body_pct",

            "compression_score",

            "breakout_ready"

        ]

    ]

)
