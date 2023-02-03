#!/usr/bin/python3
"""Function that indent text"""


def text_indentation(text):
    """Function that indent text"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars_to_indent = ['.', '?', ':']
    result = []
    current_line = ""
    for char in text:
        if char == " " and current_line == "":
            continue
        elif char in chars_to_indent:
            result.append(current_line + char)
            result.append("\n\n")
            current_line = ""
        else:
            current_line += char
    result.append(current_line)
    print("".join(result), end="")

