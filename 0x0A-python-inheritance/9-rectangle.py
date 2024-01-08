#!/usr/bin/python3
"""
Class BaseGeometry and a subclass Rectangle
"""


class BaseGeometry:
    """A class with public instance methods"""
    def area(self):
        """raises an exception when there is an error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if the value is an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Representation of a rectangle"""
    def __init__(self, width, height):
        """A rectangle instance"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """An informal string representation"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
