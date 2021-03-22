import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

url = "https://orteil.dashnet.org/cookieclicker/"
CHROME_DRIVER = os.environ.get('CHROME_DRIVER')
driver = webdriver.Chrome(executable_path = CHROME_DRIVER)
driver.get(url)
cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
action = ActionChains(driver)

action.click(cookie)
while True:
       try:
            action.perform()
            # cookie.click()
            count = int(cookie_count.text.split(" ")[0])
            # print(count)
            # upgrade_list=[driver.find_element_by_id("upgrade" + str(num)) for num in range(2)]
            products = [driver.find_element_by_id("productPrice" + str(num)) for num in range(1,-1,-1)]
            for product in products:
                price = product.text
                if price != "":
                    price = int(price.strip().replace(",", ""))
                if price <= count:
                    upgrade_action = ActionChains(driver)
                    upgrade_action.move_to_element(product)
                    upgrade_action.click()
                    upgrade_action.perform()
       except:
           print("score={count}")
           driver.quit()
