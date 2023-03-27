#!/usr/bin/python3
def safe_print_division(a, b):
    """Function for printing the division of two integers

    Args:
        a: first integer
        b: second integer

    Returns:
        The result of the division
    """
    try:
        res = a / b
    except ZeroDivisionError:
        res = None
    finally:
        print("Inside result: {}".format(res))
    return res


if __name__ == "__main__":
    a = 12
    b = 2
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))

    a = 12
    b = 0
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))
