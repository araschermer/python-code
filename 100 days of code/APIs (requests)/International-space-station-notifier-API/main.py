# https://sunrise-sunset.org/api
import requests
from datetime import datetime
import smtplib
import time

SENDER_EMAIL = ""  # to fill
SENDER_PASSWORD = ""  # to fill
RECEIVER_EMAIL = ""  # to fill
LONGITUDE = 13.411440
LATITUDE = 52.523430
# get current location # https://www.latlong.net/ #
LOCATION_PARAMETERS = {
    "lat": LATITUDE,
    "lng": LONGITUDE,
    "formatted": 0
}


def get_sunrise_sunset_hour(location_parameters):
    link = "https://api.sunrise-sunset.org/json"
    loc_param_response = requests.get(link, params = location_parameters)
    loc_param_response.raise_for_status()
    loc_data = loc_param_response.json()
    # to convert the sunrise format from :sunrise:2021-03-14T05:20:57+00:00 to 05:20:57
    sunrise = loc_data["results"]['sunrise'].split('T')[1].split('+')[0]
    sunset = loc_data["results"]['sunset'].split('T')[1].split('+')[0]
    # to get the hour  precisely
    sunrise_hour = int(sunrise.split(':')[0])
    sunset_hour = int(sunset.split(':')[0])
    return sunrise_hour, sunset_hour


def get_current_hour():
    current_time = datetime.now()  # # 2021-03-14 17:49:34.546252
    return current_time.hour


# method to check if the ISS is close to the current location
# and it is currently dark (to be able to see it)
def is_iss_overhead(current_iss_latitude, current_iss_longitude, longitude, latitude, location_parameters):
    if latitude + 5 >= current_iss_latitude >= latitude - 5 and longitude + 5 >= current_iss_longitude >= longitude - 5:
        return is_night_time(location_parameters)
    return False


def is_night_time(location_parameters):
    sunrise_hour, sunset_hour = get_sunrise_sunset_hour(location_parameters)
    if sunset_hour <= get_current_hour() <= sunrise_hour:
        return True


def get_iss_position():
    """returns iss_latitude and iss_longitude
    :rtype (int,int)
    """
    response = requests.get(url = "http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    latitude = float(data["iss_position"]["longitude"])
    longitude = float(data["iss_position"]["latitude"])
    return longitude, latitude


def send_email(sender_email, password, receiver_email, subject, message):
    """requires sender_email and the email's password, the  receiver_email
    and a subject of the email, as well as the message as the body of the Email"""
    with smtplib.SMTP(get_smtp(sender_email)) as connection:
        connection.starttls()
        connection.login(user = sender_email, password = password)
        connection.sendmail(from_addr = sender_email, to_addrs = receiver_email,
                            msg = f"Subject: {subject}\n\n{message}")


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


# getting the iss_position
iss_longitude, iss_latitude = get_iss_position()
if is_iss_overhead(current_iss_latitude = iss_latitude, current_iss_longitude = iss_longitude, longitude = LONGITUDE,
                   latitude = LATITUDE, location_parameters = LOCATION_PARAMETERS):
    send_email(sender_email = SENDER_EMAIL, password = SENDER_PASSWORD,
               receiver_email = RECEIVER_EMAIL,
               subject = "Look up", message = "THE INTERNATIONAL SPACE STATION is above you!")


def montitor_iss_location():
    """ a method that keeps checking the ISS location, and if it is night time and the ISS is above the current location
    then it sends a notification email that the ISS  is overhead"""
    while True:
        time.sleep(60)
        current_iss_longitude, current_iss_latitude = get_iss_position()
        if is_iss_overhead(current_iss_latitude = current_iss_latitude, current_iss_longitude = current_iss_longitude,
                           longitude = LONGITUDE,
                           latitude = LATITUDE, location_parameters = LOCATION_PARAMETERS):
            send_email(sender_email = SENDER_EMAIL, password = SENDER_PASSWORD,
                       receiver_email = RECEIVER_EMAIL,
                       subject = "Look up", message = "THE INTERNATIONAL SPACE STATION is above you!")
            break
