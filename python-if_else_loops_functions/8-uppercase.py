#!/usr/bin/python3
def uppercase(str):
    for element in str:
        if ord(element) >= 97 and ord(element) <= 122:
            print(chr(ord(element) - 32), end="")
        else:
            print(element, end="")
    print("\n", end="")
