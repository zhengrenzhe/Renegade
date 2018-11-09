# -*- coding: utf-8 -*-

from functools import wraps

import pickledb
from telegram.bot import Bot, Update

db = pickledb.load("db.json", True)


def env_check(func):
    @wraps(func)
    def wrapped(bot: Bot, update: Update, *args, **kwargs):
        return func(bot, update, *args, **kwargs)

    return wrapped
