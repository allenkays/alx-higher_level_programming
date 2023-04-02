#!/usr/bin/python3
"""
This script takes url input and outputs the value of
given variable found in response header
"""

from sys import argv
import urllib.request


if __name__ == "__main__":
    """
    script takes in a URL, sends a request to the URL and
    displays the value of the X-Request-Id variable
    found in the header of the response.
    """

    r = urllib.request.urlopen(argv[1])
    with r as response:
        print(dict(response.headers).get("X-Request-Id"))
