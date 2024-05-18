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
    def __int__(self, *args, **kwargs) -> None:
        """creating class attributes """
        seld.id = str(uuid4())
        self.created_at = datetime.now()
        self.udated_at = datetime.now()

        if len(kwargs > 0):
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    time = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, time)
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            storage.new(self)

        """ creating class method instances """

    def __str_(self) -> str:
        """ converts data into string to be saved """
        att = "[{}] ({}) {}".format
        (self.__class__.__name__, self.id, self.__dict__)
        return att

    def save(self) -> None:
        """ method saves data and update time of changes """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self) -> str:
        """ saves converted string data into dictionary """
        my_dico = dict(self.__dict__)
        my_dico["__class__"] = self.__class__.__name__
        my_dico["created_at"] = datetime.isoformat(self.created_at)
        my_dico['updated_at'] = datetime.isoformat(self.updated_at)
        return my_dico
