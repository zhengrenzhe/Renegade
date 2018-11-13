# -*- coding: utf-8 -*-

from functools import wraps

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ChatAction, Bot, Update

from config import cfg
from store import db


def services_buttons(callback_data_func):
    services = cfg.get("services")
    buttons = []
    for svc in services:
        buttons.append(
            [InlineKeyboardButton(text="%s (%s)" % (svc.name, svc.mode), callback_data=callback_data_func(svc))])
    return InlineKeyboardMarkup(buttons)


def service_check(func):
    """
        1. send typing action
        2. check services
          2.1 if services not exist, block action and request user add services
          2.2 if services exist, continue
    """

    @wraps(func)
    def wrapped(bot: Bot, update: Update, *args, **kwargs):
        bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)

        if len(db.list_service()) == 0:
            bot.send_message(chat_id=update.message.chat_id, text="services not found")
            return

        return func(bot, update, *args, **kwargs)

    return wrapped
