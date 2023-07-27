import os

import telegram
from src.logger import Logger
from src.peopleinspace import scrape
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from user import User
from utilities import Utilities as Util

BOT_TOKEN = os.environ.get("BOT_TOKEN")
USERS_FILENAME = "users.json"


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    hello_msg = "Welcome to people in space updates bot, a daily update will be sent every morning 08:00AM IL Time"
    await update.message.reply_text(f'Hello {update.effective_user.first_name} {hello_msg}')


async def subscribe(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = User(update.effective_user.first_name, update.effective_user.last_name, user['username'], user['id'])
    Logger.log_user_call(user)
    Logger.log_subscription_event(user)
    Logger.log_subscription_event_to_file(user)
    Util.add_user(user, USERS_FILENAME)
    await update.message.reply_text(f'Thanks {update.effective_user.first_name + " " + update.effective_user.last_name}". Your subscription has been set"')


async def unsubscribe(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # UserJsonHelper.removeUserJSON(chatId);
    # writeSubscribeLog("UN-SUBSCRIBE (fullName:"+ fullName + ", chatId:" + chatId + ")\n");
    # message.setText(fullName + " ,You've been unsubscribed successfully");
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def users(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pass


def bot():
    bot_logger = Logger()

    try:
        app = ApplicationBuilder().token(BOT_TOKEN).http_version("1.1").get_updates_http_version("1.1").build()

        app.add_handler(CommandHandler("start", hello))
        app.add_handler(CommandHandler("subscribe", subscribe))
        app.add_handler(CommandHandler("unsubscribe", unsubscribe))
        app.add_handler(CommandHandler("howmany", scrape))

        app.run_polling()

    except telegram.error.TimedOut:
        bot_logger.log_info("telegram.error.TimedOut accrued")


if __name__ == "__main__":
    # ➜  nocos-bot-dev git:(master) ✗ python3 -m src.main
    # python3 -m src.main
    bot()
