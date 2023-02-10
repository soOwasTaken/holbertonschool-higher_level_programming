#!/usr/bin/python3
"""returns a dictionary representation"""
Student = __import__('9-student').Student


def to_json(self, attrs=None):
    if attrs is None:
        return self.__dict__
    else:
        return {k: v for k, v in self.__dict__.items() if k in attrs}
