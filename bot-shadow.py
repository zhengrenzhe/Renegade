# -*- coding: utf-8 -*-

import os
import pymongo
from telegram.ext import CommandHandler
from telegram.ext import Updater

updater = Updater(token='685531245:AAGXqWyL8OYSK-gl0curHEh95nRxH9jnQsc')
dispatcher = updater.dispatcher


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="I'm a bot, please talk to me!")


def settt(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="set")


def gettt(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="%s" % os.environ.get('MONGODB_URI'))


start_handler = CommandHandler('start', start)
set_handler = CommandHandler('set', settt)
get_handler = CommandHandler('get', gettt)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(set_handler)
dispatcher.add_handler(get_handler)

updater.start_polling()
