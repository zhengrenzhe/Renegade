# -*- coding: utf-8 -*-

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.bot import Bot, Update
from telegram.ext import CommandHandler

from middleware.env_check import env_check


@env_check
def test_callback(bot: Bot, update: Update):
    button_list = [
        InlineKeyboardButton("col1", callback_data="A"),
        InlineKeyboardButton("col2", callback_data="B"),
        InlineKeyboardButton("row 2", callback_data="C")
    ]
    reply_markup = InlineKeyboardMarkup([button_list])
    bot.send_message(chat_id=update.message.chat_id, text="A two-column menu", reply_markup=reply_markup)


test = CommandHandler("test", test_callback)
