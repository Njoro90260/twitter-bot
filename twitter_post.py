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


def like_tweet(tweet_id):
    # Get v2 client from the twitter_authentication funtion
    _, client = twitter_authenticaton()

    try:
        response = client.like(tweet_id=tweet_id)
        print(f"successfully liked tweet {tweet_id}")
    except Exception as e:
        print(f"Error liking tweet: {e}")

# tweet_id = ""
# like_tweet(tweet_id)


def search_tweets_paginated(query, max_result=100):
    client = tweepy.Client(bearer_token="AAAAAAAAAAAAAAAAAAAAAGtawAEAAAAArgNN6vVvMIUVxgNRqdUIabmzjrI%3Djyxr8Uy1snOdWcAnmzuinwA3txkWJtTRJx5LM1FQHF2sdwczCR")
    tweets = []
    query = "python"
    try:
        response = client.search_recent_tweets(query=query, max_result= max_result)

        tweets.extend(response.data)

        while 'next_token' in response.meta and len(tweets) < max_result:
            response = client.search_recent_tweets(query=query, max_result=max_result)
            tweets.extend(response.data)

        return tweets
    except Exception as e:
        print(f"An error occurred: {e}")
        return[]
    
all_tweets = search_tweets_paginated("python, max_results=200")
