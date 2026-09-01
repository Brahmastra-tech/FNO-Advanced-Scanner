
from pprint import pprint

from data.universe import Universe
from data.live_quotes import LiveQuotes
from data.market_snapshot import MarketSnapshot
from data.validator import Validator
from storage.market_cache import MarketCache
from storage.snapshot_store import SnapshotStore
from data.candle_builder import CandleBuilder

from sheets.google_sheet import GoogleSheet
from settings import (
    GOOGLE_CREDENTIALS,
    GOOGLE_SPREADSHEET,
)


class Pipeline:

    def __init__(self):

        print("Initializing Pipeline...")

        self.universe = Universe()
        self.live_quotes = LiveQuotes()
        self.snapshot = MarketSnapshot()
        self.validator = Validator()
        self.cache = MarketCache()
        self.store = SnapshotStore()
        self.candles = CandleBuilder()

        try:
            self.google_sheet = GoogleSheet(
                GOOGLE_CREDENTIALS,
                GOOGLE_SPREADSHEET,
            )
            print("Google Sheet Connected")
        except Exception as e:
            self.google_sheet = None
            print(f"Google Sheet Disabled : {e}")

        print("Pipeline Ready.")

    def run(self):

        print("\n==============================")
        print("Starting Market Scan...")
        print("==============================")

        # ------------------------------------
        # Universe
        # ------------------------------------

        stocks = self.universe.get_fno_stocks()

        print(f"Universe Loaded : {len(stocks)} Stocks")

        if stocks.empty:
            print("Universe is empty.")
            return False

        # ------------------------------------
        # Instrument Keys
        # ------------------------------------

        keys = stocks["instrument_key"].tolist()

        print("\nFirst 5 Instrument Keys:")
        print(keys[:5])

        # ------------------------------------
        # Live Quotes
        # ------------------------------------

        quotes = self.live_quotes.quotes(keys)

        print(f"\nQuotes Received : {len(quotes)}")

        if not quotes:
            print("No quotes received.")
            return False

        first_key = next(iter(quotes))

        print("\n==============================")
        print("FIRST QUOTE")
        print("==============================")
        print(first_key)

        pprint(quotes[first_key])

        # ------------------------------------
        # Snapshot
        # ------------------------------------

        snapshot_df = self.snapshot.build(quotes)

        print("\n==============================")
        print("SNAPSHOT")
        print("==============================")
        print(snapshot_df)

        print(f"\nSnapshot Created : {len(snapshot_df)}")

        # ------------------------------------
        # Validation
        # ------------------------------------

        if not self.validator.validate(snapshot_df):

            self.validator.report(snapshot_df)
            print("Validation Failed.")
            return False

        self.validator.report(snapshot_df)

        # ------------------------------------
        # Cache
        # ------------------------------------

        self.cache.update_snapshot(snapshot_df)
        print("✓ Market Cache Updated")

        # ------------------------------------
        # Local Store
        # ------------------------------------

        self.store.update(snapshot_df)
        print("✓ Snapshot Store Updated")

        # ------------------------------------
        # Google Sheets
        # ------------------------------------

        if self.google_sheet is not None:

            try:
                self.google_sheet.update_stocks(snapshot_df)
                print("✓ Google Sheet Updated")
            except Exception as e:
                print(f"Google Sheet Update Failed : {e}")

        # ------------------------------------
        # Candle Builder
        # ------------------------------------

        self.candles.update(snapshot_df)
        print("✓ Candles Updated")

        print("\n==============================")
        print("Pipeline Completed Successfully")
        print("==============================")

        return True
