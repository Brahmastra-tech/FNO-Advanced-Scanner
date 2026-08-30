from datetime import datetime, time


class MarketClock:

    MARKET_OPEN = time(9, 15)

    OBSERVATION_END = time(9, 25)

    SCANNER_END = time(15, 20)

    MARKET_CLOSE = time(15, 30)

    # -----------------------------------------

    def now(self):

        return datetime.now().time()

    # -----------------------------------------

    def is_market_open(self):

        t = self.now()

        return self.MARKET_OPEN <= t <= self.MARKET_CLOSE

    # -----------------------------------------

    def is_observation(self):

        t = self.now()

        return self.MARKET_OPEN <= t < self.OBSERVATION_END

    # -----------------------------------------

    def is_scanner(self):

        t = self.now()

        return self.OBSERVATION_END <= t < self.SCANNER_END

    # -----------------------------------------

    def is_closing(self):

        t = self.now()

        return self.SCANNER_END <= t <= self.MARKET_CLOSE

    # -----------------------------------------

    def is_after_market(self):

        t = self.now()

        return t > self.MARKET_CLOSE

    # -----------------------------------------

    def current_phase(self):

        if self.is_observation():

            return "OBSERVATION"

        if self.is_scanner():

            return "SCANNER"

        if self.is_closing():

            return "CLOSING"

        if self.is_after_market():

            return "AFTER_MARKET"

        return "MARKET_CLOSED"
