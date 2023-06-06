#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    if not matrix:
        return None

    new_matrix = [[0 for _ in range(len(matrix[0]))]
                  for _ in range(len(matrix))]

    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            new_matrix = list(map(lambda row: [x**2 for x in row], matrix))

    return new_matrix
