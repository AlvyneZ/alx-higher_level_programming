#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """My delete list element function

    Args:
        my_list: Original list with unwanted element
        idx: Index of element to delete

    Returns:
        New list without unwanted element
    """
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    cp = my_list.copy()
    my_list.clear()
    for i in range(len(cp)):
        if i != idx:
            my_list.append(cp[i])
    return my_list


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_list = delete_at(my_list, idx)
    print(new_list)
    print(my_list)
