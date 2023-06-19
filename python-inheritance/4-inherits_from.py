#!/usr/bin/python3
"""
Finds if an object is an instance of a class that inherited
(directly or indirectly) from the specified class .
"""


def inherits_from(obj, a_class):
    """Function to determine if obj is an instance of a_class
    inherited from the specified class.

    Args:
        obj: object to look at
        a_class: class to verify the instance of

    Returns: True if obj is an instance of
                a_class from the specified class,
             False otherwises
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
