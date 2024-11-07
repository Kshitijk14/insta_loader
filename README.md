# insta_loader

1. make a '.env' file, similar to '.env.example'
2. ```
   python -m venv env
   ```
3. ```
   .\env\Scripts\activate
   ```
4. ```
   py script.py
   ```

## Note:

It might not work everytime due to the Instagram's policy against scapring bots & analytics bots, as repeated requests (especially for 2FA) triggers Instagram's security checks.


### How a Private Account Affects Instaloader Access

1. **More Scrutiny on Login** : For private accounts, every action requires a valid session and login credentials. Instagram often flags repeated or automated logins to private accounts as suspicious, which could result in temporary restrictions.
2. **Rate Limiting and API Restrictions** : Accessing follower and followee lists of a private account is more likely to trigger rate limiting, as private data requests are monitored more closely to prevent unauthorized access.

### Recommendations

1. **Session Handling** : Using session loading and saving, as outlined in the previous response, helps maintain an authenticated session without requiring frequent logins.
2. **Moderate Request Frequency** : Make sure not to run the script too frequently. Once a day or less is ideal to avoid rate limiting.
3. **Alternative Access Strategy** : If rate limits continue, consider running the script with a time delay between requests to mimic natural usage, as this can reduce the chances of detection.
