#!/usr/bin/python3
def print_last_digit(number):
    ldigit = number % 10
    if number < 0:
        ldigit = (number % -10) - ((number % -10) * 2)
    else:
        ldigit = number % 10
    print(ldigit, end="")
    return (ldigit)
