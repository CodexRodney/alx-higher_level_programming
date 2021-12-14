#!/usr/bin/python3
def islower(c):
    if ord(c) >= 97 and ord(c)<= 122:
        return True
    else:
        return False
def ischaracter(c):
    if c >= 65 and c <= 90:
        return True
    elif c >= 97 and c <= 122:
        return True
    else:
        return False
def upper(str):
    z = 0
    i = len(str)
    while z < i:
        if ischaracter(ord(str[z])) == True and islower(str[z]) == True:
            q = chr(ord(str[z])-32)
            print("{}".format(q), end="")
        else:
            print("{}".format(str[z]), end="")
        z += 1
