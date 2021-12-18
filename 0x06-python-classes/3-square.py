#!/usr/bin/python3
"""
Class Square that defines a square by:
    * Private instance attribute ``size``.
    * Instantiation with optional size.
If size is not an integer, Square raises a ``TypeError``
exception with the message ``size must be an integer``.
If size is less than 0, a ``ValueError`` exception
with the message ``size must be >= 0`` is raised.
"""


class Square:
    """

    defines a square
    """
    def __init__(self, size=0):
        """
        intilizes a value size to an object

        Args:
            self: a reference to an object
            size(integer:optional): length or height of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        returns the area of the square

        Args:
            self: reference to an instance
        """
        return self.__size**2
