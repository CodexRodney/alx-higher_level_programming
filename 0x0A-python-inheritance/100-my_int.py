#!/usr/bin/python3
"""
Defines a class Myint
"""


class MyInt(int):
    """
    Inherits from int
    """
    def __eq__(self, other):
        """
        Inverts the == operator to !=
        """
        return self.real != other

    def __ne__(self, other):
        """
        Inverts the != operator to ==
        """
        return self.real == other
