#!/usr/bin/env python
# pylint: disable=C0116
# This program is dedicated to the public domain under the CC0 license.
# python c:\Users\HYPERPC\PycharmProjects\pythonProject\main.py



import logging

from telegram import Update
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, CallbackContext, Updater
import requests
from bs4 import BeautifulSoup
from telegram.ext import CallbackQueryHandler
import datetime
import pytz
# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def button():
    keyboard = [
        [
            InlineKeyboardButton(text="Текущий курс валют", callback_data="money")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


def get_money(update: Update, _: CallbackContext):
    currency = ["BTC", "ETH", "USD", "EUR", "CNY"]
    result = ""
    for item in currency:
        r = requests.get(f"https://pokur.su/{item}/rub/1/")
        soup = BeautifulSoup(r.text, 'lxml')
        val = soup.find("div", attrs={"class": "blockquote-classic"}).text.strip()
        result += f"{val}\n"
    if result.strip() == update.effective_message.text:
        pass
    else:
        print("1\n" + result)
        print("2\n" + update.effective_message.text)
        update.callback_query.edit_message_text(
            text=result,
            reply_markup=button()
        )


def job_2(context: CallbackContext):
    currency = ["BTC", "ETH", "USD", "EUR", "CNY"]
    result = ""
    for item in currency:
        r = requests.get(f"https://pokur.su/{item}/rub/1/")
        soup = BeautifulSoup(r.text, 'lxml')
        val = soup.find("div", attrs={"class": "blockquote-classic"}).text.strip()
        result += f"{val}\n"
    context.bot.send_message(
        chat_id="970825811",
        text=result,
        reply_markup=button()
    )
    if context.job_queue.get_jobs_by_name("job"):
        pass
    else:
        logging.getLogger().info('skdjhbvjsdvjsdhfgjsbdfksbhdgfjsdfksjdf')
        context.job_queue.run_daily(
            job,
            time=datetime.time(
                hour=9,
                minute=00,
                tzinfo=pytz.timezone('Europe/Moscow')
            )
        )


def job(context: CallbackContext):
    currency = ["BTC", "ETH", "USD", "EUR", "CNY"]
    result = ""
    for item in currency:
        r = requests.get(f"https://pokur.su/{item}/rub/1/")
        soup = BeautifulSoup(r.text, 'lxml')
        val = soup.find("div", attrs={"class": "blockquote-classic"}).text.strip()
        result += f"{val}\n"
    context.bot.send_message(
        chat_id="970825811",
        text=result,
        reply_markup=button()
    )
    context.job_queue.run_once(job_2, 43200)


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    if context.job_queue.get_jobs_by_name("job"):
        pass
    else:
        logging.getLogger().info('skdjhbvjsdvjsdhfgjsbdfksbhdgfjsdfksjdf')
        context.job_queue.run_daily(
            job,
            time=datetime.time(
                hour=9,
                minute=00,
                tzinfo=pytz.timezone('Europe/Moscow')
            )
        )
        # context.job_queue.run_repeating(
        #     job,
        #     interval=5,
        #     first=datetime.time(
        #         hour=12,
        #         minute=54,
        #         tzinfo=pytz.timezone('Europe/Moscow')
        #     )
        # )
    user = update.effective_user
    update.message.reply_text(
        text="The Witcher 😁😁",
        reply_markup=button()
    )
    logging.getLogger().info(update.effective_user.id)


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("1821046532:AAHFNepY7ofque47KukDiE-H_hNPBZhL0c8")

    button_handler = CallbackQueryHandler(callback=get_money)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(button_handler)
    # on non command i.e message - echo the message on Telegram

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()

