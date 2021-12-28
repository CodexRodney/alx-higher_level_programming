#!/usr/bin/python3
"""Defines a function read_file."""


def read_file(filename=""):
    """
    Reads a text file and prints to stdout

    Args:
        filename(str): Filename of the file to be read
    """
    with open(filename, encoding=UTF8) as myFile:
        print(myFile.read())
