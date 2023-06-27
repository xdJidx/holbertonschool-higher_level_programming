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
        filename = cls.__name__ + ".json"
        json_list = []
        if list_objs is not None:
            json_list = [obj.to_dictionary() for obj in list_objs]
        with open(filename, 'w') as file:
            file.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """

        Args:
            json_string (_type_): _description_
        """
        if json_string is None or json_string is []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """

        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            return None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """

        Returns:
            _type_: _description_
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                instances = [cls.create(**instance) for instance in data]
                return instances
        except FileNotFoundError:
            return []
