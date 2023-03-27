#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Function for printing elements of a list

    Args:
        my_list: List whose elemnts are to be printed
        x: Maximum number of elements to print

    Returns:
        The number of printed elements
    """
    i = 0
    for i in range(0, x):
        try:
            print(my_list[i], end="")
        except IndexError:
            print("")
            return i
    print("")
    return i


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list(my_list, 2)
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))
