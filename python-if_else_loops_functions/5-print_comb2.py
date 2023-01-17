#!/usr/bin/python3
for i in range(0, 100):
    if i < 10:
        print(f"0{i:1}".format(i), end=", ")
        continue
    print(f", {i:01}".format(i), end="")
