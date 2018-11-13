# -*- coding: utf-8 -*-

from telegram.bot import Bot, Update
from telegram.ext import CommandHandler
from telegram.parsemode import ParseMode

from template import set_default_service_tpl
from utils import services_buttons


def set_default_service_callback(bot: Bot, update: Update):
    msg = set_default_service_tpl()
    buttons = services_buttons(lambda svc: "set_default %s" % svc.name)
    bot.send_message(chat_id=update.message.chat_id, text=msg, parse_mode=ParseMode.HTML, reply_markup=buttons)


set_default_service = CommandHandler("set_default_service", set_default_service_callback)
