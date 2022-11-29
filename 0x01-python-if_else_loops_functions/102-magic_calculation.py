#!/bin/python3

""""
    Returns c if a < b
    returns a +b if !(a < b) and c >b
    if none of the cases are satisfied it
    returns a*b-c 
"""


def magic_calculation(a, b, c):

    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return a * b - c 
