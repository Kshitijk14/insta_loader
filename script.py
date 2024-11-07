import os
import instaloader
# import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve Instagram credentials from environment variables
username = os.getenv("INSTAGRAM_USERNAME")
password = os.getenv("INSTAGRAM_PASSWORD")

# Create an instance of Instaloader
L = instaloader.Instaloader()

# Login with Two-Factor Authentication support
try:
    L.login(username, password)
except instaloader.TwoFactorAuthRequiredException:
    # Prompt the user for the 2FA code
    two_factor_code = input("Enter the two-factor authentication code: ")
    L.context.two_factor_login(two_factor_code)

# Load your profile
profile = instaloader.Profile.from_username(L.context, username)

# Fetch followers and followees
followers = set(follower.username for follower in profile.get_followers())
followees = set(followee.username for followee in profile.get_followees())

# Find users who don't follow back
not_following_back = followees - followers

# Print users who don't follow back
print("Users who don't follow you back:")
for user in not_following_back:
    print(user)

# # Convert the set to a DataFrame
# df = pd.DataFrame(list(not_following_back), columns=["Username"])

# # Save to a CSV file
# output_file = "not_following_back.csv"
# df.to_csv(output_file, index=False)

# print(f"Data saved to {output_file}")
