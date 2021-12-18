#!/usr/bin/python3
"""

defines a Class called a Square.
The square class does instantiation of size field with default value 0
and does verifiction which raises errors  verification is not if verification is not reached
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
        self.__size = size
    @_size.setter
    def _size(self, size):
        """
        validates the size of square

        Args:
            self: reference to object
            size(integer): height or length of square
        """
        try:
            if isinstance(size, int) != True:
                raise TypeError
            elif size < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
        else:
            self.__size = size
