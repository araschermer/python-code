import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "https://en.wikipedia.org/wiki/Wikipedia:Main_Page/1"
CHROME_DRIVER = os.environ.get('CHROME_DRIVER')
driver = webdriver.Chrome(executable_path=CHROME_DRIVER)
driver.get(url)
# getting the number of articles (Articles count)
articles_count = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
# alternative
articles_count = driver.find_element_by_css_selector(
    "#articlecount a")  # 'articlecount' is an id
print(articles_count.text)

# Finding elements by link text
all_portals = driver.find_element_by_link_text("All portals")
all_portals.click()

# Finding elements by name
search = driver.find_element_by_name("search")
search.send_keys("Python")  # to type python in the search bar
search.send_keys(Keys.ENTER)  # to click enter and search the keyword
driver.close()
