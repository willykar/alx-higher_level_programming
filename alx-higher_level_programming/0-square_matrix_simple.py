#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = lambda x: x ** 2
    squared_matrix = [[square(element) for element in row] for row in matrix]
    return squared_matrix
