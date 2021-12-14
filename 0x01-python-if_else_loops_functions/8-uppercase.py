#!/usr/bin/python3
def uppercase(str):
    if ord(str) >= 65 and ord(str) <= 90:
        print("{}".format(str))
    else:
        q = ord(str) - 32
        print("{}".format(str))
