import pandas as pd

from core.scheduler import Scheduler


def fetch():

    return pd.DataFrame({

        "instrument_key": ["1"],

        "symbol": ["SBIN"],

        "sector": ["BANK"],

        "open": [800],

        "high": [805],

        "low": [798],

        "close": [804],

        "volume": [180000],

        "turnover": [145000000]

    })


scheduler = Scheduler(fetch)

scheduler.start(interval=5)
