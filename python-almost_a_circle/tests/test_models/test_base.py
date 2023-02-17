#!/usr/bin/python3
"""Unittest for class Base
"""
import unittest
from models.base import Base
import os

class TestBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls, class_name=Base, **kwargs):
        cls._class_name = class_name
        cls._kwargs = kwargs

    def test_instance(self):
        init_id = self._class_name(**self._kwargs).id
        first_obj = self._class_name(**self._kwargs)
        second_obj = self._class_name(**self._kwargs)
        third_obj = self._class_name(id=89, **self._kwargs)
        fourth_obj = self._class_name(id=56, **self._kwargs)
        fifth_obj = self._class_name(id='a', **self._kwargs)

        self.assertEqual(first_obj.id, init_id + 1)
        self.assertEqual(second_obj.id, first_obj.id + 1)
        self.assertEqual(third_obj.id, 89)
        self.assertEqual(fourth_obj.id, 56)
        self.assertEqual(fifth_obj.id, 'a')

    # def test_to_json(self):
    #     raise NotImplemented 

    # def test_from_json(self):
     #     raise NotImplemented
