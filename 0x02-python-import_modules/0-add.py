#!/usr/bin/python3
"""
0_add.py
import module and use to print the sum of 1 and 2.
"""


if __name__ == "__main__":
    from add_0 import add

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
