#!/usr/bin/python3
"""

defines a subclass Rectangle of BaseGeometry
"""


import BaseGeometry from 7-base_geometry


class Rectangle(BaseGeometry):
    """

    subclass Rectangle inherited BaseGeometry
    """
    def __init__(self, width, height):
        """

        Instatiation with width and height
        """
        self.__width = BaseGeometry.integer_validator("width", width)
        self.__height = BaseGeometry.integer_validator("height", height)
