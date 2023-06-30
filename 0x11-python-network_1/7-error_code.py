#!/usr/bin/python3
"""
Module of a function to fetch data from a URL with error handling
"""
import requests


def fetch_url(url: str):
    """
    Fetches data from the provided url and prints the body
    """
    response = requests.get(url)
    try:
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.HTTPError:
        print("Error code: {}".format(response.status_code))


if __name__ == "__main__":
    from sys import argv

    fetch_url(argv[1])
