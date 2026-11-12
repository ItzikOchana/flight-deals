#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from pprint import pprint
from dotenv import *
import os
import requests
load_dotenv()
from data_manager import DataManager

data_manager_obj = DataManager()
sheet_data = data_manager_obj.get_response_data()
pprint(sheet_data)



if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])



    data_manager_obj.destination_data = sheet_data
    data_manager_obj.update_iata_code()



