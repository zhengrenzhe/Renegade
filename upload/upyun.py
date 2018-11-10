# -*- coding: utf-8 -*-

from upyun import UpYun

from config import cfg

up = UpYun(cfg.services[0].auth.service_name,
           cfg.services[0].auth.username, cfg.services[0].auth.password)


def upload(f, path_name):
    res = up.put(path_name, f)
