from upstox_api import UpstoxAPI

api = UpstoxAPI()

quote = api.get_quote("NSE_INDEX|Nifty 50")

print(quote)
