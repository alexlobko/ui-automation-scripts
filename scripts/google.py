import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

from webdriver_manager.chrome import ChromeDriverManager

from scripts.cookies import save_cookies, save_fingerprint
from scripts.utils import set_user_agent, save_account_data


class GoogleAccountManager:
    def __init__(
            self,
            email,
            password,
            driver_path,
            first_name='first_name',
            last_name='last_name',
            date_of_birth='1990-01-01',
            recovery_email='reserve@gmail',
            user_agent=None,
    ):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.recovery_email = recovery_email
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        if user_agent:
            set_user_agent(self.driver, user_agent)

    if not os.path.exists('data'):
        os.makedirs('data')
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
        save_cookies(self.driver, 'data/google_cookies.pkl')
        save_fingerprint(self.driver, 'data/google_fingerprints.pkl')


    def change_name(self, first_name, last_name):
        self.driver.get('https://myaccount.google.com/profile/name/edit')
        time.sleep(2)

        first_name_input = self.driver.find_element(By.ID, 'i6')
        first_name_input.clear()
        first_name_input.send_keys(first_name)

        last_name_input = self.driver.find_element(By.ID, 'i11')
        last_name_input.clear()
        last_name_input.send_keys(last_name)

        save_button = self.driver.find_element(By.XPATH, "//span[text()='Save']/..")
        save_button.click()
        time.sleep(2)
        self.first_name = first_name
        self.last_name = last_name

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

    def update_account_data(self):
        data = {
            'email': self.email,
            'password': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'date_of_birth': self.date_of_birth,
            'recovery_email': self.recovery_email
        }
        save_account_data('data/accounts_data.csv', data)

    def quit(self):
        self.driver.quit()

