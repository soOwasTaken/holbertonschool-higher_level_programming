#!/usr/bin/python3
"""Empty class Square that defines a square"""


class Square:
    """Square:

    Attributes:
        self (self): self
        size (:obj:`int`):size of the square."""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
