#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Function for getting the number of keys in a dict

    Args:
        a_dictionary: the dictionary

    Returns:
        The number of keys in a_dictionary
    """
    for key, value in sorted(a_dictionary.items()):
        print(f"{key}: {value}")


if __name__ == "__main__":
    a_dictionary = {'language': "C",
                    'Number': 89,
                    'track': "Low level",
                    'ids': [1, 2, 3]
                    }
    print_sorted_dictionary(a_dictionary)
