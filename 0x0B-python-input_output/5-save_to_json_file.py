#!/usr/bin/python3
"""Defines a JSON to object function"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an obj to a text file using a JSON representation"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
