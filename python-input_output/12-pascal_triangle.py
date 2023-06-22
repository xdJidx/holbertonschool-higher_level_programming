#!/usr/bin/python3
"""
Create a functionthat returns a list of lists of integers
representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    # Commence avec la première ligne [1]
    triangle = [[1]]

    for row_num in range(1, n):

        previous_row = triangle[row_num - 1]

        # Ajoute 1 comme premier élément de la ligne
        current_row = [1]

        for col_num in range(1, row_num):
            # Additionne les deux nombres situés directement au-dessus
            current_element = previous_row[col_num - 1] + previous_row[col_num]
            current_row.append(current_element)

        # Ajoute 1 comme dernier élément de la ligne
        current_row.append(1)

        # Ajoute la ligne actuelle au triangle
        triangle.append(current_row)

    return triangle
