import tweepy
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
# schedule_tweets()
def get_trending_topics(woeid):
    api, _ = twitter_authenticaton()

    # FEtch trending topics using the get_place_trends() method
    try:
        trends = api.get_place_trends(id=woeid)
        if trends:
            print(f"Trending in topics for WOEID {woeid}:")
            for trend in trends[0]["trends"]:
                print(f"- {trend['name']}")
        else:
            print(f"No trends available for WOEID {woeid}")
    except Exception as e:
        print(f"Error fetching trends: {e}")

# My WOEID 
# nairobi_woeid = 1528488

# # Fetch trends
# get_trending_topics(nairobi_woeid)

def search_and_like(api, query, tweet_count=10):
    try:
        # search for tweets containing keyword
        tweets = tweepy.Cursor(api.search_tweets, q=query, lang="en").items(tweet_count)

        # Like each tweets found
        for tweet in tweets:
            try:
                print(f"Linking tweets by @{tweet.user.screen_name}: {tweet.text}")
                tweet.favorite()
            except tweepy.TweepError as e:
                print(f"Error on liking tweet: {e}")
    except Exception as e:
        print(f"Error on search and like: {e}")

if __name__ == "__main__":
    api, _ = twitter_authenticaton()
    search_and_like(api, query="pizzas", tweet_count=5)