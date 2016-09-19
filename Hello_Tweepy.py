import tweepy
import tokens


consumer_key = tokens.consumer_key #APP Public Key
consumer_secret = tokens.consumer_secret
access_token = tokens.access_token #SanchezCarry Public Token
access_token_secret = tokens.access_token_secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)