from upstox_api import UpstoxAPI


class LiveQuotes:

    def __init__(self):

        self.api = UpstoxAPI()

    def quote(self, instrument_key):

        return self.api.get_quote(instrument_key)

    def quotes(self, keys):

        data = {}

        for key in keys:

            data[key] = self.quote(key)

        return data
