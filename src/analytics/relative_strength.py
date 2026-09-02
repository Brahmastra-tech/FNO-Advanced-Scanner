import pandas as pd


class RelativeStrength:
    """
    Relative Strength Engine

    Calculates

    • RS vs Nifty
    • RS vs Sector
    • Raw RS Score
    • Relative Strength Score (0-100)
    • RS Rank
    """

    def __init__(self):
        pass

    # ==========================================================
    # Main Calculation
    # ==========================================================

    def calculate(self, df, nifty_change=0.0, sector_strength=None):

        if sector_strength is None:
            sector_strength = {}

        market = df.copy()

        required = [
            "instrument_key",
            "symbol",
            "sector",
            "day_change_pct"
        ]

        for col in required:

            if col not in market.columns:
                raise Exception(f"Missing column : {col}")

        # ------------------------------------------------------
        # Ensure numeric
        # ------------------------------------------------------

        market["day_change_pct"] = pd.to_numeric(
            market["day_change_pct"],
            errors="coerce"
        ).fillna(0)

        # ------------------------------------------------------
        # RS vs Nifty
        # ------------------------------------------------------

        market["rs_nifty"] = (
            market["day_change_pct"] - nifty_change
        ).round(2)

        # ------------------------------------------------------
        # RS vs Sector
        # ------------------------------------------------------

        market["sector_strength"] = (
            market["sector"]
            .map(sector_strength)
            .fillna(0)
        )

        market["rs_sector"] = (
            market["day_change_pct"]
            - market["sector_strength"]
        ).round(2)

        # ------------------------------------------------------
        # Raw RS Score
        # ------------------------------------------------------

        market["rs_score"] = (
            market["rs_nifty"] * 0.60
            +
            market["rs_sector"] * 0.40
        ).round(2)

        # ------------------------------------------------------
        # Normalize Score (0-100)
        # ------------------------------------------------------

        minimum = market["rs_score"].min()
        maximum = market["rs_score"].max()

        if minimum == maximum:

            market["relative_strength_score"] = 50.0

        else:

            market["relative_strength_score"] = (
                (
                    market["rs_score"] - minimum
                )
                /
                (
                    maximum - minimum
                )
                * 100
            ).round(2)

        # ------------------------------------------------------
        # Rank
        # ------------------------------------------------------

        market["rs_rank"] = (
            market["relative_strength_score"]
            .rank(
                ascending=False,
                method="dense"
            )
            .astype(int)
        )

        return market

    # ==========================================================
    # Reports
    # ==========================================================

    def top(self, df, count=10):

        return (
            df
            .sort_values(
                by="relative_strength_score",
                ascending=False
            )
            .head(count)
        )

    def bottom(self, df, count=10):

        return (
            df
            .sort_values(
                by="relative_strength_score",
                ascending=True
            )
            .head(count)
        )
