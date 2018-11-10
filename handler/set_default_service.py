# -*- coding: utf-8 -*-

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.bot import Bot, Update
from telegram.ext import CommandHandler
from telegram.parsemode import ParseMode

from config import cfg
from template import set_default_service_tpl


def set_default_service_callback(bot: Bot, update: Update):
    msg = set_default_service_tpl()
    services = cfg.get("services")
    buttons = []
    for svc in services:
        buttons.append(
            [InlineKeyboardButton(text="%s (%s)" % (svc.name, svc.mode), callback_data="set_default %s" % svc.name)])

    bot.send_message(chat_id=update.message.chat_id, text=msg, parse_mode=ParseMode.HTML,
                     reply_markup=InlineKeyboardMarkup(buttons))


set_default_service = CommandHandler("set_default_service", set_default_service_callback)
