#!/usr/bin/python3
"""
A Class BaseGeometry and a subclass Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A Representation of a rectangle"""
    def __init__(self, width, height):
        """Rectangle installation"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
