#!/usr/bin/python3
def safe_print_list(my_list=[], x = 0):
    num = 0
    new_list = []
    try:
        new_list = my_list[:x]
        for i in new_list:
            print("{}".format(i), end="")
            num += 1
        print()
        return num
    except:
        print("Invalid Syntax")
