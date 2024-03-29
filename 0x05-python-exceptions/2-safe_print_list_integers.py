#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Function for printing integers of a list

    Args:
        my_list: List whose integer elements are to be printed
        x: Number of elements to look through (must be < len(my_list))

    Returns:
        The number of printed integer elements
    """
    p = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            p += 1
        except ValueError:
            pass
        except TypeError:
            pass
    print("")
    return p


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list_integers(my_list, 2)
    print("nb_print: {:d}".format(nb_print))

    my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
    nb_print = safe_print_list_integers(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))

    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))
