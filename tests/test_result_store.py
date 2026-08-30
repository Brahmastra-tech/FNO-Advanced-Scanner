import pandas as pd

from storage.result_store import ResultStore

store = ResultStore()

df = pd.DataFrame({

    "symbol": [

        "SBIN",

        "RELIANCE"

    ],

    "total_score": [

        82,

        65

    ],

    "scanner_stage": [

        "READY",

        "WATCH"

    ]

})

store.update(df)

print(store.all())

df2 = pd.DataFrame({

    "symbol": [

        "SBIN",

        "RELIANCE"

    ],

    "total_score": [

        94,

        67

    ],

    "scanner_stage": [

        "BREAKOUT",

        "WATCH"

    ]

})

store.update(df2)

print(store.should_alert("SBIN"))

store.register_alert("SBIN")

print(store.get("SBIN"))
