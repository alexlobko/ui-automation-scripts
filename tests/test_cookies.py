import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from scripts.cookies import save_cookies, load_cookies, save_fingerprint, load_fingerprint


if not os.path.exists('data'):
    os.makedirs('data')

def test_save_and_load_cookies():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.google.com")

    save_cookies(driver, 'data/test_cookies.pkl')
    driver.delete_all_cookies()
    load_cookies(driver, 'data/test_cookies.pkl')
    driver.get("https://www.google.com")
    print(driver.get_cookies())
    driver.quit()


def test_save_and_load_fingerprint():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    save_fingerprint(driver, 'data/test_fingerprint.pkl')
    load_fingerprint(driver, 'data/test_fingerprint.pkl')

    print(driver.execute_script("return navigator.userAgent;"))
    driver.quit()


if __name__ == "__main__":
    test_save_and_load_cookies()
    test_save_and_load_fingerprint()
