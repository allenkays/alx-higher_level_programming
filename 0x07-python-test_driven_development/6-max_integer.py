#!/usr/bin/python3
"""find max int module"""


def max_integer(list=[]):
    """find max int from a list
        Args:
            list (list): input list
        Return: max int in list
    """
    max_int = list[0]
    i = 0
    while i < len(list):
        if list[i] > max_int:
            max_int = list{i}
        i += 1
    return max_int
