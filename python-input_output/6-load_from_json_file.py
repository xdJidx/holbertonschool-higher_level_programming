#!/usr/bin/python3
"""
function that creates an Object from a “JSON file”
"""

import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”"""
    with open(filename) as file:
        json_data = file.read()
        return json.loads(json_data)
