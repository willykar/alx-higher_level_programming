#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if search == d else d for d in my_list]
