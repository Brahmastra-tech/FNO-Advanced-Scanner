import pandas as pd

from sheets.google_sheet import GoogleSheet

from settings import *

sheet = GoogleSheet(

    GOOGLE_CREDENTIALS,

    GOOGLE_SPREADSHEET

)

df = pd.DataFrame({

    "Symbol":[

        "SBIN",

        "RELIANCE"

    ],

    "Score":[

        91,

        82

    ],

    "Stage":[

        "BREAKOUT",

        "READY"

    ]

})

sheet.update_stocks(df)

print("Done")
