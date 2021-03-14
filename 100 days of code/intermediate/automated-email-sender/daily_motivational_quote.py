import smtplib
from random import choice
import datetime as dt

SENDER_EMAIL = ""  # to fill
SENDER_PASSWORD = ""  # to fill
RECEIVER_EMAIL = ""  # to fill


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


def send_email(sender_email, password, receiver_email, subject="Motivational Quote"):
    with smtplib.SMTP(get_smtp(sender_email)) as connection:
        connection.starttls()
        connection.login(user = sender_email, password = password)
        connection.sendmail(from_addr = sender_email, to_addrs = receiver_email,
                            msg = f"Subject: {subject}\n\n{get_random_quote()}")


def get_random_quote():
    """return a random quote chosen from the quotes.txt file
    :rtype string"""
    with open("quotes.txt") as quotes:
        lines = quotes.readlines()
        return choice(lines)


def get_current_date():
    """Gets the current daytime
     and returns the weekday (it can be adjusted to return more specific date info)
    :rtype int"""
    now = dt.datetime.now()

    # year = now.year
    # month = now.month
    # day = now.day
    weekday = now.weekday()
    return weekday


# send the email on a specific weekday (ignored; given the list [0...6])
if get_current_date() in [0, 1, 2, 3, 4, 5, 6]:
    send_email(sender_email = SENDER_EMAIL, password = SENDER_PASSWORD,
               receiver_email = RECEIVER_EMAIL)
else:
    print("Something went wrong")

# to automatically send a daily email, try running the script on pythonanywhere.com
