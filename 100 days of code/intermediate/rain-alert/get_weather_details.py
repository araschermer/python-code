import requests
API_KEY = "" # from openweathermap.org
Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    "lat": 52.520008, # latitude of berlin
    "lon": 13.404954,# longitude of berlin
    "appid": API_KEY,  # openweathermap.org provided API_KEY
}
response = requests.get(Endpoint, params = weather_params)
data = response.json()
hourly_data = data["hourly"]
will_rain = False
for hourly_info in hourly_data[0:12]: # check the weather info in the first 12 hours
    hourly_weather = hourly_info["weather"]
    weather_status_id = hourly_weather[0]["id"]
    if weather_status_id < 700:
        will_rain = True
