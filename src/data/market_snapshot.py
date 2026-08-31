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

            if not isinstance(response, dict):
                continue

            if response.get("status") != "success":
                continue

            data_dict = response.get("data", {})

            if not data_dict:
                continue

            # Upstox returns one quote keyed by symbol
            data = next(iter(data_dict.values()), None)

            if data is None:
                continue

            ohlc = data.get("ohlc", {})
            depth = data.get("depth", {})

            volume = data.get("volume")
            ltp = data.get("last_price")

            turnover = None
            if volume is not None and ltp is not None:
                turnover = volume * ltp

            row = {
                "timestamp": datetime.now(),
                "instrument_key": instrument_key,
                "symbol": data.get("symbol"),
                "exchange": data.get("exchange"),
                "ltp": ltp,
                "open": ohlc.get("open"),
                "high": ohlc.get("high"),
                "low": ohlc.get("low"),
                "close": ohlc.get("close"),
                "volume": volume,
                "turnover": turnover,
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
                "ask_qty": None,
            }

            buy = depth.get("buy", [])
            if buy:
                row["bid"] = buy[0].get("price")
                row["bid_qty"] = buy[0].get("quantity")

            sell = depth.get("sell", [])
            if sell:
                row["ask"] = sell[0].get("price")
                row["ask_qty"] = sell[0].get("quantity")

            rows.append(row)

        self.snapshot = pd.DataFrame(rows)

        return self.snapshot
