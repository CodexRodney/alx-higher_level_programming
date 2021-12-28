#!/usr/bin/python3
"""Defines a function append_write."""


def append_write(filename="", text=""):
    """
    appends a string at the end of text file

    Args:
        filename(str): filename of the file to write
        text(str): text to write
    Return:
        no of characters written
    """
    with open(filename, 'a', encoding="utf-8") as myFile:
        w = myFile.write(text)
    return w
