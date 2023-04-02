#!/usr/bin/python3
"""
Script takes in a url and an email and sends a post
request to the passed url to it with the email as a
parameter and displays the body of the response
"""

import requests
from sys import argv


if __name__ == "__main__":
    """
    Email sent as a variable email
    """

    url = argv[1]
    email = argv[2]
    cred_val = {'email': email}
    response = requests.post(url, data=cred_val)
    print(response.text)
