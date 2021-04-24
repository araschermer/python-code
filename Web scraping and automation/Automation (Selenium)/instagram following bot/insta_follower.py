import os
from selenium import webdriver
import time
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys


class InstaFollower:
    def __init__(self):
        CHROME_DRIVER = os.environ.get('CHROME_DRIVER')
        self.login_username = os.environ.get('INSTA_USERNAME')
        self.login_password = os.environ.get('INSTA_PASSWORD')
        self.driver = webdriver.Chrome(CHROME_DRIVER)
        self.to_follow_account_url = 'https://www.instagram.com/chefsteps/'

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        # accept cookies
        cookies = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]')
        cookies.click()
        time.sleep(2)
        username = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(self.login_username)
        password = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(self.login_password)
        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        # alternative 01
        followers_full_xpath = '/html/body/div[1]/section/main/div/header/section/ul/li[2]/a'
        time.sleep(5)
        self.driver.get(self.to_follow_account_url)
        time.sleep(2)
        followers = self.driver.find_element_by_xpath(followers_full_xpath)
        followers.click()
        # #alternative 02
        # followers=self.driver.get(f"{self.to_follow_account_url}followers/")
        time.sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div')
        for _ in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does. The method
            # can accept the script as well as a HTML element. The modal in this case, becomes the arguments[0] in
            # the script. Then we're using Javascript to say: "scroll the top of the modal (popup) element by the
            # height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons[:2]:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                # in case the account in the followers is already followed,  click cancel in the cancel/unfollow pop up
                # this can also be used to unfollow Friends/people that are following certain accounts XD
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


if __name__ == '__main__':
    insta_follower = InstaFollower()
    insta_follower.login()
    insta_follower.find_followers()
    insta_follower.follow()
