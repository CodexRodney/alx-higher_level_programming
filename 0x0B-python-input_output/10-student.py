#!/usr/bin/python3
"""
Defines a class Student
"""


class Student:
    """
    Defines a student
    """

    def __init__(self, first_name, last_name, age):
        """
        initializes attributes of the class

        Args:
            first_name: Value given to first_name
            last_name: Value given to last_name
            age: Value given to age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns dict representation of a Student instance
        """
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for x in attrs:
            if x in self.__dict__:
                new_dict[x] = self.__dict__.get(x)
        return new_dict
