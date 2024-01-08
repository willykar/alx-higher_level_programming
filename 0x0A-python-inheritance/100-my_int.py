#!/usr/bin/python3
"""
Class MyInt
"""


class MyInt(int):
    """A rebel version of an integer"""
    def __new__(cls, *args, **kwargs):
        """New instances of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """what is != (not equal) is now == (equal)"""
        return int(self) != other

    def __ne__(self, other):
        """what == (equal) is now != (not equal)"""
        return int(self) == other
