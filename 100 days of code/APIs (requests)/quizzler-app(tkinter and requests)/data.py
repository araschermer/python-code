import requests

AMOUNT = 10
TYPE = "boolean"
BASE_URL = f"https://opentdb.com/api.php?amount={AMOUNT}&type={TYPE}"


def get_question():
    """return a the results of the request to the opentdb API"""
    response = requests.get(url=BASE_URL)
    # to handle errors
    response.raise_for_status()
    # get the json response
    data = response.json()
    # get the questions data from the results key
    question_data = data["results"]
    return question_data


# Alternative Solution:
# parameters = {
#     "amount": 10,
#     "type": "boolean"
# }
#
# response = requests.get(url=BASE_URL, params=parameters)
# response.raise_for_status()
# data = response.json()
# question_data = data["results"]
