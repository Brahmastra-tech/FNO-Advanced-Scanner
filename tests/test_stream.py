from settings import UPSTOX_ACCESS_TOKEN
from api.market_stream import MarketStream

instrument_keys = [
    "NSE_INDEX|Nifty 50"
]

stream = MarketStream(UPSTOX_ACCESS_TOKEN)
stream.connect(instrument_keys)
