import pandas as pd

from analytics.volume_engine import VolumeEngine

current = pd.DataFrame({

    "instrument_key":["1","2"],

    "symbol":["SBIN","RELIANCE"],

    "volume":[150000,420000],

    "turnover":[180000000,1250000000]

})

previous = pd.DataFrame({

    "instrument_key":["1","2"],

    "volume":[100000,400000],

    "turnover":[150000000,1200000000]

})

engine = VolumeEngine()

result = engine.calculate(current, previous)

print(result[
    [
        "symbol",
        "volume_acceleration",
        "turnover_acceleration",
        "rvol"
    ]
])
