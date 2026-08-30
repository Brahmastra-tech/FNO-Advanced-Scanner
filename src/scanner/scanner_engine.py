from scanner.filter_engine import FilterEngine
from scanner.scoring_engine import ScoringEngine
from scanner.decision_engine import DecisionEngine


class ScannerEngine:

    """
    Main Scanner Pipeline

    Raw Market Data
            ↓
    Filter Engine
            ↓
    Scoring Engine
            ↓
    Decision Engine
            ↓
    Ranked Opportunities
    """

    def __init__(self):

        self.filter_engine = FilterEngine()

        self.scoring_engine = ScoringEngine()

        self.decision_engine = DecisionEngine()

    # --------------------------------------------------

    def run(

            self,

            current_df,

            previous_df=None,

            market_status="NEUTRAL"

    ):

        df = current_df.copy()

        # ------------------------------------------

        # Step 1
        # Mandatory Filters

        df = self.filter_engine.apply(df)

        if len(df) == 0:

            return df

        # ------------------------------------------

        # Step 2
        # Score Everything

        df = self.scoring_engine.process(df)

        # ------------------------------------------

        # Step 3
        # Final Decision

        df = self.decision_engine.process(df)

        # ------------------------------------------

        # Step 4
        # Ranking

        df = df.sort_values(

            by=[

                "total_score",

                "confidence"

            ],

            ascending=False

        )

        df.reset_index(

            drop=True,

            inplace=True

        )

        df["rank"] = df.index + 1

        return df
