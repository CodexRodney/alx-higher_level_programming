#!/usr/bin/python3
def uppercase(str):
    for q in str:
        if q >= 97 and q <= 122:
            q = chr(ord(q)-32)
        print("{}".format(q), end="")
    print("{}".format(""))
