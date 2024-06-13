import csv

import pytest
from scripts.twitter import TwitterAccountManager
from scripts.utils import generate_random_tweet, generate_random_password


def read_account_data(csv_file):
    account_data = []
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            account_data.append(row)
    return account_data


def update_account_data(csv_file, updated_data):
    fieldnames = ['email', 'password']
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(updated_data)


csv_file = 'data/test_twitter_account_data.csv'
account_data = read_account_data(csv_file)
test_email = account_data[0]['email']
test_password = account_data[0]['password']

@pytest.fixture
def twitter_account():
    email = test_email
    password = test_password
    driver_path = "/path/to/chromedriver"
    return TwitterAccountManager(email, password, driver_path)

def test_login(twitter_account):
    twitter_account.login()
    assert "X" in twitter_account.driver.title
    twitter_account.quit()


def test_make_random_post(twitter_account):
    tweet = generate_random_tweet()
    twitter_account.login()
    twitter_account.make_random_post(tweet)
    twitter_account.quit()



def test_change_password(twitter_account):
    new_password = generate_random_password()
    twitter_account.login()
    twitter_account.change_password(new_password)
    twitter_account.quit()
    account_data[0]['password'] = new_password
    update_account_data(csv_file, account_data[0])
