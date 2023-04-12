#!/usr/bin/python3
"""
This "7-add_item.py" script adds all arguments to a Python list,
 and then saves them to a file "add_item.json"
"""
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def main():
    """
    My main function to serialize the arguments and add them to
     the list saved in "add_item.json"
    """
    try:
        lis = load_from_json_file("add_item.json")
    except FileNotFoundError:
        lis = []
    lis += argv[1:]
    save_to_json_file(lis, "add_item.json")


if __name__ == "__main__":
    main()
