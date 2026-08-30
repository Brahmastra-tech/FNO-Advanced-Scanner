from datetime import datetime, timedelta

from alerts.telegram_alert import TelegramAlert


class AlertManager:

    def __init__(self, result_store):

        self.result_store = result_store

        self.telegram = TelegramAlert()

    # =====================================================
    # Process Scanner Output
    # =====================================================

    def process(self, dataframe):

        for _, row in dataframe.iterrows():

            symbol = row["symbol"]

            info = self.result_store.get(symbol)

            if info is None:
                continue

            # -------------------------
            # Cooldown Check
            # -------------------------

            if self.in_cooldown(info):
                continue

            # -------------------------
            # Stage Changed
            # -------------------------

            if info["current_stage"] != info["previous_stage"]:

                self.telegram.stage_change(

                    symbol,

                    info["previous_stage"],

                    info["current_stage"],

                    row["total_score"]

                )

                self.result_store.register_alert(symbol)

                continue

            # -------------------------
            # Score Improved
            # -------------------------

            if info["score_delta"] >= 10:

                self.telegram.score_improved(

                    symbol,

                    info["previous_score"],

                    info["current_score"]

                )

                self.result_store.register_alert(symbol)

                continue

            # -------------------------
            # Fresh Breakout
            # -------------------------

            if row["scanner_stage"] == "BREAKOUT":

                self.telegram.breakout(row)

                self.result_store.register_alert(symbol)

                continue

            # -------------------------
            # Ready
            # -------------------------

            if row["scanner_stage"] == "READY":

                self.telegram.ready(row)

                self.result_store.register_alert(symbol)

                continue

            # -------------------------
            # Watch
            # -------------------------

            if row["scanner_stage"] == "WATCH":

                self.telegram.watch(row)

                self.result_store.register_alert(symbol)

    # =====================================================
    # Cooldown
    # =====================================================

    def in_cooldown(self, info):

        last = info["last_alert"]

        if last is None:

            return False

        cooldown = timedelta(minutes=15)

        return datetime.now() < last + cooldown
