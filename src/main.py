from src.upstox_api import UpstoxAPI


def main():
    api = UpstoxAPI()

    quote = api.get_quote("NSE_INDEX|Nifty 50")

    print(quote)


if __name__ == "__main__":
    main()
