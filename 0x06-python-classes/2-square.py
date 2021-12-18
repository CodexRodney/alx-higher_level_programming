#!/usr/bin/python3
"""
Creates class Square that defines a square by:

*Private object attribute ''size''.
*Instantiation with optional size.
Size must pass some verification for it to be assigned
If it does not match the verification Square raise 
some exceptions and handles them by printing an 
appropriate message.
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
