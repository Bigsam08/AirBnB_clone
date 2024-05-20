#!/usr/bin/python3
import datetime
import uuid
import json


class BaseModel:
    """ creating a classs BaseModel of common public instance attributes """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    # A string rep to return class name id and dictionary
    def __str__(self) -> str:
        att = "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
        return att

    def save(self):
        ''' save to file storage save the updated time '''
        self.updated_at = datetime.datetime.now()

    def to_dict(self) -> dict:
        ''' 
        returns a dictionary to save object class name
        and datetime of both created and uodated file into str
        in isoformat
        '''
        my_dico = self.__dict__.copy()
        my_dico["__class__"] = self.__class__.__name__
        my_dico["created_at"] = self.created_at.isoformat
        my_dico["updated_at"] = self.updated_at.isoformat
        return my_dico
