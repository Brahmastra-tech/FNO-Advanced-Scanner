import pandas as pd


class MarketBreadth:
    """
    Market Breadth Engine

    Calculates:
    1. Advances
    2. Declines
    3. Unchanged
    4. Advance/Decline Ratio
    5. Positive %
    6. Negative %
    """

    def __init__(self):
        pass

    def calculate(self, df):

        total = len(df)

        advancing = (df["day_change_pct"] > 0).sum()

        declining = (df["day_change_pct"] < 0).sum()

        unchanged = (df["day_change_pct"] == 0).sum()

        ad_ratio = round(

            advancing / declining,

            2

        ) if declining != 0 else 999

        positive = round(

            (advancing / total) * 100,

            2

        )

        negative = round(

            (declining / total) * 100,

            2

        )

        return {

            "total": total,

            "advancing": advancing,

            "declining": declining,

            "unchanged": unchanged,

            "ad_ratio": ad_ratio,

            "positive_percent": positive,

            "negative_percent": negative

        }

    def market_status(self, breadth):

        ratio = breadth["ad_ratio"]

        if ratio >= 2:

            return "VERY BULLISH"

        elif ratio >= 1.3:

            return "BULLISH"

        elif ratio >= 0.8:

            return "NEUTRAL"

        elif ratio >= 0.5:

            return "BEARISH"

        else:

            return "VERY BEARISH"
