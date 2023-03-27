#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    """Function for printing integers only (prints exception messages)

    Args:
        value: Integer to be printed

    Returns:
        True if value is an integer, False otherwise
    """
    try:
        print("{:d}".format(value))
        return True
    except ValueError as e:
        print("Exception: {}".format(e), file=stderr)
        return False
    except TypeError as e:
        print("Exception: {}".format(e), file=stderr)
        return False


if __name__ == "__main__":
    value = 89
    has_been_print = safe_print_integer_err(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = -89
    has_been_print = safe_print_integer_err(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = "School"
    has_been_print = safe_print_integer_err(value)
    if not has_been_print:
        print("{} is not an integer".format(value))
