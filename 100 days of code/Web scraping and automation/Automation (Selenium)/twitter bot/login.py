from selenium.webdriver.common.keys import Keys
import time


def login(login_username, login_password, driver):
    # SIGN IN twitter account

    login_url = "https://twitter.com/login"
    driver.get(login_url)
    time.sleep(5)
    username = driver.find_element_by_xpath(
        '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
    username.send_keys(login_username)
    password = driver.find_element_by_xpath(
        '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
    password.send_keys(login_password)
    password.send_keys(Keys.ENTER)
