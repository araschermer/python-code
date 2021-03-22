from selenium.webdriver.common.keys import Keys

import time


def search_for_job(search_term, driver):
    time.sleep(3)
    search = driver.find_element_by_xpath('/html/body/div[9]/header/div[2]/div/div/div[1]/div[2]/input')
    search.send_keys(search_term)
    search.send_keys(Keys.ENTER)
    # to redirect to the all jobs page:
    new_url = "https://www.linkedin.com/jobs/search/?keywords="
    for term in search_term.split():
        new_url += f"{term}%20"
    driver.get(new_url)
    time.sleep(3)
    all_listings = driver.find_elements_by_class_name("jobs-search-results__list-item")
    # all_listings = driver.find_elements_by_xpath('//div/div/div[2]/ul/li')
    for job in all_listings:
        print(job.text)
    return all_listings
