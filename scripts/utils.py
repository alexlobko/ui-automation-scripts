from faker import Faker
from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


fake = Faker()

def generate_random_name():
    return fake.first_name(), fake.last_name()

def generate_random_password():
    return fake.password()

def generate_random_tweet():
    # return fake.random_letter()

    prompt = "Generate a random tweet."
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message

def save_account_data(filename, data):
    with open(filename, 'a') as file:
        file.write(','.join(data) + '\n')

