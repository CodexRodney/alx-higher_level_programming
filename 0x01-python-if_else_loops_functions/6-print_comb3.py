#!/usr/bin/python3
for i in range(0, 10):
    j = i + 1
    while j < 10:
        print("{}{}".format(i, j), end="")
        if i == 8 and j == 9:
            break
        print(",", end=" ")
        j += 1
