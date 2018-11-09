# -*- coding: utf-8 -*-


from telegram.bot import Bot, Update
from telegram.ext import CallbackQueryHandler


def kb_callback(bot: Bot, update: Update):
    print(update.callback_query.data)


kb = CallbackQueryHandler(callback=kb_callback)
