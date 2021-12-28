#!/usr/bin/python3
"""Defines a function write_file."""


def write_file(filename="", text=""):
    """
    writes a string to a text file

    Args:
        filename(str): filename of the file to write
        text(str): text to write
    Return:
        no of characters written
    """
    with open(filename, 'w', encoding="utf-8") as myFile:
        w = myFile.write(text)
    return w
