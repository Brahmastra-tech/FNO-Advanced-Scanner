import requests
from datetime import datetime

from settings import (
    TELEGRAM_BOT_TOKEN,
    TELEGRAM_CHAT_ID
)


class TelegramAlert:

    def __init__(self):

        self.token = TELEGRAM_BOT_TOKEN

        self.chat_id = TELEGRAM_CHAT_ID

        self.base_url = (
            f"https://api.telegram.org/bot{self.token}"
        )

    # =====================================================
    # Send Raw Message
    # =====================================================

    def send(self, message):

        if not self.token or not self.chat_id:

            print("Telegram not configured.")

            return

        url = f"{self.base_url}/sendMessage"

        payload = {

            "chat_id": self.chat_id,

            "text": message,

            "parse_mode": "Markdown"

        }

        try:

            response = requests.post(

                url,

                json=payload,

                timeout=15

            )

            if response.status_code != 200:

                print(response.text)

        except Exception as e:

            print(e)

    # =====================================================
    # BREAKOUT ALERT
    # =====================================================

    def breakout(self, row):

        msg = f"""
🚀 *BREAKOUT ALERT*

*{row['symbol']}*

Score : *{row['total_score']}*

Confidence : *{row['confidence']}%*

LTP : {row['close']}

RS : {row['rs_score']}

RVOL : {row['rvol']}

Sector : {row['sector_strength']}

Smart Money : {row['smart_money_score']}

Time : {datetime.now().strftime("%H:%M:%S")}
"""

        self.send(msg)

    # =====================================================
    # READY ALERT
    # =====================================================

    def ready(self, row):

        msg = f"""
🟢 *READY*

*{row['symbol']}*

Score : *{row['total_score']}*

Confidence : *{row['confidence']}%*

LTP : {row['close']}

Time : {datetime.now().strftime("%H:%M:%S")}
"""

        self.send(msg)

    # =====================================================
    # WATCH ALERT
    # =====================================================

    def watch(self, row):

        msg = f"""
🟡 *WATCH*

*{row['symbol']}*

Score : *{row['total_score']}*

Confidence : *{row['confidence']}%*

LTP : {row['close']}
"""

        self.send(msg)

    # =====================================================
    # STAGE CHANGE
    # =====================================================

    def stage_change(

            self,

            symbol,

            old_stage,

            new_stage,

            score

    ):

        msg = f"""
📈 *STAGE UPGRADE*

{symbol}

{old_stage}

➡️

{new_stage}

Score : {score}
"""

        self.send(msg)

    # =====================================================
    # SCORE IMPROVEMENT
    # =====================================================

    def score_improved(

            self,

            symbol,

            old_score,

            new_score

    ):

        msg = f"""
⭐ *SCORE IMPROVED*

{symbol}

{old_score}

➡️

{new_score}
"""

        self.send(msg)

    # =====================================================
    # End Of Day Summary
    # =====================================================

    def summary(

            self,

            watch,

            ready,

            breakout

    ):

        msg = f"""
📊 *Scanner Summary*

WATCH : {watch}

READY : {ready}

BREAKOUT : {breakout}

Generated :

{datetime.now().strftime("%d-%m-%Y %H:%M")}
"""

        self.send(msg)

    # =====================================================
    # Error
    # =====================================================

    def error(self, message):

        self.send(

            f"❌ Scanner Error\n\n{message}"

        )
