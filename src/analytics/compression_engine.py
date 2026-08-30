import pandas as pd
import numpy as np


class CompressionEngine:
    """
    Compression Engine

    Calculates:
    - Range %
    - Candle Body %
    - Compression Score
    - Breakout Readiness
    """

    def __init__(self):
        pass

    def calculate(self, df):

        market = df.copy()

        required = [
            "high",
            "low",
            "open",
            "close"
        ]

        for col in required:
            if col not in market.columns:
                raise Exception(f"Missing column : {col}")

        # ----------------------------
        # Candle Range
        # ----------------------------

        market["range"] = (

            market["high"]

            -

            market["low"]

        )

        # ----------------------------
        # Candle Body
        # ----------------------------

        market["body"] = (

            market["close"]

            -

            market["open"]

        ).abs()

        # ----------------------------
        # Range %
        # ----------------------------

        market["range_pct"] = (

            market["range"]

            /

            market["close"]

            * 100

        ).round(2)

        # ----------------------------
        # Body %
        # ----------------------------

        market["body_pct"] = (

            market["body"]

            /

            market["range"]

            .replace(0, np.nan)

        ).fillna(0).round(2)

        # ----------------------------
        # Compression Score
        # ----------------------------

        score = []

        for _, row in market.iterrows():

            s = 100

            if row["range_pct"] > 3:
                s -= 40

            elif row["range_pct"] > 2:
                s -= 20

            if row["body_pct"] > 0.70:
                s -= 20

            elif row["body_pct"] > 0.50:
                s -= 10

            score.append(max(s, 0))

        market["compression_score"] = score

        # ----------------------------
        # Breakout Readiness
        # ----------------------------

        market["breakout_ready"] = np.where(

            market["compression_score"] >= 80,

            "YES",

            "NO"

        )

        return market

    def best_setups(self, df, top=20):

        return df.sort_values(

            by="compression_score",

            ascending=False

        ).head(top)
