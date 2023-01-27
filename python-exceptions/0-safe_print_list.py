def safe_print_list(my_list=[], x=0):
    printed_elements = 0
    try:
        for i in range(x):
            if i < sum(1 for _ in my_list):
                print(my_list[i], end="")
                printed_elements += 1
            else:
                break
    except:
        pass
    print()
    return printed_elements
