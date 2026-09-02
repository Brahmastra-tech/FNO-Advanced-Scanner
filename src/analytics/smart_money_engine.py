import pandas as pd
import numpy as np


class SmartMoneyEngine:
    """
    Smart Money Analytics

    Detects institutional participation using
    price, volume and turnover behaviour.
    """

    def __init__(self):
        pass

    def calculate(self, current_df, previous_df):

        df = current_df.copy()

        # -----------------------------------
        # Remove existing previous columns
        # -----------------------------------

        for col in [
            "prev_volume",
            "prev_turnover",
            "prev_close",
        ]:
            if col in df.columns:
                df.drop(columns=col, inplace=True)

        # -----------------------------------
        # First Scan
        # -----------------------------------

        if previous_df is None or previous_df.empty:

            df["prev_volume"] = df["volume"]
            df["prev_turnover"] = df["turnover"]
            df["prev_close"] = df["close"]

        else:

            prev = previous_df[
                [
                    "instrument_key",
                    "volume",
                    "turnover",
                    "close",
                ]
            ].copy()

            prev.columns = [
                "instrument_key",
                "prev_volume",
                "prev_turnover",
                "prev_close",
            ]

            df = df.merge(
                prev,
                on="instrument_key",
                how="left",
            )

            df["prev_volume"] = df["prev_volume"].fillna(df["volume"])
            df["prev_turnover"] = df["prev_turnover"].fillna(df["turnover"])
            df["prev_close"] = df["prev_close"].fillna(df["close"])

        # -----------------------------------
        # Price Change %
        # -----------------------------------

        df["price_change_pct"] = (
            (
                df["close"] - df["prev_close"]
            )
            / df["prev_close"].replace(0, np.nan)
            * 100
        ).fillna(0)

        # -----------------------------------
        # Volume Acceleration
        # -----------------------------------

        df["volume_acceleration"] = (
            df["volume"] - df["prev_volume"]
        ).fillna(0)

        # -----------------------------------
        # Turnover Acceleration
        # -----------------------------------

        df["turnover_acceleration"] = (
            df["turnover"] - df["prev_turnover"]
        ).fillna(0)

        # -----------------------------------
        # Average Trade Value
        # -----------------------------------

        df["average_trade_value"] = (
            df["turnover"]
            / df["volume"].replace(0, np.nan)
        ).fillna(0)

        # -----------------------------------
        # Participation Score
        # -----------------------------------

        df["participation_score"] = (
            (
                df["volume_acceleration"]
                / df["volume"].replace(0, np.nan)
            )
            * 100
        ).fillna(0)

        # -----------------------------------
        # Smart Money Score
        # -----------------------------------

        smart_score = []
        accumulation = []
        distribution = []

        for _, row in df.iterrows():

            score = 0

            if row["volume_acceleration"] > 0:
                score += 20

            if row["turnover_acceleration"] > 0:
                score += 20

            if abs(row["price_change_pct"]) < 1:
                score += 20

            if row["participation_score"] > 15:
                score += 20

            if row["average_trade_value"] > 5000:
                score += 20

            score = min(score, 100)

            smart_score.append(score)

            accumulation.append(
                "YES" if score >= 70 else "NO"
            )

            distribution.append(
                "YES"
                if (
                    row["turnover_acceleration"] > 0
                    and row["price_change_pct"] < -0.5
                )
                else "NO"
            )

        df["smart_money_score"] = smart_score
        df["accumulation"] = accumulation
        df["distribution"] = distribution

        return df

    def top_accumulation(self, df, n=20):
        return df.sort_values(
            "smart_money_score",
            ascending=False,
        ).head(n)

    def institutional_buying(self, df):
        return df[df["accumulation"] == "YES"]

    def institutional_selling(self, df):
        return df[df["distribution"] == "YES"]
