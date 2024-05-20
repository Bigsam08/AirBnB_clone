#!/usr/bin/python3
"""
creating a class called BaseModel that has a private attributes and methods
for initialization, serilization and deserialization of file storage
lets enjoy the fun
"""

import uuid
import models
from datetime import datetime


class BaseModel:
    """ initializing a class """
    def __init__(self, *args, **kwargs) -> None:
        """creating class attributes """
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

        """ creating class method instances """

    def __str_(self) -> str:
        """
        converts data into string to be saved
        Return: class name, id and dictionary
        """
        return "[{}] ({}) {}".format
    (self.__class__.__name__, self.id, self.__dict__)

    def save(self) -> None:
        """ method saves data and update time of changes """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self) -> dict:
        """ saves converted string data into dictionary """
        temp_dico = self.__dict__.copy()
        temp_dico["__class__"] = self.__class__.__name__
        temp_dico["created_at"] = temp_dico["created_at"].isoformat()
        temp_dico["updated_at"] = temp_dico["updated_at"].isoformat()
        return temp_dico
