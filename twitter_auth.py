import tweepy

def twitter_authenticaton():
    api_key = "EU2h7fBeycRWC6b9SmbO80C91"
    api_secret_key = "0PfB3DhOP5nih9jIVuDemi3l0GRRGSoYZi4qOEKQxqdJeit30M"
    access_token = "1659190073626091525-yE8TubUneFbl2KCZzLIGrcAcPYGmSY"
    access_token_secret = "zywTHfMn1YAetKZ69zzAFtp2ldjzeSOJKgHq4of85Fu5g"
    bearer_token = ""
    client = tweepy.client(bearer_token=bearer_token)

    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    user = api.verify_credentials()
    if user:
        print(f"Authenticated as {user.name}")
    else:
        print("Authentication failed")
    return api, client

    