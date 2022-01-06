#!/usr/bin/python3
"""

Defines a class Rectangle
"""

from base import Base


class Rectangle(Base):
    """
    Represents a Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instatiation of values

        Args:
            width(int): width of the rectangle
            height(int): height of the circle
            x(int): x coordinate of rectangle
            y(int): y coordinate of rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        set/get width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        set/get height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
        set/get x coordinate of rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """
        set/get y coordinate of rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        Returns area of rectangle
        """
        return self.width * self.height

    def display(self):
        """
        Prints rectangle in stdout
        """
        for y in range(self.y):
            print()
        for i in range(self.height):
            for w in range(self.x):
                print(" ", end="")
            for z in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """
        Changes string representation of an object
        """
        rst = "[Rectangle] ({id}) {x}/{y} - {w}/{h}"
        return rst.format(id=self.id, x=self.x, y=self.y, w=self.width, h=self.height)

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute
        """
        if len(args) > 0:
            for i, val in enumerate(args):
                if i == 0:
                    self.id = val
                if i == 1:
                    self.width = val
                if i == 2:
                    self.height = val
                if i == 3:
                    self.x = val
                if i == 4:
                    self.y = val
                if i > 4:
                    break
        else:
            for key, value in kwargs.items():
                if key == 'height':
                    self.height = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value
                if key == 'width':
                    self.width = value
                if key == 'id':
                    self.id = value

    def to_dictionary(self):
        """
        Returns Dictionary representation of a Rectangle
        """
        rep_dic = {'x' : self.x, 'y' : self.y, 'id' :  self.id, 'height' : self.height, 'width' : self.width}
        return rep_dic