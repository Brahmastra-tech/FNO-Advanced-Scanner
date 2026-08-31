import pandas as pd


class Universe:

    def __init__(self):

        self.stocks = pd.read_csv("src/data/nifty500.csv")
        self.indices = pd.read_parquet("src/data/indices.parquet")

    def get_indices(self):

        wanted = [
            "NIFTY 50",
            "NIFTY BANK",
            "NIFTY FIN SERVICE",
            "NIFTY MIDCAP SELECT",
            "SENSEX",
            "BANKEX"
        ]

        return self.indices[
            self.indices["trading_symbol"].isin(wanted)
        ]

    def get_fno_stocks(self):

        return self.stocks
