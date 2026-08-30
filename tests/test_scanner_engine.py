import pandas as pd

from scanner.scanner_engine import ScannerEngine

engine = ScannerEngine()

df = pd.DataFrame({

    "symbol":["SBIN","RELIANCE"],

    "close":[810,2910],

    "turnover":[900000000,2500000000],

    "avg_volume":[400000,800000],

    "relative_strength_score":[90,82],

    "volume_acceleration_score":[88,81],

    "turnover_score":[91,80],

    "sector_strength_score":[92,83],

    "compression_score":[82,70],

    "structure_score":[93,81],

    "market_context_score":[90,85],

    "breakout_score":[92,75],

    "smart_money_score":[88,77],

    "move_from_open":[0.8,1.2]

})

result = engine.run(df)

print(result[[
    "symbol",
    "total_score",
    "confidence",
    "decision",
    "rank"
]])
