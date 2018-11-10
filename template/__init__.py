# -*- coding: utf-8 -*-

import os

from mako.template import Template

from config import cfg
from middleware.db import db, keys

__DIR__ = os.path.dirname(os.path.realpath(__file__))


def tpl(file_name):
    return Template(filename="%s/%s" % (__DIR__, file_name), input_encoding="utf-8")


def start_tpl():
    services = cfg.get("services")
    default_service = default_service = db.get(keys.default_service)
    return tpl("start.mako").render_unicode(**locals())


def set_default_service_tpl():
    default_service = db.get(keys.default_service)
    return tpl("set_default_service.mako").render_unicode(**locals())


def set_default_service_success_tpl():
    default_service = db.get(keys.default_service)
    return tpl("set_default_service_success.mako").render_unicode(**locals())


def remove_default_service_success_tpl(old_default_service_name):
    return tpl("remove_default_service_success.mako").render_unicode(**locals())
