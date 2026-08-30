import pandas as pd

from scanner.decision_engine import DecisionEngine

engine = DecisionEngine()

df = pd.DataFrame({

    "symbol":["SBIN"],

    "total_score":[91],

    "confidence":[90],

    "relative_strength_score":[92],

    "volume_acceleration_score":[90],

    "sector_strength_score":[88],

    "breakout_score":[91],

    "smart_money_score":[87],

    "move_from_open":[0.8]

})

print(engine.process(df))
