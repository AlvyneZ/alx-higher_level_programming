#!/usr/bin/python3
"""
Module of a function to post data to a URL and print the returned json
"""
import requests


def post_data(url: str, dict_data: dict):
    """
    Posts data to the provided url and prints the body
    """
    response = requests.post(url, data=dict_data)
    if response.status_code == 204:
        return None
    try:
        return response.json()
    except Exception:
        return 0


if __name__ == "__main__":
    from sys import argv

    data = {"q": ""}
    if len(argv) > 2:
        data.update({"q": argv[2]})
    res = post_data(argv[1], data)
    if res is None:
        print("No result")
    elif res == 0:
        print("Not a valid JSON")
    else:
        print("[{}] {}".format(res["id"], res["name"]))
