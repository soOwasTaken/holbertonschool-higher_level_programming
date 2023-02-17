#!/usr/bin/python3
"""Module that contains class Rectangle that
   inherits from Base
"""
from models.base import Base

class Rectangle(Base):
    """Class Rectangle that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        Base.__init__(self, id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Calculate the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Print the rectangle"""
        for line in range(self.__y):
            print("")
        for row in range(self.__height):
            print((" " * self.__x) + ('#' * self.__width))

    def __str__(self):
        id = self.id
        width = self.__width
        height = self.__height
        x = self.__x
        y = self.__y
        return '[Rectangle] (%s) %s/%s - %s/%s' % (id, x, y, width, height)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute
        """
        if len(args) > 0:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.width = args[1]
            elif len(args) == 3:
                self.height = args[2]
            elif len(args) == 4:
                self.x = args[3]
            else:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
            }

    def save_to_file(cls, list_objs):
        """writes the JSON string representation
        of list_objs to a file
        """
        if list_objs is None or len(list_objs) == 0:
            with open(f"{cls.__name__}.json", 'w') as f:
                f.write("[]")
        else:
            myDict = []
            for obj in list_objs:
                myDict.append(obj.to_dictionary())
            with open(f"{cls.__name__}.json", 'w') as f:
                f.write(cls.to_json_string(myDict))
