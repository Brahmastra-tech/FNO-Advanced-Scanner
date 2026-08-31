from pprint import pprint

from data.universe import Universe
from data.live_quotes import LiveQuotes
from data.market_snapshot import MarketSnapshot
from data.validator import Validator
from storage.market_cache import MarketCache
from storage.snapshot_store import SnapshotStore
from data.candle_builder import CandleBuilder


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

        print("Pipeline Ready.")

    def run(self):

        print("\n==============================")
        print("Starting Market Scan...")
        print("==============================")

        # -------------------------
        # Load Universe
        # -------------------------

        stocks = self.universe.get_fno_stocks()

        print(f"Universe Loaded : {len(stocks)} Stocks")

        if stocks.empty:
            print("Universe is empty.")
            return False

        # -------------------------
        # Instrument Keys
        # -------------------------

        keys = stocks["instrument_key"].tolist()

        print("\nFirst 5 Instrument Keys:")
        print(keys[:5])

        # -------------------------
        # Fetch Live Quotes
        # -------------------------

        quotes = self.live_quotes.quotes(keys)

        print(f"\nQuotes Received : {len(quotes)}")

        if not quotes:
            print("LiveQuotes returned an empty dictionary.")
            return False

        first_key = next(iter(quotes))

        print("\n==============================")
        print("FIRST QUOTE")
        print("==============================")
        print("Instrument Key:")
        print(first_key)

        print("\nResponse:")
        pprint(quotes[first_key])

        # -------------------------
        # Build Snapshot
        # -------------------------

        snapshot_df = self.snapshot.build(quotes)

        print("\n==============================")
        print("SNAPSHOT")
        print("==============================")
        print(snapshot_df)

        print(f"\nSnapshot Created : {len(snapshot_df)}")

        # -------------------------
        # Validate
        # -------------------------

        status = self.validator.validate(snapshot_df)

        self.validator.report(snapshot_df)

        if not status:
            print("Validation Failed.")
            return False

        # -------------------------
        # Update Cache
        # -------------------------

        self.cache.update_snapshot(snapshot_df)
        print("Market Cache Updated")

        # -------------------------
        # Update Snapshot Store
        # -------------------------

        self.store.update(snapshot_df)
        print("Snapshot Store Updated")

        # -------------------------
        # Build Candles
        # -------------------------

        self.candles.update(snapshot_df)
        print("Candles Updated")

        print("\nPipeline Completed Successfully.")

        return True
