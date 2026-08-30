import pandas as pd

from storage.market_cache import MarketCache

cache = MarketCache()

df = pd.DataFrame({

    "symbol": ["SBIN", "RELIANCE"],

    "ltp": [812.50, 2988.40]

})

cache.update_snapshot(df)

print(cache.get_latest_snapshot())

print()

print(cache.status())
