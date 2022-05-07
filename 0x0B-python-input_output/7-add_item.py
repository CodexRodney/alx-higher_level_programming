#!/usr/bin/python3
"""
Adds all arguments to a python list then saves them to a file
"""


import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def append_to_list(list1):
    """
    Adds items to a list

    Args:
        list1: list in which itmes are added
    """
    for i, x in enumerate(sys.argv):
        if i == 0:
            continue
        list1.append(x)


def main():
    """
    Runs only if __name__ == "__main__"
    """
    filename = "add_item.json"
    arg_list = []
    try:
        arg_list = load_from_json_file(filename)
    except FileNotFoundError:
        append_to_list(arg_list)
        save_to_json_file(arg_list, filename)
    else:
        append_to_list(arg_list)
        save_to_json_file(arg_list, filename)


if __name__ == "__main__":
    main()
