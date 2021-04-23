from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import os
from selenium.webdriver.common.keys import Keys

# Using beautiful soup to get the apartments info
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
# creating a request to get the page
response = requests.get("https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D"
                        "%2C%22mapBounds%22%3A%7B%22west%22%3A-122.57924117041016%2C%22east%22%3A-122.28741682958984"
                        "%2C%22south%22%3A37.690847562583855%2C%22north%22%3A37.85963900298693%7D%2C%22mapZoom%22"
                        "%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22"
                        "%3A872627%2C%22min%22%3A587174%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22pmf%22%3A%7B"
                        "%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22"
                        "%3A3000%2C%22min%22%3A2000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B"
                        "%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22"
                        "%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D"
                        "%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D",
                        headers = header).text

soup = BeautifulSoup(response, "html.parser")  # processing the page py BeautifulSoup
# print(soup)
links = soup.select(".list-card-info a")  # by inspecting the online page, it is found that the list-card-info class
# contains info about the addresses and the links of the listing

# solution01 to get the addresses
# addresses = soup.select(".list-card-addr")
# addresses_list = [address.text.split("|")[-1] for address in addresses]
# print(addresses_list)
# alternative solution02
addresses_list = [address.text.split("|")[-1] for address in links]
print(f"addresses list={addresses_list}")
# getitng the prices using the list_card_price class
prices = soup.select(".list-card-price")
prices_list = [price.text.split(" ")[0] for price in prices]
print(f"prices list={prices_list}")
links_list = []
for link in links:
    href = link["href"]
    if "http" in href:
        links_list.append(href)
    else:
        href = f"https://www.zillow.com{href}"
        links_list.append(href)

print(f"links_list: {links_list}")
links_address_dict = dict(zip(links_list, addresses_list))
print(links_address_dict)
# Selenium
CHROME_DRIVER = os.environ.get("CHROME_DRIVER")
GOOGLE_FORM = os.environ.get("GOOGLE_FORM")
driver = webdriver.Chrome(CHROME_DRIVER)
for index, (link, address) in enumerate(links_address_dict.items()):
    driver.get(GOOGLE_FORM)
    time.sleep(3)
    address_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
    send_address = driver.find_element_by_xpath(address_xpath)
    send_address.send_keys(address)
    price_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
    send_price = driver.find_element_by_xpath(price_xpath)
    send_price.send_keys(prices_list[index])

    link_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
    send_link = driver.find_element_by_xpath(link_xpath)
    send_link.send_keys(link)
    send_link.send_keys(Keys.ENTER)
    submit_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span'
    submit_btn = driver.find_element_by_xpath(submit_xpath)
    submit_btn.click()
    # return to submit  the next apartment info
    click_return_btn = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    click_return_btn.click()
