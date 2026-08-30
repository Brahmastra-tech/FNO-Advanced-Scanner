import pandas as pd


class IndexEngine:
    """
    Index Analytics Engine

    Tracks major indices and calculates:

    - LTP
    - Day Change %
    - Opening Gap %
    - Opening Range
    - Trend
    """

    def __init__(self):

        self.index_snapshot = pd.DataFrame()

    def calculate(self, df):

        if df.empty:
            return pd.DataFrame()

        required = [
            "symbol",
            "ltp",
            "open",
            "high",
            "low",
            "day_change_pct"
        ]

        for col in required:
            if col not in df.columns:
                raise Exception(f"Missing column : {col}")

        result = df.copy()

        # -------------------------
        # Opening Gap %
        # -------------------------

        result["opening_gap_pct"] = (
            (result["open"] - result["ltp"] + result["day_change_pct"])
        ).round(2)

        # -------------------------
        # Opening Range
        # -------------------------

        result["opening_range"] = (
            result["high"] - result["low"]
        ).round(2)

        # -------------------------
        # Trend
        # -------------------------

        trend = []

        for _, row in result.iterrows():

            if row["ltp"] > row["open"]:

                trend.append("UP")

            elif row["ltp"] < row["open"]:

                trend.append("DOWN")

            else:

                trend.append("SIDEWAYS")

        result["trend"] = trend

        self.index_snapshot = result

        return result

    def strongest(self):

        if self.index_snapshot.empty:
            return None

        return self.index_snapshot.sort_values(
            by="day_change_pct",
            ascending=False
        )

    def weakest(self):

        if self.index_snapshot.empty:
            return None

        return self.index_snapshot.sort_values(
            by="day_change_pct"
        )

    def market_direction(self):

        if self.index_snapshot.empty:
            return "UNKNOWN"

        avg = self.index_snapshot["day_change_pct"].mean()

        if avg >= 1:
            return "STRONG BULLISH"

        elif avg >= 0.30:
            return "BULLISH"

        elif avg <= -1:
            return "STRONG BEARISH"

        elif avg <= -0.30:
            return "BEARISH"

        else:
            return "SIDEWAYS"
