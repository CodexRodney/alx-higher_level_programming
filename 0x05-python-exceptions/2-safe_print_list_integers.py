#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    numitems = 0
    for z in my_list:
        numitems += 1

    num = 0

    new_list = []
    try:
        new_list = my_list[:x]
        for i in new_list:
            if not isinstance(i, int):
                continue
            print("{:d}".format(i), end="")
            num += 1
        if x > numitems:
            raise IndexError
    except IndexError:
        raise
    else:
        print()
        return num
