from options.option_chain import OptionChain
from options.oi_analyzer import OIAnalyzer

chain = OptionChain()

data = chain.fetch(

    instrument_key="NSE_INDEX|Nifty 50",

    expiry_date="2025-08-28"

)

engine = OIAnalyzer()

df = engine.analyze(data)

print(engine.summary(df))
