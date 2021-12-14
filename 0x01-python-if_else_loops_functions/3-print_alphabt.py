#!/usr/bin/python3
a = 97
while a < 123:
    if a == 101 or a == 81:
        a += 1
        continue
    print("{}".format(chr(a)), end="")
    a += 1
