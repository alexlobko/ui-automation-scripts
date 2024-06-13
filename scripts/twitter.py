from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


from webdriver_manager.chrome import ChromeDriverManager


class TwitterAccountManager:
    def __init__(self, email, password, driver_path):
        self.email = email
        self.password = password
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def login(self):
        self.driver.get('https://twitter.com/login')
        time.sleep(10)
        email_input = self.driver.find_element(By.NAME, 'text')
        email_input.send_keys(self.email)
        email_input.send_keys(Keys.ENTER)
        time.sleep(10)
        password_input = self.driver.find_element(By.NAME, 'password')
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.ENTER)
        time.sleep(5)

    def change_password(self, new_password):
        self.driver.get('https://x.com/settings/password')
        time.sleep(2)

        current_password_input = self.driver.find_element(By.NAME, 'current_password')
        current_password_input.send_keys(self.password)

        new_password_input = self.driver.find_element(By.NAME, 'new_password')
        new_password_input.send_keys(new_password)

        confirm_password_input = self.driver.find_element(By.NAME, 'password_confirmation')
        confirm_password_input.send_keys(new_password)

        save_button = self.driver.find_element(By.XPATH, "//span[text()='Save']/..")
        save_button.click()
        time.sleep(2)

        self.password = new_password

    def make_random_post(self, tweet):
        self.driver.get('https://x.com/home')
        time.sleep(5)
        tweet_textarea = self.driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Post text"][role="textbox"]')
        tweet_textarea.click()
        tweet_textarea.send_keys(tweet)
        tweet_button = self.driver.find_element(By.CSS_SELECTOR, 'button[data-testid="tweetButtonInline"]')
        tweet_button.click()
        time.sleep(2)

    def quit(self):
        self.driver.quit()