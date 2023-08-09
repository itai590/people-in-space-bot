import requests
from logger import Logger
from peopleinspace import scrape
from utilities import Utilities as Util
from __main__ import BotDefinitions


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
            SendUpdatesBot.send_update(bot_token, str(user), message)


if __name__ == "__main__":
    SendUpdatesBot.send_updates(BotDefinitions.BOT_TOKEN, BotDefinitions.USERS_FILENAME, scrape())
