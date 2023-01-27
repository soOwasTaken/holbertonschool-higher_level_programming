def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        print("division by zero")
    finally:
        print("Inside result: {:}".format(result))
    return result
