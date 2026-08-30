import pandas as pd

from scanner.opportunity_engine import OpportunityEngine

df = pd.DataFrame({

    "symbol":["SBIN","RELIANCE"],

    "rs_score":[4.2,2.1],

    "rvol":[1.8,1.2],

    "sector_strength":[3.5,1.0],

    "compression_score":[92,70],

    "structure_score":[95,75]

})

engine = OpportunityEngine()

result = engine.calculate(

    df,

    market_status="BULLISH"

)

print(

    result[

        [

            "symbol",

            "total_score",

            "confidence",

            "stage"

        ]

    ]

)
