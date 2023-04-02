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
    q = "" if len(argv) == 1 else argv[1]
    response = requests.post(url, data={'q': q})
    try:
        r = response.json()
        if r == {}:
            print("No result")
        else:
            print(f"[{r.get('id')}] {r.get('name')}")
    except ValueError:
        print("Not a valid JSON")
