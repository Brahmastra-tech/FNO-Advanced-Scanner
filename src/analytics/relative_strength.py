import pandas as pd


class RelativeStrength:

    """
    Calculates Relative Strength against
    Nifty and Sector.
    """

    def __init__(self):
        pass

    def calculate(
        self,
        stock_df: pd.DataFrame,
        nifty_change: float,
        sector_changes: dict
    ):

        df = stock_df.copy()

        # ---------- RS vs Nifty ----------

        df["rs_nifty"] = df["day_change_pct"] - nifty_change

        # ---------- RS vs Sector ----------

        rs_sector = []

        for _, row in df.iterrows():

            sector = row["sector"]

            sector_change = sector_changes.get(sector, 0)

            rs_sector.append(
                row["day_change_pct"] - sector_change
            )

        df["rs_sector"] = rs_sector

        # ---------- Relative Strength Score ----------

        df["rs_score"] = (

            (df["rs_nifty"] * 0.60)

            +

            (df["rs_sector"] * 0.40)

        )

        return df
