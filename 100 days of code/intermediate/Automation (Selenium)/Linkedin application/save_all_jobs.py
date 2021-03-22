from selenium.webdriver.common.keys import Keys
import time


def save_all_jobs(driver, all_listings):
    time.sleep(2)
    for job in all_listings:
        job.click()
        time.sleep(2)
        # save_button= driver.find_element_by_xpath('/html/body/div[8]/div[3]/div[3]/div/div/section[2]/div/div/div[1]/'
        #                                           'div/div[1]/div/div/div[2]/div[2]/div[1]/button')
        save_button = driver.find_element_by_css_selector('.jobs-save-button button')
        save_button.click()
        time.sleep(3)
