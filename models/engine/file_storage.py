#!/usr/bin/python3
""" file storage to store dictionary
convertig to json
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """ A storage that serializes dictonary into json data
    and also deserialize from json data file to object dictionary
    """
    # private class attributes
    # __file_path is a string PATH to the JSON  file
    # __objects is an empty dictionary

    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' returns the dictionary of object files '''
        return FileStorage.__objects

    def new(self, obj):
        ''' add new objects to the python dictionary
        Args:
            obj: with key class name is  to the
            object to be stored to te python dict
        '''
        class_name = __class__.__name__
        FileStorage.__objects[obj.class_name + '.' + obj.id] = obj

    def save(self):
        """
            time to serialize python objects dico to
            JSON dico through the json FILE PATH
        """
        my_dict = {}
        for key, value in FileStorage.__objects.items():
            my_dict[key] = value.to_dict().copy
            with open(FileStorage.__file_path, 'w') as my_folder:
                json.dump(my_dict, my_folder)

    def reload(self):
        '''
        deserialize means to convert JSON file back to
        object file called python dictioanry
        RELOAD!!
        desrialize if the JSON FILE PATH exists otherwise do NOTHING
        '''
        try:
            with open(FileStorage.__file_path, 'r') as my_folder:
                my_dict = json.load(my_folder)

            for key, value in my_dict.items():
                class_name = value.get("__class__")
                obj = eval(class_name + "(**value)")
                FileStorage.__objects[key] = obj

        except FileNotFoundError:
            pass
    """ json mode with file to serialize and deserialize
        with r and w mode and loads and json.dumps
    """
