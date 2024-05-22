#!/usr/bin/python3

from models.base_model import BaseModel


class State(BaseModel):
    """class State getting the user state """

    name = ""

    def __init__(self, *args, **kwargs):
        '''initializes State'''
        super().__init__(*args, **kwargs)
