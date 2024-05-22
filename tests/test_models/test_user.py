#!/usr/bin/python3
""" unit test case for the method
user from the models dirc
"""
from models.user import User
from datetime import datetime
import unittest


class UserTestCase(unittest.TestCase):
    """ lets create a testclass to see if our user class 
    works well or not
    """

    def test_user(self):
        """ check if it exist or not"""
        new = User()
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertTrue(hasattr(new, "email"))
        self.assertTrue(hasattr(new, "password"))
        self.assertTrue(hasattr(new, "first_name"))
        self.assertTrue(hasattr(new, "last_name"))

        """
        check tests on all user atributes
        """
        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)
        self.assertIsInstance(new.email, str)
        self.assertIsInstance(new.password, str)
        self.assertIsInstance(new.first_name, str)
        self.assertIsInstance(new.last_name, str)


if __name__ == '__main__':
    unittest.main()
