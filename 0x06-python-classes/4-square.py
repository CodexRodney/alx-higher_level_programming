#!/usr/bin/python3
"""

defines a square
"""


class Square:
    """
    Creates class Square that defines a square by:

    """
    def __init__(self, size=0):
        """
        Initializes a value to __size attribute

        Args:
            self: reference to instance
            size(int): height or length of square
        """
        self.__size = size

    @property
    def size(self):
        """Gets the size of a square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        returns the area of the square

        Args:
            self: reference to an instance
        """
        return self.__size**2
