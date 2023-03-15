#!/usr/bin/python3
from xmlrpc.client import MAXINT


def best_score(a_dictionary):
    """Function for getting the key of the largest element in a dict

    Args:
        a_dictionary: the dictionary

    Returns:
        The dictionary without the deleted key
    """
    if type(a_dictionary) != dict:
        return "None"
    max_key = "None"
    max_value = -MAXINT
    for key, value in a_dictionary.items():
        if value > max_value:
            max_key = key
            max_value = value
    return max_key


if __name__ == "__main__":
    a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
    best_key = best_score(a_dictionary)
    print("Best score: {}".format(best_key))

    best_key = best_score(None)
    print("Best score: {}".format(best_key))
