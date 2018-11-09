# -*- coding: utf-8 -*-

from io import BytesIO

from telegram.bot import Bot, Update
from telegram.ext import MessageHandler, Filters

from upload.upyun import upload


def receive_callback(bot: Bot, update: Update):
    file_target = update.message.document or update.message.photo[-1]
    file = bot.get_file(file_target.file_id)
    file_name = file.file_path.split("/")[-1]
    file_binary = BytesIO(file.download_as_bytearray())
    upload(file_binary, file_name)
    bot.send_message(chat_id=update.message.chat_id, text="%s upload success 😜" % file_name)


receive = MessageHandler(Filters.document | Filters.photo, receive_callback)
