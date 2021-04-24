import os
from selenium import webdriver
from login import login
from search_for_job import search_for_job
from send_easy_application import send_easy_application
from save_all_jobs import save_all_jobs
import time
CHROME_DRIVER = os.environ.get('CHROME_DRIVER')
driver = webdriver.Chrome(CHROME_DRIVER)
phone = 12345678
login_username = os.environ.get('LINKEDIN_USERNAME')
login_password = os.environ.get('LINKEDIN_PASSWORD')
login(login_username=login_username, login_password=login_password, driver=driver)
time.sleep(20)
all_listings = search_for_job(search_term="python developer jobs ", driver=driver)
for listing in all_listings:
    print(listing.text)
save_all_jobs(driver=driver, all_listings=all_listings)
send_easy_application(driver=driver, phone=phone, all_listings=all_listings)
print("Done!")
