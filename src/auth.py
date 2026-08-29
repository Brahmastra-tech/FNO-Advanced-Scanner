class UpstoxAuth:

    def __init__(self):
        self.access_token = None

    def login(self):
        """
        Generate or refresh Upstox token
        """
        pass

    def get_token(self):
        return self.access_token
