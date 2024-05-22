#!/usr/bin/python3

""" A class inherent of BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """A class for review """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """ enjoy!! """
