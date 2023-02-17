#!/usr/bin/python3
"""Unittest for class Rectangle
"""
from .test_base import TestBase
from models.rectangle import Rectangle
import os


class TestRectangle(TestBase):
    @classmethod
    def setUpClass(cls, class_name=Rectangle, **kwargs):
        defaultKwargs = { 'width': 10, 'height': 20 }
        kwargs = defaultKwargs if kwargs == {} else kwargs
        return super().setUpClass(class_name, **kwargs)
