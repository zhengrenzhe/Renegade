# -*- coding: utf-8 -*-

from telegram.bot import Bot, Update
from telegram.ext import CommandHandler
from telegram.parsemode import ParseMode

from template import start_tpl
from utils import service_check


@service_check
def start_callback(bot: Bot, update: Update):
    msg = start_tpl()
    bot.send_message(chat_id=update.message.chat_id, text=msg, parse_mode=ParseMode.HTML)


start = CommandHandler("start", start_callback)
