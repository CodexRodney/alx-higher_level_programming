#!/usr/bin/python3
"""
defines a class MyList
"""


class MyList(list):
    """
    Inherited Class from baseclass list
    """
    def print_sorted(self):
        """
        Prints list in a sorted manner asscending order
        """
        print(sorted(self))
