#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Function for sorting and printing a dict by the keys

    Args:
        a_dictionary: the dictionary
    """
    if type(a_dictionary) is dict:
        for key, value in sorted(a_dictionary.items()):
            print(f"{key}: {value}")


if __name__ == "__main__":
    a_dictionary = {'language': "C",
                    'Number': 89,
                    'track': "Low level",
                    'ids': [1, 2, 3]
                    }
    print_sorted_dictionary(a_dictionary)
