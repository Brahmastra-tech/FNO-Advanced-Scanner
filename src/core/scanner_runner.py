import time
from datetime import datetime

from scanner.scanner_engine import ScannerEngine


class ScannerRunner:

    def __init__(self):

        self.scanner = ScannerEngine()

    def execute(

            self,

            current_df,

            previous_df,

            market_status="NEUTRAL"

    ):

        print("\n" + "=" * 70)
        print(f"SCAN STARTED : {datetime.now()}")
        print("=" * 70)

        result = self.scanner.run(

            current_df=current_df,

            previous_df=previous_df,

            market_status=market_status

        )

        print("\nTOP OPPORTUNITIES\n")

        print(

            result[

                [

                    "symbol",

                    "total_score",

                    "confidence",

                    "scanner_stage"

                ]

            ].head(20)

        )

        print("\nSCAN COMPLETED")

        return result

    def loop(

            self,

            fetch_function,

            interval=60,

            market_status="NEUTRAL"

    ):

        previous_df = None

        while True:

            try:

                current_df = fetch_function()

                if previous_df is None:

                    previous_df = current_df.copy()

                    print("Waiting for next snapshot...")

                    time.sleep(interval)

                    continue

                self.execute(

                    current_df=current_df,

                    previous_df=previous_df,

                    market_status=market_status

                )

                previous_df = current_df.copy()

            except Exception as e:

                print("\nScanner Error")

                print(e)

            print(f"\nSleeping {interval} seconds...\n")

            time.sleep(interval)
