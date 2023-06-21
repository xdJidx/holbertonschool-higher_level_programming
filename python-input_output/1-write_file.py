#!/usr/bin/python3
"""
Function for write a text file UTF-8 and return characters written
"""


def write_file(filename="", text=""):
    """Write and return the number of characters"""
    with open(filename, 'w', encoding="utf-8") as file:
        numChars = file.write(text)
    return numChars
