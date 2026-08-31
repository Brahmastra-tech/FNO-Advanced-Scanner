import pandas as pd


class Universe:

    def __init__(self):

        # Upstox instrument master
        all_stocks = pd.read_parquet("data/stocks.parquet")

        # Nifty 500 list
        nifty500 = pd.read_csv("src/data/nifty500.csv")

        # Symbols from CSV
        symbols = (
            nifty500["Symbol"]
            .astype(str)
            .str.strip()
            .str.upper()
        )

        # Keep only Nifty 500 stocks
        self.stocks = all_stocks[
            all_stocks["trading_symbol"]
            .astype(str)
            .str.strip()
            .str.upper()
            .isin(symbols)
        ].reset_index(drop=True)

        self.indices = pd.read_parquet("data/indices.parquet")

    def get_indices(self):

        wanted = [
            "NIFTY 50",
            "NIFTY BANK",
            "NIFTY FIN SERVICE",
            "NIFTY MIDCAP SELECT",
            "SENSEX",
            "BANKEX",
        ]

        return self.indices[
            self.indices["trading_symbol"].isin(wanted)
        ]

    def get_fno_stocks(self):

        return self.stocks
