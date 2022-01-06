#!/usr/bin/python3
"""

Defines a class Base from which other classes inherit from
"""

import json


class Base:
    """
    Base class for all other classes in the project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instantiation of id attribute
        """
        if id is None:
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
            return "[]"
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

    @classmethod
    def create(cls, **dictionary):
        """
        Return a class instantiated from a dictionary of attributes.

        Args:
            **dictionary: value pairs of attributes to instatiate
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """
        Return list of classes instantiated from a file of JSON strings
        """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, 'r') as myFile:
                list_dict = Base.from_json_string(myFile.read())
                return [cls.create(**d) for d in list_dict]
        except IOError:
            return []
