import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "https://secure-retreat-92358.herokuapp.com/"
CHROME_DRIVER = os.environ.get('CHROME_DRIVER')
driver = webdriver.Chrome(executable_path = CHROME_DRIVER)
driver.get(url)
fname = driver.find_element_by_name("fName")
fname.send_keys("fName")
# filling in the last name
lname = driver.find_element_by_name("lName")
lname.send_keys("fName")
# filling in the email
email = driver.find_element_by_name("email")
email.send_keys("email@email.com")
email.send_keys(Keys.ENTER)
# submitting the form ( alternative is # email.send_keys(Keys.ENTER))
submit = driver.find_element_by_css_selector("form button")
submit.click()
# driver.close()
