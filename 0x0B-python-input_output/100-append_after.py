#!/usr/bin/python3
"""append_after module"""

def append_after(file_name="", p_search_tring="", p_new_string=""):
    """A function that inserts a line of text to a file"""
    with open(file_name, "r") as f:
        text_file = f.readlines()

    with open(file_name, "w") as fi:
        s = ""
        for line in text_file:
            s += line
            if search_string in line:
                s += new_string
        fi.write(s)
