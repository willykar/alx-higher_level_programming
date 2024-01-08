#!/usr/bin/python3
"""
A module that inherits_from(obj, a_class)
"""


def inherits_from(obj, a_class):
    """Checks if an object is an an inherited instance of a class
    Args:
        object : The object to check
        a_class (type): The class to match the type of object to
    Returns:
        If object is an inherited instance of a_class return (True)
        Otherwise - False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
