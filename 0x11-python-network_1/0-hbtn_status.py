#!/usr/bin/python3
"""
This script fetches a given url
"""
import urllib.request


if __name__ == '__main__':
    """
    Using the builtin urlib to open the website and read the header.
    """

    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:\n"
              "\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
              .format(type(body), body, body.decode("utf-8")))
