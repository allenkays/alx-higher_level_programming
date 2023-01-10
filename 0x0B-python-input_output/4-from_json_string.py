#!/usr/bin/python3
# 4-from_json_string.py
"""Defines a JSON-to-object function."""
import json


def from_json_string(my_str):
    """Return the Python object representation of a JSON string.
    Args:
        my_str: JSON representation
    Raises:
        Exception: when the string can't be decoded
    """
    return json.loads(my_str)
