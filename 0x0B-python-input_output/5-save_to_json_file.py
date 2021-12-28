#!/usr/bin/python3
"""Defines a function save_to_json_file"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a textfile using
    JSON representation
    """
    with open(filename, 'w') as myFile:
        json.dump(my_obj, filename)
