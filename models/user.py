#!/usr/bin/python3

from models.base_model import BaseModel


class User(BaseModel):
    """ Defines the User class attributes
        getting user email, names and password
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
