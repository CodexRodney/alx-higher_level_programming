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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes JSON string representation of list_objs to a file

        Args:
            list_objs: a list of instances who inherits from Base
        """
        list_dict = []
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w') as myFile:
            if list_objs is None:
                myFile.write("[]")
            else:
                for q in list_objs:
                    list_dict.append(q.to_dictionary())
                myFile.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation

        Args:
            Json_string: string representing a list of dictionaries
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)