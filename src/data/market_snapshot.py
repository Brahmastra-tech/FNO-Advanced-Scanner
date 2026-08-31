from datetime import datetime
import pandas as pd


class MarketSnapshot:
    """
    Converts raw Upstox quote responses into
    a clean dataframe used throughout the system.
    """

    def __init__(self):
        self.snapshot = pd.DataFrame()

    def build(self, quotes: dict) -> pd.DataFrame:

        rows = []

        for instrument_key, response in quotes.items():

            # Skip empty responses
            if not response or not isinstance(response, dict):
                continue

            # Skip failed API responses
            if response.get("status") != "success":
                print(f"Skipping {instrument_key}: {response}")
                continue

            # Extract quote payload
            data_dict = response.get("data", {})

            if not data_dict:
                continue

            # Upstox returns one quote inside the data dictionary
            data = next(iter(data_dict.values()))

            if not isinstance(data, dict):
                continue

            ohlc = data.get("ohlc", {})
            depth = data.get("depth", {})

            row = {
                "timestamp": datetime.now(),

                "instrument_key": instrument_key,

                "symbol": data.get("symbol"),

                "exchange": data.get("exchange"),

                "ltp": data.get("last_price"),

                "open": ohlc.get("open"),

                "high": ohlc.get("high"),

                "low": ohlc.get("low"),

                "close": ohlc.get("close"),

                "volume": data.get("volume"),

                "turnover": data.get("turnover"),

                "oi": data.get("oi"),

                "prev_oi": data.get("prev_oi"),

                "avg_price": data.get("average_price"),

                "last_trade_time": data.get("last_trade_time"),

                "total_buy_qty": data.get("total_buy_quantity"),

                "total_sell_qty": data.get("total_sell_quantity"),

                "upper_circuit": data.get("upper_circuit_limit"),

                "lower_circuit": data.get("lower_circuit_limit"),

                "bid": None,

                "bid_qty": None,

                "ask": None,

                "ask_qty": None
            }

            # Best Bid
            buy = depth.get("buy", [])
            if buy:
                row["bid"] = buy[0].get("price")
                row["bid_qty"] = buy[0].get("quantity")

            # Best Ask
            sell = depth.get("sell", [])
            if sell:
                row["ask"] = sell[0].get("price")
                row["ask_qty"] = sell[0].get("quantity")

            rows.append(row)

        self.snapshot = pd.DataFrame(rows)

        return self.snapshot
