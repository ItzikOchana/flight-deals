import os
from pprint import pprint

import requests
from dotenv import load_dotenv

load_dotenv()

SHEET_URL = os.getenv("SHEET_URL_GET")
AUTH = os.getenv("AUTH")

if not SHEET_URL or not AUTH:
    raise SystemExit("Missing SHEET_URL_GET or AUTH. Copy .env.example to .env and fill in your values.")

headers = {
    "Authorization": f"Basic {AUTH}"
}


class DataManager:
    """Reads the flight prices sheet (Sheety) and writes back the IATA codes."""

    def __init__(self):
        self.auth = headers
        self.destination_data = []
        self.sheet_data = []

    def get_response_data(self):
        response = requests.get(url=SHEET_URL, headers=self.auth)
        response.raise_for_status()
        self.sheet_data = response.json()["prices"]
        return self.sheet_data

    def update_iata_code(self):
        for row in self.destination_data:
            if not row["iataCode"]:
                continue
            new_data = {
                "price": {
                    "iataCode": row["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEET_URL}/{row['id']}", headers=self.auth, json=new_data)
            response.raise_for_status()

        pprint(self.destination_data)
