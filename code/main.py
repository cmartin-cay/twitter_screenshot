import tweepy
from dotenv import load_dotenv
import os

load_dotenv()

# CONSUMER_KEY = os.getenv("CONSUMER_KEY")
# CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
# ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
# ACCESS_SECRET = os.getenv("ACCESS_SECRET")


def authorize_tweepy(consumer_key, consumer_secret, access_token, access_secret):
    """
    Sign in to Twitter and gain access to the API
    :param consumer_key:
    :param consumer_secret:
    :param access_token:
    :param access_secret:
    :return:
    """
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    return api


# api = authorize_tweepy(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

sample_tweet = "https://x.com/DougJBalloon/status/1824748529459339306"
