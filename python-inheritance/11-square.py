#!/usr/bin/python3
from 9-rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
