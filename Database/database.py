# Imports
from pymongo import MongoClient
from datetime import datetime
import config as db_conf


# Database Class
class Database:
    def __init__(self) -> None:
        client = MongoClient(db_conf.MONGODB_URI)
        self.tweets = client.get_database("twitterbot").get_collection("tweets")

    def save_tweet(self, tweet: str) -> bool:
        res = self.tweets.insert_one({
            "content": tweet,
            "time": datetime.utcnow(),
            "published": False
        })

        if res:
            return True

        return False

    def update_tweet_status(self, _id: str):
        self.tweets.update_one(filter={"id": _id}, update={"published": True})

    def get_latest_tweet(self) -> dict:
        tweet = self.tweets.find_one(filter={"published": False})

        return tweet

    def is_db_empty(self) -> bool:
        return len(self.tweets.find()) < 1
