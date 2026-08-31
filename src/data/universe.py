import pandas as pd


class Universe:

    def __init__(self):

        self.stocks = pd.read_parquet("data/stocks.parquet")
        self.indices = pd.read_parquet("data/indices.parquet")

        # Load NIFTY 500 list
        nifty500 = pd.read_csv("data/nifty500.csv")

        # Convert symbols to uppercase and remove spaces
        nifty500["Symbol"] = (
            nifty500["Symbol"]
            .astype(str)
            .str.upper()
            .str.strip()
        )

        self.nifty500_symbols = set(nifty500["Symbol"])

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

        stocks = self.stocks.copy()

        stocks["trading_symbol"] = (
            stocks["trading_symbol"]
            .astype(str)
            .str.upper()
            .str.strip()
        )

        stocks = stocks[
            stocks["trading_symbol"].isin(self.nifty500_symbols)
        ]

        print(f"NIFTY 500 Universe Loaded: {len(stocks)} stocks")

        return stocks
