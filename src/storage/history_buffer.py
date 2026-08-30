from collections import defaultdict, deque
import pandas as pd


class HistoryBuffer:

    def __init__(self):

        self.one_minute = defaultdict(lambda: deque(maxlen=500))

        self.five_minute = defaultdict(lambda: deque(maxlen=200))

        self.fifteen_minute = defaultdict(lambda: deque(maxlen=100))

        self.daily = defaultdict(lambda: deque(maxlen=30))

    def add_1m(self, instrument_key, candle):

        self.one_minute[instrument_key].append(candle)

    def add_5m(self, instrument_key, candle):

        self.five_minute[instrument_key].append(candle)

    def add_15m(self, instrument_key, candle):

        self.fifteen_minute[instrument_key].append(candle)

    def add_daily(self, instrument_key, candle):

        self.daily[instrument_key].append(candle)

    def get_1m(self, instrument_key):

        return pd.DataFrame(self.one_minute[instrument_key])

    def get_5m(self, instrument_key):

        return pd.DataFrame(self.five_minute[instrument_key])

    def get_15m(self, instrument_key):

        return pd.DataFrame(self.fifteen_minute[instrument_key])

    def get_daily(self, instrument_key):

        return pd.DataFrame(self.daily[instrument_key])
