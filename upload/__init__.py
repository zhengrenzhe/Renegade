# -*- coding: utf-8 -*-


from telegram.bot import Bot, Update

from config import cfg
from upload.upyun import upload as upyun_upload
from upload.qiniu import upload as qiniu_upload


def get_file(bot: Bot, file_target):
    tg_file = bot.get_file(file_target.file_id)
    file_name = tg_file.file_path.split("/")[-1]
    file_binary = tg_file.download_as_bytearray()
    return file_name, file_binary


def upload(bot: Bot, chat_id, service_name, file_target, message_id):
    c = [svc for svc in cfg.services if svc.name == service_name][0]

    if c.mode == "upyun":
        file_name, file_binary = get_file(bot, file_target)
        upyun_upload(c.name, c.mode, c.auth.service_name, c.auth.username, c.auth.password,
                     file_binary, file_name, c.domain, bot, chat_id, message_id)

    if c.mode == "qiniu":
        file_name, file_binary = get_file(bot, file_target)
        qiniu_upload(c.auth.access_key, c.auth.secret_key,
                     c.auth.bucket_name, file_name, file_binary, c.domain, bot, chat_id, message_id, c.name, c.mode)
