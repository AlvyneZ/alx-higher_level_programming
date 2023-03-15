#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Function for Summing unique elements of a list

    Args:
        my_list: List with the values to be sumed

    Returns:
        The sum of the unique elements
    """
    sum = 0
    for i in range(len(my_list)):
        sum += my_list[i] if my_list[i] not in my_list[:i] else 0
    return sum


if __name__ == "__main__":
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))
