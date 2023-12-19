#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represen class square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square instance
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.size = size

        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2 or not all(isinstance(v, int) for v in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(num >= 0 for num in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

        def __str__(self):
            """Prints a square to stdout """
            square = []
            if self.__size == 0:
                return ""

            [square.append("\n") for a in range(self.position[1])]
            for a in range(self.__size):
                for b in range(self.__position[0]):
                    square.append(" ")
                    for c in range(self.__size):
                        square.append("#")
                        if a < (self.__size - 1):
                            square.append("\n")
                            return "".join(square)

        def area(self):
            """Returns area of the square"""
            return (self.__size * self.__size)

        @property
        def size(self):
            """Gets the current size of the square"""
            return (self.__size)

        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            if value < 0:
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
                raise TypeError("position must be a tuple"
                        "of 2 positive integers")
            self.__position = value

            def my_print(self):
                """Prints the # character"""
                if self.__size == 0:
                    print()
                    return

                [print() for a in range(self.position[1])]
                for a in range(self.__size):
                    for a in range(self.__position[0]):
                        print(" ", end="")
                        for a in range(self.__size):
                            print("#", end="")
                            print()
