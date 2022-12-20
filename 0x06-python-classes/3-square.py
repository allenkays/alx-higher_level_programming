#!/usr/bin/python3
# 3-square.py
"""calculate area of a square"""


class Square:
    def __init__(self, size=0):
        """defining a square class"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """Calculates the area of a square and returns result"""
        return (self.__size ** 2)
