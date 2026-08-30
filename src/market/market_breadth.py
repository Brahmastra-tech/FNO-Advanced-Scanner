import pandas as pd


class MarketBreadth:
    """
    Market Breadth Engine

    Produces a market health score
    used by the scanner.
    """

    def __init__(self):
        pass

    # ----------------------------------------------------

    def advance_decline(self, dataframe):

        advances = len(
            dataframe[dataframe["day_change"] > 0]
        )

        declines = len(
            dataframe[dataframe["day_change"] < 0]
        )

        return {

            "advances": advances,

            "declines": declines,

            "ratio": round(
                advances / max(declines, 1),
                2
            )

        }

    # ----------------------------------------------------

    def bullish_percentage(self, dataframe):

        bullish = len(

            dataframe[
                dataframe["day_change"] > 0
            ]

        )

        return round(

            bullish /

            len(dataframe) *

            100,

            2

        )

    # ----------------------------------------------------

    def market_score(self, dataframe):

        pct = self.bullish_percentage(

            dataframe

        )

        if pct >= 75:
            return 100

        if pct >= 60:
            return 80

        if pct >= 50:
            return 60

        if pct >= 40:
            return 40

        return 20

    # ----------------------------------------------------

    def trend(self, dataframe):

        score = self.market_score(dataframe)

        if score >= 80:
            return "BULLISH"

        if score >= 60:
            return "POSITIVE"

        if score >= 40:
            return "NEUTRAL"

        return "BEARISH"

    # ----------------------------------------------------

    def analyze(self, dataframe):

        return {

            "breadth": self.advance_decline(dataframe),

            "market_score": self.market_score(dataframe),

            "trend": self.trend(dataframe)

        }
