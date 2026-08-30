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

    # ---------------------------------------------------------
    # Create worksheet if it doesn't exist
    # ---------------------------------------------------------

    def get_or_create_sheet(
        self,
        sheet_name,
        rows=5000,
        cols=60
    ):

        try:

            worksheet = self.sheet.worksheet(sheet_name)

        except gspread.WorksheetNotFound:

            worksheet = self.sheet.add_worksheet(
                title=sheet_name,
                rows=rows,
                cols=cols
            )

        return worksheet

    # ---------------------------------------------------------
    # Replace entire worksheet
    # ---------------------------------------------------------

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

    # ---------------------------------------------------------
    # Append rows (used for Alert History)
    # ---------------------------------------------------------

    def append_dataframe(
        self,
        dataframe,
        sheet_name
    ):

        ws = self.get_or_create_sheet(sheet_name)

        rows = dataframe.fillna("").values.tolist()

        if rows:

            # Add header if sheet is empty
            if not ws.get_all_values():

                ws.append_row(dataframe.columns.tolist())

            ws.append_rows(rows)

    # ---------------------------------------------------------
    # Stocks (Overwrite)
    # ---------------------------------------------------------

    def update_stocks(
        self,
        dataframe
    ):

        self.update_dataframe(
            dataframe,
            "Stocks"
        )

    # ---------------------------------------------------------
    # Indices (Overwrite)
    # ---------------------------------------------------------

    def update_indices(
        self,
        dataframe
    ):

        self.update_dataframe(
            dataframe,
            "Indices"
        )

    # ---------------------------------------------------------
    # Alerts (Append History)
    # ---------------------------------------------------------

    def update_alerts(
        self,
        dataframe
    ):

        self.append_dataframe(
            dataframe,
            "Alerts"
        )

    # ---------------------------------------------------------
    # Swing Scanner (Overwrite)
    # ---------------------------------------------------------

    def update_swing(
        self,
        dataframe
    ):

        self.update_dataframe(
            dataframe,
            "Swing"
        )

    # ---------------------------------------------------------
    # Generic overwrite
    # ---------------------------------------------------------

    def write(
        self,
        sheet_name,
        dataframe
    ):

        self.update_dataframe(
            dataframe,
            sheet_name
        )

    # ---------------------------------------------------------
    # Generic append
    # ---------------------------------------------------------

    def append(
        self,
        sheet_name,
        dataframe
    ):

        self.append_dataframe(
            dataframe,
            sheet_name
        )
