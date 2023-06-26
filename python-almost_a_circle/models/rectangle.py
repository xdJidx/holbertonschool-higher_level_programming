#!/usr/bin/python3
"""
1-main
"""


from models.base import Base


class Rectangle(Base):
    """Define Rectangle

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Characteristic of Rectangle

        Args:
            width (int): width of Rectangle
            height (int): height of Rectangle
            x (int, optional): number of #. Defaults to 0.
            y (int, optional): number of #. Defaults to 0.
            id (_type_, optional): number of Rectangle. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
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
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
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
        """Calcul the area of Rectangle

        Returns:
            area: area of Rectangle
        """
        return self.width * self.height

    def display(self):
        """print in stdout in stdout the rectangle with #
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self) -> str:
        string = "[Rectangle] " + "(" + str(self.id) + ") "
        string += str(self.__x) + "/" + str(self.y) + " - "
        string += str(self.__width) + "/" + str(self.__height)
        return string

    def update(self, *args):
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]
