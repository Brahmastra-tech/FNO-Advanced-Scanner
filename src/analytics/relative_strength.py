import pandas as pd


class RelativeStrength:
    """
    Relative Strength Engine

    Calculates:

    1. RS vs Nifty
    2. RS vs Sector
    3. Relative Strength Score
    """

    def __init__(self):
        pass

    def calculate(self, df, nifty_change=0.0, sector_strength=None):

        if sector_strength is None:
            sector_strength = {}

        market = df.copy()

        # -----------------------------
        # Check Required Columns
        # -----------------------------

        required = [
            "instrument_key",
            "symbol",
            "sector",
            "day_change_pct"
        ]

        for col in required:

            if col not in market.columns:

                raise Exception(f"Missing column : {col}")

        # -----------------------------
        # RS vs Nifty
        # -----------------------------

        market["rs_nifty"] = (

            market["day_change_pct"]

            -

            nifty_change

        )

        # -----------------------------
        # RS vs Sector
        # -----------------------------

        rs_sector = []

        for _, row in market.iterrows():

            sector = row["sector"]

            sector_move = sector_strength.get(sector, 0)

            rs_sector.append(

                row["day_change_pct"]

                -

                sector_move

            )

        market["rs_sector"] = rs_sector

        # -----------------------------
        # Normalized Score
        # -----------------------------

        market["rs_score"] = (

            market["rs_nifty"] * 0.60

            +

            market["rs_sector"] * 0.40

        )

        # -----------------------------
        # Rank
        # -----------------------------

        market["rs_rank"] = (

            market["rs_score"]

            .rank(ascending=False, method="dense")

        )

        return market

    def top(self, df, count=10):

        return (

            df

            .sort_values(

                by="rs_score",

                ascending=False

            )

            .head(count)

        )

    def bottom(self, df, count=10):

        return (

            df

            .sort_values(

                by="rs_score"

            )

            .head(count)

        )
