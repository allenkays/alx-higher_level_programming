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

    url = request.get(argv[1])
    header = url.headers.get('X-Request-Id')
    print(header)
