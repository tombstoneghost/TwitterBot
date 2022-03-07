# Imports
from telegram.ext import Updater, CommandHandler, CallbackContext, Filters, MessageHandler
from telegram.update import Update
from Database.database import Database
import config as telegram_conf


# Class Telegram
class Telegram:
    def __init__(self) -> None:
        self.handler = Updater(token=telegram_conf.BOT_ID, use_context=True)
        self.handleTweet = False
        self.load_commands()

        self.db_handler = Database()

    # Add Commands to the Bot
    def load_commands(self):
        self.handler.dispatcher.add_handler(CommandHandler(command="addTweet", callback=self.add_tweet_to_database))
        self.handler.dispatcher.add_handler(MessageHandler(filters=Filters.text, callback=self.handle_messages))

    # Add Tweet
    def add_tweet_to_database(self, update: Update, context: CallbackContext) -> None:
        update.message.reply_text("Kindly enter the tweet you want to save?")
        self.handleTweet = True

    # Handle Messages
    def handle_messages(self, update: Update, context: CallbackContext) -> None:
        if self.handleTweet:
            tweet = update.message.text

            if len(tweet) > 280:
                update.message.reply_text("Tweet more than 280 characters.")
            else:
                if self.db_handler.save_tweet(tweet=tweet):
                    update.message.reply_text("Your tweet has been saved. Kindly use the command again "
                                              "to save another tweet.")
                else:
                    update.message.reply_text("There was an error saving the tweet.")
        else:
            update.message.reply_text("Kindly use the command to save Tweet")

    # Send Message
    def send_message(self, message: str) -> None:
        pass

    def run(self):
        return self.handler.start_polling()
