#!/usr/bin/python3
"""Function that indent text"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.replace("? ", "?\n\n")
    text = text.replace(". ", ".\n\n").replace(": ", ":\n\n")

    result = '\n'.join(line.strip() for line in text.splitlines())
    print(result, end="")
