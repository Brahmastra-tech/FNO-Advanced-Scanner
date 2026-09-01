from pprint import pprint

from data.universe import Universe
from data.live_quotes import LiveQuotes
from data.market_snapshot import MarketSnapshot
from data.validator import Validator
from data.candle_builder import CandleBuilder

from storage.market_cache import MarketCache
from storage.snapshot_store import SnapshotStore

from sheets.google_sheet import GoogleSheet
import settings


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

        # -----------------------------
        # Google Sheets
        # -----------------------------
        self.google = GoogleSheet(
            settings.GOOGLE_CREDENTIALS,
            settings.GOOGLE_SPREADSHEET
        )

        print("Pipeline Ready.")

    def run(self):

        print("\n==============================")
        print("Starting Market Scan...")
        print("==============================")

        # ---------------------------------
        # Universe
        # ---------------------------------

        stocks = self.universe.get_fno_stocks()

        print(f"Universe Loaded : {len(stocks)} Stocks")

        if stocks.empty:
            print("Universe is empty.")
            return False

        # ---------------------------------
        # Instrument Keys
        # ---------------------------------

        keys = stocks["instrument_key"].tolist()

        print("\nFirst 5 Instrument Keys:")
        print(keys[:5])

        # ---------------------------------
        # Live Quotes
        # ---------------------------------

        quotes = self.live_quotes.quotes(keys)

        print(f"\nQuotes Received : {len(quotes)}")

        if not quotes:
            print("LiveQuotes returned an empty dictionary.")
            return False

        first_key = next(iter(quotes))

        print("\n==============================")
        print("FIRST QUOTE")
        print("==============================")
        print(first_key)

        pprint(quotes[first_key])

        # ---------------------------------
        # Snapshot
        # ---------------------------------

        snapshot_df = self.snapshot.build(quotes)

        print("\n==============================")
        print("SNAPSHOT")
        print("==============================")

        print(snapshot_df)

        print(f"\nSnapshot Created : {len(snapshot_df)}")

        # ---------------------------------
        # Validation
        # ---------------------------------

        status = self.validator.validate(snapshot_df)

        self.validator.report(snapshot_df)

        if not status:
            print("Validation Failed.")
            return False

        # ---------------------------------
        # Market Cache
        # ---------------------------------

        self.cache.update_snapshot(snapshot_df)

        print("Market Cache Updated")

        # ---------------------------------
        # Snapshot Store
        # ---------------------------------

        self.store.update(snapshot_df)

        print("Snapshot Store Updated")

        # ---------------------------------
        # Candle Builder
        # ---------------------------------

        self.candles.update(snapshot_df)

        print("Candles Updated")

        # ---------------------------------
        # Google Sheets
        # ---------------------------------

        print("\nUpdating Google Sheet...")

        self.google.update_stocks(snapshot_df)

        print("Google Sheet Updated")

        print("\nPipeline Completed Successfully.")

        return True
