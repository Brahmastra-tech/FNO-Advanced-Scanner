import pandas as pd


class DataFrameBuilder:
    """
    Master Market DataFrame

    Every module updates this dataframe.

    Scanner, Alerts and Google Sheets
    read ONLY from this dataframe.
    """

    def __init__(self):

        self.df = pd.DataFrame()

    # ==================================================
    # Create Base DataFrame
    # ==================================================

    def build(self, snapshot_df):

        self.df = snapshot_df.copy()

        # -------- Intraday Analytics --------

        self.df["rvol"] = None

        self.df["volume_acceleration"] = None

        self.df["turnover_acceleration"] = None

        self.df["rs_nifty"] = None

        self.df["rs_sector"] = None

        self.df["sector_strength"] = None

        self.df["compression_score"] = None

        self.df["structure_score"] = None

        self.df["breakout_readiness"] = None

        self.df["smart_money_score"] = None

        self.df["momentum_score"] = None

        self.df["total_score"] = None

        self.df["confidence"] = None

        self.df["intraday_signal"] = None

        self.df["trend_stage"] = None

        self.df["event_type"] = None

        self.df["priority"] = None

        # -------- Swing --------

        self.df["swing_trend"] = None

        self.df["swing_rs"] = None

        self.df["swing_score"] = None

        self.df["swing_confidence"] = None

        self.df["swing_signal"] = None

        self.df["swing_stoploss"] = None

        self.df["swing_target"] = None

        self.df["holding_days"] = None

        # -------- Alert Control --------

        self.df["setup_id"] = None

        self.df["setup_state"] = None

        self.df["signal_since"] = None

        self.df["last_alert"] = None

        self.df["alert_count"] = 0

        self.df["previous_score"] = 0

        self.df["score_delta"] = 0

        self.df["cooldown_until"] = None

        self.df["alert_status"] = "READY"

        return self.df

    # ==================================================
    # Generic Update Function
    # ==================================================

    def update_column(self, column_name, values):

        if column_name not in self.df.columns:
            self.df[column_name] = None

        self.df[column_name] = values

    # ==================================================
    # Update Single Symbol
    # ==================================================

    def update_symbol(self, instrument_key, column, value):

        self.df.loc[
            self.df["instrument_key"] == instrument_key,
            column
        ] = value

    # ==================================================
    # Return DataFrame
    # ==================================================

    def get_dataframe(self):

        return self.df

    # ==================================================
    # Save Snapshot
    # ==================================================

    def save_csv(self, filename="market_dataframe.csv"):

        self.df.to_csv(filename, index=False)

    # ==================================================
    # Statistics
    # ==================================================

    def stats(self):

        return {

            "rows": len(self.df),

            "columns": len(self.df.columns),

            "signals":

                self.df["intraday_signal"].notna().sum()

                if "intraday_signal" in self.df.columns

                else 0

        }
