import pandas as pd

from scanner.scoring_engine import ScoringEngine

engine = ScoringEngine()

df = pd.DataFrame({

    "symbol":["SBIN"],

    "relative_strength_score":[90],

    "volume_acceleration_score":[85],

    "turnover_score":[82],

    "sector_strength_score":[91],

    "compression_score":[75],

    "structure_score":[88],

    "market_context_score":[90]

})

print(engine.process(df))
