import os
import telegram
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from src.logger import Logger
from src.peopleinspace import scrape

BOT_TOKEN = os.environ.get("BOT_TOKEN")
USERS_FILENAME = "users.json"


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    hello_msg = "Welcome to people in space updates bot, a daily update will be sent every morning 08:00AM IL Time"
    await update.message.reply_text(f'Hello {update.effective_user.first_name} {hello_msg}')


async def subscribe(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def unsubscribe(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


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
