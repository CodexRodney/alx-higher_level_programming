#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not type(my_list) is list:
        return
    my_list.reverse()
    for items in my_list:
        print("{:d}".format(items))
