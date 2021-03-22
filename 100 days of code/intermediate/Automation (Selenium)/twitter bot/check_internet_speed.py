import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def check_internet_speed(driver):
    driver.get("https://www.speedtest.net/")
    time.sleep(2)
    consent='//*[@id="_evidon-banner-acceptbutton"]'
    element = driver.find_element_by_xpath(consent)
    element.click()
    go_btn = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]'
    element = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.XPATH, go_btn)))
    element.click()
    time.sleep(50)
    download_speed = driver.find_element_by_xpath(
        '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
        '2]/div/div[2]/span').text
    upload_speed = driver.find_element_by_xpath(
        '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
        '3]/div/div[2]/span').text
    ping = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]'
                                        '/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
    return download_speed, upload_speed, ping
