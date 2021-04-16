import datetime
import os
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()
ORIGIN_CITY_IATA = os.environ.get("ORIGIN_CITY_IATA")

#  check if sheet_data  doesn't contain any values for the "iataCode" key.
#  If so, then get the IATA Codes from the flight search get_destination_code method and update the corresponding column
#  in the Google Sheet.
if sheet_data[0]["iataCode"] == "":
    for entry in sheet_data:
        entry["iataCode"] = flight_search.get_destination_code(entry["city"])
    print(f"sheet_data:\n {sheet_data}")
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

for destination in sheet_data:
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    six_month_from_today = datetime.date.today() + datetime.timedelta(days=30 * 6)
    flight_data = flight_search.search_deals(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today)
    if flight_data and int(flight_data.price) < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight_data.price} to fly "
                    f"from {flight_data.origin_city}-{flight_data.origin_airport} "
                    f"to {flight_data.destination_city}-{flight_data.destination_airport},"
                    f" from {flight_data.out_date} to {flight_data.return_date}. "
        )
