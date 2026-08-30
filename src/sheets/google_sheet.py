import gspread
import pandas as pd

from google.oauth2.service_account import Credentials


class GoogleSheet:

    def __init__(

            self,

            credentials_file,

            spreadsheet_name

    ):

        scope = [

            "https://www.googleapis.com/auth/spreadsheets",

            "https://www.googleapis.com/auth/drive"

        ]

        creds = Credentials.from_service_account_file(

            credentials_file,

            scopes=scope

        )

        client = gspread.authorize(creds)

        self.sheet = client.open(spreadsheet_name)

    # ---------------------------------------------------

    def get_or_create_sheet(

            self,

            sheet_name,

            rows=5000,

            cols=50

    ):

        try:

            worksheet = self.sheet.worksheet(sheet_name)

        except Exception:

            worksheet = self.sheet.add_worksheet(

                title=sheet_name,

                rows=rows,

                cols=cols

            )

        return worksheet

    # ---------------------------------------------------

    def update_dataframe(

            self,

            dataframe,

            sheet_name

    ):

        ws = self.get_or_create_sheet(sheet_name)

        ws.clear()

        values = [

            dataframe.columns.tolist()

        ] + dataframe.fillna("").values.tolist()

        ws.update(values)

    # ---------------------------------------------------

    def update_stocks(

            self,

            dataframe

    ):

        self.update_dataframe(

            dataframe,

            "Stocks"

        )

    # ---------------------------------------------------

    def update_indices(

            self,

            dataframe

    ):

        self.update_dataframe(

            dataframe,

            "Indices"

        )

    # ---------------------------------------------------

    def update_alerts(

            self,

            dataframe

    ):

        self.update_dataframe(

            dataframe,

            "Alerts"

        )

    # ---------------------------------------------------

    def update_swing(

            self,

            dataframe

    ):

        self.update_dataframe(

            dataframe,

            "Swing"

        )
