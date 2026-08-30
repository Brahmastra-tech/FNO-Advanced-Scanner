import pandas as pd

from alerts.alert_manager import AlertManager
from storage.result_store import ResultStore

store = ResultStore()

df = pd.DataFrame({

    "symbol":["SBIN"],

    "total_score":[94],

    "confidence":[92],

    "close":[812],

    "scanner_stage":["BREAKOUT"],

    "rs_score":[3],

    "rvol":[2.2],

    "sector_strength":[4],

    "smart_money_score":[87]

})

store.update(df)

manager = AlertManager(store)

manager.process(df)
