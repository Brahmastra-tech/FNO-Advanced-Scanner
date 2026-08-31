from datetime import datetime
import pandas as pd


class MarketSnapshot:

    def __init__(self):
        self.snapshot = pd.DataFrame()

    def build(self, quotes):

        rows = []

        print("TOTAL QUOTES:", len(quotes))

        for instrument_key, response in quotes.items():

            print("\n====================")
            print("KEY:", instrument_key)
            print("TYPE:", type(response))
            print("STATUS:", response.get("status"))

            if not response:
                print("FAILED -> response empty")
                continue

            if response.get("status") != "success":
                print("FAILED -> status")
                continue

            data_dict = response.get("data", {})

            print("DATA_DICT TYPE:", type(data_dict))
            print("DATA_DICT LENGTH:", len(data_dict))

            if not data_dict:
                print("FAILED -> empty data")
                continue

            data = next(iter(data_dict.values()))

            print("SYMBOL:", data.get("symbol"))

            row = {
                "timestamp": datetime.now(),
                "instrument_key": instrument_key,
                "symbol": data.get("symbol"),
                "ltp": data.get("last_price"),
            }

            rows.append(row)

            print("ROW ADDED")

            # Only inspect the first successful record
            break

        print("\nTOTAL ROWS BUILT:", len(rows))

        self.snapshot = pd.DataFrame(rows)

        return self.snapshot
