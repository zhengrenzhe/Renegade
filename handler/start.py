# -*- coding: utf-8 -*-

from telegram.bot import Bot, Update
from telegram.ext import CommandHandler
from telegram.parsemode import ParseMode

from middleware.env_check import env_check


@env_check
def start_callback(bot: Bot, update: Update):
    bot.send_message(chat_id=update.message.chat_id, text="🥳 Renegade is working.", parse_mode=ParseMode.HTML)


start = CommandHandler("start", start_callback)
