import os
from selenium import webdriver
from check_internet_speed import check_internet_speed
from login import login
from tweet import write_tweet

PROMISED_DOWNLOAD_SPEED = 100
PROMISED_UPLOAD_SPEED = 10
PROMISED_PING = 100
CHROME_DRIVER = os.environ.get('CHROME_DRIVER')
login_username = os.environ.get('TWITTER_USERNAME')
login_password = os.environ.get('TWITTER_PASSWORD')
driver = webdriver.Chrome(CHROME_DRIVER)
while True:
    download_speed, upload_speed, ping = check_internet_speed(driver)
    # sometimes it takes longer than 50 seconds
    # to perform the tests. So for a full test results, the test is repeated
    if download_speed != " " and upload_speed != " " and ping != " ":
        complaint_text = "Hey Internet provider, "
        if float(download_speed) < PROMISED_DOWNLOAD_SPEED:
            complaint_text += f"why is my download speed down to {download_speed}?\n"

        if float(upload_speed) < PROMISED_UPLOAD_SPEED and float(ping) < PROMISED_PING:
            complaint_text += f"my upload speed is down to {upload_speed} and my ping up to {ping}"
        if complaint_text != "Hey Internet provider, ":
            login(login_password = login_password, login_username = login_username, driver = driver)
            write_tweet(driver = driver, text = complaint_text)
            driver.quit()