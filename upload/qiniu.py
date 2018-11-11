# -*- coding: utf-8 -*-

from qiniu import Auth, put_data
from telegram import ParseMode
from telegram.bot import Bot, Update

from template import upload_success, upload_error


def upload(access_key, secret_key, bucket_name, path_name, file_binary, domain, bot: Bot, chat_id, message_id, service_name, mode):
    try:
        q = Auth(access_key, secret_key)
        token = q.upload_token(bucket_name, path_name, 3600)
        _, info = put_data(token, path_name, file_binary)

        if info.status_code == 200:
            cdn_url = "%s/%s" % (domain, path_name)

            bot.send_message(chat_id=chat_id, text=upload_success(
                service_name, mode, cdn_url), reply_to_message_id=message_id, parse_mode=ParseMode.HTML)
        else:
            error_detail = """
            HTTP Status Code: %s
            Error Message: %s
            """ % (info.status_code, info.exception)

            bot.send_message(chat_id=chat_id, text=upload_error(
                service_name, error_detail), reply_to_message_id=message_id, parse_mode=ParseMode.HTML)

    except KeyError as ke:
        error_detail = """
        Error Message: %s
        """ % ke

        bot.send_message(chat_id=chat_id, text=upload_error(
            service_name, error_detail), reply_to_message_id=message_id, parse_mode=ParseMode.HTML)
