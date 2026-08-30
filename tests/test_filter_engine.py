import pandas as pd

from scanner.filter_engine import FilterEngine

engine = FilterEngine()

df = pd.DataFrame({

    "symbol":["SBIN","ABC"],

    "close":[810,45],

    "turnover":[500000000,1000000],

    "avg_volume":[300000,10000],

    "relative_strength_score":[90,30],

    "sector_strength_score":[88,20],

    "volume_acceleration_score":[82,10],

    "compression_score":[80,10],

    "structure_score":[91,15],

    "market_context_score":[85,50],

    "smart_money_score":[88,20],

    "move_from_open":[0.8,4.2]

})

print(engine.apply(df))
