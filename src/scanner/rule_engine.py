import pandas as pd


class RuleEngine:
    """
    Rule Engine

    Applies scanner rules and assigns points.

    Final Output

    - rule_score
    - passed_rules
    - failed_rules
    - scanner_stage
    """

    def __init__(self):

        self.weights = {

            "relative_strength": 20,
            "volume": 20,
            "sector": 15,
            "smart_money": 20,
            "compression": 5,
            "structure": 10,
            "breakout": 10

        }

    def calculate(self, df, market_status="NEUTRAL"):

        market = df.copy()

        rule_score = []

        passed_rules = []

        failed_rules = []

        stage = []

        for _, row in market.iterrows():

            score = 0

            passed = []

            failed = []

            # ---------------------------------
            # Relative Strength
            # ---------------------------------

            if row.get("rs_score", 0) >= 2:

                score += self.weights["relative_strength"]

                passed.append("RS")

            else:

                failed.append("RS")

            # ---------------------------------
            # Volume
            # ---------------------------------

            if row.get("rvol", 0) >= 1.5:

                score += self.weights["volume"]

                passed.append("RVOL")

            else:

                failed.append("RVOL")

            # ---------------------------------
            # Sector
            # ---------------------------------

            if row.get("sector_strength", 0) >= 2:

                score += self.weights["sector"]

                passed.append("SECTOR")

            else:

                failed.append("SECTOR")

            # ---------------------------------
            # Smart Money
            # ---------------------------------

            if row.get("smart_money_score", 0) >= 70:

                score += self.weights["smart_money"]

                passed.append("SMART")

            else:

                failed.append("SMART")

            # ---------------------------------
            # Compression
            # ---------------------------------

            if row.get("compression_score", 0) >= 80:

                score += self.weights["compression"]

                passed.append("COMP")

            else:

                failed.append("COMP")

            # ---------------------------------
            # Structure
            # ---------------------------------

            if row.get("structure_score", 0) >= 80:

                score += self.weights["structure"]

                passed.append("STRUCT")

            else:

                failed.append("STRUCT")

            # ---------------------------------
            # Breakout
            # ---------------------------------

            if row.get("breakout_score", 0) >= 75:

                score += self.weights["breakout"]

                passed.append("BREAKOUT")

            else:

                failed.append("BREAKOUT")

            # ---------------------------------
            # Market Context
            # ---------------------------------

            if market_status == "VERY BEARISH":

                score -= 20

            elif market_status == "BEARISH":

                score -= 10

            elif market_status == "BULLISH":

                score += 5

            elif market_status == "VERY BULLISH":

                score += 10

            score = max(0, min(score, 100))

            # ---------------------------------
            # Stage
            # ---------------------------------

            if score >= 90:

                signal = "BREAKOUT"

            elif score >= 80:

                signal = "READY"

            elif score >= 65:

                signal = "WATCH"

            else:

                signal = "IGNORE"

            rule_score.append(score)

            passed_rules.append(", ".join(passed))

            failed_rules.append(", ".join(failed))

            stage.append(signal)

        market["rule_score"] = rule_score

        market["passed_rules"] = passed_rules

        market["failed_rules"] = failed_rules

        market["scanner_stage"] = stage

        return market

    def opportunities(self, df):

        return (

            df

            [

                df["scanner_stage"] != "IGNORE"

            ]

            .sort_values(

                by="rule_score",

                ascending=False

            )

        )

    def breakout_candidates(self, df):

        return (

            df

            [

                df["scanner_stage"] == "BREAKOUT"

            ]

            .sort_values(

                by="rule_score",

                ascending=False

            )

        )

    def ready_candidates(self, df):

        return (

            df

            [

                df["scanner_stage"] == "READY"

            ]

            .sort_values(

                by="rule_score",

                ascending=False

            )

        )
