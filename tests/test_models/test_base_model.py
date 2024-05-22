#!/usr/bin/python3
''' unittest for vase_model.py '''
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel_save(unittest.TestCase):
    """ Testing the save method in Basemodel class """
    @classmethod
