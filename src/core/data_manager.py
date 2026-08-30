from analytics.opening_engine import OpeningEngine
from storage.snapshot_store import SnapshotStore
from storage.market_cache import MarketCache


class DataManager:
    """
    Central data manager.

    Responsible for

    • Current Snapshot
    • Previous Snapshot
    • Market Cache
    • Opening Snapshot
    """

    def __init__(self):

        self.snapshot_store = SnapshotStore()

        self.market_cache = MarketCache()

        self.opening_engine = OpeningEngine()

        self.current_df = None

        self.previous_df = None

    # ----------------------------------------------------

    def update(self, dataframe):

        self.previous_df = self.current_df

        self.current_df = dataframe.copy()

        self.snapshot_store.save(self.current_df)

        self.market_cache.update(self.current_df)

    # ----------------------------------------------------

    def capture_opening(self):

        if self.current_df is None:
            return

        if not self.opening_engine.is_ready():

            self.opening_engine.capture(

                self.current_df

            )

    # ----------------------------------------------------

    def dataframe(self):

        if self.current_df is None:

            return None

        return self.opening_engine.merge(

            self.current_df

        )

    # ----------------------------------------------------

    def current(self):

        return self.current_df

    # ----------------------------------------------------

    def previous(self):

        return self.previous_df

    # ----------------------------------------------------

    def cache(self):

        return self.market_cache

    # ----------------------------------------------------

    def reset(self):

        self.current_df = None

        self.previous_df = None

        self.market_cache.clear()

        self.opening_engine.reset()
