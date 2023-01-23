#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i,row in enumerate(matrix):
        for j,num in enumerate(row):
            print("{:d}".format(num), end=' ' if j != len(row)-1 else '')
        print()