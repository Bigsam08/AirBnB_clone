#!/usr/bin/python3
"""
    creating a unique FILESTORAGE  instance for applicaiton
    importing using the reload() method
"""
from models.engine.file_storage import FileStorage


''' create an instance and load from
    JSON file into instance storage
'''
storage = Filestorage()
storage.reload()
