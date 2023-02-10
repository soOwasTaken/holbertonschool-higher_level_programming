#!/usr/bin/python3
"""a script that adds all arguments to a Python list, and then save them to a file"""
import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save-to_json_file').save_to_json_file
    load_from_json_file = __import__(
        '6-load_from_json_file').load_from_json_file
    filename = "add_item.json"
    args = sys.argv[1:]
    try:
        items = load_from_json_file(filename)
    except:
        items = []
    items += args
    save_to_json_file(items, filename)
