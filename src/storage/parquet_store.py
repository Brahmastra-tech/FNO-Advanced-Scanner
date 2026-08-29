from pathlib import Path
import pandas as pd


class ParquetStore:

    def __init__(self):

        self.base = Path("data/intraday")

        self.base.mkdir(parents=True, exist_ok=True)

    def save(self, symbol, df):

        file = self.base / f"{symbol}.parquet"

        df.to_parquet(file, index=False)
