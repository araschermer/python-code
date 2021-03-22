import os
from selenium import webdriver
import time
# time.sleep(1)
# alternative  EXPLICIT WAIT
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER = os.environ.get('CHROME_DRIVER')
driver = webdriver.Chrome(executable_path = CHROME_DRIVER)
driver.get("http://www.amazon.com")
 # getting the page title:
print(driver.title)
# accessing an element happens using the one of the following properties
# id, or  the xpath (both are unique to the element)
# name
# tag:
# class_name: not unique, can contain many elements
driver = webdriver.Chrome(CHROME_DRIVER)
driver.get("https://techwithtim.net")
search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.ENTER)
try:
    #searching a key word and printing the results
    main = WebDriverWait(driver, 2).until(
        expected_conditions.presence_of_element_located((By.ID, "main")))
    articles=main.find_elements_by_tag_name("article")
    for article in articles:
        head = article.find_element_by_class_name("entry-summary")
        print(f"\n {head.text}\n")
    # to navigate to another page:
    #navigating to between pages and signing up for a course
    driver.refresh()
    element = WebDriverWait(driver, 1).until(
        expected_conditions.presence_of_element_located((By.LINK_TEXT, "Python Programming")))
    element.click()
    element = WebDriverWait(driver, 2).until(
        expected_conditions.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials")))
    element.click()
    element = WebDriverWait(driver, 2).until(
        expected_conditions.presence_of_element_located((By.ID, "sow-button-19310003")))
    element.click()
    driver.forward()
    driver.back()
    element.clear()
except:
    print("Job Done")
    driver.close()
# driver.quit() # shuts down the entire browser
