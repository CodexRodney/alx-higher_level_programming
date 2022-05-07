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

    def to_json(self):
        """
        Returns dict representation of a Student instance
        """
        return self.__dict__
