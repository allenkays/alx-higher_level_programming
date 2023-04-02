#!/usr/bin/python3
"""
This script takes in a letter and sends a post
request to the given url with the letter as a parameter
"""

import requests
from sys import argv


if __name__ == "__main__":
    """
    letter sent in a variable q
    """

    url = "http://0.0.0.0:5000/search_user"
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    response = requests.post(url, data={'q': q})

    if response.json():
        print()
    else:
        print("Not a valid JSON")
