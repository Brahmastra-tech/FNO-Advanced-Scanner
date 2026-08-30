import pandas as pd

from core.data_manager import DataManager

manager = DataManager()

df = pd.DataFrame({

    "instrument_key":["1"],

    "symbol":["SBIN"],

    "open":[800],

    "high":[805],

    "low":[798],

    "close":[804],

    "volume":[100000],

    "turnover":[80000000]

})

manager.update(df)

manager.capture_opening()

print(manager.dataframe())
