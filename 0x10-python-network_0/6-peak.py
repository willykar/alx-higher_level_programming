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
  start = 0
  end = len(list_of_integers) - 1
  while start < end:
      mid = (start + end) // 2
      if list_of_integers[mid] < list_of_integers[mid + 1]:
          start = mid + 1
      else:
          end = mid
  return start
