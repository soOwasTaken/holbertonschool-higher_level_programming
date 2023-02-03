#!/usr/bin/python3
"""division of matrix"""


def matrix_divided(matrix, div):
    """division of every number in the matrix"""
    if not all(map(lambda x: all(map(lambda y:
                                     type(y) in [int, float], x)), matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not all(map(lambda x: len(x) == len(matrix[0]), matrix)):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(y / div, 2) for y in x] for x in matrix]
