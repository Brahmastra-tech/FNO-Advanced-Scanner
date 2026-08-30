import pandas as pd


class OpeningEngine:
    """
    Opening Observation Engine

    Runs ONLY between

    09:15

    and

    09:25

    After 09:25

    values remain frozen.
    """

    def __init__(self):

        self.snapshot = None

    # ----------------------------------------------------

    def capture(self, dataframe):

        df = dataframe.copy()

        self.snapshot = df[

            [

                "instrument_key",

                "symbol",

                "open",

                "high",

                "low",

                "close",

                "volume",

                "turnover"

            ]

        ].copy()

        self.snapshot.rename(

            columns={

                "open": "opening_open",

                "high": "opening_high",

                "low": "opening_low",

                "close": "opening_close",

                "volume": "opening_volume",

                "turnover": "opening_turnover"

            },

            inplace=True

        )

        return self.snapshot

    # ----------------------------------------------------

    def merge(self, dataframe):

        if self.snapshot is None:

            return dataframe

        return dataframe.merge(

            self.snapshot,

            on=[

                "instrument_key",

                "symbol"

            ],

            how="left"

        )

    # ----------------------------------------------------

    def is_ready(self):

        return self.snapshot is not None

    # ----------------------------------------------------

    def reset(self):

        self.snapshot = None
