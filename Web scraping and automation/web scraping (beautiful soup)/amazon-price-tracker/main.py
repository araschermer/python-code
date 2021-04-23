import requests
import lxml
import smtplib
from bs4 import BeautifulSoup
import os

MINIMUM_PRICE = 100
PRODUCT_URL = os.environ.get("PRODUCT_URL")
response = requests.get(url=PRODUCT_URL, headers={'Accept-Language': 'en-US,en;q=0.9',
                                                  "User-Agent": "Mozilla/5.0 (Windows NT 10.0;"
                                                                " Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                                                                " Chrome/89.0.4389.90 Safari/537.36"})
# print(response.text)
soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())
price = soup.find(id="priceblock_ourprice").get_text()
price_without_currency = price.split()
price = ""
for index, p in enumerate(price_without_currency[0]):
    if (p == ","):
        price = price + "."
    else:
        price = price + p

price_as_float = float((price))
print(price_as_float)
item = soup.find(id="productTitle").get_text().strip()
print(item)

# SENDING EMAIL WITH THE PRICE UPDATE
SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
SENDER_PASSWORD = os.environ.get("SENDER_PASSWORD")
RECEIVER_EMAIL = os.environ.get("RECEIVER_EMAIL")


def get_smtp(sender_email):
    if "yahoo" in sender_email:
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


def send_email(sender_email, password: str, receiver_email: str, subject: str, topic: str):
    with smtplib.SMTP(get_smtp(sender_email)) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        sending = connection.sendmail(from_addr=sender_email, to_addrs=receiver_email,
                                      msg=f"Subject: {subject}\n\n{topic}")
        print(sending)


send_price_update = True
while send_price_update:
    if price_as_float < MINIMUM_PRICE:
        send_email(SENDER_EMAIL, SENDER_PASSWORD, RECEIVER_EMAIL, "Amazon Price Alert!",
                   f"The price of {item} went down to {price_as_float}")
        send_price_update = False
