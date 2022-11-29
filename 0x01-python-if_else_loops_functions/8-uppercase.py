#!/usr/bin/python3
'''
uppercase- converts given string to uppercase
'''


def uppercase(str):
    str2 = ""
    for c in (str):
        if ord(c) >= 97 and ord(c) <= 122:
            str2 = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
