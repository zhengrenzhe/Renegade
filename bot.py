# -*- coding: utf-8 -*-


import sys

from telegram.ext import Updater

from config import config_check, cfg
from handler.kb_callback import kb_callback
from handler.receive import receive
from handler.remove_default_service import remove_default_service
from handler.set_default_service import set_default_service
from handler.start import start

check_result = config_check()

if not check_result[0]:
    print(check_result[1])
    sys.exit(0)

if cfg.bot.debug:
    import logging

    logging.basicConfig(level=logging.ERROR,
                        format="%(name)s-%(levelname)s: %(message)s")
    bot_logger = logging.getLogger("telegram.bot")
    bot_logger.setLevel(logging.ERROR)

updater = Updater(token=cfg.bot.token)
dispatcher = updater.dispatcher

dispatcher.add_handler(start)
dispatcher.add_handler(receive)
dispatcher.add_handler(set_default_service)
dispatcher.add_handler(kb_callback)
dispatcher.add_handler(remove_default_service)
updater.start_polling()

print("✨ bot is running...")
