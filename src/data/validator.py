import pandas as pd
from datetime import datetime


class Validator:

    def __init__(self):
        self.errors = []

    def validate(self, snapshot_df: pd.DataFrame):

        self.errors = []

        if snapshot_df is None or snapshot_df.empty:
            self.errors.append("Snapshot is empty.")
            return False

        required_columns = [
            "instrument_key",
            "symbol",
            "ltp",
            "volume",
            "turnover",
            "timestamp"
        ]

        # -----------------------------
        # Required Columns
        # -----------------------------
        for col in required_columns:

            if col not in snapshot_df.columns:
                self.errors.append(f"Missing Column : {col}")

        if self.errors:
            return False

        # -----------------------------
        # Duplicate Instrument Keys
        # -----------------------------
        duplicate_keys = snapshot_df["instrument_key"].duplicated().sum()

        if duplicate_keys > 0:
            self.errors.append(
                f"Duplicate Instrument Keys : {duplicate_keys}"
            )

        # -----------------------------
        # Missing LTP
        # -----------------------------
        missing_ltp = snapshot_df["ltp"].isna().sum()

        if missing_ltp > 0:
            self.errors.append(
                f"Missing LTP : {missing_ltp}"
            )

        # -----------------------------
        # Missing Volume
        # -----------------------------
        missing_volume = snapshot_df["volume"].isna().sum()

        if missing_volume > 0:
            self.errors.append(
                f"Missing Volume : {missing_volume}"
            )

        # -----------------------------
        # Missing Turnover
        # -----------------------------
        missing_turnover = snapshot_df["turnover"].isna().sum()

        if missing_turnover > 0:
            self.errors.append(
                f"Missing Turnover : {missing_turnover}"
            )

        # -----------------------------
        # Missing Symbol
        # -----------------------------
        missing_symbol = snapshot_df["symbol"].isna().sum()

        if missing_symbol > 0:
            self.errors.append(
                f"Missing Symbol : {missing_symbol}"
            )

        # -----------------------------
        # Missing Timestamp
        # -----------------------------
        missing_time = snapshot_df["timestamp"].isna().sum()

        if missing_time > 0:
            self.errors.append(
                f"Missing Timestamp : {missing_time}"
            )

        return len(self.errors) == 0

    def report(self, snapshot_df: pd.DataFrame):

        print("\n" + "=" * 55)
        print("MARKET DATA VALIDATION REPORT")
        print("=" * 55)

        print(f"Validation Time : {datetime.now()}")

        if snapshot_df is not None:
            print(f"Total Records   : {len(snapshot_df)}")
        else:
            print("Total Records   : 0")

        if len(self.errors) == 0:

            print("\nSTATUS : PASS")
            print("No validation errors found.")

        else:

            print("\nSTATUS : FAILED")

            for error in self.errors:
                print(f"• {error}")

        print("=" * 55)

    def get_errors(self):

        return self.errors

    def has_errors(self):

        return len(self.errors) > 0
