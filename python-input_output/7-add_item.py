#!/usr/bin/python3
"""a script that adds all arguments to a Python list, and then save them to a file"""
import sys
import json


def save_to_json_file(my_obj, filename):
    """save to json"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """load from json"""
    with open(filename, 'r') as file:
        return json.load(file)


filename = "add_item.json"
args = sys.argv[1:]
try:
    items = load_from_json_file(filename)
except:
    items = []
items += args
save_to_json_file(items, filename)
