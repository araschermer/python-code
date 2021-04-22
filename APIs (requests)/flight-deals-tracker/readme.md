<br />
<p align="center">

  <h3 align="center">FLIGHT DEALS TRACKER</h3>

  <p align="center">
    project_description
    <br />
The FLIGHT DEALS TRACKER:
To track flight offers to certain destination when an offer of a lower price than their usual price is available and send an sms notification message with the offer details.
    <br />
  </p>
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
        <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
In this project: the following APIs are used:
#####1-the Flight Search  API of kiwi, and the Sheety API are used to populate a Google Sheet with International Air Transport Association (IATA) codes for each city.
#####2-the Flight Search API is used to check for the cheapest flights from the next day up to 6 months ahead for all the cities in the Google Sheet.
#####3-If the price is lower than the lowest price listed in the Google Sheet then send an SMS to the provided and  twilio verified number with the Twilio API.
#####4-The SMS should include the departure airport IATA code, destination airport IATA code, departure city, destination city, flight price and flight dates. e.g.

[comment]: <> (##Example:)

[comment]: <> (![Alt text]&#40;example.PNG?raw=true "Title"&#41;)


### Built Using:
* [Python](Python)
* [Google sheets](Google sheets)
### Modules used:
* [requests](https://pypi.org/project/requests/)
* [twilio.rest](twilio.rest)
* [datetime](datetime)
### APIs used:
* [tequila-api](https://tequila.kiwi.com/portal/docs/tequila_api)
* [twilio api ](https://www.twilio.com/docs/sms)
* [sheety api ](https://api.sheety.co/)



<!-- GETTING STARTED -->
#Getting Started

To get a local copy up and running follow these simple steps.

### Installation
1-download the project file.\
2-install and import the `requests` module and the `twilio.rest` module .\
3- get a Bearer Authentication `TOKEN`  and the endpoint of the records sheet (`SHEET_ENDPOINT`) from [sheety](https://api.sheety.co/) and save it in the environment variables in `data_manager.py`\
######Usage: 
 ```py
 response = requests.get(url=SHEET_ENDPOINT, headers=authentication_headers)
 data = response.json()
 self.destination_data = data["prices"]
 return self.destination_data
```
4- get a private `ACCOUNT_SID`, `AUTH_TOKEN`,`TWILIO_PHONE_NUMBER`, and a verified `RECEIVER_NUMBER`  from [twilio api ](https://www.twilio.com) and save them in the environment variables in `notification_manager.py`,
 There environment variables are required to set up the API credentials to send the notification message.
######Usage: 
```py
    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=RECEIVER_NUMBER,
        )
```

5- form the [tequila-api](https://tequila-api.kiwi.com) get `FLIGHT_SEARCH_API_KEY` and  save the API key in the environment variables.
######Usage: 
     1- Getting the IATA code of the destination city 
   ```py
        location_endpoint = f"{FLIGHT_SEARCH_ENDPOINT}/locations/query"
           headers = {"apikey": FLIGHT_SEARCH_API_KEY}
           query_params = {"term": destination, "location_types": "city"}
           response = requests.get(url=location_endpoint, headers=headers, params=query_params)
   ```
    2- searching for the flight deals:
   ```py
   headers = {"apikey": FLIGHT_SEARCH_API_KEY}
   query = {
           # Query  attributes
   }
   response = requests.get(
       url=f"{FLIGHT_SEARCH_ENDPOINT}/v2/search",
       headers=headers,
       params=query,
   )
   ```
6- run the `main.py` script

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

