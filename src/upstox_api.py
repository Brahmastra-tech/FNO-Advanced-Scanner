import requests

from src.settings import (
    UPSTOX_ACCESS_TOKEN,
    BASE_URL,
)


class UpstoxAPI:

    def __init__(self):

        self.headers = {
            "Authorization": f"Bearer {UPSTOX_ACCESS_TOKEN}",
            "Accept": "application/json"
        }

    def get_quote(self, instrument_key):

        url = f"{BASE_URL}/market-quote/quotes"

        response = requests.get(
            url,
            headers=self.headers,
            params={
                "instrument_key": instrument_key
            },
            timeout=30
        )

        return response.json()
