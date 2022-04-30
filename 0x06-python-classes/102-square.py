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
    def __eq__(self, other):
        """
        Checks whether two squares are equal returns true else false

        """
        if self.__size == other.__size:
            return True
        return False

    def __ne__(self, other):
        """
        Checks whether two squares are not equal returns true else false

        """
        if self.__size != other.__size:
            return True
        return False

    def __gt__(self, other):
        """
        Compares two square

        If square1 is greater it returns true else returns false
        """
        if self.__size > other.__size:
            return True
        return False

    def __ge__(self, other):
        """
        Compares two squares

        If square1 >= square2 returns true else false
        """
        if self.__size >= other.__size:
            return True
        return False

    def __lt__(self, other):
        """
        Compares two squares

        if square1 < square2 returns true else false
        """
        if self.__size < other.__size:
            return True
        return False

    def __le__(self, other):
        """
        Compares two squares

        If square1 <= square2 returns true else false
        """
        if self.__size <= other.__size:
            return True
        return False
