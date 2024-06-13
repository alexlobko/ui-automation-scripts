import csv

import pytest
from scripts.google import GoogleAccountManager
from scripts.utils import generate_random_name, generate_random_password, save_account_data


def read_account_data(csv_file):
    account_data = []
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            account_data.append(row)
    return account_data


csv_file = 'data/test_google_account_data.csv'
account_data = read_account_data(csv_file)[-1]
test_email = account_data['email']
test_password = account_data['password']
test_first_name = account_data['first_name']
test_last_name = account_data['last_name']
test_date_of_birth = account_data['date_of_birth']
test_recovery_email = account_data['recovery_email']



@pytest.fixture
def google_account():
    email = test_email
    password = test_password
    first_name = test_first_name
    last_name = test_last_name
    date_of_birth = test_date_of_birth
    recovery_email = test_recovery_email
    driver_path = "C:/path/to/chromedriver"
    return GoogleAccountManager(email, password, driver_path,first_name, last_name, date_of_birth, recovery_email)


def test_login(google_account):
    google_account.login()
    assert "Google" in google_account.driver.title
    google_account.quit()


def test_change_name(google_account):
    first_name, last_name = generate_random_name()
    google_account.login()
    google_account.change_name(first_name, last_name)
    google_account.quit()
    account_data['first_name'] = first_name
    account_data['last_name'] = last_name
    save_account_data(csv_file, account_data)
    google_account.update_account_data()

def test_change_password(google_account):
    new_password = generate_random_password()
    print(new_password)
    google_account.login()
    google_account.change_password(new_password)
    google_account.quit()
    account_data['password'] = new_password
    save_account_data(csv_file, account_data)


