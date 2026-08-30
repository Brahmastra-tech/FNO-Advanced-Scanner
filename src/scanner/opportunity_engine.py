import pandas as pd


class OpportunityEngine:
    """
    Converts scanner output into
    ranked opportunities.
    """

    def __init__(self):
        pass

    # ---------------------------------------------------

    def classify(self, row):

        score = row["total_score"]

        decision = row["decision"]

        confidence = row["confidence"]

        if decision == "BREAKOUT":

            return "A+"

        if decision == "READY" and confidence >= 90:

            return "A"

        if decision == "READY":

            return "B+"

        if decision == "WATCH":

            return "B"

        return "IGNORE"

    # ---------------------------------------------------

    def priority(self, row):

        score = row["total_score"]

        confidence = row["confidence"]

        return round(

            score * 0.60 +

            confidence * 0.40,

            2

        )

    # ---------------------------------------------------

    def process(self, dataframe):

        df = dataframe.copy()

        df["opportunity"] = df.apply(

            self.classify,

            axis=1

        )

        df["priority_score"] = df.apply(

            self.priority,

            axis=1

        )

        df = df.sort_values(

            by=[

                "priority_score",

                "total_score"

            ],

            ascending=False

        )

        df.reset_index(

            drop=True,

            inplace=True

        )

        df["scanner_rank"] = df.index + 1

        return df
