#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i,row in enumerate(matrix):
        for num in row:
            print("{:d}".format(num), end='')
        if i != len(matrix) - 1:
            print()
