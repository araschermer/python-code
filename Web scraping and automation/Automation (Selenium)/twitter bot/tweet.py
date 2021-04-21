
from selenium.webdriver.common.keys import Keys
import time

def write_tweet(driver,text):
    time.sleep(3)
    input_xpath='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[' \
                '1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[' \
                '2]/div/div/div/div '
    input_tweet=driver.find_element_by_xpath(input_xpath)
    input_tweet.send_keys(text)
    input_tweet.send_keys(Keys.ENTER)
    tweet_btn_xpath='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[' \
                    '1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div/span/span '
    tweet_btn=driver.find_element_by_xpath(tweet_btn_xpath)
    tweet_btn.click()
    print("Tweeted successfully!")
