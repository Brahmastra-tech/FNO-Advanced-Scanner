import requests

from settings import (
    UPSTOX_ACCESS_TOKEN,
    BASE_URL
)


class OptionChain:

    def __init__(self):

        self.headers = {

            "Authorization": f"Bearer {UPSTOX_ACCESS_TOKEN}",

            "Accept": "application/json"

        }

    # --------------------------------------------------

    def fetch(

            self,

            instrument_key,

            expiry_date

    ):

        url = f"{BASE_URL}/option/chain"

        params = {

            "instrument_key": instrument_key,

            "expiry_date": expiry_date

        }

        response = requests.get(

            url,

            headers=self.headers,

            params=params,

            timeout=30

        )

        if response.status_code != 200:

            raise Exception(response.text)

        return response.json()

    # --------------------------------------------------

    def calls(

            self,

            option_chain

    ):

        data = option_chain["data"]

        return [

            row

            for row in data

            if row.get("call_options")

        ]

    # --------------------------------------------------

    def puts(

            self,

            option_chain

    ):

        data = option_chain["data"]

        return [

            row

            for row in data

            if row.get("put_options")

        ]

    # --------------------------------------------------

    def atm(

            self,

            option_chain

    ):

        data = option_chain["data"]

        underlying = option_chain["data"][0]["underlying_spot_price"]

        nearest = min(

            data,

            key=lambda x: abs(

                x["strike_price"] -

                underlying

            )

        )

        return nearest

    # --------------------------------------------------

    def strikes(

            self,

            option_chain

    ):

        return [

            row["strike_price"]

            for row in option_chain["data"]

        ]
