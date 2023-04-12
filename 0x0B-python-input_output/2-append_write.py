#!/usr/bin/python3
"""
This "2-append_write.py" module provides one function:
    append_write(filename="", text="")
"""


def append_write(filename="", text=""):
    """
    Function that appends text to a UTF-8 encoded text file and returns
     the number of characters added

    Args:
        filename: name of the file to be written to

    Returns:
        Number of characters added
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)


if __name__ == "__main__":
    nb_characters_added = append_write(
        "my_file.txt",
        "This School is so cool!\n"
    )
    print(nb_characters_added)
