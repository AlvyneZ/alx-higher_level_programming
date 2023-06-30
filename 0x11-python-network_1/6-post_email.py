#!/usr/bin/python3
"""
Module of a function to post data to a URL
"""
import requests


def post_data(url: str, dict_data: dict):
    """
    Posts data to the provided url and prints the body
    """
    response = requests.post(url, data=dict_data)
    print(response.text)


if __name__ == "__main__":
    from sys import argv

    data = {}
    data.update({"email": argv[2]})
    post_data(argv[1], data)
