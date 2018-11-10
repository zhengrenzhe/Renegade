# -*- coding: utf-8 -*-


from telegram.bot import Bot, Update

from config import cfg
from upload.upyun import upload as upyun_upload


def upload(bot: Bot, chat_id, service_name, file_target, message_id):
    c = [svc for svc in cfg.services if svc.name == service_name][0]

    if c.mode == "upyun":
        tg_file = bot.get_file(file_target.file_id)
        file_name = tg_file.file_path.split("/")[-1]
        file_binary = tg_file.download_as_bytearray()

        upyun_upload(c.name, c.mode, c.auth.service_name, c.auth.username, c.auth.password,
                     file_binary, file_name, c.domain, bot, chat_id, message_id)
