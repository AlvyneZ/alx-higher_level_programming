#!/usr/bin/python3
def raise_exception():
    """Function for raising a TypeError

    Args:
        none

    Returns:
        none
    """
    raise(TypeError)


if __name__ == "__main__":
    try:
        raise_exception()
    except TypeError as te:
        print("Exception raised")
