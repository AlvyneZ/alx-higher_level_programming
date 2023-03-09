#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div


def main():
    """My main function
    """
    n = len(argv)
    if n != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    elif len(argv[2]) != 1 or argv[2] not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        fn = {"+": add, "-": sub, "*": mul, "/": div}
        a = int(argv[1])
        b = int(argv[3])
        print("{} {} {} = {}".format(a, argv[2], b,
              fn[argv[2]](a, b)))
        exit(0)


if __name__ == "__main__":
    main()
