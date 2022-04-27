#!/usr/bin/python3
import hidden_4
for x in dir(hidden_4):
    if x[0] == "_" and x[1] == "_":
        continue
    print(x)
