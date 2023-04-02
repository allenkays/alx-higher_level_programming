#!/usr/bin/python3
"""
Script takes in url, sends a request to the url and displays
the value of a given variable in the response header
"""

import requests
from sys import argv


if __name__ == "__main__":
    """
    getting value of given url
    """

    response = requests.get(argv[1])
    print(response.headers.get('X-Request-Id'))
