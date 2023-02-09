#!/usr/bin/python3
"""Module that contains a class BaseGeometry"""
Rectangle = __import__('9-rectangle').BaseGeometry

class Square(Rectangle):
    """Class Square that inherits from Rectangle"""

    def __init__(self, size):
        """Instantiation with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
