#!/usr/bin/env python3
"""
Module for initializing storage engine
"""

from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import environ

# using environmental variable to know which storage method to user
if environ.get("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
