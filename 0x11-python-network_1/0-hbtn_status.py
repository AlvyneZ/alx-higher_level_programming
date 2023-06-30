#!/usr/bin/python3
"""
Module of a function to fetch a URL and print the body
"""
import urllib.request


def fetch_url(url: str):
    """
    Fetches data from the provided url and prints the body
    """
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(body.__class__))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))


if __name__ == "__main__":
    fetch_url("https://alx-intranet.hbtn.io/status")
