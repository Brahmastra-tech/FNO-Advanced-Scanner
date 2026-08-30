import time
from datetime import datetime

from scanner.scanner_engine import ScannerEngine
from storage.result_store import ResultStore
from alerts.alert_manager import AlertManager


class Scheduler:

    def __init__(
            self,
            fetch_function,
            google_sheet=None
    ):

        self.fetch_function = fetch_function

        self.sheet = google_sheet

        self.scanner = ScannerEngine()

        self.store = ResultStore()

        self.alert_manager = AlertManager(self.store)

        self.previous_df = None

    # ----------------------------------------------------

    def run_once(self):

        current_df = self.fetch_function()

        if current_df is None or len(current_df) == 0:

            print("No market data.")

            return

        if self.previous_df is None:

            self.previous_df = current_df.copy()

            print("Initial snapshot stored.")

            return

        result = self.scanner.run(

            current_df=current_df,

            previous_df=self.previous_df

        )

        self.store.update(result)

        self.alert_manager.process(result)

        if self.sheet:

            self.sheet.update_stocks(result)

        self.previous_df = current_df.copy()

        print(

            f"Completed : {datetime.now()}"

        )

    # ----------------------------------------------------

    def start(self, interval=60):

        print("Scheduler Started")

        while True:

            try:

                self.run_once()

            except Exception as e:

                print(e)

            time.sleep(interval)
