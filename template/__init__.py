# -*- coding: utf-8 -*-

import os

from mako.lookup import TemplateLookup

from config import cfg
from store import db

__DIR__ = os.path.dirname(os.path.realpath(__file__))

lookup = TemplateLookup(directories=[__DIR__], input_encoding="utf-8", module_directory="/tmp/mako_modules")


def tpl(file_name):
    tp = lookup.get_template(file_name)
    return tp


def start_tpl():
    services = cfg.get("services")
    default_service = db.default_service
    return tpl("start.mako").render_unicode(**locals())


def set_default_service_tpl():
    default_service = db.default_service
    return tpl("set_default_service.mako").render_unicode(**locals())


def set_default_service_success_tpl():
    default_service = db.default_service
    return tpl("set_default_service_success.mako").render_unicode(**locals())


def remove_default_service_success_tpl(old_default_service_name):
    return tpl("remove_default_service_success.mako").render_unicode(**locals())


def remove_default_service_error_tpl():
    return tpl("remove_default_service_error.mako").render_unicode(**locals())


def choice_service_tpl():
    return tpl("choice_service.mako").render_unicode(**locals())


def session_expire_tpl():
    return tpl("session_expire.mako").render_unicode(**locals())


def upload_success(service_name, mode, cdn_url):
    return tpl("upload_success.mako").render_unicode(**locals())


def upload_error(service_name, error_detail):
    return tpl("upload_error.mako").render_unicode(**locals())


def service_not_found():
    return tpl("service_not_found.mako").render_unicode(**locals())
