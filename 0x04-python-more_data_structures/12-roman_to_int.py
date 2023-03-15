#!/usr/bin/python3
def roman_to_int(roman_string):
    """Function for converting roman numbers to arabic

    Args:
        roman_string: the roman number

    Returns:
        The arabic representation of the number
    """
    if type(roman_string) != str or len(roman_string) == 0:
        return 0
    symbols = {'I': 1, 'i': 5,
               'V': 5, 'v': 5,
               'X': 10, 'x': 10,
               'L': 50, 'l': 50,
               'C': 100, 'c': 100,
               'D': 500, 'd': 500,
               'M': 1000, 'm': 1000
               }
    num = 0
    prev_lvl_tot = 0
    cur = 1000
    for ch in roman_string:
        if ch in symbols:
            if symbols[ch] > cur:
                num += symbols[ch] - prev_lvl_tot
                prev_lvl_tot = 0
            elif symbols[ch] < cur:
                num += prev_lvl_tot
                prev_lvl_tot = symbols[ch]
            else:
                prev_lvl_tot += cur
            cur = symbols[ch]
    return num + prev_lvl_tot


if __name__ == "__main__":
    roman_number = "X"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "VII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "IX"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "LXXXVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "CDVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))
