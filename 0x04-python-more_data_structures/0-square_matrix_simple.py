#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Function for squaring elements of a 2 x 2 matrix

    Args:
        matrix: 2D List whose elemnts are squared
    """
    return [[element**2 for element in row] for row in matrix]


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    print(matrix)
