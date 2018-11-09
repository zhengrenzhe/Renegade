# -*- coding: utf-8 -*-

from telegram.bot import Bot, Update
from telegram.ext import CommandHandler

__all__ = ["start"]


def start_callback(bot: Bot, update: Update):
    bot.send_message(chat_id=update.message.chat_id, text="Renegade is working 🎉")


start = CommandHandler("start", start_callback)
