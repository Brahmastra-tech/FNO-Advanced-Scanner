import pandas as pd


class IndexEngine:
    """
    Index Analysis Engine

    Tracks the major indices and assigns
    an overall strength score.
    """

    INDEX_MAP = {
        "NIFTY": "NIFTY 50",
        "BANKNIFTY": "NIFTY BANK",
        "FINNIFTY": "NIFTY FINANCIAL SERVICES",
        "MIDCPNIFTY": "NIFTY MIDCAP SELECT",
        "SENSEX": "SENSEX"
    }

    def __init__(self):
        pass

    # -----------------------------------------------------

    def calculate_strength(self, row):

        score = 0

        day_change = row.get("day_change", 0)

        if day_change > 1:
            score += 35
        elif day_change > 0.5:
            score += 25
        elif day_change > 0:
            score += 15

        rvol = row.get("rvol", 1)

        if rvol > 2:
            score += 20
        elif rvol > 1.5:
            score += 15
        elif rvol > 1:
            score += 10

        rs = row.get("relative_strength_score", 50)
        score += min(rs * 0.30, 30)

        breadth = row.get("breadth_score", 50)
        score += min(breadth * 0.15, 15)

        return round(min(score, 100), 2)

    # -----------------------------------------------------

    def process(self, dataframe):

        df = dataframe.copy()

        df["index_strength"] = df.apply(

            self.calculate_strength,

            axis=1

        )

        return df

    # -----------------------------------------------------

    def strongest(self, dataframe):

        df = self.process(dataframe)

        return df.sort_values(

            "index_strength",

            ascending=False

        )

    # -----------------------------------------------------

    def summary(self, dataframe):

        df = self.process(dataframe)

        summary = {}

        for _, row in df.iterrows():

            summary[row["symbol"]] = {

                "strength": row["index_strength"],

                "day_change": row.get("day_change", 0)

            }

        return summary
