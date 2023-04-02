#!/usr/bin/python3
"""
This script takes as input a url and an email and sends a post request
to the url passed.
"""

from sys import argv
import urllib.request
import urllib.parse

if __name__ = "__main__":
    """
    This should display the body of the response decoded as utf-8
    """

    r = urllib.parse.urlencode({'email': argv[2]}).encode('utf-8')
    data = urllib.request.urlopen(argv[1], email=r)
    with data as response:
        body = response.read()
        print(body.decode('utf-8'))
