from settings import (
    READY_SCORE,
    BREAKOUT_SCORE
)


class DecisionEngine:

    """
    Final Decision Engine

    Converts analytics into:

    WATCH
    READY
    BREAKOUT
    IGNORE
    """

    def __init__(self):

        pass

    # -------------------------------------------------------

    def decision(self, row):

        score = row["total_score"]

        confidence = row["confidence"]

        rs = row.get("relative_strength_score", 0)

        volume = row.get("volume_acceleration_score", 0)

        sector = row.get("sector_strength_score", 0)

        breakout = row.get("breakout_score", 0)

        smart = row.get("smart_money_score", 0)

        move = row.get("move_from_open", 0)

        # ---------------------------------------------

        if abs(move) > 1.5:

            return "IGNORE"

        # ---------------------------------------------

        if (

            score >= BREAKOUT_SCORE

            and confidence >= 85

            and rs >= 80

            and volume >= 80

            and sector >= 80

            and breakout >= 80

            and smart >= 75

        ):

            return "BREAKOUT"

        # ---------------------------------------------

        if (

            score >= READY_SCORE

            and confidence >= 80

            and rs >= 70

            and volume >= 70

            and sector >= 70

        ):

            return "READY"

        # ---------------------------------------------

        if score >= 65:

            return "WATCH"

        return "IGNORE"

    # -------------------------------------------------------

    def process(self, dataframe):

        df = dataframe.copy()

        df["decision"] = df.apply(

            self.decision,

            axis=1

        )

        return df
