#!/usr/bin/python3
"""
A module that inherits_from(obj, a_class)
"""


def inherits_from(obj, a_class):
    """return true if the object is an instance of a class"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
