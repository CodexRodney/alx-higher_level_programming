#!/usr/bin/python3

def read_file(filename=""):
    """
    Reads a text file and prints to stdout

    Args:
        filename: Filename of the file to be read
    """
    with open(filename, encoding=UTF8) as myFile:
        print(myFile.read())
