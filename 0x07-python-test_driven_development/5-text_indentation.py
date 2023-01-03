#!/usr/bin/python3

"""
prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
        Args:
            text (str): input text
        Raise:
            TypeError: text must be a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text) and text[i] == ' ':
        i += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
