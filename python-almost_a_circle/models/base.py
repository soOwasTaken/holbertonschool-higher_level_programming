#!/usr/bin/python3
"""class Base"""
import json
from rectangle import Rectangle
from square import Square


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """json representation of all objects"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            dict_list = []
            for dict_obj in list_dictionaries:
                if isinstance(dict_obj, dict):
                    if "size" in dict_obj:
                        obj = Square(1)
                    else:
                        obj = Rectangle(1, 1)
                    obj.update(**dict_obj)
                    dict_list.append(obj.to_dictionary())
            return json.dumps(dict_list)
