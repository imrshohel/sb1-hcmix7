import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
import uuid

class LicenseManager:
    def __init__(self):
        self.credentials = self._load_credentials()
        self.service = build('sheets', 'v4', credentials=self.credentials)
        self.sheet = self.service.spreadsheets()
        self.SPREADSHEET_ID = 'your_spreadsheet_id'  # Replace with your actual spreadsheet ID
        self.RANGE_NAME = 'Sheet1!A:D'

    def _load_credentials(self):
        credentials_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'credentials.json')
        return service_account.Credentials.from_service_account_file(
            credentials_path,
            scopes=["https://www.googleapis.com/auth/spreadsheets"]
        )

    def _get_hardware_id(self):
        return str(uuid.getnode())  # This uses the MAC address as a hardware ID

    def validate_license(self, license_key):
        hardware_id = self._get_hardware_id()
        result = self.sheet.values().get(spreadsheetId=self.SPREADSHEET_ID, range=self.RANGE_NAME).execute()
        rows = result.get('values', [])

        for i, row in enumerate(rows):
            if row[0] == license_key:
                if len(row) > 1 and row[1] == hardware_id:
                    return True  # License valid for this hardware
                elif len(row) == 1:
                    # Activate license for this hardware
                    row.extend([hardware_id, "Active", str(datetime.now())])
                    self.sheet.values().update(
                        spreadsheetId=self.SPREADSHEET_ID,
                        range=f'Sheet1!A{i + 1}:D',
                        valueInputOption="RAW",
                        body={"values": [row]}
                    ).execute()
                    return True
                else:
                    return False  # License key already in use
        return False  # License key not found

    def deactivate_license(self, license_key):
        result = self.sheet.values().get(spreadsheetId=self.SPREADSHEET_ID, range=self.RANGE_NAME).execute()
        rows = result.get('values', [])

        for i, row in enumerate(rows):
            if row[0] == license_key:
                row = [row[0]]  # Keep only the license key
                self.sheet.values().update(
                    spreadsheetId=self.SPREADSHEET_ID,
                    range=f'Sheet1!A{i + 1}:D',
                    valueInputOption="RAW",
                    body={"values": [row]}
                ).execute()
                return True
        return False  # License key not found