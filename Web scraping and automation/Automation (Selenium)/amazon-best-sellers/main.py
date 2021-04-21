import os
from selenium import webdriver

CHROME_DRIVER = os.environ.get('CHROME_DRIVER')
driver = webdriver.Chrome(executable_path = CHROME_DRIVER)
url="https://www.amazon.de/-/en/gp/bestsellers/books"
driver.get(url)
prices = [price.text for price in driver.find_elements_by_class_name("p13n-sc-price")]
items = [item.get_attribute("title") for item in driver.find_elements_by_class_name("p13n-sc-truncate-desktop-type2")]
best_sellers=dict(zip(items, prices))
for item,price in best_sellers.items():
    print(f"{item}:{price}\n")
driver.close()
# driver.quit() # shuts the browser down
