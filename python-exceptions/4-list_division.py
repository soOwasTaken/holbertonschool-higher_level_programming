#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            if type(my_list_1[i]) not in (int, float):
                raise TypeError("wrong type")
            if type(my_list_2[i]) not in (int, float):
                raise TypeError("wrong type")
            result.append(my_list_1[i] / my_list_2[i])
        except IndexError:
            print("out of range")
            result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except TypeError as te:
            print(te)
            result.append(0)
        finally:
            pass
    return result
