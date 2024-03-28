#!/usr/bin/python3
"""
peak module
"""


def find_peak(list_of_integers):
    """
    A method that finds the peak in a list of intergers
    Args:
        A list_of_integers(list)
    Return:
        int(the peak integer(s))
    """
    if not list_of_integers:
        return None

    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
