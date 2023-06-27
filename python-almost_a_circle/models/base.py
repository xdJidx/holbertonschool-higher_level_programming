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
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Change json format in to a file

        Args:
                list_objs (list): instance de Base
        """
        filename = type(list_objs[0]).__name__ + ".json"
        json_file = open(filename, "w")
        if list_objs is None:
            json.dump([], json_file)

        if type(list_objs[0]).__name__ == "Rectangle":
            new_dict = [item.to_dictionary() for item in list_objs]
            json_string = cls.to_json_string(new_dict)
            json.dump(new_dict, json_file)

        json_file.close()
