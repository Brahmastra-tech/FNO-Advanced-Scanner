import pandas as pd


class Universe:

    def __init__(self):

        # Load Upstox instrument master
        all_stocks = pd.read_parquet("data/stocks.parquet")

        # Load Nifty 500 constituents
        nifty500 = pd.read_csv("data/nifty500.csv")

        # Normalize symbols from Nifty 500
        symbols = (
            nifty500["Symbol"]
            .astype(str)
            .str.strip()
            .str.upper()
        )

        # Normalize trading symbols in instrument master
        all_stocks["trading_symbol"] = (
            all_stocks["trading_symbol"]
            .astype(str)
            .str.strip()
            .str.upper()
        )

        # Keep only NSE equity instruments in the Nifty 500
        self.stocks = (
            all_stocks[
                (all_stocks["exchange"] == "NSE_EQ")
                & (all_stocks["trading_symbol"].isin(symbols))
            ]
            .drop_duplicates(subset="instrument_key")
            .reset_index(drop=True)
        )

        # Load indices
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
        ].reset_index(drop=True)

    def get_fno_stocks(self):

        return self.stocks
