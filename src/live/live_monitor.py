from pipeline.pipeline import MarketPipeline
from engine.trading_engine import TradingEngine
from sheets.google_sheet import GoogleSheet
from alerts.telegram import TelegramNotifier

import pandas as pd
import time


class LiveMonitor:

    def __init__(self):

        self.pipeline = MarketPipeline()

        self.sheet = GoogleSheet(
            credentials_file="credentials.json",
            spreadsheet_name="Opportunity Scanner"
        )

        self.telegram = TelegramNotifier()

        self.engine = TradingEngine(
            sheet=self.sheet,
            telegram=self.telegram
        )

    # ------------------------------------------------------

    def run_once(self):

        print("=" * 80)
        print("Fetching Market Data...")
        print("=" * 80)

        stocks = self.pipeline.fetch_stocks()
        indices = self.pipeline.fetch_indices()

        print(f"Stocks : {len(stocks)}")
        print(f"Indices: {len(indices)}")

        result = self.engine.run(stocks)

        ranked = result["stocks"]

        print()
        print("Top Opportunities")
        print("-" * 80)

        cols = [
            "symbol",
            "total_score",
            "confidence",
            "decision",
            "scanner_rank"
        ]

        existing = [c for c in cols if c in ranked.columns]

        print(ranked[existing].head(20))

        print()

        print("Market")

        print(result["market"])

        print()

        print("Indices")

        print(result["indices"])

        return result

    # ------------------------------------------------------

    def loop(self, interval=60):

        while True:

            try:

                self.run_once()

            except Exception as e:

                print(e)

            time.sleep(interval)
