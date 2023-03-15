#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Function to replace all occurences of value in list

    Args:
        my_list: List with the value to be replaced
        search: Value to be replaced
        replace: New value of the occurences

    Returns:
        The new list with the replaced occurences
    """
    return [replace if element == search else element for element in my_list]


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
    new_list = search_replace(my_list, 2, 89)

    print(new_list)
    print(my_list)
