import os

import telegram
from logger import Logger
from peopleinspace import scrape
from user import User
from utilities import Utilities as Util
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


class BotDefinitions:
    BOT_TOKEN = os.environ["BOT_TOKEN"]
    GET_USERS_TOKEN = os.environ['GET_USERS_TOKEN']

    USERS_FILENAME = "users.json"
    SUBSCRIPTION_LOG_FILENAME = "./logs/subscription_log.log"


class SubscriptionHandlerBot():

    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user = update.message.from_user
        user = User(update.effective_user.first_name, update.effective_user.last_name, user['username'], user['id'])
        Logger.log_user_call(user, "start")

        hello_msg = "Welcome to people in space updates bot.\nA daily update will be sent every morning 08:00AM IL Time."
        format_explanation = "\nFormat Explanation:\n \
            🚀   🪐  🌍    10 🧑‍🚀🧑‍🚀\n \
            🚀   🪐  🌍    <Number of people in space> 🧑‍🚀🧑‍🚀\n \
            1.Jame James🇺🇸 - FLT Eng. - 120 \n \
            1<Name> <Country> - <Role> - <Days in space>\n"

        ans = f'{hello_msg}\n{format_explanation}'

        await update.message.reply_text(f'Hello {update.effective_user.first_name},\n{ans}')

    async def subscribe(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

        user = update.message.from_user
        user = User(update.effective_user.first_name, update.effective_user.last_name, user['username'], user['id'])
        Logger.log_user_call(user, "subscribe")
        Logger.log_subscription_event(BotDefinitions.SUBSCRIPTION_LOG_FILENAME, user)
        Util.add_user(user, BotDefinitions.USERS_FILENAME)
        await update.message.reply_text(f'Thanks {user.full_name()}. Your subscription has been set')

    async def unsubscribe(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user = update.message.from_user
        user = User(update.effective_user.first_name, update.effective_user.last_name, user['username'], user['id'])
        Logger.log_user_call(user, "unsubscribe")
        Logger.log_subscription_event(BotDefinitions.SUBSCRIPTION_LOG_FILENAME, user, subscribe=False)
        Util.remove_user(user, BotDefinitions.USERS_FILENAME)
        await update.message.reply_text(f"{user.full_name()}, You've been unsubscribed successfully")

    async def users(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user = update.message.from_user
        user = User(update.effective_user.first_name, update.effective_user.last_name, user['username'], user['id'])
        Logger.log_user_call(user, "users")
        ans = Util._get_users(BotDefinitions.USERS_FILENAME)
        if ans == "":
            ans = "No users subscribed"
        await update.message.reply_text(f"{ans}")

    async def howmany(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user = update.message.from_user
        user = User(update.effective_user.first_name, update.effective_user.last_name, user['username'], user['id'])
        Logger.log_user_call(user, "howmany")
        ans = scrape(True)
        await update.message.reply_text(f"{ans}")

    async def howmanydetailed(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user = update.message.from_user
        user = User(update.effective_user.first_name, update.effective_user.last_name, user['username'], user['id'])
        Logger.log_user_call(user, "howmanydetailed")
        ans = scrape()
        await update.message.reply_text(f"{ans}")

    def main():
        Logger.set_logger()
        get_users_command = f'gus{BotDefinitions.GET_USERS_TOKEN}'

        try:
            app = ApplicationBuilder().token(BotDefinitions.BOT_TOKEN).http_version("1.1").get_updates_http_version("1.1").build()

            app.add_handler(CommandHandler("start", SubscriptionHandlerBot.start))
            app.add_handler(CommandHandler("subscribe", SubscriptionHandlerBot.subscribe))
            app.add_handler(CommandHandler("unsubscribe", SubscriptionHandlerBot.unsubscribe))
            app.add_handler(CommandHandler("howmany", SubscriptionHandlerBot.howmany))
            app.add_handler(CommandHandler("howmanydetailed", SubscriptionHandlerBot.howmanydetailed))
            app.add_handler(CommandHandler(get_users_command, SubscriptionHandlerBot.users))

            app.run_polling()

        except telegram.error.TimedOut:
            Logger.log_info("telegram.error.TimedOut accrued")


if __name__ == "__main__":
    # python3 -m src.subscription_handler
    # TODO Bot Father Add test Bot
    SubscriptionHandlerBot.main()
