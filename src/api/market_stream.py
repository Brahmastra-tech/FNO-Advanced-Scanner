import upstox_client


class MarketStream:

    def __init__(self, access_token):

        configuration = upstox_client.Configuration()
        configuration.access_token = access_token

        self.client = upstox_client.ApiClient(configuration)

        self.streamer = None

    def connect(self, instrument_keys):

        self.streamer = upstox_client.MarketDataStreamerV3(
            self.client,
            instrument_keys,
            "full"
        )

        self.streamer.on("open", self.on_open)
        self.streamer.on("message", self.on_message)
        self.streamer.on("close", self.on_close)
        self.streamer.on("error", self.on_error)

        self.streamer.connect()

    def on_open(self):
        print("WebSocket Connected")

    def on_message(self, message):
        print(message)

    def on_close(self):
        print("WebSocket Closed")

    def on_error(self, error):
        print(error)
