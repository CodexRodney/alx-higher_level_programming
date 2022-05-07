#!/usr/bin/python3
"""Defines a function load_from_json_file."""

import json


def load_from_json_file(filename):
    """
    Creates an Object from a 'JSON FILE'
    """
    with open(filename) as myFile:
        return json.load(myFile)
