import pandas as pd

from scanner.rule_engine import RuleEngine

df = pd.DataFrame({

    "symbol": ["SBIN", "RELIANCE"],

    "rs_score": [3.2, 1.0],

    "rvol": [1.8, 0.9],

    "sector_strength": [3, 1],

    "smart_money_score": [82, 55],

    "compression_score": [90, 60],

    "structure_score": [92, 70],

    "breakout_score": [88, 45]

})

engine = RuleEngine()

result = engine.calculate(

    df,

    market_status="BULLISH"

)

print(

    result[

        [

            "symbol",

            "rule_score",

            "scanner_stage",

            "passed_rules",

            "failed_rules"

        ]

    ]

)
