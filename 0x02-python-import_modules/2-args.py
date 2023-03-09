#!/usr/bin/python3
from sys import argv


def main():
    """My main function
    """
    n = len(argv)
    print("{} argument".format(n - 1), end="")
    if n <= 1:
        print("s.")
    else:
        if n > 2:
            print("s", end="")
        print(":")
        for i in range(1, n):
            print("{}: {}".format(i, argv[i]))


if __name__ == "__main__":
    main()
