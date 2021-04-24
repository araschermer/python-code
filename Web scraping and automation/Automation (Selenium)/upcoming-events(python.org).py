import os
from selenium import webdriver

CHROME_DRIVER = os.environ.get('CHROME_DRIVER')
driver = webdriver.Chrome(executable_path=CHROME_DRIVER)
url = "https://www.python.org"
driver.get(url)
# locate the  dates of upcoming events class using css selector
# get time element in the event-widget class
events_dates = driver.find_elements_by_css_selector(".event-widget time")
for date in events_dates:
    print(date.text)
# get the texts  which hold the upcoming events which are located as texts of the anchor tags that are in lists
# inside the event-widget class
events_names = driver.find_elements_by_css_selector(".event-widget li a")
# for name in events_names:
    # print(name.text)
upcoming_events = dict(zip(events_dates, events_names))

for date, event in upcoming_events.items():
    print(f"{date.text.split('-')[1]}-{date.text.split('-')[2]}: {event.text}")
driver.close()
