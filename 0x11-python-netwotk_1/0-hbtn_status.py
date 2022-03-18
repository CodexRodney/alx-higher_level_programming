#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request

def main():
    """
    MainFunction where everything runs from
    """
    url = "https://alx-intranet.hbtn.io/status"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode("utf-8")))



if __name__ == "__main__":
    main()
