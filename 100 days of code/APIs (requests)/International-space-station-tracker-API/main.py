import requests
from datetime import datetime
import smtplib
import time
import os

SENDER_EMAIL = os.environ['SENDER_EMAIL']
SENDER_PASSWORD = os.environ['SENDER_PASSWORD']
RECEIVER_EMAIL = os.environ['RECEIVER_EMAIL']
LONGITUDE = os.environ['LONGITUDE']
LATITUDE = os.environ['LATITUDE']
SUNRISE_SUNSET_API = "https://api.sunrise-sunset.org/json"
ISS_API = "http://api.open-notify.org/iss-now.json"
# get current location # https://www.latlong.net/ #
LOCATION_PARAMETERS = {
    "lat": LATITUDE,
    "lng": LONGITUDE,
    "formatted": 0
}


def get_sunrise_sunset_hour(location_parameters) -> (int,int):
    """returns the sunrise and the sunset hours of a given location.
    :rtype: int,int
    """
    loc_param_response = requests.get(SUNRISE_SUNSET_API, params=location_parameters)
    loc_param_response.raise_for_status()
    loc_data = loc_param_response.json()
    # to convert the sunrise format from :sunrise:2021-03-14T05:20:57+00:00 to 05:20:57
    sunrise = loc_data["results"]['sunrise'].split('T')[1].split('+')[0]
    sunset = loc_data["results"]['sunset'].split('T')[1].split('+')[0]
    # to get the hour  precisely
    sunrise_hour = int(sunrise.split(':')[0])
    sunset_hour = int(sunset.split(':')[0])
    return sunrise_hour, sunset_hour


def get_current_hour() -> int:
    """returns the current time
    :rtype int """

    current_time = datetime.now()  # # 2021-03-14 17:49:34.546252
    return current_time.hour


x = get_current_hour()
print(type(x))


# method to check if the ISS is close to the current location
# and it is currently dark (to be able to see it)
def is_iss_overhead(current_iss_latitude, current_iss_longitude, longitude, latitude, location_parameters) -> bool:
    """ checks if the ISS is within 5 degrees from the  given longitude and latitude of a certain location,
    returns true if the iss is close enough to be seen in the night time, otherwise false
    :rtype bool"""
    if latitude + 5 >= current_iss_latitude >= int(latitude) - 5 and int(longitude) + 5 >= current_iss_longitude >=\
            int(longitude) - 5:
        return is_night_time(location_parameters)
    return False


def is_night_time(location_parameters) -> bool:
    """checks is the current time is between sunset and sunrise, returns true it it is night time, otherwise false.
     :rtype bool"""
    sunrise_hour, sunset_hour = get_sunrise_sunset_hour(location_parameters)
    if sunset_hour <= get_current_hour() <= sunrise_hour:
        return True


def get_iss_position() -> (float, float):
    """returns iss_latitude and iss_longitude
    :rtype (float,float)
    """
    response = requests.get(url=ISS_API)
    response.raise_for_status()
    data = response.json()
    latitude = float(data["iss_position"]["longitude"])
    longitude = float(data["iss_position"]["latitude"])
    return longitude, latitude


def send_email(sender_email: str, password: str, receiver_email: str, subject: str, message: str):
    """requires sender_email and the email's password, the  receiver_email
    and a subject of the email, as well as the message as the body of the Email"""
    with smtplib.SMTP(get_smtp(sender_email)) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(from_addr=sender_email, to_addrs=receiver_email,
                            msg=f"Subject: {subject}\n\n{message}")


def get_smtp(sender_email: str) -> str:
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
if is_iss_overhead(current_iss_latitude=iss_latitude, current_iss_longitude=iss_longitude, longitude=LONGITUDE,
                   latitude=LATITUDE, location_parameters=LOCATION_PARAMETERS):
    send_email(sender_email=SENDER_EMAIL, password=SENDER_PASSWORD,
               receiver_email=RECEIVER_EMAIL,
               subject="Look up", message="THE INTERNATIONAL SPACE STATION is above you!")


def monitor_iss_location():
    """ a method that keeps checking the ISS location, and if it is night time and the ISS is above the current location
    then it sends a notification email that the ISS  is overhead"""
    while True:
        time.sleep(60)
        current_iss_longitude, current_iss_latitude = get_iss_position()
        if is_iss_overhead(current_iss_latitude=current_iss_latitude, current_iss_longitude=current_iss_longitude,
                           longitude=LONGITUDE,
                           latitude=LATITUDE, location_parameters=LOCATION_PARAMETERS):
            send_email(sender_email=SENDER_EMAIL, password=SENDER_PASSWORD,
                       receiver_email=RECEIVER_EMAIL,
                       subject="Look up", message="THE INTERNATIONAL SPACE STATION is above you!")
            break
