# encoding: utf-8
import sys
import core_telegram

def _help(bot, update):
    APP.sendMessage('')

def _info(bot, update):
    APP.sendMessage('')

def _status(bot, update):
    APP.sendMessage('')
APP = core.TelegramBot()
APP.add_handler('help', _help)
APP.add_handler('system', _info)
APP.add_handler('status', _status)
APP.start()
