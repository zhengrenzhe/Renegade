# -*- coding: utf-8 -*-


from telegram.ext import Updater

from handler.receive import receive
from handler.start import start
from settings import BOT_TOKEN, DEBUG

if DEBUG:
    import logging

    logging.basicConfig(level=logging.ERROR, format="%(name)s-%(levelname)s: %(message)s")
    bot_logger = logging.getLogger("telegram.bot")
    bot_logger.setLevel(logging.ERROR)

updater = Updater(token=BOT_TOKEN)
dispatcher = updater.dispatcher

dispatcher.add_handler(start)
dispatcher.add_handler(receive)
updater.start_polling()
