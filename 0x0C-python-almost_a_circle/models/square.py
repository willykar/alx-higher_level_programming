#!/usr/bin/python3
"""Square Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a class Square that inherits from class Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes instance attributes
        Arguments:
            size: of type (int)
            x: of type(int)
            y: of type(int)
            id: of type(int)
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter method for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter method for size"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update the square attribute
        Arguments:
            args: of type list
            kwargs: of type dict
        """
        if args and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    if args[i] is None:
                        self.__init__(self.width, self.width, self.x, self.y)
                    else:
                        self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                    self.height = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        else:
            if kwargs and len(kwargs) != 0:
                for key, value in kwargs.items():
                    if key == "id":
                        if value is None:
                            self.__init__(self.width, self.width, self.x, self.y)
                        else:
                            self.id = value
                    elif key == "size":
                        self.width = value
                        self.height = value
                    elif key == "x":
                        self.x = value
                    elif key == "y":
                        self.y = value


    def __str__(self):
        """str representation"""
        return f"[square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {"id" : self.id, "x" : self.x, "size" : self.width, "y" : self.y}
