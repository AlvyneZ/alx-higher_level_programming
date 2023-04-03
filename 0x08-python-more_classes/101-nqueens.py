#!/usr/bin/python3
"""
nqueens - backtracking program to get all possible coordinates for
    N non-attacking queens in an N*N grid
"""
from sys import argv


def main():
    """
    My main function for getting possible coordinates

    Returns:
        None
    """
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if n < 4:
        print("N must be at least 4")
        exit(1)

    a = [-1] * n
    sol = []

    def place_queen(row=0):
        """
        Places a queen on a given row such that it is not on the same column
            as a previously placed queen

        Returns:
            True, if a valid place is found;
            False, if there is no valid placement
        """
        inv_col = set(a[:row])
        nxt_col = set(range(a[row] + 1, n))
        poss = list(nxt_col.difference(inv_col))
        if len(poss) == 0:
            a[row] = -1
            return False
        a[row] = poss[0]
        return True

    def check_validity(row=0):
        """
        Checks validity of queen placement till a given row

        Returns:
            True, if valid; False, if invalid
        """
        i = row - 1
        for x in range(a[row] - 1, -1, -1):
            if i < 0:
                break
            if a[i] == x:
                return False
            i -= 1
        i = row - 1
        for x in range(a[row] + 1, n):
            if i < 0:
                break
            if a[i] == x:
                return False
            i -= 1
        return True

    i = 0
    while 1:
        if not place_queen(i):
            if i == 0:
                break
            i -= 1
            continue
        if not check_validity(i):
            continue
        elif i == n - 1:
            sol.append(a.copy())
            a[i] = -1
        i += 1
        if i == n:
            i = n - 2

    for x in sol:
        a = []
        for i in range(n):
            a.append([i, x[i]])
        print(a)


if __name__ == "__main__":
    main()
