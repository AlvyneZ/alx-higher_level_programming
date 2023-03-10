#!/usr/bin/python3
def element_at(my_list, idx):
    """My retrieve element of list function

    Args:
        my_list: List with the element to be retrieved
        idx: Index of the element to be retrieved

    Returns:
        The element at the requested index
    """
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    return my_list[idx]


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
