from scripts.utils import generate_random_name, generate_random_password, generate_random_tweet

def test_generate_random_name():
    first_name, last_name = generate_random_name()
    assert isinstance(first_name, str)
    assert isinstance(last_name, str)

def test_generate_random_password():
    password = generate_random_password()
    assert isinstance(password, str)

def test_generate_random_tweet():
    tweet = generate_random_tweet()
    assert isinstance(tweet, str)
