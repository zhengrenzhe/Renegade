# -*- coding: utf-8 -*-


from telegram.bot import Bot, Update
from telegram.ext import CallbackQueryHandler

from middleware.env_check import env_check


@env_check
def kb_callback(bot: Bot, update: Update):
    print(update.callback_query.data)


kb = CallbackQueryHandler(callback=kb_callback)
