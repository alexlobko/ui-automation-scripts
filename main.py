import argparse
from scripts.google import GoogleAccountManager
from scripts.twitter import TwitterAccountManager


def manage_google_account(email, password, new_password, first_name, last_name, date_of_birth, recovery_email,
                          user_agent):
    google_manager = GoogleAccountManager(email, password, driver_path=None, first_name=first_name, last_name=last_name,
                                          date_of_birth=date_of_birth, recovery_email=recovery_email,
                                          user_agent=user_agent)
    google_manager.login()
    google_manager.change_password(new_password)
    google_manager.change_name(first_name, last_name)
    google_manager.update_account_data()
    google_manager.quit()


def manage_twitter_account(email, password, new_password, tweet, user_agent):
    twitter_manager = TwitterAccountManager(email, password, driver_path=None, user_agent=user_agent)
    twitter_manager.login()
    twitter_manager.change_password(new_password)
    twitter_manager.make_random_post(tweet)
    twitter_manager.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Manage Google and Twitter accounts.")

    parser.add_argument("platform", choices=["google", "twitter"], help="The platform to manage.")
    parser.add_argument("email", help="Email address of the account.")
    parser.add_argument("password", help="Current password of the account.")
    parser.add_argument("new_password", help="New password for the account.")
    parser.add_argument("--first_name", help="New first name (for Google).", default="John")
    parser.add_argument("--last_name", help="New last name (for Google).", default="Doe")
    parser.add_argument("--date_of_birth", help="Date of birth (for Google).", default="1990-01-01")
    parser.add_argument("--recovery_email", help="Recovery email (for Google).", default="reserve@gmail")
    parser.add_argument("--tweet", help="Tweet content (for Twitter).", default="")
    parser.add_argument("--user_agent", help="User agent for the browser.", default=None)

    args = parser.parse_args()

    if args.platform == "google":
        manage_google_account(args.email, args.password, args.new_password, args.first_name, args.last_name,
                              args.date_of_birth, args.recovery_email, args.user_agent)
    elif args.platform == "twitter":
        manage_twitter_account(args.email, args.password, args.new_password, args.tweet, args.user_agent)
