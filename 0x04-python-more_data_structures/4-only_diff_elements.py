#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Function for Getting uncommon elements of 2 sets

    Args:
        set_1: First set
        set_2: Second set

    Returns:
        Set with the elements that are not common
    """
    return set.union(set_2.difference(set_1), set_1.difference(set_2))


if __name__ == "__main__":
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Ruby", "Perl"}
    od_set = only_diff_elements(set_1, set_2)
    print(sorted(list(od_set)))
