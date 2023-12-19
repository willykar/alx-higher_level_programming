#!/usr/bin/python3
"""A module for class square"""


class Square:
    """Represent a class called square"""

    def __init__(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        def area(self):
            return self._size * self._size
