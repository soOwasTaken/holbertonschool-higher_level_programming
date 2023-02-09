#!/usr/bin/python3
"""appends a string at the end of a text file (UTF8) and returns the num of char"""


def append_write(filename="", text=""):
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
