# -*- coding: utf-8 -*-

from telegram.bot import Bot, Update
from telegram.ext import CommandHandler
from telegram.parsemode import ParseMode


def start_callback(bot: Bot, update: Update):
    bot.send_message(chat_id=update.message.chat_id, text="Renegade is <b>working</b>🎉", parse_mode=ParseMode.HTML)


start = CommandHandler("start", start_callback)
