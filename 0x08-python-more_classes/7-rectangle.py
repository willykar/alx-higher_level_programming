#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """ Class Rectangle with private width and height"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initialize rectangles """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Returns width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets width if int > 0 """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Returns height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets height if int > 0 """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Return width * height """
        return self.__width * self.__height

    def perimeter(self):
        """ Return 2*width + 2*height """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.height)

    def __str__(self):
        """
        Return the printable representation of the Rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            return ((str(self.print_symbol) * self.__width + "\n") * self.__height)[:-1]

    def __repr__(self):
        """Returns string representation of the Rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
    def __del__(self):
        """Print message for deletion of a Rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
