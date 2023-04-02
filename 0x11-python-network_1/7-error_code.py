#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and
displays the response body while handling errors
"""

import requests
from sys import argv


if __name__ == "__main__":
    """
    prints an error code if HTTP status is higher than 400
    followed by the value of the status code
    """

    url = argv[1]
    response = requests.get(url)
    if response.status_code < 400:
        print(response.text)
    else:
        print(f"Error Code {response.status_code}")
