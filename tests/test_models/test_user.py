#!/usr/bin/python3
"""Module that contains unittests for models/user.py"""
from models.user import User
from tests.test_models.test_base_model import test_baseModel


class test_user(test_baseModel):
    """Defines unit tests for models/user.py"""

    def __init__(self, *args, **kwargs):
        """initantiate user instance"""
        super().__init__(*args, *kwargs)
        self.name = 'User'
        self.value = User

    def test_first_name(self):
        """check type of first_name is string"""
        new_user = self.value()
        self.assertIsInstance(new_user.first_name, str)

    def test_last_name(self):
        """check type of last_name is string"""
        new_user = self.value()
        self.assertIsInstance(new_user.last_name, str)

    def test_email(self):
        """check type of email is string"""
        new_user = self.value()
        self.assertIsInstance(new_user.email, str)

    def test_password(self):
        """check type of password is string"""
        new_user = self.value()
        self.assertIsInstance(new_user.password, str)
