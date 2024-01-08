#!/usr/bin/python3
"""
A module that inherits_from(obj, a_class)
"""


def inherits_from(obj, a_class):
    """
    Method that returns true if an object is a subclass
    of a_class, otherwise false

    Args:
        obj (any): The object to check
        a_class (type): The class to match the type of object to

    Returns:
        If object is an inherited instance of a_class return True
        Otherwise - False
    """

    return(issubclass(type(obj), a_class) and type(obj) != a_class)
