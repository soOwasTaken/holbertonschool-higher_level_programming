#!/usr/bin/python3
"""Class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    "class Square that inherit Rectangle"

    def __init__(self, size, x=0, y=0, id=None):
        Rectangle.__init__(self, size, size, x, y, id)

    def __str__(self):
        return "[Square] ({})".format(self.id) + \
            " {}/{} - {}".format(self.x, self.y, self.size)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value

    def area(self):
        """area of square"""
        return self.size * self.size

    def update(self, *args, **kwargs):
        """Update by args or kwargs (id, size, x and y.)"""
        if args:
            num_args = len(args)
            if num_args > 0:
                self.id = args[0]
            if num_args > 1:
                self.size = args[1]
            if num_args > 2:
                self.x = args[2]
            if num_args > 3:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
