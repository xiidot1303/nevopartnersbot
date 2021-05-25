from telegram import Bot
from telegram.ext import Dispatcher
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from hello.bot import start, contact, text, callback_query
from os import getenv
from dotenv import load_dotenv
import os

basedir = os.path.abspath(os.path.dirname(''))
load_dotenv(os.path.join(basedir, '.env'))
TOKEN = os.environ.get('TOKEN')

bot_obj = Bot(TOKEN)
dp = Dispatcher(bot_obj, None, workers=0, use_context=True)

dp.add_handler(CommandHandler('start', start))
dp.add_handler(MessageHandler(Filters.contact, contact))
dp.add_handler(MessageHandler(Filters.text, text))
dp.add_handler(CallbackQueryHandler(callback_query))
