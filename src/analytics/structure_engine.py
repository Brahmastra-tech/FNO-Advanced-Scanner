import pandas as pd
import numpy as np


class StructureEngine:
    """
    Price Structure Engine

    Calculates:

    • Higher High
    • Higher Low
    • Lower High
    • Lower Low
    • Trend
    • Structure Score
    """

    def __init__(self):
        pass

    def calculate(self, current_df, previous_df):

        df = current_df.copy()

        prev = previous_df[
            [
                "instrument_key",
                "high",
                "low",
                "close"
            ]
        ].copy()

        prev.columns = [

            "instrument_key",

            "prev_high",

            "prev_low",

            "prev_close"

        ]

        df = df.merge(
            prev,
            on="instrument_key",
            how="left"
        )

        # -------------------------
        # Higher High
        # -------------------------

        df["higher_high"] = (
            df["high"] > df["prev_high"]
        )

        # -------------------------
        # Higher Low
        # -------------------------

        df["higher_low"] = (
            df["low"] > df["prev_low"]
        )

        # -------------------------
        # Lower High
        # -------------------------

        df["lower_high"] = (
            df["high"] < df["prev_high"]
        )

        # -------------------------
        # Lower Low
        # -------------------------

        df["lower_low"] = (
            df["low"] < df["prev_low"]
        )

        # -------------------------
        # Trend
        # -------------------------

        trend = []

        for _, row in df.iterrows():

            if row["higher_high"] and row["higher_low"]:

                trend.append("UPTREND")

            elif row["lower_high"] and row["lower_low"]:

                trend.append("DOWNTREND")

            else:

                trend.append("SIDEWAYS")

        df["trend"] = trend

        # -------------------------
        # Structure Score
        # -------------------------

        score = []

        for _, row in df.iterrows():

            if row["trend"] == "UPTREND":

                score.append(100)

            elif row["trend"] == "SIDEWAYS":

                score.append(50)

            else:

                score.append(0)

        df["structure_score"] = score

        return df

    def best_trend(self, df, top=20):

        return df.sort_values(
            by="structure_score",
            ascending=False
        ).head(top)
