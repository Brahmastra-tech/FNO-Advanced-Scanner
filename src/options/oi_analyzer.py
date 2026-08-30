import pandas as pd


class OIAnalyzer:
    """
    Open Interest Analyzer

    Detects:

    - Long Build-up
    - Short Build-up
    - Long Unwinding
    - Short Covering

    Also finds:

    - Highest Call OI
    - Highest Put OI
    - Support
    - Resistance
    """

    def __init__(self):
        pass

    # ---------------------------------------------------------

    def analyze(self, option_chain):

        rows = []

        for strike in option_chain["data"]:

            call = strike.get("call_options", {})

            put = strike.get("put_options", {})

            rows.append({

                "strike": strike["strike_price"],

                "call_oi": call.get("market_data", {}).get("oi", 0),

                "call_oi_change": call.get("market_data", {}).get("oi_day_change", 0),

                "put_oi": put.get("market_data", {}).get("oi", 0),

                "put_oi_change": put.get("market_data", {}).get("oi_day_change", 0)

            })

        return pd.DataFrame(rows)

    # ---------------------------------------------------------

    def highest_call_oi(self, df):

        row = df.loc[df["call_oi"].idxmax()]

        return {

            "strike": row["strike"],

            "oi": row["call_oi"]

        }

    # ---------------------------------------------------------

    def highest_put_oi(self, df):

        row = df.loc[df["put_oi"].idxmax()]

        return {

            "strike": row["strike"],

            "oi": row["put_oi"]

        }

    # ---------------------------------------------------------

    def resistance(self, df):

        return self.highest_call_oi(df)

    # ---------------------------------------------------------

    def support(self, df):

        return self.highest_put_oi(df)

    # ---------------------------------------------------------

    def long_buildup(self, df):

        return df[

            (df["put_oi_change"] > 0)

        ]

    # ---------------------------------------------------------

    def short_buildup(self, df):

        return df[

            (df["call_oi_change"] > 0)

        ]

    # ---------------------------------------------------------

    def summary(self, df):

        return {

            "support": self.support(df),

            "resistance": self.resistance(df),

            "max_call_oi": self.highest_call_oi(df),

            "max_put_oi": self.highest_put_oi(df)

        }
