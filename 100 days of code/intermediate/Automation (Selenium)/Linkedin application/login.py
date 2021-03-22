from selenium.webdriver.common.keys import Keys


def login(login_username, login_password, driver):
    # SIGN IN LINKEDIN
    login_url = "https://www.linkedin.com/login"
    driver.get(login_url)
    username = driver.find_element_by_id("username")
    username.send_keys(login_username)
    password = driver.find_element_by_id("password")
    password.send_keys(login_password)
    password.send_keys(Keys.ENTER)
