#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """My print list in reverse function

    Args:
        my_list: List to be printed in reverse
    """
    if my_list is None:
        return
    for x in reversed(my_list):
        print("{:d}".format(x))


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print_reversed_list_integer(my_list)
