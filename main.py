from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
import time

CHROME_DRIVER_PATH = "C:\\Development\\chromedriver.exe"
SIMILAR_ACCOUNT = "ACCOUNT"
USERNAME = "YOUR USERNAME"
PASSWORD = "YOUR PASSWORD"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.driver.get("https://www.instagram.com")
        time.sleep(3)

    def login(self):
        self.username = self.driver.find_element_by_name("username")
        self.username.send_keys(USERNAME)
        self.password = self.driver.find_element_by_name("password")
        self.password.send_keys(PASSWORD)
        self.button = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        self.button.click()
        time.sleep(3)
        self.save_info = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        self.save_info.click()
        time.sleep(3)
        self.notification = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        self.notification.click()

    def find_followers(self):
        self.search = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        self.search.send_keys(SIMILAR_ACCOUNT)
        time.sleep(3)
        self.account_click = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div['
                                                               '2]/div[3]/div/div[2]/div/div[1]/a')
        self.account_click.click()
        time.sleep(3)
        self.follwers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul'
                                                          '/li[2]/a')
        self.follwers.click()
        time.sleep(2)
        self.bar = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", self.bar)
            time.sleep(2)

    def follow(self):
        self.all_buttons = self.driver.find_elements_by_css_selector("li button")
        for self.button in self.all_buttons:
            try:
                self.button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                self.cancel = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                self.cancel.click()


insta_follower = InstaFollower()
insta_follower.login()
insta_follower.find_followers()
insta_follower.follow()
