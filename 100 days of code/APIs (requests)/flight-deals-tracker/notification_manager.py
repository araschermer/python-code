import os
from twilio.rest import Client

ACCOUNT_SID = os.environ.get('ACCOUNT_SID')
AUTH_TOKEN = os.environ.get('AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.environ.get('PHONE_NUMBER')
RECEIVER_NUMBER = os.environ.get('RECEIVER_NUMBER')


class NotificationManager:

    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=RECEIVER_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
