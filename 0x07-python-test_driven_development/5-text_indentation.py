#!/usr/bin/python3
"""
Text indentation module
"""


def text_indentation(text):
    """prints a text with 2 new lines"""

    if type(text) is not str:
        raise TypeError("text must be a string")
    flags = 0
    for w in text:
        if flags == 0:
            if w == ' ':
                continue
            else:
                flags = 1
        if flags == 1:
            if w == '?' or w == '.' or w == ':':
                print(w)
                print()
                flags = 0
            else:
                print(w, end="")
