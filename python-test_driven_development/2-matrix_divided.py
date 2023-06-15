#!/usr/bin/python3
""" function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """
    Addition two var
    Verify is they are int or float
    If they are float, convert in interger
    """

    # Check if a is an integer or float
    if not all(
                isinstance(row, list) and
                all(isinstance(elem, (int, float)) for elem in row)
                for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix has the same size
    row_sizes = [len(row) for row in matrix]
    if len(set(row_sizes)) > 1:
        raise TypeError(
            "Each row of the matrix must have the same size")

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
