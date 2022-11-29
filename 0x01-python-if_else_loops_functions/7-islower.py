#!/usr/bin/python3
'''
islower - function to check for lowercase in string
@ c: string to check
'''


def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
