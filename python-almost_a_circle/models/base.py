#!/usr/bin/python3
"""
0-main
"""

import json


class Base:
    """
    This class will be the “base”
    of all other classes in this project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Change dictionnary in json format

        Args:
            list_dictionaries (dictionnary): key/value format

        Returns:
            dictionnary: Return jason string dictionary
        """
        if list_dictionaries is None or list_dictionaries is []:
            list_dictionaries = []
            return list_dictionaries
        else:
            return json.dumps(list_dictionaries)
