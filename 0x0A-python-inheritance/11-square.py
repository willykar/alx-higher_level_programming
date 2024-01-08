#!/usr/bin/python3
"""
Class BaseGeometry and a subcategory Rectangle
"""


class BaseGeometry:
    """A class with public instance methods: area and validator"""
    def area(self):
        """A method that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks if a value is an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A Rectangle representation"""
    def __init__(self, width, height):
        """rectangle instantiation"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area"""
        return self.__width * self.__height

    def __str__(self):
        """an informal string representation"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


class Square(Rectangle):
    """A square representation"""
    def __init__(self, size):
        """a square instantiation"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"a method that returns the area"""
        return self.__size ** 2

    def __str__(self):
        """An informal string reepresentation"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
