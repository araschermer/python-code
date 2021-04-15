import os
from twilio.rest import Client
from get_stock_news import get_news
from get_stock_updates import get_stock_latest_info


def send_messages(stock: str, company_name: str, number_of_messages):
    for article in get_news(company_name=company_name, number_or_articles=number_of_messages):
        client = Client(os.environ.get("TWILIO_ACCOUNT_SID"), os.environ.get("TWILIO_AUTH_TOKEN"))
        message_body = f"\n{company_name}: {get_stock_latest_info(stock)}\n {article}"
        message = client.messages.create(
            body=message_body, from_=os.environ.get("TWILIO_SENDER_NUMBER"),
            to=os.environ.get("RECEIVER_NUMBER")
        )
        print(message.feedback)
