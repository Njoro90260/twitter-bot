import tweepy

def twitter_authenticaton():
    api_key = "EU2h7fBeycRWC6b9SmbO80C91"
    api_secret_key = "0PfB3DhOP5nih9jIVuDemi3l0GRRGSoYZi4qOEKQxqdJeit30M"
    access_token = "1659190073626091525-yE8TubUneFbl2KCZzLIGrcAcPYGmSY"
    access_token_secret = "zywTHfMn1YAetKZ69zzAFtp2ldjzeSOJKgHq4of85Fu5g"
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAGtawAEAAAAArgNN6vVvMIUVxgNRqdUIabmzjrI%3Djyxr8Uy1snOdWcAnmzuinwA3txkWJtTRJx5LM1FQHF2sdwczCR"
    
    # Creating the client object for v2 requests with OAuth1.1 credentials
    client = tweepy.Client(
        bearer_token=bearer_token,
        consumer_key=api_key,
        consumer_secret=api_secret_key,
        access_token=access_token,
        access_token_secret=access_token_secret
    )

    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    return api, client
