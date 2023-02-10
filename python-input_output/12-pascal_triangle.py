#!/usr/bin/python3
"""Module that prints Pascal's triangle"""


def pascal_triangle(n):
    """Returns the Pascal's triangle of n"""
    triangle = [[] for i in range(n)]

    for i in range(n):
        for j in range(i + 1):
            if (j < i):
                if (j == 0):
                    triangle[i].append(1)
                else:
                    nb = triangle[i - 1][j] + triangle[i - 1][j - 1]
                    triangle[i].append(nb)
            elif (j == i):
                triangle[i].append(1)
    return triangle
