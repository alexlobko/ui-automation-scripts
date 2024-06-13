# UI Automation Scripts

This project provides scripts to automate Google and Twitter account management, including changing passwords, changing first and last names (for Google), and posting tweets (for Twitter).

## Installation

1. Clone the repository::
    ```bash
    git clone <repository-url>
    ```

2. Go to the project directory::
    ```bash
    cd project-directory
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Managing your Google account

To manage your Google account, run the command:

```bash
python main.py google <email> <password> <  > --first_name <first_name> --last_name <last_name> --date_of_birth <date_of_birth> --recovery_email <recovery_email> --user_agent <user_agent>
```


### Managing your Twitter account

To manage Twitter account, run the command:

```bash
python main.py twitter <email> <password> <new_password> --tweet <tweet> --user_agent <user_agent>
```
## Using OpenAI for Random Tweets
### To use OpenAI for generating random tweets, you need to create a .env file in the root directory and add your OpenAI API key. Then uncomment the relevant code in utils.py.

Create a `.env` file and add your OpenAI API key:
```env
OPENAI_API_KEY=your_openai_api_key
```

Uncomment the relevant code in scripts/utils.py:
```python
    #prompt = "Generate a random tweet."
    # completion = client.chat.completions.create(
    #     model="gpt-3.5-turbo",
    #     messages=[
    #         {"role": "user", "content": prompt}
    #     ]
    # )
    # return completion.choices[0].message
```
### *The scripts are intended for use for educational and testing purposes.
