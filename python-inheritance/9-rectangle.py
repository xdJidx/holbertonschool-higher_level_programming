#!/usr/bin/python3
"""
Based on 8-base_geometry.py
Defines an Rectangle inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Definie les caracteristique le classe Rectangle
    """

    def __init__(self, width, height):
        """
        Initialise la longeur de with et height et verifie si
        elles sont des integers

        Args:
            with: longeurs of Rectangle
            height: largeur of Rectangle
        """
        self.__width = width
        self.__height = height

        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string

    def area(self):
        return (self.__width * self.__height)
