import pandas as pd

from analytics.relative_strength import RelativeStrength
from analytics.sector_strength import SectorStrength
from analytics.volume_engine import VolumeEngine
from analytics.market_breadth import MarketBreadth
from analytics.compression_engine import CompressionEngine
from analytics.structure_engine import StructureEngine
from analytics.smart_money_engine import SmartMoneyEngine
from analytics.breakout_engine import BreakoutEngine

from scanner.rule_engine import RuleEngine
from scanner.opportunity_engine import OpportunityEngine


class ScannerEngine:

    def __init__(self):

        self.rs = RelativeStrength()

        self.sector = SectorStrength()

        self.volume = VolumeEngine()

        self.market = MarketBreadth()

        self.compression = CompressionEngine()

        self.structure = StructureEngine()

        self.smart = SmartMoneyEngine()

        self.breakout = BreakoutEngine()

        self.rule = RuleEngine()

        self.opportunity = OpportunityEngine()

    def run(

            self,

            current_df,

            previous_df,

            market_status="NEUTRAL"

    ):

        df = current_df.copy()

        print("\nRunning Relative Strength")

        df = self.rs.calculate(

            df,

            previous_df

        )

        print("Running Sector Strength")

        df = self.sector.calculate(df)

        print("Running Volume Engine")

        df = self.volume.calculate(

            df,

            previous_df

        )

        print("Running Market Breadth")

        df = self.market.calculate(df)

        print("Running Compression Engine")

        df = self.compression.calculate(df)

        print("Running Structure Engine")

        df = self.structure.calculate(

            df,

            previous_df

        )

        print("Running Smart Money")

        df = self.smart.calculate(

            df,

            previous_df

        )

        print("Running Breakout Engine")

        df = self.breakout.calculate(df)

        print("Running Rule Engine")

        df = self.rule.calculate(

            df,

            market_status

        )

        print("Running Opportunity Engine")

        df = self.opportunity.calculate(

            df,

            market_status

        )

        df = df.sort_values(

            by=[

                "total_score",

                "confidence"

            ],

            ascending=False

        )

        return df

    def watchlist(

            self,

            df

    ):

        return df[

            df["scanner_stage"] == "WATCH"

        ]

    def ready(

            self,

            df

    ):

        return df[

            df["scanner_stage"] == "READY"

        ]

    def breakout(

            self,

            df

    ):

        return df[

            df["scanner_stage"] == "BREAKOUT"

        ]

    def top(

            self,

            df,

            n=20

    ):

        return df.head(n)
