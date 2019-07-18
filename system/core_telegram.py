# encoding: utf-8
import telegram
from telegram.ext import Updater, CommandHandler
from config import telegram_bot_token as telegram_bot_token
from config import NAME as NAME
from config import DEBUG as DEBUG 
import asyncio
import datetime
import sys

class TelegramBot:
    def __init__(self):
        self.token = telegram_bot_token
        TelegramBot.__init__(self, NAME, self.token)
        self.updater.stop()

    def add_handler(self, cmd, func):
        self.updater.dispatcher.add_handler(CommandHandler(cmd, func))

    def start(self):
        self.sendMessage('STARTING')
        self.updater.start_polling()
        self.updater.idle()