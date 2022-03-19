#!/usr/bin/python3
"""
Takes in a URL sends a request and displays
value of X-Request_Id variable
"""

import urllib.request
import sys


def main():
    """
    runs as the main methos
    """
    url = str(sys.argv[1])
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        header = response.headers
        print(header['X-Request-Id'])


if __name__ == "__main__":
    main()
