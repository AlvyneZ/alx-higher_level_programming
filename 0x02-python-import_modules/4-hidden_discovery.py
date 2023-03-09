#!/usr/bin/python3
from inspect import getmembers, isfunction
import hidden_4


def get_module_fn():
    """My main function
    """
    fn = getmembers(hidden_4, isfunction)
    for i in fn:
        if i[0][:2] != "__":
            print("{}".format(i[0]))


if __name__ == "__main__":
    get_module_fn()
