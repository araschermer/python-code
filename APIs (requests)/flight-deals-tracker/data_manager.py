import os
import requests

SHEET_ENDPOINT = os.environ.get('SHEET_ENDPOINT')
SHEET__BEARER_AUTH_TOKEN = os.environ.get('SHEET__BEARER_AUTH_TOKEN')
authentication_headers = {
    "Authorization": f"Bearer {SHEET__BEARER_AUTH_TOKEN}"
}


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        """Returns the destination cities from City column in the the google sheet"""
        # use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEET_ENDPOINT, headers=authentication_headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    #  PUT request and use the entry id from sheet_data
    # to update the Google Sheet with the IATA codes.
    def update_destination_codes(self):
        """updates the IATA Code column in the google sheet with the IATA code of each city in the City column"""
        for entry in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": entry["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEET_ENDPOINT}/{entry['id']}",
                json=new_data,
                headers=authentication_headers
            )
            print(response.text)
