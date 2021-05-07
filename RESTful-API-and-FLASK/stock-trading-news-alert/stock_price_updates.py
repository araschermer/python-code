import os

import requests

STOCK_ENDPOINT = "https://www.alphavantage.co/query"


def get_stock_latest_info(stock: str):
    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock,
        "apikey": os.environ.get("STOCK_API_KEY")
    }
    response = requests.get(STOCK_ENDPOINT, params=stock_params)
    # print(response.json())
    data = response.json()["Time Series (Daily)"]
    data_list = [value for (key, value) in data.items()]
    # getting yesterday's data:
    yesterday_data = data_list[0]
    yesterday_closing_price = yesterday_data["4. close"]
    # getting the day before yesterday's data:
    day_before_yesterday_data = data_list[1]
    day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
    difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
    direction = ""
    if difference > 0.0:
        direction = '🔼'
    elif difference < 0.0:
        direction = "🔻"
    abs_difference = abs(difference)
    latest_closing_price_difference_percentage = round((abs_difference / float(yesterday_closing_price) * 100))
    return f"{latest_closing_price_difference_percentage} {direction}"
