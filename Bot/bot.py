# Imports
from Telegram.telegramAPI import Telegram
from Twitter.twitter import Twitter
from Database.database import Database


# Class - Bot
class Bot:
    def __init__(self) -> None:
        self.telegram_bot = Telegram()
        self.twitter_handler = Twitter()
        self.db_handler = Database()

    def update_tweet(self):
        tweet = self.db_handler.get_latest_tweet()

        tweet_id = tweet["_id"]
        tweet_msg = tweet["content"]

        if self.twitter_handler.make_tweet(tweet=tweet_msg):
            self.db_handler.update_tweet_status(_id=tweet_id)

    def run(self) -> None:
        if self.telegram_bot.run():
            self.update_tweet()
