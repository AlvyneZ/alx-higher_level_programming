#!/usr/bin/python3
def number_keys(a_dictionary):
    """Function for getting the number of keys in a dict

    Args:
        a_dictionary: the dictionary

    Returns:
        The number of keys in a_dictionary
    """
    return len(a_dictionary)


if __name__ == "__main__":
    a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
    nb_keys = number_keys(a_dictionary)
    print("Number of keys: {:d}".format(nb_keys))
