#!/usr/bin/python3
"""
Script takes in github username and password and
prints user id using github api
"""

import requests
from sys import argv


if __name__ == "__main__":
    """
    use Basic Authentication with a personal access token
    as password to access to your information
    (only read:user permission is needed)
    """

    username = argv[1]
    passwd = argv[2]

    r = requests.get('https://api.github.com/user', auth=(username, passwd))
    print(r.json().get('id'))
