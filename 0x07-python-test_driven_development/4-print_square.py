#!/usr/bin/python3

# 4-print_square.py
"""
    Prints a square of #
"""


def print_square(size):
    """
        Args:
            size (int): must be an integer
        Raises:
            TypeError: if not int
            ValueError: if less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
