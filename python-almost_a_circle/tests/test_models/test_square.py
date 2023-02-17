#!/usr/bin/python3
"""Unittest for class Square
"""
from models.square import Square
from .test_rectangle import TestRectangle

class Testsquare(TestRectangle):
    @classmethod
    def setUpClass(cls, class_name=Square, **kwargs):
        defaultKwargs = { 'size': 10 }
        kwargs = defaultKwargs if kwargs == {} else kwargs
        return super().setUpClass(class_name, **kwargs)
