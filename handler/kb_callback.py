# -*- coding: utf-8 -*-

from telegram import ParseMode
from telegram.bot import Bot, Update
from telegram.ext import CallbackQueryHandler

from middleware.db import db, keys
from template import set_default_service_success_tpl


def set_default(bot: Bot, update: Update):
    name = update.callback_query.data.split(" ").pop()
    db.set(keys.default_service, name)
    msg = set_default_service_success_tpl()
    bot.send_message(chat_id=update.callback_query.message.chat.id,
                     text=msg, parse_mode=ParseMode.HTML)


def kbcallback_callback(bot: Bot, update: Update):
    if update.callback_query.data.startswith("set_default"):
        set_default(bot, update)


kb_callback = CallbackQueryHandler(kbcallback_callback)
