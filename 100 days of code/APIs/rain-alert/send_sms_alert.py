import os
from get_weather_details import will_rain
from twilio.rest import Client
from twilio.http.http_client import\
    TwilioHttpClient  # if the script is to be automatically executed on a pythonanywhere

TWILIO_SENDER_NUMBER = ""  # Twilio provided "sender" number
TWILIO_VERIFIED_RECEIVER_NUMBER = ""  # a verified number for testing the code
# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "os.environ['TWILIO_ACCOUNT_SID']"  # replace this string with the twilio account_sid
auth_token = "os.environ['TWILIO_AUTH_TOKEN']"  # replace this string with the twilio auth_token
if will_rain:
    # proxy_client = TwilioHttpClient()  # script is to be automatically executed by pythonanywhere
    # proxy_client.session.proxies = {"https": os.environ["https_proxy"]} #script is to be executed by pythonanywhere
    client = Client(account_sid, auth_token)
    # client = Client(account_sid, auth_token, http_client = proxy_client) #script is to be executed by pythonanywhere
    send_message = client.messages\
        .create(body = "It's going to rain today, Remember to bring an Umbrella ☂️.",
                from_ = TWILIO_SENDER_NUMBER, to = TWILIO_VERIFIED_RECEIVER_NUMBER)
    print(send_message.status)  # send the message and return "queued": sent successfully
    print(send_message.sid)
