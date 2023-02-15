#!/usr/bin/python3
"""class Base"""
import json


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        list_dictionaries = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dictionaries)

        with open(filename, "w") as file:
            file.write(json_string)