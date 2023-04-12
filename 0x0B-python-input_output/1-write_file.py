#!/usr/bin/python3
"""
This "1-write_file.py" module provides one function:
    write_file(filename="", text="")
"""


def write_file(filename="", text=""):
    """
    Function that writes text to a UTF-8 encoded text file and returns the
     number of lines written

    Args:
        filename: name of the file to be written to

    Returns:
        Number of characters written
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)


if __name__ == "__main__":
    nb_characters = write_file("my_file.txt", "This School is so cool!\n")
    print(nb_characters)
