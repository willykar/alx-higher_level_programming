#!/usr/bin/python3
"""A module for class square"""


class Square:
    """Represent a class called square"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Gets the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''method that returns area'''
        return (self.__size * self.__size)
~                                           
