import pandas as pd

from analytics.relative_strength import RelativeStrength

df = pd.DataFrame({

    "instrument_key": ["1", "2", "3"],

    "symbol": [

        "SBIN",

        "RELIANCE",

        "TCS"

    ],

    "sector": [

        "BANK",

        "ENERGY",

        "IT"

    ],

    "day_change_pct": [

        1.50,

        0.80,

        -0.40

    ]

})

sector = {

    "BANK":1.10,

    "ENERGY":0.30,

    "IT":-0.60

}

engine = RelativeStrength()

result = engine.calculate(

    df,

    nifty_change=0.50,

    sector_strength=sector

)

print(result[
    [
        "symbol",
        "rs_nifty",
        "rs_sector",
        "rs_score",
        "rs_rank"
    ]
])
