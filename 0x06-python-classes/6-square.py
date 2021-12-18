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
    def __init__(self,size=0,position=(0,0)):
        """
        Initializes value to instances created

        Args:
            self: reference to instance
            size(int): height or length of square
            position(tuple): contains coordinates of the square
        """
        self.__size = size
        self.__position = position[:]

    @property
    def size(self):
        """Get/set size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Gets/sets position of a square"""
        return self.__position

    @position.setter
    def position(self, value):
        if not len(value) == 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive intergers")
        else:
            self.__position = value[:]

    def area(self):
        """Retutn Area of square"""
        return self.__size**2
    def my_print(self):
        """
        Prints a square with the # character

        """
        if self.__size == 0
            print("")
            return
        for y in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for w in range(sel.__position[0]:
                    print(" ", end="")
            for z in range(self.__size):
                print("#", end="")
            print()
