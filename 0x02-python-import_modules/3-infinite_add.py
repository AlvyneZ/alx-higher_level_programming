#!/usr/bin/python3
from sys import argv


def add_argv():
    """My main function
    """
    n = len(argv)
    sum = 0
    for i in range(1, n):
        sum += int(argv[i])
    print("{}".format(sum))


if __name__ == "__main__":
    add_argv()
