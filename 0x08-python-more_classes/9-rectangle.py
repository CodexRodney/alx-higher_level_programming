#!/usr/bin/python3
"""
Defines a class called Rectangle

"""


class Rectangle:
    """
    A class Rectangle

    """
    number_of_instances = 0  # contains number of rectangles
    print_symbol = "#"  # represents the symbol to represent rectangle

    def __init__(self, width=0, height=0):
        """
        Initializes two instances attributes

        Args:
            width: defines width of a rectangle
            height: defined height of a rectangle
        """
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

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
                print(self.print_symbol, end="")
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
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns biggest rectangle based on area

        Args:
            rect_1(Rectangle): 1st rectangle instance to compare
            rect_2(Rectangle): 2nd rectangle instance to comopare
        """
        rect1_area = rect_1.area()
        rect2_area = rect_2.area()
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect1_area >= rect2_area:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Returns a new rectangle instance which is a square

        Args:
            size: the size of the square
        """
        return cls(size, size)
