from config import TELEGRAM_TOKEN
from telegram import Bot
from telegram.ext import Updater, CommandHandler

bot = Bot(token=TELEGRAM_TOKEN)
updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    update.message.reply_text("Бот запущен!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
