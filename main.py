from pprint import pprint

from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
sheet_data = data_manager.get_response_data()
pprint(sheet_data)

# Fill in the IATA code for every row that does not have one yet.
# Rows are only updated when a real code was found, so the sheet is never overwritten with placeholders.
if sheet_data and sheet_data[0]["iataCode"] == "":
    flight_search = FlightSearch()
    for row in sheet_data:
        code = flight_search.get_destination_code(row["city"])
        if code:
            row["iataCode"] = code

    data_manager.destination_data = sheet_data
    data_manager.update_iata_code()
