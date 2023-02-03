#!/usr/bin/python3
"""Function that indent text"""


def text_indentation(text):
    """Function that indent text"""
    if type(text) != str:
        raise TypeError("text must be a string")
    text = text.strip()
    new_text = text.replace(".", ".\n\n")
    new_text = new_text.replace("?", "?\n\n").replace(":", ":\n\n")
    print(new_text, end="")
