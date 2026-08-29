import gzip
import json
import requests
import pandas as pd
from pathlib import Path

MASTER_URL = "https://assets.upstox.com/market-quote/instruments/exchange/complete.json.gz"

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)


class InstrumentMaster:

    def __init__(self):
        self.df = None

    def download(self):

        r = requests.get(MASTER_URL, timeout=60)
        r.raise_for_status()

        data = json.loads(gzip.decompress(r.content))

        self.df = pd.DataFrame(data)

        return self.df

    def save_all(self):

        self.df.to_parquet(DATA_DIR / "instrument_master.parquet", index=False)

    def split(self):

        df = self.df.copy()

        stocks = df[
            (df["segment"].str.contains("NSE", na=False)) &
            (df["instrument_type"] == "EQ")
        ]

        futures = df[
            df["instrument_type"] == "FUT"
        ]

        options = df[
            df["instrument_type"].isin(["CE", "PE"])
        ]

        indices = df[
            df["instrument_type"] == "INDEX"
        ]

        stocks.to_parquet(DATA_DIR / "stocks.parquet", index=False)
        futures.to_parquet(DATA_DIR / "futures.parquet", index=False)
        options.to_parquet(DATA_DIR / "options.parquet", index=False)
        indices.to_parquet(DATA_DIR / "indices.parquet", index=False)


if __name__ == "__main__":

    im = InstrumentMaster()

    im.download()

    im.save_all()

    im.split()

    print("Instrument master created.")
