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

        prev = previous_df[
            [
                "instrument_key",
                "volume",
                "turnover",
                "close"
            ]
        ].copy()

        prev.columns = [
            "instrument_key",
            "prev_volume",
            "prev_turnover",
            "prev_close"
        ]

        df = df.merge(
            prev,
            on="instrument_key",
            how="left"
        )

        # -----------------------------------
        # Price Change %
        # -----------------------------------

        df["price_change_pct"] = (
            (
                df["close"] -
                df["prev_close"]
            )
            /
            df["prev_close"]
            * 100
        ).fillna(0)

        # -----------------------------------
        # Volume Acceleration
        # -----------------------------------

        df["volume_acceleration"] = (

            df["volume"]

            -

            df["prev_volume"]

        ).fillna(0)

        # -----------------------------------
        # Turnover Acceleration
        # -----------------------------------

        df["turnover_acceleration"] = (

            df["turnover"]

            -

            df["prev_turnover"]

        ).fillna(0)

        # -----------------------------------
        # Average Trade Value
        # -----------------------------------

        df["average_trade_value"] = (

            df["turnover"]

            /

            df["volume"].replace(0, np.nan)

        ).fillna(0)

        # -----------------------------------
        # Participation Score
        # -----------------------------------

        df["participation_score"] = (

            (
                df["volume_acceleration"]

                /

                df["volume"].replace(0, np.nan)

            )

            * 100

        ).fillna(0)

        # -----------------------------------
        # Accumulation
        # High turnover
        # Low price movement
        # -----------------------------------

        accumulation = []

        distribution = []

        smart_score = []

        for _, row in df.iterrows():

            score = 0

            # Volume participation

            if row["volume_acceleration"] > 0:

                score += 20

            # Turnover participation

            if row["turnover_acceleration"] > 0:

                score += 20

            # Small move = hidden buying

            if abs(row["price_change_pct"]) < 1:

                score += 20

            # Healthy participation

            if row["participation_score"] > 15:

                score += 20

            # Expensive trades

            if row["average_trade_value"] > 5000:

                score += 20

            score = min(score, 100)

            smart_score.append(score)

            if score >= 70:

                accumulation.append("YES")

            else:

                accumulation.append("NO")

            if (

                row["turnover_acceleration"] > 0

                and

                row["price_change_pct"] < -0.5

            ):

                distribution.append("YES")

            else:

                distribution.append("NO")

        df["accumulation"] = accumulation

        df["distribution"] = distribution

        df["smart_money_score"] = smart_score

        return df

    def top_accumulation(self, df, n=20):

        return (

            df

            .sort_values(

                by="smart_money_score",

                ascending=False

            )

            .head(n)

        )

    def institutional_buying(self, df):

        return df[

            df["accumulation"] == "YES"

        ]

    def institutional_selling(self, df):

        return df[

            df["distribution"] == "YES"

        ]
