#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squared = []
    for row in matrix:
        squared.append([col ** 2 for col in row])
    return squared
