#!/usr/bin/python3
"""
creating a class called BaseModel that has a private attributes and methods
for initialization, serilization and deserialization of file storage
lets enjoy the fun
"""

from uuid import uuid4
import models
from datetime import datetime


class BaseModel:
    """ initializing a class """
    def __init__(self, *args, **kwargs) -> None:
        """creating class attributes """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.udated_at = datetime.now()

        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    time = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, time)
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            models.storage.new(self)

        """ creating class method instances """

    def __str_(self) -> str:
        """ converts data into string to be saved """
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self) -> None:
        """ method saves data and update time of changes """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self) -> dict:
        """ saves converted string data into dictionary """
        temp_dico = self.__dict__.copy()
        temp_dico["__class__"] = type(self).__name__
        temp_dico["created_at"] = temp_dico["created_at"].isoformat()
        temp_dico["updated_at"] = temp_dico["updated_at"].isoformat()
        return temp_dico
