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
        raise ValueError("List cannot be empty")

    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] > list_of_integers[mid - 1]
        and list_of_integers[mid] > list_of_integers[mid + 1]:
            return list_of_integers[mid]

        elif list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1

        else:
            high = mid - 1

    return list_of_integers[low]
