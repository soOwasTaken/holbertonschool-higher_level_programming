#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ldigit = number % 10
if number < 0:
    ldigit = number % -10
else:
    ldigit = number % 10
if ldigit > 5 and number > 0:
    print(f"Last digit of {number} is {ldigit} and is greater than 5")
if ldigit == 0:
    print(f"Last digit of {number} is {ldigit} and is 0")
elif ldigit < 5:
    print(f"Last digit of {number} is {ldigit} and is less than 6 and not 0")
