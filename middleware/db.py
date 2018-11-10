# -*- coding: utf-8 -*-


from dotmap import DotMap
from pickledb import load

db = load("db.json", True)

keys = DotMap({
    "default_service": "default_service"
})
