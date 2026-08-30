from options.option_engine import OptionEngine

engine = OptionEngine()

result = engine.analyze(

    instrument_key="NSE_INDEX|Nifty 50",

    expiry_date="2025-08-28"

)

print(result["support"])

print(result["resistance"])
