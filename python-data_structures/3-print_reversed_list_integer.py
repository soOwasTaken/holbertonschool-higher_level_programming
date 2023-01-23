#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    i = len(my_list) - 1
    while i >= 0:
        num = my_list[i]
        print("{:d}".format(num))
        i -= 1
