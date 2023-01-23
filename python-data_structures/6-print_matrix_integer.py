#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for num in row:
            print("{:d} ".format(num), end='')
            if num +1 == None:
                print("{:d}".format(num), end='')
        print()
