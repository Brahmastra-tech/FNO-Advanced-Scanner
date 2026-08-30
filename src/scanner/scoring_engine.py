import numpy as np


class ScoringEngine:

    def __init__(self):

        self.weights = {

            "relative_strength": 20,

            "volume_acceleration": 20,

            "turnover": 15,

            "sector_strength": 15,

            "compression": 10,

            "structure": 10,

            "market_context": 10

        }

    # ---------------------------------------------------------

    def calculate(self, row):

        score = 0

        score += row.get(
            "relative_strength_score", 0
        ) * self.weights["relative_strength"] / 100

        score += row.get(
            "volume_acceleration_score", 0
        ) * self.weights["volume_acceleration"] / 100

        score += row.get(
            "turnover_score", 0
        ) * self.weights["turnover"] / 100

        score += row.get(
            "sector_strength_score", 0
        ) * self.weights["sector_strength"] / 100

        score += row.get(
            "compression_score", 0
        ) * self.weights["compression"] / 100

        score += row.get(
            "structure_score", 0
        ) * self.weights["structure"] / 100

        score += row.get(
            "market_context_score", 0
        ) * self.weights["market_context"] / 100

        return round(score, 2)

    # ---------------------------------------------------------

    def confidence(self, row):

        values = [

            row.get("relative_strength_score", 0),

            row.get("volume_acceleration_score", 0),

            row.get("turnover_score", 0),

            row.get("sector_strength_score", 0),

            row.get("compression_score", 0),

            row.get("structure_score", 0),

            row.get("market_context_score", 0)

        ]

        return round(np.mean(values), 2)

    # ---------------------------------------------------------

    def stage(self, score):

        if score >= 90:

            return "BREAKOUT"

        if score >= 80:

            return "READY"

        if score >= 65:

            return "WATCH"

        return "IGNORE"

    # ---------------------------------------------------------

    def priority(self, score):

        if score >= 95:

            return "CRITICAL"

        if score >= 85:

            return "HIGH"

        if score >= 75:

            return "MEDIUM"

        return "LOW"

    # ---------------------------------------------------------

    def process(self, dataframe):

        df = dataframe.copy()

        df["total_score"] = df.apply(

            self.calculate,

            axis=1

        )

        df["confidence"] = df.apply(

            self.confidence,

            axis=1

        )

        df["scanner_stage"] = df["total_score"].apply(

            self.stage

        )

        df["priority"] = df["total_score"].apply(

            self.priority

        )

        return df
