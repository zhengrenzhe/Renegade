# -*- coding: utf-8 -*-

from upyun import UpYun, UpYunServiceException, UpYunClientException
from telegram import ParseMode
from telegram.bot import Bot, Update

from template import upload_success, upload_error


def upload(main_service_name, mode, service_name, username, password, f, path_name, domain, bot: Bot, chat_id, message_id):
    up = UpYun(service_name, username, password)

    try:
        up.put(path_name, f)
        cdn_url = "%s/%s" % (domain, path_name)
        bot.send_message(chat_id=chat_id, text=upload_success(
            main_service_name, mode, cdn_url), reply_to_message_id=message_id, parse_mode=ParseMode.HTML)

    except UpYunServiceException as se:
        error_detail = """
        HTTP Status Code: %s
        Error Message: %s
        """ % (se.status, se.msg)

        bot.send_message(chat_id=chat_id, text=upload_error(
            service_name, error_detail), reply_to_message_id=message_id, parse_mode=ParseMode.HTML)

    except UpYunClientException as ce:
        error_detail = """
        Error Message: %s
        """ % ce.msg

        bot.send_message(chat_id=chat_id, text=upload_error(
            service_name, error_detail), reply_to_message_id=message_id, parse_mode=ParseMode.HTML)
