import tweepy
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

def twitter_authentication():
    api_key = os.getenv('API_KEY')
    api_secret_key = os.getenv('API_KEY_SECRET')
    access_token = os.getenv('ACCESS_TOKEN')
    access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
    bearer_token = os.getenv('BEARER_TOKEN')
    
    # Creating the client object for v2 requests using OAuth 2.0 Bearer Token
    client = tweepy.Client(
        bearer_token=bearer_token,
        consumer_key=api_key,
        consumer_secret=api_secret_key,
        access_token=access_token,
        access_token_secret=access_token_secret
    )

    # Creating the API object for v1.1 requests using OAuth 1.1
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True)

    # Verify the authentication
    try:
        api.verify_credentials()
        print("Authentication successful!")
    except tweepy.TweepError as e:
        print(f"Error during authentication: {e}")
    
    return api, client


# twitter_authentication()