#!/usr/bin/python3
"""
Based on 7-base_geometry.py
Defines an Rectangle inherits from BaseGeometry.
"""


class BaseGeometry:
    """Define an area"""

    def area(self):
        """Only raise an Exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Resume:
            Verify if value is a interger

        Args:
            -name: always string, the name of Geometry.
            -value: interger to ckeck
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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
