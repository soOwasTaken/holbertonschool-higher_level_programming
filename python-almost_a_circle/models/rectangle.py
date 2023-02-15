#!/usr/bin/python3
"""Class Square that inherits from Rectangle"""
from models.base import Base


class Rectangle(Base):
    "class Rectangle that inherit Base"

    def __init__(self, width, height, x=0, y=0, id=None):
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
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        Base.__init__(self, id)

    def area(self):
        """Return the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Return the Rectangle printed"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return values of the Rectangle"""
        return "[Rectangle] ({})".format(self.id) + \
            " {}/{} - {}/{}".format(self.x, self.y,
                                    self.width, self.height)

    def update(self, *args, **kwargs):
        """Update by args or kwargs (id,width,height, x and y.)"""
        if args:
            num_args = len(args)
            if num_args > 0:
                self.id = args[0]
            if num_args > 1:
                self.width = args[1]
            if num_args > 2:
                self.height = args[2]
            if num_args > 3:
                self.x = args[3]
            if num_args > 4:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

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
