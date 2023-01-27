def safe_print_list_integers(my_list=[], x=0):
    i = 0
    count = 0
    while i < x:
        try:
            print("{:d}".format(int(my_list[i])), end="")
            count += 1
        except:
            pass
        i += 1
    print()
    return count
