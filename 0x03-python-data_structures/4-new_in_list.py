#!/usr/bin/python3
# 4-new_in_list.py


def new_in_list(my_list, idx, element):
    """Replace element in a cpy list at index"""

    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)

    cpy = [0:]
    cpy[idx] = element
    return (cpy)
