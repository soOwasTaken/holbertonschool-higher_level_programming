#!/usr/bin/python3
"""Class Square that inherits from Rectangle"""
from models.base import Base


class Rectangle(Base):
    "class Rectangle that inherit Base"

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def area(self):
        """Return the area of the rectangle"""
        return self._width * self._height

    def display(self):
        """Return the # of the rectangle"""
        for i in range(self._height):
            print("#" * self._width)

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(id(self), self._x,
                                               self._y, self._width, self._height)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError(f"width must be an integer")
        if value <= 0:
            raise ValueError(f"width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError(f"height must be an integer")
        if value <= 0:
            raise ValueError(f"height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError(f"x must be an integer")
        if value < 0:
            raise ValueError(f"x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError(f"y must be an integer")
        if value < 0:
            raise ValueError(f"y must be >= 0")
        self.__y = value
