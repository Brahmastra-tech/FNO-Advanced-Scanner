import pandas as pd

from analytics.structure_engine import StructureEngine

current = pd.DataFrame({

    "instrument_key":["1","2"],

    "symbol":["SBIN","RELIANCE"],

    "high":[805,2925],

    "low":[799,2898],

    "close":[803,2915]

})

previous = pd.DataFrame({

    "instrument_key":["1","2"],

    "high":[802,2930],

    "low":[795,2902],

    "close":[800,2920]

})

engine = StructureEngine()

result = engine.calculate(current, previous)

print(result[
[
"symbol",
"trend",
"structure_score"
]
])
