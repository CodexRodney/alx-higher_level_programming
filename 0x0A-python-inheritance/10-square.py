#!/usr/bin/python3
"""
Defines a class Square
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Defines a square
    """
    def __init__(self, size):
        """
        Instantiates the size of the square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Returns area of a square
        """
        return self.__size ** 2
