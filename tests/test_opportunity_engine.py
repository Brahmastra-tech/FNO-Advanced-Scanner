import pandas as pd

from scanner.opportunity_engine import OpportunityEngine

engine = OpportunityEngine()

df = pd.DataFrame({

    "symbol":[

        "SBIN",

        "BEL",

        "HAL"

    ],

    "decision":[

        "BREAKOUT",

        "READY",

        "WATCH"

    ],

    "total_score":[

        95,

        87,

        72

    ],

    "confidence":[

        92,

        90,

        78

    ]

})

print(

    engine.process(df)

)
