#!/usr/bin/python3
'''
uppercase- converts given string to uppercase
'''


def uppercase(str):
    for c in (str):
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
