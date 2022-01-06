#!/usr/bin/python3
"""

Defines a class Square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Defines a square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Instatiation of values

        Args:
            size(int): size of square
            x = x coordinate of square
            y = y coordinate of square
            id = id of square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Changes string representation of an object
        """
        rst = "[Square] ({id}) {x}/{y} - {w}"
        return rst.format(id=self.id, x=self.x, y=self.y, w=self.width)

    @property
    def size(self):
        """
        Setter/getter of size
        """
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each list
        """
        if len(args) > 0:
            for i, val in enumerate(args):
                if i == 0:
                    self.id = val
                if i == 1:
                    self.width = val
                    self.height = val
                if i == 2:
                    self.x = val
                if i == 3:
                    self.y = val
                if i > 3:
                    break
        else:
            for key, value in kwargs.items():
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value
                if key == 'size':
                    self.width = value
                    self.height = value
                if key == 'id':
                    self.id = value

    def to_dictionary(self):
        """
        Returns dictionary representation of a square
        """
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
