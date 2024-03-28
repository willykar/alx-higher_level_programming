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
    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left
