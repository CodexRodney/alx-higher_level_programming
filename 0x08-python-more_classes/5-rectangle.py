#!/usr/bin/python3
"""
Defines a class called Rectangle

"""


class Rectangle:
    """
    A class Rectangle

    """
    def __init__(self, width=0, height=0):
        """
        Initializes two instances attributes

        Args:
            width: defines width of a rectangle
            height: defined height of a rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Returns the width of a rectangle

        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Ensures width is an integer and is >= 0

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Returns the height of a rectangle

        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Ensures height is an integer and is >= 0

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Returns the area of a rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of a rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Prints representation of rectangle using # character
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for w in range(self.__width):
                print("#", end="")
            if i != (self.__height - 1):
                print("")
        return ""

    def __repr__(self):
        """
        Returns string representation of a rectangle

        """
        # variable to show string representation of a rectangle
        rec_rep = "Rectangle({}, {})".format(self.__width, self.__height)
        return rec_rep

    def __del__(self):
        """
        Prints Bye rectangle... when Rectangle instance is deleted
        """
        print("Bye rectangle...")
