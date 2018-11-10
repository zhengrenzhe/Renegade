# -*- coding: utf-8 -*-

from telegram.bot import Bot, Update
from telegram.ext import CommandHandler
from telegram.parsemode import ParseMode

from middleware.db import db, keys
from template import remove_default_service_success_tpl


def remove_default_service_callback(bot: Bot, update: Update):
    default_service = db.get(keys.default_service)
    db.rem(keys.default_service)

    msg = remove_default_service_success_tpl(default_service)

    bot.send_message(chat_id=update.message.chat_id,
                     text=msg, parse_mode=ParseMode.HTML)


remove_default_service = CommandHandler(
    "remove_default_service", remove_default_service_callback)
