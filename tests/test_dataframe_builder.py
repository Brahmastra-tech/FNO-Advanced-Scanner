from engine.dataframe_builder import DataFrameBuilder
import pandas as pd

df = pd.DataFrame({

    "instrument_key": ["1", "2"],

    "symbol": ["SBIN", "RELIANCE"],

    "ltp": [820, 3010],

    "volume": [120000, 450000],

    "turnover": [95000000, 780000000]

})

builder = DataFrameBuilder()

master = builder.build(df)

print(master.head())

print()

print(builder.stats())
