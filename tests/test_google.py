import csv

import pytest
from scripts.google import GoogleAccountManager
from scripts.utils import generate_random_name, generate_random_password


def read_account_data(csv_file):
    account_data = []
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            account_data.append(row)
    return account_data


def update_account_data(csv_file, updated_data):
    fieldnames = ['email', 'password', 'first_name', 'last_name']
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(updated_data)


csv_file = 'data/test_google_account_data.csv'
account_data = read_account_data(csv_file)
test_email = account_data[0]['email']
test_password = account_data[0]['password']


def write_account_data_to_csv(csv_file, new_account_data):
    fieldnames = ['email', 'password', 'first_name', 'last_name']
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(new_account_data)


@pytest.fixture
def google_account():
    email = test_email
    password = test_password
    driver_path = "C:/path/to/chromedriver"
    return GoogleAccountManager(email, password, driver_path)


def test_login(google_account):
    google_account.login()
    assert "Google" in google_account.driver.title
    google_account.quit()


def test_change_name(google_account):
    first_name, last_name = generate_random_name()
    google_account.login()
    google_account.change_name(first_name, last_name)
    google_account.quit()
    account_data[0]['first_name'] = first_name
    account_data[0]['last_name'] = last_name
    update_account_data(csv_file, account_data[0])


def test_change_password(google_account):
    new_password = generate_random_password()
    google_account.login()
    google_account.change_password(new_password)
    google_account.quit()
    account_data[0]['password'] = new_password
    update_account_data(csv_file, account_data[0])


