from datetime import datetime
import pandas as pd
from random import randint
from smtplib import SMTP

#
SENDER_EMAIL = ""
SENDER_PASSWORD = ""


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


today = datetime.now()
today_tuple = (today.month, today.day)
# read the birthdays.csv
data = pd.read_csv("birthdays.csv")
# dictionary comprehension to create a dictionary from birthday.csv that is formatted like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# compare and see if today's month/day tuple matches one of the keys in birthday_dict
# If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt)
# from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
if today_tuple in birthdays_dict:
    file_path = f"letter_templates/letter_{randint(1, 3)}.txt"
    with open(file_path) as letter_template:
        birthday_person = birthdays_dict[today_tuple]
        content = letter_template.read()
        content = content.replace("[NAME]", birthday_person["name"].item())

    # Sends the letter generated in content to that birthday_person's email address.
    with SMTP(get_smtp(SENDER_EMAIL)) as connection:
        connection.starttls()
        connection.login(SENDER_EMAIL, SENDER_PASSWORD)
        connection.sendmail(from_addr = SENDER_EMAIL, to_addrs = birthday_person["email"],
                            msg = f"Subject:Happy Birthday!\n\n{content}")
# to automatically send a daily email, try running the script on pythonanywhere.com