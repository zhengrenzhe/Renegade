# -*- coding: utf-8 -*-

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from config import cfg


def services_buttons(callback_data_func):
    services = cfg.get("services")
    buttons = []
    for svc in services:
        buttons.append(
            [InlineKeyboardButton(text="%s (%s)" % (svc.name, svc.mode), callback_data=callback_data_func(svc))])
    return InlineKeyboardMarkup(buttons)
