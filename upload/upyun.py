# -*- coding: utf-8 -*-

from upyun import UpYun

from settings import UPYUN_SERVICE, UPYUN_PASSWORD, UPYUN_USERNAME

up = UpYun(UPYUN_SERVICE, UPYUN_USERNAME, UPYUN_PASSWORD)


def upload(f, path_name):
    res = up.put(path_name, f)
    print(res)
