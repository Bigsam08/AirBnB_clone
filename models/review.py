#!/usr/bin/python3
""" a class called Review """
from models.base_model import BaseModel


class Review(BaseModel):
    """ public class attributes to review the data below"""
    place_id = ""
    user_id = ""
    text = ""

