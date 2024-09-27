import tweepy
from twitter_auth import twitter_authenticaton as tweet

def create_tweet(text):
    client = tweet()
    client.create_tweet(text=text)

create_tweet("Hello world! This is my first tweet using Tweepy")