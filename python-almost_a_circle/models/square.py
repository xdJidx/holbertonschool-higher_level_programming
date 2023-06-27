#!/usr/bin/python3
"""
10-main
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Define class

    """

    def __init__(self, size, x=0, y=0, id=None):
        """Characteristic of Square
        Args:
            size (int): Size of Square
            x (int, optional): number of #. Defaults to 0.
            y (int, optional): number of #. Defaults to 0.
            id (_type_, optional): number of Rectangle. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self) -> str:
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
