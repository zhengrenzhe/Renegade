# -*- coding: utf-8 -*-


import sys

from telegram.ext import Updater

from config import config_check, cfg
from handler.kb import kb
from handler.receive import receive
from handler.start import start
from handler.test import test

check_result = config_check()

if not check_result[0]:
    print(check_result[1])
    sys.exit(0)

if cfg.bot.debug:
    import logging

    logging.basicConfig(level=logging.ERROR, format="%(name)s-%(levelname)s: %(message)s")
    bot_logger = logging.getLogger("telegram.bot")
    bot_logger.setLevel(logging.ERROR)

updater = Updater(token=cfg.bot.token)
dispatcher = updater.dispatcher

dispatcher.add_handler(start)
dispatcher.add_handler(receive)
dispatcher.add_handler(test)
dispatcher.add_handler(kb)
updater.start_polling()
