# -*- coding: utf-8 -*-

from functools import wraps

import pickledb
from telegram.bot import Bot, Update
from telegram.parsemode import ParseMode

from settings import UPYUN_SERVICE, UPYUN_PASSWORD, UPYUN_USERNAME

db = pickledb.load("db.json", True)


def env_check(func):
    @wraps(func)
    def wrapped(bot: Bot, update: Update, *args, **kwargs):
        # check upyun
        if not UPYUN_SERVICE or not UPYUN_USERNAME or not UPYUN_PASSWORD:
            bot.send_message(chat_id=update.message.chat_id, text="😫 <b>Error</b>: Upyun not set",
                             parse_mode=ParseMode.HTML)
            return

        return func(bot, update, *args, **kwargs)

    return wrapped
