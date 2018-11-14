# -*- coding: utf-8 -*-


import logging
import os

from telegram.ext import Updater

from handler.kb_callback import kb_callback
from handler.receive import receive
from handler.remove_default_service import remove_default_service
from handler.set_default_service import set_default_service
from handler.start import start

# logger
logging.basicConfig(level=logging.INFO, format="%(name)s: %(message)s")
bot_logger = logging.getLogger("telegram.bot")
bot_logger.setLevel(logging.INFO)

updater = Updater(token=os.environ.get('BOT_TOKEN'))
dispatcher = updater.dispatcher

# handlers
dispatcher.add_handler(start)
dispatcher.add_handler(receive)
dispatcher.add_handler(set_default_service)
dispatcher.add_handler(kb_callback)
dispatcher.add_handler(remove_default_service)

updater.start_polling()

print("bot is running...")
