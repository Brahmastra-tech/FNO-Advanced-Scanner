from collections import defaultdict, deque
from datetime import datetime
import pandas as pd


class SnapshotStore:
    """
    Stores rolling market snapshots in memory.

    Structure:

    {
        instrument_key: deque([
            {...snapshot1...},
            {...snapshot2...},
            ...
        ])
    }
    """

    def __init__(self, max_history=5000):

        # One deque per instrument
        self.store = defaultdict(lambda: deque(maxlen=max_history))

    def update(self, snapshot_df: pd.DataFrame):

        """
        Add latest snapshot dataframe into memory.
        """

        if snapshot_df.empty:
            return

        records = snapshot_df.to_dict("records")

        for row in records:

            key = row["instrument_key"]

            self.store[key].append(row)

    def get_history(self, instrument_key):

        """
        Return complete history for one instrument.
        """

        return list(self.store[instrument_key])

    def get_dataframe(self, instrument_key):

        """
        Return history as dataframe.
        """

        history = self.get_history(instrument_key)

        if not history:
            return pd.DataFrame()

        return pd.DataFrame(history)

    def latest(self, instrument_key):

        """
        Latest snapshot only.
        """

        if len(self.store[instrument_key]) == 0:
            return None

        return self.store[instrument_key][-1]

    def latest_all(self):

        """
        Latest snapshot of all instruments.
        """

        rows = []

        for key in self.store:

            if len(self.store[key]) > 0:

                rows.append(self.store[key][-1])

        return pd.DataFrame(rows)

    def size(self):

        """
        Number of tracked instruments.
        """

        return len(self.store)

    def clear(self):

        self.store.clear()

    def stats(self):

        return {

            "instruments": len(self.store),

            "snapshots": sum(len(v) for v in self.store.values()),

            "updated_at": datetime.now()

        }
