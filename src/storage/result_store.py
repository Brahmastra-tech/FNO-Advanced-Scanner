from datetime import datetime


class ResultStore:

    def __init__(self):

        self.results = {}

    def update(self, dataframe):

        for _, row in dataframe.iterrows():

            symbol = row["symbol"]

            current_score = row["total_score"]

            stage = row["scanner_stage"]

            now = datetime.now()

            if symbol not in self.results:

                self.results[symbol] = {

                    "symbol": symbol,

                    "current_score": current_score,

                    "previous_score": current_score,

                    "score_delta": 0,

                    "current_stage": stage,

                    "previous_stage": stage,

                    "alert_count": 0,

                    "last_alert": None,

                    "first_seen": now,

                    "last_seen": now

                }

                continue

            item = self.results[symbol]

            item["previous_score"] = item["current_score"]

            item["current_score"] = current_score

            item["score_delta"] = (

                current_score -

                item["previous_score"]

            )

            item["previous_stage"] = item["current_stage"]

            item["current_stage"] = stage

            item["last_seen"] = now

    def should_alert(self, symbol):

        if symbol not in self.results:

            return False

        item = self.results[symbol]

        if item["current_stage"] != item["previous_stage"]:

            return True

        if item["score_delta"] >= 10:

            return True

        return False

    def register_alert(self, symbol):

        if symbol not in self.results:

            return

        self.results[symbol]["alert_count"] += 1

        self.results[symbol]["last_alert"] = datetime.now()

    def get(self, symbol):

        return self.results.get(symbol)

    def all(self):

        return self.results

    def reset(self):

        self.results = {}
