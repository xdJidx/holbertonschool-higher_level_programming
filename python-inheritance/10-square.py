#!/usr/bin/python3
"""
Based on 8-base_geometry.py
Defines an Rectangle inherits from BaseGeometry.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Definie les caracteristique le classe Rectangle
    """

    def __init__(self, size):
        """
        Initialise la longeur de with et height et verifie si
        elles sont des integers

        Args:
            size(int): longueur d'un côté du carré
        """
        super().__init__(size, size)
        self.__size = size

        self.integer_validator("size", self.__size)

    def area(self):
        return (self.__size * self.__size)
