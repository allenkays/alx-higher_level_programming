#!/usr/bin/python3
""" Module containngs a function that appends to a text file
"""


def append_write(filename="", text=""):
    """ Function that appends to a text file
    Args:
        filename: filename
        text: text to write
    Raises
        Exception: when the file can't be opened
    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)