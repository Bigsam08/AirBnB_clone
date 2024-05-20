#!/usr/bin/python3
import datetime
import uuid
import json


class BaseModel:
    """ creating a classs BaseModel of common public instance attributes """
    def __init__(self, *args, **kwargs):
        ''' if kwargs is not empty, initialize dico attributes
        if key is same with updated or created time convert
        string to datetime objects
        '''
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "upadted_at":
                    setattr(self, key, datetime.strptime
                            (value, '%Y-%m-%dT%H%M%S.%F'))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            ''' kwargs is empty create new instance '''
            self.updated_at = datetime.datetime.now()
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()

    def __str__(self) -> str:
        """ A string rep to return class name id and dictionary """
        class_name = self.__class__.__name__
        att = "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
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
#        my_dico = self.__dict__.copy()
        my_dico["created_at"] = self.created_at.isoformat
        my_dico["updated_at"] = self.updated_at.isoformat
        return my_dico
