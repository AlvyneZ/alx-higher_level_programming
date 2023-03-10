#!/usr/bin/python3
def max_integer(my_list=[]):
    """My maximum value finder function

    Args:
        my_list: To be searched thru to get max

    Returns:
        Max value in my_list
    """
    if len(my_list) == 0:
        return None
    max = my_list[0]
    for i in my_list:
        if i > max:
            max = i
    return max


if __name__ == "__main__":
    my_list = [1, 90, 2, 13, 34, 5, -13, 3]
    max_value = max_integer(my_list)
    print("Max: {}".format(max_value))
