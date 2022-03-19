#!/usr/bin/python3
"""
Takes in  a URL sends a request and displays the value
of the variable X-Request-Id in the response header
"""

import requests
import sys

def main():
    url = str(sys.argv[1])
    req = requests.get(url)
    print(req.headers.get('X-Request-Id'))


if __name__ == "__main__":
    main()
