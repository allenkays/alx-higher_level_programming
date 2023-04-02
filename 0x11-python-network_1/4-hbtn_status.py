#!/usr/bin/python3
"""
This script fetches given url using the requests module
"""

import requests


if __name__ == "__main__":
    """
    requests module works as shown
    """

    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    body = response.text
    print(f"Body response:\n"
          f"\t - type: {type(body)}\n"
          f"\t - content: {body}"
          )
