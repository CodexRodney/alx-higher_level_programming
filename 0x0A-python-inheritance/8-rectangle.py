#!/usr/bin/python3
"""Defines a subclass rectangle from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
