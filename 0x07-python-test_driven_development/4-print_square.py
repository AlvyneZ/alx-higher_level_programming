#!/usr/bin/python3
"""
4-print_square module
Functions:
    print_square: prints a square with the character '#'
"""


def print_square(size):
    """
    Function to print a square with the character '#'
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("".join(["#"] * size))


if __name__ == "__main__":
    print_square(4)
    print("")
    print_square(10)
    print("")
    print_square(0)
    print("")
    print_square(1)
    print("")
    try:
        print_square(-1)
    except Exception as e:
        print(e)
    print("")
