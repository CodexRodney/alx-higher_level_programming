"""

Defines a class Base
"""


class Base:
    """
    Base class
    """
    __nb_objects = 0
    def __init__(self, id=None):
        if id is None:
            """
            Instatiation of id attribute
            """
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
