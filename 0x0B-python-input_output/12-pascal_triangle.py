#!/usr/bin/python3
"""
This "12-pascal_triangle.py" module provides one function:
    pascal_triangle(n)

Tests
=====
    >>> pascal_triangle = __import__('12-pascal_triangle').pascal_triangle
    >>> def print_triangle(triangle):
    ...     for row in triangle:
    ...         print("[{}]".format(",".join([str(x) for x in row])))

    >>> print_triangle(pascal_triangle(5))
    [1]
    [1,1]
    [1,2,1]
    [1,3,3,1]
    [1,4,6,4,1]
"""


def pascal_triangle(n):
    """
    Function that  returns a list of lists of integers representing the
     Pascal's triangle of n

    Args:
        n: size of the Pascal's triangle

    Returns:
        List of lists of integers
    """
    trgl = []
    for i in range(n):
        ln = []
        for j in range(i + 1):
            if (j == 0) or (j == i):
                ln.append(1)
            else:
                ln.append(trgl[i - 1][j] + trgl[i - 1][j - 1])
        trgl.append(ln)
    return trgl
