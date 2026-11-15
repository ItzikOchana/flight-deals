from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
sheet_data = data_manager.get_response_data()

# fill in the airport codes that are missing in the sheet
if sheet_data and sheet_data[0]["iataCode"] == "":
    flight_search = FlightSearch()
    for row in sheet_data:
        code = flight_search.get_destination_code(row["city"])
        if code:
            row["iataCode"] = code

    data_manager.destination_data = sheet_data
    data_manager.update_iata_code()
