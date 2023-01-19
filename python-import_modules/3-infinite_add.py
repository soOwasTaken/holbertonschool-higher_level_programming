#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv[1:]
    result = 0
    for i in argv:
        result += int(i)
    print(result)
