#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the
body of the response decoded in utf-8
"""

import urllib.error
import urllib.request
import sys

def main():
    """
    Main function where the program runs
    """
    url = str(sys.argv[1])
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode('utf-8'))
    except urllib.error. HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    main()
