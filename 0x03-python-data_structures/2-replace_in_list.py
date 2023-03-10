#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """My replace element of list function

    Args:
        my_list: List with the element to be replaced
        idx: Index of the element to be replaced
        element: New value of the element

    Returns:
        The new list with the replaced element
    """
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    my_list[idx] = element
    return my_list


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_element = 9
    new_list = replace_in_list(my_list, idx, new_element)

    print(new_list)
    print(my_list)
