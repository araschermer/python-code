import requests
from datetime import datetime
import os

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
Base_URL = "https://developer.nutritionix.com/login"
APPLICATION_ID = os.environ.get("APPLICATION_ID")
APPLICATION_KEY = os.environ.get("APPLICATION_KEY")
TOKEN = os.environ.get("TOKEN")
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")
USER_GENDER = os.environ.get("USER_GENDER")
USER_WEIGHT = os.environ.get("USER_WEIGHT")
USER_HEIGHT = os.environ.get("USER_HEIGHT")
USER_AGE = os.environ.get("USER_AGE")

headers = {
    "x-app-id": APPLICATION_ID,
    "x-app-key": APPLICATION_KEY,
    "x-remote-user-id": "0",
}
# Setup API Credentials
response = requests.get(url = Base_URL, headers = headers)
print(response.status_code)
print(response.text)

#  create unauthenticated post request
query_params = {
    "query": input("Tell me which exercises did you do?"),
    "gender": f"{USER_GENDER}",
    "weight_kg": float(USER_WEIGHT),
    "height_cm": int(USER_HEIGHT),
    "age": int(USER_AGE)
}
post_response = requests.post(url = exercise_endpoint, json = query_params, headers = headers)
print(post_response.json())
results = post_response.json()
print(post_response.status_code)

#  writing the recorded results into sheet
sheet_endpoint = f"https://api.sheety.co/{SHEET_ENDPOINT}/workoutTracking/workouts"
date = datetime.now()
Date = date.strftime("%d/%m/%Y")
Time = date.strftime("%X")

for exercise in results["exercises"]:
    nutritionix_exercise_data = {
        "workout": {
            "date": Date,
            "time": Time,
            "exercise": exercise["name"].item(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    print(nutritionix_exercise_data)

    # sending post request with no authentication
    # sheety_response = requests.post(url = sheet_endpoint, json = nutritionix_exercise_data)
    # print(sheety_response.status_code)

    # send post request with Bearer authentication
    bearer_headers = {
        "Authorization": f"Bearer {TOKEN}"
    }
    sheet_authentication_response = requests.post(
        sheet_endpoint,
        json = nutritionix_exercise_data,
        headers = bearer_headers
    )
    print(sheet_authentication_response.status_code)
    print(sheet_authentication_response.json())
