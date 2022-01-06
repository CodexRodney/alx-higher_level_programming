"""

Defines a class Base
"""

import json


class Base:
    """
    Base class
    """
    __nb_objects = 0
    def __init__(self, id=None):
        if id is None:
            """
            Instatiation of id attribute
            """
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries: is a list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)