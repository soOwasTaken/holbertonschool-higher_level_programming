#!/usr/bin/python3
"""addition of 2 integer"""


def add_integer(a, b=98):
    """addition of 2 integer, a and b must be integer"""
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    if type(a) is float or type(b) is float:
        a = int(a)
        b = int(b)
    return a + b

