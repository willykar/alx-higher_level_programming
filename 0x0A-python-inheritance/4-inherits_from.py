#!/usr/bin/python3
"""
A module that inherits_from(obj, a_class)
"""


def inherits_from(obj, a_class):
    """Method that returns true if an object is a subclass of a_class, otherwise false"""

    return(issubclass(type(obj), a_class) and type(obj) != a_class)
