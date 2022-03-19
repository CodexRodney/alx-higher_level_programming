#!/usr/bin/python3
"""
Takes in a url and an email and sends a POST request to the passed URL
with the email as the parameter and displays the body of the response
decoded in utf-8
"""

import sys
import urllib


def main():
    """
    runs as the main method
    """
    url = str(sys.argv[1])
    mail = str(sys.argv[2])
    value = {'email': mail}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, headers)
    with urllib.request.urlopen(request) as response:
        body = response.read().decode("utf-8")
        print("Your email is: {}".format(body))


if __name__ == "__main__":
    main()
