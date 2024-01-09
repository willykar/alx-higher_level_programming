#!/usr/bin/python3
""" Defines a pascal_triangle class"""


def pascal_triangle(n):
    """Returns a list of lists of integers"""

     if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        t = triangles[-1]
        tmp = [1]
        for a in range(len(t) - 1):
            tmp.append(t[a] + t[a + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
