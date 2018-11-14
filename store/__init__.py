# -*- coding: utf-8 -*-

import os

from pymongo import MongoClient

SUPPORTED_SERVICE = ("upyun", "qiniu")


class __db__():

    def __init__(self):
        mongo_url = os.environ.get('MONGODB_URI')

        self.client = MongoClient(mongo_url)
        self.db = self.client.heroku_q2mp63z1
        self.config_collection = self.db.config
        self.services_collection = self.db.services

    @property
    def default_service(self):
        data = self.config_collection.find_one()
        if not data:
            return None
        return data["default_service"]

    @default_service.setter
    def default_service(self, value):
        self.config_collection.remove()
        self.config_collection.insert({"default_service": value})

    @default_service.deleter
    def default_service(self):
        self.config_collection.remove()


db = __db__()
