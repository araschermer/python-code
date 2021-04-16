import os
import requests
from flight_data import FlightData

FLIGHT_SEARCH_API_KEY = os.environ.get('FLIGHT_SEARCH_API_KEY')
FLIGHT_SEARCH_ENDPOINT = "https://tequila-api.kiwi.com"


class FlightSearch:

    def get_destination_code(self, destination):
        # print("get destination codes triggered")
        location_endpoint = f"{FLIGHT_SEARCH_ENDPOINT}/locations/query"
        headers = {"apikey": FLIGHT_SEARCH_API_KEY}
        query_params = {"term": destination, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query_params)
        results = response.json()["locations"]
        destination_code = results[0]["code"]
        return destination_code

    def search_deals(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": FLIGHT_SEARCH_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "EUR"
        }

        response = requests.get(
            url=f"{FLIGHT_SEARCH_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            start_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: €{flight_data.price}")
        return flight_data # contains   many attributes such as price, origin_city, origin_airport, ... etc
