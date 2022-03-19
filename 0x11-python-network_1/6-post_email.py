#!/usr/bin/python3
"""
Takes in a URL and an email address sends a POST
request to the passed URL with the email as a
parameter and displays the body of the response
"""

import sys
import requests


def main():
    """
    runs as the main method
    """
    url = str(sys.argv[1])
    email = str(sys.argv[2])
    header = {'email': email}
    res = requests.post(url, data=header)
    print("Email: {}".format(res.text))


if __name__ == "__main__":
    main()
