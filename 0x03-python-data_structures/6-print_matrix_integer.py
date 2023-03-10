#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """My print matrix function

    Args:
        matrix: 2D List to be printed
    """
    if len(matrix) == 0:
        print("")
    for lst in matrix:
        for i in range(len(lst)):
            print("{:d}".format(lst[i]), end="")
            if i != (len(lst) - 1):
                print(" ", end="")
        print("")


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print_matrix_integer(matrix)
    print("--")
    print_matrix_integer()
