#!/usr/bin/python3
"""

Defines a function inherits_from
"""


def inherits_from(obj, a_class):
    """

    Checks whether an obj is a kind of an instance
    of the specified type
    """
    if isinstance(obj, a_class) and not type(obj) is a_class:
        return True
    else:
        return False
