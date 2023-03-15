#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """Function for multiplying values in a list with a given number

    Args:
        my_list: the list whose elements are to be updated
        number: the number to multiply to the elements

    Returns:
        The new dictionary
    """
    return list(map(lambda x: x * number, my_list))


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 6]
    new_list = multiply_list_map(my_list, 4)
    print(new_list)
    print(my_list)
