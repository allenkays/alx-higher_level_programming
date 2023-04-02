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
    print(f"Body response:\n"
          "\t - type: {type(response)}\n"
          "\t - content: {response.text}"
          )
