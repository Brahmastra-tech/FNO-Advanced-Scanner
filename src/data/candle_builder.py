from collections import defaultdict
import pandas as pd


class CandleBuilder:

    def __init__(self):

        self.current = {}

        self.completed = defaultdict(list)

    def update(self, snapshot_df):

        if snapshot_df.empty:

            return

        for row in snapshot_df.to_dict("records"):

            key = row["instrument_key"]

            minute = row["timestamp"].strftime("%Y-%m-%d %H:%M")

            if key not in self.current:

                self.current[key] = {

                    "minute": minute,

                    "instrument_key": key,

                    "symbol": row["symbol"],

                    "open": row["ltp"],

                    "high": row["ltp"],

                    "low": row["ltp"],

                    "close": row["ltp"],

                    "volume": row["volume"],

                    "turnover": row["turnover"]

                }

                continue

            candle = self.current[key]

            if candle["minute"] != minute:

                self.completed[key].append(candle)

                self.current[key] = {

                    "minute": minute,

                    "instrument_key": key,

                    "symbol": row["symbol"],

                    "open": row["ltp"],

                    "high": row["ltp"],

                    "low": row["ltp"],

                    "close": row["ltp"],

                    "volume": row["volume"],

                    "turnover": row["turnover"]

                }

                continue

            candle["high"] = max(candle["high"], row["ltp"])

            candle["low"] = min(candle["low"], row["ltp"])

            candle["close"] = row["ltp"]

            candle["volume"] = row["volume"]

            candle["turnover"] = row["turnover"]

    def get_latest(self, instrument_key):

        return self.current.get(instrument_key)

    def get_completed(self, instrument_key):

        return pd.DataFrame(self.completed[instrument_key])

    def latest_dataframe(self):

        return pd.DataFrame(self.current.values())
