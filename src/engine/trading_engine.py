from core.data_manager import DataManager

from analytics.feature_engine import FeatureEngine

from scanner.filter_engine import FilterEngine
from scanner.scoring_engine import ScoringEngine
from scanner.decision_engine import DecisionEngine
from scanner.opportunity_engine import OpportunityEngine

from market.market_breadth import MarketBreadth
from market.index_engine import IndexEngine

from alerts.alert_manager import AlertManager

from sheets.google_sheet import GoogleSheet


class TradingEngine:

    def __init__(

            self,

            sheet=None,

            telegram=None

    ):

        self.data = DataManager()

        self.feature = FeatureEngine()

        self.filter = FilterEngine()

        self.scoring = ScoringEngine()

        self.decision = DecisionEngine()

        self.opportunity = OpportunityEngine()

        self.market = MarketBreadth()

        self.indices = IndexEngine()

        self.alerts = AlertManager()

        self.sheet = sheet

        self.telegram = telegram

    # ----------------------------------------------------

    def run(

            self,

            live_dataframe

    ):

        # Update cache

        self.data.update(

            live_dataframe

        )

        df = self.data.dataframe()

        # --------------------------

        # Build Features

        df = self.feature.process(df)

        # --------------------------

        # Mandatory Filters

        df = self.filter.apply(df)

        # --------------------------

        # Score

        df = self.scoring.process(df)

        # --------------------------

        # Decision

        df = self.decision.process(df)

        # --------------------------

        # Rank

        df = self.opportunity.process(df)

        # --------------------------

        # Google Sheet

        if self.sheet:

            self.sheet.update_stocks(df)

        # --------------------------

        # Alerts

        alerts = self.alerts.process(df)

        # --------------------------

        return {

            "stocks": df,

            "alerts": alerts,

            "market": self.market.analyze(df),

            "indices": self.indices.summary(df)

        }
