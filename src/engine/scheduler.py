import time


class Scheduler:

    def __init__(self, fn, interval):

        self.fn = fn

        self.interval = interval

    def run(self):

        while True:

            self.fn()

            time.sleep(self.interval)
