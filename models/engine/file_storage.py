#!/usr/bin/python3
""" file storage """

import json
import datetime
from models.base_model import BaseModel
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.user import User
import os


class FileStorage:
    """ creating a new class called file storage """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ this method returns the dictonary of objects """
        return self.__objects

    def new(self, obj):
        id = obj.to_dict()["id"]
        className = obj.to_dict()["__class__"]
        keyName = className+"."+id
        self.__objects[keyName] = obj

    def save(self):
        """ time to serialize our python object file into a json
            file data base
        """
        client_data = dict(self.__objects)
        for key, value in client_data.items():
            client_data[key] = value.to_dict()
        with open(self.__file_path, 'w') as fle:
            json.dump(client_data, fle)

    def reload(self):
        """
        decerialization is bring out data out of json database
        for corrections
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as fle:
                client_data = json.load(fle)
            for keys in client_data.keys():
                if client_data[keys]['__class__'] == "User":
                    self.__objects[keys] = User(**client_data[keys])
                elif client_data[keys]['__class__'] == "BaseModel":
                    self.__objects[keys] = BaseModel(**client_datal[keys])
                elif client_data[keys]['__class__'] == "Review":
                    self.__objects[keys] = Review(**client_data[keys])
                elif client_data[keys]['__class__'] == "User":
                    self.__objects[keys] = User(**client_data[keys])
                elif client_data[keys]['__class__'] == "State":
                    self.__objects[keys] = State(**client_data[keys])
                elif client_data[keys]['__class__'] == "Place":
                    self.__objects[keys] = Place(**client_data[keys])
                elif client_data[keys]['__class__'] == "City":
                    self.__objects[keys] = City(**client_data[keys])
                elif client_data[keys]['__class__'] == "Amenity":
                    self.__objects[keys] = Amenity(**client_data[keys])
