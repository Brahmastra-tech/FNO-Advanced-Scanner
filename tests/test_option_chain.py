from options.option_chain import OptionChain

chain = OptionChain()

data = chain.fetch(

    instrument_key="NSE_INDEX|Nifty 50",

    expiry_date="2025-08-28"

)

print(

    chain.atm(data)

)
