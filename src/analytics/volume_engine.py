import pandas as pd


class VolumeEngine:
    """
    Volume Analytics Engine

    Calculates:
    1. Relative Volume (RVOL)
    2. Volume Acceleration
    3. Turnover Acceleration
    """

    def __init__(self):
        pass

    def calculate(self, current_df, previous_df):

        df = current_df.copy()

        # -----------------------------
        # Merge Previous Snapshot
        # -----------------------------

        prev = previous_df[
            [
                "instrument_key",
                "volume",
                "turnover"
            ]
        ].copy()

        prev.columns = [
            "instrument_key",
            "prev_volume",
            "prev_turnover"
        ]

        df = df.merge(
            prev,
            on="instrument_key",
            how="left"
        )

        # -----------------------------
        # Volume Acceleration
        # -----------------------------

        df["volume_acceleration"] = (

            df["volume"]

            -

            df["prev_volume"]

        )

        # -----------------------------
        # Turnover Acceleration
        # -----------------------------

        df["turnover_acceleration"] = (

            df["turnover"]

            -

            df["prev_turnover"]

        )

        # -----------------------------
        # Relative Volume (Temporary)
        # -----------------------------
        # Later we'll compare against
        # 20-day average intraday volume.

        df["rvol"] = (

            df["volume"]

            /

            df["prev_volume"]

        ).fillna(1).round(2)

        return df

    def top_volume(self, df, n=10):

        return df.sort_values(
            by="volume_acceleration",
            ascending=False
        ).head(n)

    def top_turnover(self, df, n=10):

        return df.sort_values(
            by="turnover_acceleration",
            ascending=False
        ).head(n)

    def top_rvol(self, df, n=10):

        return df.sort_values(
            by="rvol",
            ascending=False
        ).head(n)
