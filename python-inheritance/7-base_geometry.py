#!/usr/bin/python3
"""
Based on 6-base_geometry.py
Defines an empty class BaseGeometry.
"""


class BaseGeometry:
    """Reprsent base geometry."""

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
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
