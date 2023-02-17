#!/usr/bin/python3
"""Module that contains class Base"""
import json
from os import path


class Base:
    """Class that manage id attribute in all your future classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation
           of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return json.dumps([])
        else:
            return json.dumps(list_dictionaries)

    @classmethod
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

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string
        representation json_string
        """
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        cls(**dictionary)

        return cls

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        if not path.isfile(filename):
            return []
        else:
            with open(filename, 'r') as f:
                lines = f.read()
                Mydictionary = cls.from_json_string(lines)
                instance = []
                for obj in Mydictionary:
                    instance.append(cls.create(**obj))
                return instance
