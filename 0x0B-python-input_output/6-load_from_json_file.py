#!/usr/bin/python3
"""json_file function"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file"""
    with open(filename, "r") as f:
        f.load()
