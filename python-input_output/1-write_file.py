#!/usr/bin/python3
"""writes a string to a text file (UTF8) and returns the num of char"""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
