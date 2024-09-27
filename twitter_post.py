import schedule
import time
from twitter_auth import twitter_authenticaton
import random
from datetime import datetime
import pytz

def get_nairobi_time():
    nairobi_tz = pytz.timezone("Africa/Nairobi")
    return datetime.now(nairobi_tz)

#function to create a tweet.
def create_tweet():
    # Get the client object from twitter_authentication function
    client = twitter_authenticaton()
    tweets = [
        "This is my first scheduled tweet!",
        "Hello from the bot! Here's another scheduled tweeet.",
        "Automated tweets are fun! scheduled with Tweepy."
    ]
    tweet_text = random.choice(tweets)
    # Post a tweet using the client object
    response = client.create_tweet(text=tweet_text)
    print(f"Tweet posted successfully: {response}")

# function to schedule the tweets
def schedule_tweets():
    schedule.every().day.at("09:00").do(create_tweet)

    while True:
        current_time = get_nairobi_time().strftime("%H:%M:%S")
        print(f"Current time in Nairobi: {current_time}")
        schedule.run_pending()
        schedule.run_pending()
        time.sleep(60)

# start scheduling
schedule_tweets()
