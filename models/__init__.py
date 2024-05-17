#!/usr/bin/python3
""" Create unique instance app gor storage """
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
