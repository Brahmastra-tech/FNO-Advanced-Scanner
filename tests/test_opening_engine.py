import pandas as pd

from analytics.opening_engine import OpeningEngine

engine = OpeningEngine()

df = pd.DataFrame({

    "instrument_key":["1"],

    "symbol":["SBIN"],

    "open":[800],

    "high":[805],

    "low":[798],

    "close":[804],

    "volume":[180000],

    "turnover":[145000000]

})

engine.capture(df)

live = df.copy()

merged = engine.merge(live)

print(merged.columns)
