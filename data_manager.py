from pprint import pprint
from dotenv import *
import os
import requests
load_dotenv()


PUT_SHEET_URL = os.getenv("SHEET_URL_GET")

# json_conifg ={
#     "price":{
#     "iataCode":2
#
#
#     }
#
# }












headers ={

"Authorization": f"Basic {os.getenv("AUTH")}"
}

class DataManager:

    def __init__(self):
        self.auth=headers
        self.destination_data = {}



    def get_response_data(self):
        response = requests.get(url=os.getenv("SHEET_URL_GET"),headers=self.auth)
        self.sheet_data = response.json()["prices"]
        return self.sheet_data

    def update_iata_code(self):
        for i in self.destination_data:
            new_updated_data ={
                "price":{
                    "iataCode": i["iataCode"]

                }


            }
            response_put_sheet = requests.put(url=f"{PUT_SHEET_URL}/{i["id"]}",headers=self.auth,json=new_updated_data )

        pprint(self.destination_data)