#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    count = 0
    while i < x:
        try:
            print("{:d}".format(int(my_list[i])), end="")
            count += 1
        except IndexError:
            print()
            print("An error occurred: list index out of range")
            return count
        except:
            pass
        i += 1
    print()
    return count
