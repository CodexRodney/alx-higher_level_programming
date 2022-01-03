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
        return self.x * self.y

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

    def update(self, *args):
        """
        Assigns an argument to each attribute
        """
        if len(args) == 0:
            self.__init__(width, height)
        if len(args) == 1:
            self.id = args[0]
        if len(args) == 2:
            self.id = args[0]
            self.width = args[1]
        if len(args) == 3:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
        if len(args) == 4:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
        if len(args) >= 5:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]