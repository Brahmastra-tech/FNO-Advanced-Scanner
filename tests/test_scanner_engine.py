import pandas as pd

from scanner.scanner_engine import ScannerEngine

current = pd.DataFrame({

    "instrument_key":["1","2"],

    "symbol":["SBIN","RELIANCE"],

    "sector":[

        "BANK",

        "ENERGY"

    ],

    "open":[800,2900],

    "high":[805,2930],

    "low":[798,2890],

    "close":[804,2925],

    "volume":[180000,420000],

    "turnover":[

        145000000,

        1800000000

    ]

})

previous = pd.DataFrame({

    "instrument_key":["1","2"],

    "symbol":["SBIN","RELIANCE"],

    "sector":[

        "BANK",

        "ENERGY"

    ],

    "open":[795,2895],

    "high":[802,2925],

    "low":[794,2885],

    "close":[800,2915],

    "volume":[150000,380000],

    "turnover":[

        120000000,

        1600000000

    ]

})

scanner = ScannerEngine()

result = scanner.run(

    current,

    previous,

    market_status="BULLISH"

)

print(

    result[

        [

            "symbol",

            "total_score",

            "scanner_stage"

        ]

    ]

)
