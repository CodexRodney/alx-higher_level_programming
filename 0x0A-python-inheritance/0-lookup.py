#!/usr/bin/python3
"""

defines a function lookup
"""


def lookup(obj):
    """

    Returns a list of available attributes and methods
    of an object
    """
    return dir(obj)
