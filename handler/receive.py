# -*- coding: utf-8 -*-

import io

from telegram.bot import Bot, Update
from telegram.ext import MessageHandler, Filters

from upload.upyun import upload
from utils import services_buttons
from middleware.db import db, keys
from template import choice_service_tpl


def receive_callback(bot: Bot, update: Update, user_data):

    default_service = db.get(keys.default_service)

    file_target = update.message.document or update.message.photo[-1]

    if not default_service:
        user_data[file_target.file_id] = {
            "file_target": file_target,
            "message_id": update.message.message_id
        }

        buttons = services_buttons(
            lambda svc: "upload %s %s" % (svc.name, file_target.file_id))

        bot.send_message(chat_id=update.message.chat_id,
                         text=choice_service_tpl(),
                         reply_to_message_id=update.message.message_id,
                         reply_markup=buttons)

    # file = bot.get_file(file_target.file_id)
    # raw_file_name = file_target.file_name
    # file_name = file.file_path.split("/")[-1]
    # file_binary = file.download_as_bytearray()

    # f = io.BytesIO(file_binary)

    # if not default_service:
    #     user_data[]
    #     bot.send_document(chat_id=update.message.chat_id, document=f)
    # else:
    #     pass

    # upload(file_binary, file_name)
    # bot.send_message(chat_id=update.message.chat_id,
    #                  text="%s upload success 😜" % file_name)


receive = MessageHandler(Filters.document | Filters.photo,
                         receive_callback, pass_user_data=True)
