from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

from webdriver_manager.chrome import ChromeDriverManager


class GoogleAccountManager:
    def __init__(self, email, password, driver_path):
        self.email = email
        self.password = password
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def login(self):
        self.driver.get('https://accounts.google.com/')
        email_input = self.driver.find_element(By.ID, 'identifierId')
        email_input.send_keys(self.email)
        email_input.send_keys(Keys.ENTER)
        time.sleep(5)
        password_input = self.driver.find_element(By.NAME, 'Passwd')
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.ENTER)
        time.sleep(2)

    def change_name(self, first_name, last_name):
        self.driver.get('https://myaccount.google.com/profile/name/edit')
        time.sleep(2)

        # Enter new first name and last name
        first_name_input = self.driver.find_element(By.ID, 'i6')
        first_name_input.clear()
        first_name_input.send_keys(first_name)

        last_name_input = self.driver.find_element(By.ID, 'i11')
        last_name_input.clear()
        last_name_input.send_keys(last_name)

        # Save new name
        save_button = self.driver.find_element(By.XPATH, "//span[text()='Save']/..")
        save_button.click()
        time.sleep(2)


    def change_password(self, new_password):
        self.driver.get('https://myaccount.google.com/signinoptions/password')
        time.sleep(5)

        new_password_input = self.driver.find_element(By.NAME, 'password')
        new_password_input.send_keys(new_password)

        confirm_password_input = self.driver.find_element(By.NAME, 'confirmation_password')
        confirm_password_input.send_keys(new_password)

        confirm_password_input.send_keys(Keys.ENTER)
        time.sleep(2)

        self.password = new_password



    def quit(self):
        self.driver.quit()
