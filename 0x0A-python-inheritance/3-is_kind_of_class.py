#!/usr/bin/python3
"""

Defines a function is_same_class
"""


def is_same_class(obj, a_class):
    """

    Checks whether an obj is a kind of an instance
    of the specified type
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
