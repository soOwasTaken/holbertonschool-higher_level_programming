#!/usr/bin/python3
"""True, or false if Only sub class of  """


def inherits_from(obj, a_class):
    """True, or false if Only sub class of  """
    return issubclass(type(obj), a_class) and type(obj) != a_class

