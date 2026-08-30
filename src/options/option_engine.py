from options.option_chain import OptionChain
from options.oi_analyzer import OIAnalyzer


class OptionEngine:
    """
    Central Options Analytics Engine

    Pipeline:

    Option Chain
          ↓
    OI Analyzer
          ↓
    PCR (future)
          ↓
    Greeks (future)
          ↓
    Max Pain (future)
          ↓
    Final Option Score
    """

    def __init__(self):

        self.chain = OptionChain()

        self.oi = OIAnalyzer()

    # ------------------------------------------------------

    def analyze(

            self,

            instrument_key,

            expiry_date

    ):

        option_chain = self.chain.fetch(

            instrument_key,

            expiry_date

        )

        oi_df = self.oi.analyze(

            option_chain

        )

        oi_summary = self.oi.summary(

            oi_df

        )

        return {

            "option_chain": option_chain,

            "oi_dataframe": oi_df,

            "support": oi_summary["support"],

            "resistance": oi_summary["resistance"],

            "max_call_oi": oi_summary["max_call_oi"],

            "max_put_oi": oi_summary["max_put_oi"],

            # Future Modules
            "pcr": None,

            "max_pain": None,

            "writer_bias": None,

            "greeks": None,

            "option_score": None

        }

    # ------------------------------------------------------

    def support(

            self,

            instrument_key,

            expiry_date

    ):

        return self.analyze(

            instrument_key,

            expiry_date

        )["support"]

    # ------------------------------------------------------

    def resistance(

            self,

            instrument_key,

            expiry_date

    ):

        return self.analyze(

            instrument_key,

            expiry_date

        )["resistance"]
