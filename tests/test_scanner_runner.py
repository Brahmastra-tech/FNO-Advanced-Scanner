import pandas as pd

from core.scanner_runner import ScannerRunner


def fetch():

    return pd.DataFrame({

        "instrument_key":["1","2"],

        "symbol":["SBIN","RELIANCE"],

        "sector":["BANK","ENERGY"],

        "open":[800,2900],

        "high":[805,2930],

        "low":[798,2890],

        "close":[804,2925],

        "volume":[180000,420000],

        "turnover":[145000000,1800000000]

    })


runner = ScannerRunner()

runner.loop(

    fetch_function=fetch,

    interval=5,

    market_status="BULLISH"

)
