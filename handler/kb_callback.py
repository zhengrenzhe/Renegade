# -*- coding: utf-8 -*-

from telegram import ParseMode
from telegram.bot import Bot, Update
from telegram.ext import CallbackQueryHandler

from upload import upload
from middleware.db import db, keys
from template import set_default_service_success_tpl, session_expire_tpl


def set_default(bot: Bot, update: Update):
    name = update.callback_query.data.split(" ").pop()
    db.set(keys.default_service, name)
    msg = set_default_service_success_tpl()
    bot.send_message(chat_id=update.callback_query.message.chat.id,
                     text=msg, parse_mode=ParseMode.HTML)


def pre_upload(bot: Bot, update: Update, user_data):
    data = update.callback_query.data.split(" ")
    chat_id = update.callback_query.message.chat.id
    file_id = data.pop()
    service_name = data.pop()

    if not file_id in user_data:
        msg = session_expire_tpl()
        bot.send_message(chat_id=chat_id, text=msg, parse_mode=ParseMode.HTML)
        return

    file_target = user_data[file_id]["file_target"]
    message_id = user_data[file_id]["message_id"]

    user_data.pop(file_id, None)

    upload(bot, chat_id, service_name, file_target, message_id)


def kbcallback_callback(bot: Bot, update: Update, user_data):
    if update.callback_query.data.startswith("set_default"):
        set_default(bot, update)

    if update.callback_query.data.startswith("upload"):
        pre_upload(bot, update, user_data)


kb_callback = CallbackQueryHandler(kbcallback_callback, pass_user_data=True)
