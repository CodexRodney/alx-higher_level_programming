#!/usr/bin/python3
"""Adds all arguments to a Python list"""

import sys

if __name__ == "__main__":
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    try:
    s_args = load_from_json_file("add_item.json")
    except FileNotFoundError:
        s_args = []

    for i in sys.argv:
        s_args.append(i)

    s_args.pop(0)
    save_to_json_file(s_args, "add_item.json")
