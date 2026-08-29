from collections import defaultdict
from datetime import datetime
import pandas as pd


class CandleBuilder:

    def __init__(self):

        self.current = {}
        self.completed = defaultdict(list)

    def update(self, snapshot_df):

        if snapshot_df.empty:
            return

        now = datetime.now()

        minute_key = now.strftime("%Y-%m-%d %H:%M")

        for row in snapshot_df.to_dict("records"):

            key = row["instrument_key"]

            if key not in self.current:

                self.current[key] = {
                    "minute": minute_key,
                    "instrument_key": key,
                    "symbol": row["symbol"],
                    "open": row["ltp"],
                    "high": row["ltp"],
                    "low": row["ltp"],
                    "close": row["ltp"],
                    "volume": row["volume"] or 0,
                    "turnover": row["turnover"] or 0
                }

                continue

            candle = self.current[key]

            if candle["minute"] != minute_key:

                self.completed[key].append(candle)

                self.current[key] = {
                    "minute": minute_key,
                    "instrument_key": key,
                    "symbol": row["symbol"],
                    "open": row["ltp"],
                    "high": row["ltp"],
                    "low": row["ltp"],
                    "close": row["ltp"],
                    "volume": row["volume"] or 0,
                    "turnover": row["turnover"] or 0
                }

                continue

            candle["high"] = max(candle["high"], row["ltp"])

            candle["low"] = min(candle["low"], row["ltp"])

            candle["close"] = row["ltp"]

            candle["volume"] = row["volume"] or candle["volume"]

            candle["turnover"] = row["turnover"] or candle["turnover"]
    def get_1m(self, instrument_key):

        return pd.DataFrame(self.completed[instrument_key])


    def latest(self, instrument_key):

        return self.current.get(instrument_key)


    def latest_all(self):

        rows = []

        for candle in self.current.values():

            rows.append(candle)

        return pd.DataFrame(rows)
