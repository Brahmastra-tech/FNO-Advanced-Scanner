import os
from dotenv import load_dotenv

# ==========================================================
# Load Environment Variables
# ==========================================================

load_dotenv()

# ==========================================================
# Upstox
# ==========================================================

UPSTOX_ACCESS_TOKEN = os.getenv("UPSTOX_ACCESS_TOKEN", "")

BASE_URL = "https://api.upstox.com/v2"

# ==========================================================
# Scanner Configuration
# ==========================================================

SCAN_INTERVAL = int(os.getenv("SCAN_INTERVAL", "60"))

MARKET_START = "09:15"

MARKET_OBSERVATION_END = "09:25"

MARKET_CLOSE = "15:30"

# ==========================================================
# Scanner Filters
# ==========================================================

MIN_PRICE = float(os.getenv("MIN_PRICE", "100"))

MIN_DAILY_TURNOVER = float(os.getenv("MIN_DAILY_TURNOVER", "250000000"))

MIN_AVG_VOLUME = int(os.getenv("MIN_AVG_VOLUME", "200000"))

MIN_RVOL = float(os.getenv("MIN_RVOL", "1.5"))

MAX_MOVE_FROM_OPEN = float(os.getenv("MAX_MOVE_FROM_OPEN", "1.5"))

# ==========================================================
# Scanner Thresholds
# ==========================================================

WATCH_SCORE = int(os.getenv("WATCH_SCORE", "65"))

READY_SCORE = int(os.getenv("READY_SCORE", "80"))

BREAKOUT_SCORE = int(os.getenv("BREAKOUT_SCORE", "90"))

SMART_MONEY_THRESHOLD = int(os.getenv("SMART_MONEY_THRESHOLD", "70"))

COMPRESSION_THRESHOLD = int(os.getenv("COMPRESSION_THRESHOLD", "80"))

STRUCTURE_THRESHOLD = int(os.getenv("STRUCTURE_THRESHOLD", "80"))

BREAKOUT_THRESHOLD = int(os.getenv("BREAKOUT_THRESHOLD", "75"))

# ==========================================================
# Google Sheets
# ==========================================================

GOOGLE_CREDENTIALS = os.getenv(
    "GOOGLE_CREDENTIALS",
    "credentials.json"
)

GOOGLE_SPREADSHEET = os.getenv(
    "GOOGLE_SPREADSHEET",
    "FNO Advanced Scanner"
)

# ==========================================================
# Telegram
# ==========================================================

TELEGRAM_BOT_TOKEN = os.getenv(
    "TELEGRAM_BOT_TOKEN",
    ""
)

TELEGRAM_CHAT_ID = os.getenv(
    "TELEGRAM_CHAT_ID",
    ""
)

# ==========================================================
# Logging
# ==========================================================

LOG_LEVEL = os.getenv(
    "LOG_LEVEL",
    "INFO"
)

# ==========================================================
# Output Files
# ==========================================================

DATA_FOLDER = "data"

LOG_FOLDER = "logs"

EXPORT_FOLDER = "exports"

# ==========================================================
# Alert Settings
# ==========================================================

ALERT_SCORE_DELTA = int(
    os.getenv("ALERT_SCORE_DELTA", "10")
)

ALERT_COOLDOWN_MINUTES = int(
    os.getenv("ALERT_COOLDOWN_MINUTES", "15")
)

# ==========================================================
# Scanner Version
# ==========================================================

APP_NAME = "FNO Advanced Scanner"

VERSION = "1.0.0"
