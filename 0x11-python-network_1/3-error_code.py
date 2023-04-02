#!/usr/bin/python3
"""
This script takes url input and sends a request to it
displaying the body of the response decoded as utf-8
"""

import sys
import urlib.requests
import urllib.error

if __name__ == "__main__":
    """
    Manages urllib.error.HTTPError exceptions and
    prints the Error code
    """

    url = argv[1]
    try:
        with urllib.requests.urlopen(url) as response:
            body = respose.read
            print(body.decode('utf-8'))
    Exception:
        print(f"{urllib.error.HTTPError(url).code}")
