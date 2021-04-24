import os
import time
from selenium import webdriver
CHROME_DRIVER = os.environ.get('CHROME_DRIVER')
driver = webdriver.Chrome(CHROME_DRIVER)
driver.get("https://orteil.dashnet.org/experiments/cookie/")
# Get cookie
cookie = driver.find_element_by_id("cookie")

# Get upgrade-items ids.
items = driver.find_elements_by_css_selector("#store div")
print(f"items={items}")
item_ids = [item.get_attribute("id") for item in items]
print(f"item_ids={item_ids}")

timeout = time.time() + 5
five_min = time.time() + 60 * 5  # 5minutes


def get_items_prices():
    # Get all upgrade <b> tags
    all_prices = driver.find_elements_by_css_selector("#store b")
    item_prices = []
    # Convert <b> text into an integer price.
    for price in all_prices:
        element_text = price.text
        print(f"price: {element_text}")
        if element_text != "":
            cost = int(element_text.split("-")[1].strip().replace(",", ""))
            item_prices.append(cost)
    print(f"item prices={item_prices}")
    return item_prices


def get_affordable_upgrades():
    affordable_upgrades = {}
    cookie_upgrades = {}
    for n in range(len(items_prices)):
        cookie_upgrades[items_prices[n]] = item_ids[n]
    print(f"cookie_upgrades: {cookie_upgrades}")
    # Get current cookie count
    money_element = driver.find_element_by_id("money").text
    if "," in money_element:
        money_element = money_element.replace(",", "")
    cookie_count = int(money_element)
    # Find upgrades that we can currently afford
    for cost, id in cookie_upgrades.items():
        if cookie_count > cost:
            affordable_upgrades[cost] = id
    return affordable_upgrades


def purchase_item(highest_price_affordable_upgrade):
    to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
    driver.find_element_by_id(to_purchase_id).click()


while True:
    cookie.click()
    # Every 5 seconds:
    if time.time() > timeout:
        items_prices = get_items_prices()
        # Create dictionary of store items and prices
        affordable_upgrades = get_affordable_upgrades()
        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        purchase_item(highest_price_affordable_upgrade)
        # Add another 5 seconds until the next check
        timeout = time.time() + 5
