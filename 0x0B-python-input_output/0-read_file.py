#!/usr/bin/python3
"""
This "0-read_file.py" module provides one function:
    read_file(filename="")
"""


def read_file(filename=""):
    """
    Function that reads a UTF-8 encoded text file and prints it to stdout

    Args:
        filename: name of the file to be read and printed

    Returns:
        None
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")


if __name__ == "__main__":
    read_file("README.md")
