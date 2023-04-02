#!/usr/bin/python3
"""
This script takes url input and sends a request to it
displaying the body of the response decoded as utf-8
"""

from sys import argv
import urllib.request
import urllib.error


if __name__ == "__main__":
    """
    Manages urllib.error.HTTPError exceptions and
    prints the Error code
    """

    url = argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            body = respose.read
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"{e.code}")
