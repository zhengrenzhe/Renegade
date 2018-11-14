# -*- coding: utf-8 -*-

import os

from dotmap import DotMap
from yaml import load

UPLOAD_SERVICE = os.environ.get("UPLOAD_SERVICE")

__cfg_yaml = load(UPLOAD_SERVICE)

cfg = DotMap(__cfg_yaml)


def config_check():
    if not len(cfg.services):
        return [False, "未填写存储服务"]

    for index, svc in enumerate(cfg.services):
        if svc.mode not in ["upyun", "qiniu"]:
            return [False, "第 %s 个服务: 不支持 \"%s\" 模式" % (index + 1, svc.mode)]

        if not svc.name:
            return [False, "第 %s 个服务: 未填写服务名" % (index + 1)]

        if svc.mode == "upyun":
            if not svc.auth.service_name:
                return [False, "第 %s 个服务: 未填写 upyun service name" % (index + 1)]
            if not svc.auth.username:
                return [False, "第 %s 个服务: 未填写 upyun username" % (index + 1)]
            if not svc.auth.password:
                return [False, "第 %s 个服务: 未填写 upyun password" % (index + 1)]

        if svc.mode == "qiniu":
            if not svc.auth.bucket_name:
                return [False, "第 %s 个服务: 未填写 qiniu bucket name" % (index + 1)]
            if not svc.auth.access_key:
                return [False, "第 %s 个服务: 未填写 qiniu access_key" % (index + 1)]
            if not svc.auth.secret_key:
                return [False, "第 %s 个服务: 未填写 qiniu secret_key" % (index + 1)]

    names = list(map(lambda x: x.name, cfg.services))
    names_set = list(set(names))

    if len(names) != len(names_set):
        return [False, "服务名不能重复"]

    return [True, ""]
