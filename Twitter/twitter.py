# Imports
import tweepy
import config as twitter_conf


# Class Twitter
class Twitter:
    def __init__(self) -> None:
        self.auth = None
        self.authenticate()
        self.api = tweepy.API(auth=self.auth)

    # Authenticate User
    def authenticate(self):
        self.auth = tweepy.OAuthHandler(consumer_key=twitter_conf.CONSUMER_KEY,
                                        consumer_secret=twitter_conf.CONSUMER_SECRET)
        self.auth.set_access_token(key=twitter_conf.ACCESS_TOKEN, secret=twitter_conf.ACCESS_TOKEN_SECRET)

    # Make Tweet
    def make_tweet(self, tweet: str) -> bool:
        return self.api.update_status(tweet)
