import pandas as pd


class OpportunityEngine:
    """
    Opportunity Detection Engine

    Combines all analytics engines into
    one Opportunity Score.
    """

    def __init__(self):

        self.weights = {

            "rs": 20,

            "volume": 20,

            "sector": 15,

            "compression": 15,

            "structure": 15,

            "market": 15

        }

    def calculate(self, df, market_status="NEUTRAL"):

        market = df.copy()

        # -----------------------------
        # Default Missing Values
        # -----------------------------

        defaults = {

            "rs_score": 0,

            "rvol": 1,

            "sector_strength": 0,

            "compression_score": 0,

            "structure_score": 0

        }

        for col, value in defaults.items():

            if col not in market.columns:

                market[col] = value

            market[col] = market[col].fillna(value)

        # -----------------------------
        # Relative Strength
        # -----------------------------

        market["rs_points"] = (

            market["rs_score"]

            .clip(-5, 5)

            + 5

        ) * 2

        # 0–20

        # -----------------------------
        # Volume
        # -----------------------------

        market["volume_points"] = (

            market["rvol"]

            .clip(0, 2)

            / 2

        ) * 20

        # -----------------------------
        # Sector
        # -----------------------------

        market["sector_points"] = (

            market["sector_strength"]

            .clip(-5, 5)

            + 5

        ) * 1.5

        # -----------------------------
        # Compression
        # -----------------------------

        market["compression_points"] = (

            market["compression_score"]

            / 100

        ) * 15

        # -----------------------------
        # Structure
        # -----------------------------

        market["structure_points"] = (

            market["structure_score"]

            / 100

        ) * 15

        # -----------------------------
        # Market Context
        # -----------------------------

        if market_status == "VERY BULLISH":

            market_points = 15

        elif market_status == "BULLISH":

            market_points = 12

        elif market_status == "NEUTRAL":

            market_points = 8

        elif market_status == "BEARISH":

            market_points = 4

        else:

            market_points = 0

        market["market_points"] = market_points

        # -----------------------------
        # Total Score
        # -----------------------------

        market["total_score"] = (

            market["rs_points"]

            +

            market["volume_points"]

            +

            market["sector_points"]

            +

            market["compression_points"]

            +

            market["structure_points"]

            +

            market["market_points"]

        ).round(2)

        # -----------------------------
        # Confidence
        # -----------------------------

        market["confidence"] = (

            market["total_score"]

        ).clip(0, 100)

        # -----------------------------
        # Stage
        # -----------------------------

        stage = []

        for _, row in market.iterrows():

            score = row["total_score"]

            if score >= 90:

                stage.append("BREAKOUT")

            elif score >= 80:

                stage.append("READY")

            elif score >= 65:

                stage.append("WATCH")

            else:

                stage.append("IGNORE")

        market["stage"] = stage

        return market

    def opportunities(self, df):

        return (

            df

            [

                df["stage"] != "IGNORE"

            ]

            .sort_values(

                by="total_score",

                ascending=False

            )

        )
