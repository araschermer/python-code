# https://sunrise-sunset.org/api
import requests
from datetime import datetime
import smtplib

SENDER_EMAIL = ""  # to fill
SENDER_PASSWORD = ""  # to fill
RECEIVER_EMAIL = ""  # to fill
LONGITUDE = 13.411440 # to fill
LATITUDE = 52.523430 # to fill
# get current location # https://www.latlong.net/ #
parameters = {
    "lat": LATITUDE,
    "lng": LONGITUDE,
    "formatted": 0
}


def get_smtp(sender_email):
    if "yahoo" in sender_email.lower():
        # SMTP_YAHOO = "smtp.mail.yahoo.com"
        return "smtp.mail.yahoo.com"
    elif "gmail" in sender_email.lower():
        # SMTP_GMAIL = "smtp.gmail.com"
        return "smtp.gmail.com"
    elif "hotmail" in sender_email.lower():
        # SMTP_HOTMAIL = "smtp.live.com"
        return "smtp.live.com"
    else:
        print("SMTP for your email address is not defined")


def send_email(sender_email, password, receiver_email, subject="Reminder", message="Sunrise and Sunset time reminder"):
    with smtplib.SMTP(get_smtp(sender_email)) as connection:
        connection.starttls()
        connection.login(user = sender_email, password = password)
        connection.sendmail(from_addr = sender_email, to_addrs = receiver_email,
                            msg = f"Subject: {subject}\n\n{message}")

link = "https://api.sunrise-sunset.org/json"
response = requests.get(link, params = parameters)
response.raise_for_status()
data = response.json()
# to convert the sunrise format from :sunrise:2021-03-14T05:20:57+00:00 to 05:20:57
sunrise = data["results"]['sunrise'].split('T')[1].split('+')[0]
sunset = data["results"]['sunset'].split('T')[1].split('+')[0]
sunrise_hour = sunrise.split(':')[0]
sunset_hour = sunset.split(':')[0]
current_time = datetime.now()  # # 2021-03-14 17:49:34.546252
current_hour = current_time.hour

if current_hour == sunrise_hour:
    send_email(sender_email = SENDER_EMAIL, password = SENDER_PASSWORD, receiver_email = RECEIVER_EMAIL,
               subject = "Sunrise reminder", message = "It's sunrise time")
elif current_hour == sunset_hour:
    send_email(sender_email = SENDER_EMAIL, password = SENDER_PASSWORD, receiver_email = RECEIVER_EMAIL,
               subject = "Sunrise reminder", message = "It's Sunrise time")
else:
    send_email(sender_email = SENDER_EMAIL, password = SENDER_PASSWORD, receiver_email = RECEIVER_EMAIL,
               subject = "Sunrise and sunset times", message = f"Sunrise is at {sunrise}\n Sunset is at {sunset}")
