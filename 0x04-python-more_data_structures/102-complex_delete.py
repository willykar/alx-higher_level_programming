#!/usr/bin/python3
def complex_delete(my_dict, value):
    dict_copy = my_dict.copy()
    for k, j in dict_copy.items():
        if value == j:
            my_dict.pop(k)
    return my_dict
