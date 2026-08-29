from dotenv import load_dotenv
import os

load_dotenv()

CLIENT_ID = os.getenv("UPSTOX_CLIENT_ID")
CLIENT_SECRET = os.getenv("UPSTOX_CLIENT_SECRET")
REDIRECT_URI = os.getenv("UPSTOX_REDIRECT_URI")

MOBILE = os.getenv("UPSTOX_MOBILE")
PIN = os.getenv("UPSTOX_PIN")
TOTP_SECRET = os.getenv("UPSTOX_TOTP_SECRET")


def check_env():
    print("Checking environment...")

    required = {
        "CLIENT_ID": CLIENT_ID,
        "CLIENT_SECRET": CLIENT_SECRET,
        "REDIRECT_URI": REDIRECT_URI,
        "MOBILE": MOBILE,
        "PIN": PIN,
        "TOTP_SECRET": TOTP_SECRET,
    }

    for key, value in required.items():
        if value:
            print(f"✅ {key}")
        else:
            print(f"❌ Missing {key}")
