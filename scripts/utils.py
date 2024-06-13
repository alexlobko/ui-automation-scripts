import csv

from faker import Faker
from openai import OpenAI
from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


fake = Faker()

def generate_random_name():
    return fake.first_name(), fake.last_name()

def generate_random_password():
    return fake.password()

def generate_random_tweet():
    #prompt = "Generate a random tweet."
    # completion = client.chat.completions.create(
    #     model="gpt-3.5-turbo",
    #     messages=[
    #         {"role": "user", "content": prompt}
    #     ]
    # )
    # return completion.choices[0].message
    return fake.text(max_nb_chars=100)


def save_account_data(csv_file, updated_data):
    fieldnames = ['email', 'password', 'first_name', 'last_name', 'date_of_birth', 'recovery_email']
    with open(csv_file, mode='a', newline='\n') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(updated_data)

def set_user_agent(driver, user_agent):
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": user_agent})



def get_mobile_driver(proxy=None):
    mobile_emulation = {
        "deviceName": "Nexus 5"
    }

    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    if proxy:
        chrome_options.add_argument(f'--proxy-server={proxy}')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver