#!/usr/bin/python3
"""appends a string and returns the num of char"""


def append_write(filename="", text=""):
    """appends a string file and returns the num of char"""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
