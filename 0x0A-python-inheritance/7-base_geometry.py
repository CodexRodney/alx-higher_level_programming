#!/usr/bin/python3
"""

Defines a class BaseGeometry
"""


class BaseGeometry:
    """

    A class called baseGeometry
    """
    def area(self):
        """

        Raises an exception with error message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """

        Validates arg value to be always an int
        and > than 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
