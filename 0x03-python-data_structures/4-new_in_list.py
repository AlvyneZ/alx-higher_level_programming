#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """My replace element of list copy function

    Args:
        my_list: List with the element to be replaced
        idx: Index of the element to be replaced
        element: New value of the element

    Returns:
        The new list with the replaced element
    """
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_element = 9
    new_list = new_in_list(my_list, idx, new_element)

    print(new_list)
    print(my_list)
