#!/usr/bin/python3
"""Defines a Python class-to-JSON function"""


def class_to_json(obj):
    """Return the dictionary description with simple data structure"""
    return obj.__dict__
