#!/usr/bin/python3

"""Define a MagicClass matching exactly a bytecode"""

import math


class MagicClass:
    """Represent class circle"""

    def __init__(self, radius=0):
        """Initialize a Magic Class
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return area of the Magic Class"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """circumference of the Magic Class"""
        return (2 * math.pi * self.__radius)
