#!/usr/bin/python3
"""
Function for read a text file
"""


def read_file(filename=""):
    """open the file filename and read him"""
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end='')
