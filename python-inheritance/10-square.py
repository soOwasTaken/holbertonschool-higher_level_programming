#!/usr/bin/python3
"""
Module that defines a class BaseGeometry
"""

class BaseGeometry:
    """Class BaseGeometry"""
    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

class Square(Rectangle):
    """Class Square that inherits from Rectangle"""
    def __init__(self, size):
        """Instantiation with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)