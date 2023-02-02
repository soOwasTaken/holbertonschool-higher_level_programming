#!/usr/bin/python3
"""Initialize the rectangle with optional width and height"""


class Rectangle:
    """Initialize the rectangle with optional width and height"""

    def __init__(self, widght=0, height=0):
        self.width = widght
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.height == 0 or self.height == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        return '\n'.join(['#' * self.width for _ in range(self.height)])

    def __repr__(self):
        return "<3-rectangle.Rectangle object at {}>".format(hex(id(self)))
