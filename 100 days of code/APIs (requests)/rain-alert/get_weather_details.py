import os

import requests

API_KEY = os.environ["API_KEY"]  # from openweathermap.org
Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    "lat": 52.520008,  # latitude of berlin
    "lon": 13.404954,  # longitude of berlin
    "appid": API_KEY,  # openweathermap.org provided API_KEY
}
response = requests.get(Endpoint, params=weather_params)
print(f"Response:{response}")  # returns Response:<Response [200]> in case of a success request
response.raise_for_status()
data = response.json()
hourly_data = data["hourly"]  # to retrieve te 48 data entries of the next 48 hours weather forecast

print(f"DATA:{data['hourly'][0]}")
# example of one hour weather forecast:
# DATA:[{'dt': 1618502400, 'temp': 280.67, 'feels_like': 277.33, 'pressure': 1026, 'humidity': 43,
# 'dew_point': 269.39, 'uvi': 0.38, 'clouds': 20, 'visibility': 10000, 'wind_speed': 5.76, 'wind_deg': 8,
# 'wind_gust': 9.25, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}],

will_rain = False
for hourly_info in hourly_data[0:12]:  # check the weather info in the first 12 hours
    hourly_weather = hourly_info["weather"]
    weather_status_id = hourly_weather[0]["id"]
    # https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
    if 200 <= weather_status_id < 700:  # Group 5xx: Rain
        print("Rain")
        will_rain = True
