#!/usr/bin/python3
def no_c(my_string):
    """My remove c's function

    Args:
        my_string: String whose c's are to be removed

    Returns:
        The new string without c's
    """
    return ''.join([ch for ch in my_string if ch not in 'cC'])


if __name__ == "__main__":
    print(no_c("Best School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
