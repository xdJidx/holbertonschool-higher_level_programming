#!/usr/bin/python3
"""
Based on 6-base_geometry.py
Defines an empty class BaseGeometry.
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
