#!/usr/bin/python3
""" create  User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """
        new user details
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
