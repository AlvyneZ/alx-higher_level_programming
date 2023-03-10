#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """My add tuple elements function (with 2 elements minimum)

    Args:
        tuple_a: First tuple
        tuple_b: Second Tuple

    Returns:
        The tuple with sum of elements of the 2 tuples
    """
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    sum = [0, ] * max(len_a, len_b, 2)
    for i in range(len_a):
        sum[i] += tuple_a[i]
    for i in range(len_b):
        sum[i] += tuple_b[i]
    return (sum[0], sum[1])


if __name__ == "__main__":
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)

    print(add_tuple(tuple_a, (1, )))
    print(add_tuple(tuple_a, ()))
