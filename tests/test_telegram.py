from alerts.telegram_alert import TelegramAlert

telegram = TelegramAlert()

row = {

    "symbol": "SBIN",

    "total_score": 94,

    "confidence": 91,

    "close": 812.45,

    "rs_score": 3.6,

    "rvol": 2.4,

    "sector_strength": 4,

    "smart_money_score": 86

}

telegram.breakout(row)
