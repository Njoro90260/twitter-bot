from twitter_auth import twitter_authenticaton

def create_tweet():
    # Get the client object from twitter_authentication function
    client = twitter_authenticaton()
    
    # Post a tweet using the client object
    response = client.create_tweet(text="Hello world! This is my first tweet using Tweepy API v2!")
    print(f"Tweet posted successfully: {response}")

# Call the function to create a tweet
create_tweet()
