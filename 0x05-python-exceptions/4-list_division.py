#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Function for printing the division of integers in 2 lists

    Args:
        my_list_1: first list of integers
        my_list_2: second list of integers
        list_length: length of final list

    Returns:
        List containing the results of the divisions
    """
    list_res = [0] * list_length
    for i in range(0, list_length):
        try:
            list_res[i] = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
    return list_res


if __name__ == "__main__":
    my_l_1 = [10, 8, 4]
    my_l_2 = [2, 4, 4]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)

    print("--")

    my_l_1 = [10, 8, 4, 4]
    my_l_2 = [2, 0, "H", 2, 7]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)
