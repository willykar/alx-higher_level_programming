#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square

        Arguments:
            size type(int): The size of the new Square
            x type(int): The x coordinate of the new Square
            y type(int): The y coordinate of the new Square
            id type(int): The identity of the new Square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets the size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square

        Arguments:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1

        elif kwargs and len(kwargs) != 0:
            for keys, value in kwargs.items():
                if keys == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif keys == "size":
                    self.size = value
                elif keys == "x":
                    self.x = value
                elif keys == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the str() representation of a Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
