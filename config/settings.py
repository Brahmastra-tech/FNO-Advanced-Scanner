from dotenv import load_dotenv
import os

load_dotenv()

UPSTOX_API_KEY = os.getenv("UPSTOX_API_KEY")
UPSTOX_API_SECRET = os.getenv("UPSTOX_API_SECRET")
UPSTOX_REDIRECT_URI = os.getenv("UPSTOX_REDIRECT_URI")

UPSTOX_MOBILE = os.getenv("UPSTOX_MOBILE")
UPSTOX_PIN = os.getenv("UPSTOX_PIN")
UPSTOX_TOTP_SECRET = os.getenv("UPSTOX_TOTP_SECRET")

GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID")
GOOGLE_SERVICE_ACCOUNT = os.getenv(
    "GOOGLE_SERVICE_ACCOUNT",
    "service_account.json"
)
