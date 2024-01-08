#!/usr/bin/python3
"""
lookup module that returns the list of variables
"""


def lookup(obj):
    """returns a list of available attributes and methods"""
    return dir(obj)
