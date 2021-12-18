#!/usr/bin/python3
"""

defines a square
"""


class Square:
    """
    Creates class Square that defines a square by:

        *Private object attribute ''size''.
        *Instantiation with optional size.
        Size must pass some verification for it to be assigned
        If it does not match the verification Square raise
        some exceptions and handles them by printing an
        appropriate message.
    """
    def __init__(self,size=0):
        """
        Initializes a value to __size attribute

        Args:
            self: reference to instance
            size(int): height or length of square
        """
        self.__size = size

    @property
    def size(self):
    """
    Get size of square.

    Returns:
        The size of the square.
    """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets a value size to an object

        It validates whether the value
        is > 0 or an integer if not it raises exceptions

        Args:
            self: a reference to an object
            Value: length or height of square
        """
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
