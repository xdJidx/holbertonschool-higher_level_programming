#!/usr/bin/python3
""" function that prints a square with the character #."""


def print_square(size):
    """
    Args:
        size (int): the size length of the square
    Raises:
        TypeError: If either size must be an integer.
        ValueError: size must be >= 0
        TypeError: if size is a float and is less than 0
                    size must be an integer
    """
    if not isinstance(size, int):
        raise TypeError(
            "size must be an integer")

    if size < 0:
        raise TypeError("size must be >= 0")

    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print("")
