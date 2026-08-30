from settings import (
    MIN_PRICE,
    MIN_DAILY_TURNOVER,
    MIN_AVG_VOLUME,
    MAX_MOVE_FROM_OPEN
)


class FilterEngine:

    """
    Mandatory filters.

    Stocks failing any filter
    never reach the scoring engine.
    """

    # -----------------------------------------------------

    def universe_filter(self, df):

        df = df.copy()

        if "price" in df.columns:
            df = df[df["price"] >= MIN_PRICE]
        elif "close" in df.columns:
            df = df[df["close"] >= MIN_PRICE]

        if "turnover" in df.columns:
            df = df[df["turnover"] >= MIN_DAILY_TURNOVER]

        if "avg_volume" in df.columns:
            df = df[df["avg_volume"] >= MIN_AVG_VOLUME]

        if "fo_ban" in df.columns:
            df = df[df["fo_ban"] == False]

        return df

    # -----------------------------------------------------

    def opening_filter(self, df):

        if "opening_quality_score" not in df.columns:
            return df

        return df[
            df["opening_quality_score"] >= 70
        ]

    # -----------------------------------------------------

    def move_from_open_filter(self, df):

        if "move_from_open" not in df.columns:
            return df

        return df[
            abs(df["move_from_open"])
            <= MAX_MOVE_FROM_OPEN
        ]

    # -----------------------------------------------------

    def relative_strength_filter(self, df):

        if "relative_strength_score" not in df.columns:
            return df

        return df[
            df["relative_strength_score"] >= 60
        ]

    # -----------------------------------------------------

    def sector_filter(self, df):

        if "sector_strength_score" not in df.columns:
            return df

        return df[
            df["sector_strength_score"] >= 60
        ]

    # -----------------------------------------------------

    def volume_filter(self, df):

        if "rvol" in df.columns:
            df = df[df["rvol"] >= 1.5]

        if "volume_acceleration_score" in df.columns:
            df = df[
                df["volume_acceleration_score"] >= 60
            ]

        return df

    # -----------------------------------------------------

    def smart_money_filter(self, df):

        if "smart_money_score" not in df.columns:
            return df

        return df[
            df["smart_money_score"] >= 60
        ]

    # -----------------------------------------------------

    def compression_filter(self, df):

        if "compression_score" not in df.columns:
            return df

        return df[
            df["compression_score"] >= 60
        ]

    # -----------------------------------------------------

    def structure_filter(self, df):

        if "structure_score" not in df.columns:
            return df

        return df[
            df["structure_score"] >= 60
        ]

    # -----------------------------------------------------

    def market_filter(self, df):

        if "market_context_score" not in df.columns:
            return df

        return df[
            df["market_context_score"] >= 60
        ]

    # -----------------------------------------------------

    def apply(self, dataframe):

        df = dataframe.copy()

        df = self.universe_filter(df)

        df = self.opening_filter(df)

        df = self.move_from_open_filter(df)

        df = self.relative_strength_filter(df)

        df = self.sector_filter(df)

        df = self.volume_filter(df)

        df = self.smart_money_filter(df)

        df = self.compression_filter(df)

        df = self.structure_filter(df)

        df = self.market_filter(df)

        return df.reset_index(drop=True)
