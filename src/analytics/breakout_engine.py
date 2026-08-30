import pandas as pd
import numpy as np


class BreakoutEngine:
    """
    Breakout Readiness Engine

    Determines whether a stock is
    preparing for expansion.
    """

    def __init__(self):
        pass

    def calculate(self, df):

        market = df.copy()

        required = [

            "high",
            "low",
            "close",
            "compression_score",
            "structure_score",
            "smart_money_score"

        ]

        for col in required:

            if col not in market.columns:

                raise Exception(f"Missing column : {col}")

        # -----------------------------------
        # Distance From High
        # -----------------------------------

        market["distance_high_pct"] = (

            (

                market["high"]

                -

                market["close"]

            )

            /

            market["high"]

            * 100

        ).round(2)

        # -----------------------------------
        # Distance From Low
        # -----------------------------------

        market["distance_low_pct"] = (

            (

                market["close"]

                -

                market["low"]

            )

            /

            market["low"]

            * 100

        ).round(2)

        # -----------------------------------
        # Breakout Score
        # -----------------------------------

        score = []

        ready = []

        for _, row in market.iterrows():

            s = 0

            # Compression

            if row["compression_score"] >= 80:

                s += 25

            # Structure

            if row["structure_score"] >= 80:

                s += 25

            # Smart Money

            if row["smart_money_score"] >= 70:

                s += 25

            # Close Near High

            if row["distance_high_pct"] <= 0.50:

                s += 25

            score.append(s)

            ready.append("YES" if s >= 75 else "NO")

        market["breakout_score"] = score

        market["breakout_ready"] = ready

        return market

    def ready(self, df):

        return df[

            df["breakout_ready"] == "YES"

        ].sort_values(

            by="breakout_score",

            ascending=False

        )

    def watchlist(self, df):

        return df[

            df["breakout_score"] >= 50

        ].sort_values(

            by="breakout_score",

            ascending=False

        )
