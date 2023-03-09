#!/usr/bin/python3
from sys import argv


def main():
    """My main function
    """
    n = len(argv)
    if n <= 1:
        print(".")
    else:
        print("{} arguments:".format(n - 1))
        for i in range(1, n):
            print("{}: {}".format(i, argv[i]))


if __name__ == "__main__":
    main()
