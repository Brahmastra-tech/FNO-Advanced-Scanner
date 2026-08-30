from datetime import datetime


class MarketCache:
    """
    Central in-memory cache for the entire scanner.

    Nothing should directly read API responses.
    Everything reads from this cache.
    """

    def __init__(self):

        # ----------------------------
        # Live Market Data
        # ----------------------------
        self.latest_snapshot = None
        self.previous_snapshot = None
        self.opening_snapshot = None

        # ----------------------------
        # Candle Data
        # ----------------------------
        self.current_1m = None
        self.current_5m = None
        self.current_15m = None

        # ----------------------------
        # Historical Data
        # ----------------------------
        self.history_1m = {}
        self.history_5m = {}
        self.history_15m = {}
        self.daily_history = {}

        # ----------------------------
        # Market DataFrames
        # ----------------------------
        self.master_dataframe = None

        # ----------------------------
        # Indices
        # ----------------------------
        self.indices = {}

        # ----------------------------
        # Sector Data
        # ----------------------------
        self.sectors = {}

        # ----------------------------
        # Market Breadth
        # ----------------------------
        self.market_breadth = {}

        # ----------------------------
        # Scanner Results (Future)
        # ----------------------------
        self.scanner_output = None

        # ----------------------------
        # Last Update
        # ----------------------------
        self.last_update = None

    # ==========================================================
    # Snapshot Methods
    # ==========================================================

    def update_snapshot(self, snapshot_df):

        self.previous_snapshot = self.latest_snapshot

        self.latest_snapshot = snapshot_df

        self.last_update = datetime.now()

        if self.opening_snapshot is None:
            self.opening_snapshot = snapshot_df.copy()

    def get_latest_snapshot(self):

        return self.latest_snapshot

    def get_previous_snapshot(self):

        return self.previous_snapshot

    def get_opening_snapshot(self):

        return self.opening_snapshot

    # ==========================================================
    # Candle Methods
    # ==========================================================

    def update_1m(self, candles):

        self.current_1m = candles

    def update_5m(self, candles):

        self.current_5m = candles

    def update_15m(self, candles):

        self.current_15m = candles

    def get_1m(self):

        return self.current_1m

    def get_5m(self):

        return self.current_5m

    def get_15m(self):

        return self.current_15m

    # ==========================================================
    # Master DataFrame
    # ==========================================================

    def update_master_dataframe(self, df):

        self.master_dataframe = df

    def get_master_dataframe(self):

        return self.master_dataframe

    # ==========================================================
    # Market Breadth
    # ==========================================================

    def update_market_breadth(self, breadth):

        self.market_breadth = breadth

    def get_market_breadth(self):

        return self.market_breadth

    # ==========================================================
    # Sector Data
    # ==========================================================

    def update_sectors(self, sectors):

        self.sectors = sectors

    def get_sectors(self):

        return self.sectors

    # ==========================================================
    # Index Data
    # ==========================================================

    def update_indices(self, indices):

        self.indices = indices

    def get_indices(self):

        return self.indices

    # ==========================================================
    # Scanner Output
    # ==========================================================

    def update_scanner(self, scanner_df):

        self.scanner_output = scanner_df

    def get_scanner(self):

        return self.scanner_output

    # ==========================================================
    # Status
    # ==========================================================

    def status(self):

        return {

            "last_update": self.last_update,

            "snapshot_loaded": self.latest_snapshot is not None,

            "opening_loaded": self.opening_snapshot is not None,

            "1m_loaded": self.current_1m is not None,

            "5m_loaded": self.current_5m is not None,

            "15m_loaded": self.current_15m is not None,

            "master_loaded": self.master_dataframe is not None,

            "scanner_loaded": self.scanner_output is not None

        }
