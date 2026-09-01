from pprint import pprint

from data.universe import Universe
from data.live_quotes import LiveQuotes
from data.market_snapshot import MarketSnapshot
from data.validator import Validator
from data.candle_builder import CandleBuilder

from storage.market_cache import MarketCache
from storage.snapshot_store import SnapshotStore

from sheets.google_sheet import GoogleSheet
from core.config import settings


class Pipeline:

    def __init__(self):

        print("Initializing Pipeline...")

        self.universe = Universe()
        self.live_quotes = LiveQuotes()
        self.snapshot = MarketSnapshot()
        self.validator = Validator()

        self.cache = MarketCache()
        self.store = SnapshotStore()

        # Google Sheets
        self.gs = GoogleSheet(
            settings.GOOGLE_CREDENTIALS,
            settings.GOOGLE_SPREADSHEET
        )

        self.candles = CandleBuilder()

        print("Pipeline Ready.")

    def run(self):

        print("\n==============================")
        print("Starting Market Scan...")
        print("==============================")

        # ---------------------------------
        # Load Universe
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

        # ---------------------------------
        # Fetch Quotes
        # ---------------------------------

        quotes = self.live_quotes.quotes(keys)

        print(f"Quotes Received : {len(quotes)}")

        if not quotes:
            print("No quotes received.")
            return False

        # ---------------------------------
        # Build Snapshot
        # ---------------------------------

        snapshot_df = self.snapshot.build(quotes)

        print(f"Snapshot Created : {len(snapshot_df)}")

        # ---------------------------------
        # Validate
        # ---------------------------------

        status = self.validator.validate(snapshot_df)

        self.validator.report(snapshot_df)

        if not status:
            print("Validation Failed.")
            return False

        # ---------------------------------
        # Update Cache
        # ---------------------------------

        self.cache.update_snapshot(snapshot_df)

        print("Market Cache Updated")

        # ---------------------------------
        # Update Snapshot Store
        # ---------------------------------

        self.store.update(snapshot_df)

        print("Snapshot Store Updated")

        # ---------------------------------
        # Upload to Google Sheets
        # ---------------------------------

        try:

            self.gs.update_stocks(snapshot_df)

            print("Google Sheet Updated")

        except Exception as e:

            print(f"Google Sheet Error : {e}")

        # ---------------------------------
        # Update Candles
        # ---------------------------------

        self.candles.update(snapshot_df)

        print("Candles Updated")

        print("\nPipeline Completed Successfully.")

        return True
