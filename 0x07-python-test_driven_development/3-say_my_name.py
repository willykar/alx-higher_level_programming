#!/usr/bin/python3
"""
Module that prints the names
"""


def say_my_name(first_name, last_name=""):
    """
    prints the names
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
         raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
