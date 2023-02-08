#!/usr/bin/python3
"""class of BaseGeometry"""


class BaseGeometry:
    """class of BaseGeometry"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        if type(value)  != int and value <= 0:
            raise ValueError(f"{value} must be an integer")

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        BaseGeometry.__init__(self, width, height)
        self.__width = width
        self.__height = height