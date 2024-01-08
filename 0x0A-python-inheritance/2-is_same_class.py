#!/usr/bin/python3
"""
This module contains is_same_class
"""


def is_same_class(obj, a_class):
    """return true if the obj is exactly an
    instance of the specified class, otherwise false"""
    return (type(obj) == a_class)
