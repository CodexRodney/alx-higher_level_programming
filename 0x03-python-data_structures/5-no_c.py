#!/usr/bin/python3
def no_c(my_string):
    the_string = ''
    for item in my_string:
        if item == 'c' or item == 'C':
            continue
        the_string += item
    return the_string
