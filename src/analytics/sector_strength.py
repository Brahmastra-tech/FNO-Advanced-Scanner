import pandas as pd


class SectorStrength:
    """
    Sector Strength Engine

    Calculates:
    1. Average Sector Change
    2. Average Sector RS
    3. Advancing Stocks
    4. Declining Stocks
    5. Sector Breadth
    """

    def __init__(self):
        pass

    def calculate(self, df):

        required = [
            "sector",
            "day_change_pct",
            "rs_nifty"
        ]

        for col in required:
            if col not in df.columns:
                raise Exception(f"Missing column: {col}")

        sectors = []

        for sector, data in df.groupby("sector"):

            avg_change = round(
                data["day_change_pct"].mean(), 2
            )

            avg_rs = round(
                data["rs_nifty"].mean(), 2
            )

            advancing = (
                data["day_change_pct"] > 0
            ).sum()

            declining = (
                data["day_change_pct"] < 0
            ).sum()

            total = len(data)

            breadth = round(
                (advancing / total) * 100,
                2
            )

            sectors.append({

                "sector": sector,

                "stocks": total,

                "avg_change": avg_change,

                "avg_rs": avg_rs,

                "advancing": advancing,

                "declining": declining,

                "breadth": breadth

            })

        result = pd.DataFrame(sectors)

        result = result.sort_values(
            by="avg_rs",
            ascending=False
        ).reset_index(drop=True)

        return result

    def sector_dictionary(self, sector_df):

        return dict(
            zip(
                sector_df["sector"],
                sector_df["avg_change"]
            )
        )

    def strongest(self, sector_df, top=5):

        return sector_df.head(top)

    def weakest(self, sector_df, top=5):

        return sector_df.tail(top)
