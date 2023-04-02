#!/usr/bin/python3
"""
This script fetches given url using the requests module
"""

import requests


if __name__ == "__main__":
    """
    requests module works as shown
    """

    url = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:\n\t - type: {}\n\t - content: {}"
          .format(type(url.text), url.text))
