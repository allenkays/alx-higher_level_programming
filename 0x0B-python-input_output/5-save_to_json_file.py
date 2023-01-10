#!/usr/bin/python3
""" Module writes an Object to a text file in JSON
"""
import json


def save_to_json_file(my_obj, filename):
    """ Writes an object to a text file in JSON
    Args:
        my_obj: object
        filename: textfile name
    Raises:
        Exception: when the object can't be encoded
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
