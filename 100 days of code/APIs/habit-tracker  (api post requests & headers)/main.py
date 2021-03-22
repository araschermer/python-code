import requests
from datetime import datetime

TOKEN = ""
USERNAME = ""
HABIT_ID = ""
PROJECT_NAME = ""
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

post_endpoint = f"{graph_endpoint}/{HABIT_ID}"

headers = {
    "X-USER-TOKEN": TOKEN
}


# Creating a new user account
def create_account(token, username, url):
    user_parameters = {
        "token": token,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    post_response = requests.post(url = url, json = user_parameters)
    print(post_response.text)
    return post_response.text


create_account(token = TOKEN, username = USERNAME, url = pixela_endpoint)


# create a new project (with a graph)
def create_habit(habit_id: str, project_name: str, url: str, headers: dict):
    graph_config = {
        "id": habit_id,
        "name": project_name,
        "unit": "hours",
        "type": "float",
        "color": "momiji"
    }

    graph_response = requests.post(url = url, json = graph_config, headers = headers)
    graph_url = f"{url}/{HABIT_ID}.html"
    print(f"{graph_response.text}\nCheck the Pixel here: {graph_url}")
    return graph_response.text


create_habit(habit_id = HABIT_ID, project_name = PROJECT_NAME, url = graph_endpoint, headers = headers)


# create post request
def post_data(headers: dict, day="YYYYMMDD"):
    if day == "YYYYMMDD":
        # year = datetime.now().year
        # month = datetime.now().month
        # day = datetime.now().day
        # if month < 10:
        #     month = f"0{month}"
        # today = f"{year}{month}{day}"
        # ALTERNATIVE solution for  today's date
        now = datetime.now()
        day = now.strftime("%Y%m%d")
    post_request_body = {
        "date": day,
        "quantity": input("How many hours did you code today?"),
    }
    post_request = requests.post(url = post_endpoint, json = post_request_body, headers = headers)
    print(post_request.text)
    return post_request.text


post_data(headers = headers)


# Update today's pixels
def update_pixels(headers, day="YYYYMMDD", quantity=""):
    url = f"{post_endpoint}/{day}"
    if day == "YYYYMMDD":
        now = datetime.now()
        day = now.strftime("%Y%m%d")
        url = f"{post_endpoint}/{day}"
    if quantity == "":
        quantity = input("How many hours did you code today?")
    new_data = {
        "quantity": quantity
    }
    post_request = requests.put(url = url, json = new_data, headers = headers)
    print(post_request.text)
    return post_request.text


update_pixels(headers = headers)


# delete pixel data
def delete_day_data(headers, day="YYYYMMDD"):
    url = f"{post_endpoint}/{day}"
    if day == "YYYYMMDD":
        now = datetime.now()
        day = now.strftime("%Y%m%d")
        url = f"{post_endpoint}/{day}"
    delete_response = requests.delete(url = url, headers = headers)
    print(delete_response.text)
delete_day_data(headers = headers)
