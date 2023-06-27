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

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute
        """
        if args is not []:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]

        if 'id' in kwargs:
            self.id = kwargs['id']
        if 'size' in kwargs:
            self.size = kwargs['size']
        if 'x' in kwargs:
            self.x = kwargs['x']
        if 'y' in kwargs:
            self.y = kwargs['y']

    def to_dictionary(self):
        """"Dictionnary of Square

        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
