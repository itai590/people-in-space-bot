import requests
import sys
import peopleinspace
from logger import Logger
from subscription_handler import BotDefinitions
from utilities import Utilities as Util


class SendUpdatesBot():

    def send_update(bot_token, chat_id, message):
        apiURL = f'https://api.telegram.org/bot{bot_token}/sendMessage'
        try:
            response = requests.post(apiURL, json={'chat_id': chat_id, 'text': message})
            Logger.log_info("send_update to: " + chat_id + " " + response.text)
        except Exception as e:
            Logger.log_err(e)

    def send_updates(bot_token, users, message):
        users = Util._get_users(BotDefinitions.USERS_FILENAME, True)
        for user in users:
            Logger.log_info("send_update to: " + str(user))
            SendUpdatesBot.send_update(bot_token, str(user), message)


if __name__ == "__main__":
    Logger.set_logger()
    Logger.set_logger()
    if len(sys.argv) > 1:
        notification = sys.argv[1]
        Logger.log_info("using notification from command line:\n" + notification)
    else:
        Logger.log_info("command line argument was not given, scraping peopleinspace")
        notification = peopleinspace.scrape()
    Logger.log_info("sending updates..")
    SendUpdatesBot.send_updates(BotDefinitions.BOT_TOKEN, BotDefinitions.USERS_FILENAME, message=notification)
    Logger.log_info("sending updates finished successfully")    
