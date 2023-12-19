#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Class square"""

    def __init__(self, size=0, position=(0,0)):
        '''New square'''

    @property
    def size(self):
        """Gets the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets the current position of the square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(number, int) for number in value) or
                not all(number >= 0 for number in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints square with the # character"""
        if self.__size == 0:
            print("")
            return

        [print("") for a in range(0, self.__position[1])]
        for a in range(0, self.__size):
            [print(" ", end="") for b in range(0, self.__position[0])]
            [print("#", end="") for c in range(0, self.__size)]
            print("")

    def __str__(self):
        """Print() representation of a Square"""
        if self.__size != 0:
            [print("") for a in range(0, self.__position[1])]
        for a in range(0, self.__size):
            [print(" ", end="") for b in range(0, self.__position[0])]
            [print("#", end="") for c in range(0, self.__size)]
            if a != self.__size - 1:
                print("")
        return ("")
